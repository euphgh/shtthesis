#!/usr/bin/env python3
"""Generate the standalone thesis workflow figure with OfficeCLI outside sandbox.

The diagram is not registered in the midterm slide deck. Coordinates use a
19-by-7.6 design grid, scaled to a 15.2-by-6.08 inch custom PowerPoint canvas.
Only the two existing conceptual illustrations are raster images.
"""

import argparse
import json
import os
from pathlib import Path
import shutil
import subprocess
from midterm_pptx.theme import DEFAULT_THEME, THEMES, recolor_commands

ROOT = Path(__file__).resolve().parents[1]
BUILD = ROOT / "build/pptx/fpga-rtl-workflow"
NAVY, TEAL, AMBER = "183B56", "008C95", "DF973E"
BLUE, GREEN = "A9D3EC", "ACE0D4"
SCALE = 0.8


def unit(value):
    return f"{value * SCALE:.6f}in"


class Diagram:
    """Build named native shapes and connectors without writing the PPTX."""

    def __init__(self):
        self.commands = []

    def add(self, kind, name, **props):
        self.commands.append(dict(command="add", parent="/slide[1]", type=kind,
                                  props={"name": name, **{k: str(v) for k, v in props.items()}}))

    def shape(self, name, x, y, w, h, **props):
        self.add("shape", name, x=unit(x), y=unit(y), width=unit(w), height=unit(h),
                 **dict(dict(fill="none", line="none", font="Arial", size=18,
                             color=NAVY, margin="0pt", autoFit="none", shadow="none",
                             align="center", valign="middle"), **props))

    def line(self, name, x1, y1, x2, y2, color=NAVY, arrow=False, both=False, dash=False):
        # All routes are orthogonal; reverse direction uses the start arrowhead.
        reverse = x2 < x1 or y2 < y1
        self.add("connector", name, x=unit(min(x1, x2)), y=unit(min(y1, y2)),
                 width=unit(abs(x2-x1)), height=unit(abs(y2-y1)), shape="straight",
                 color=color, lineWidth="1.5pt", lineDash="dash" if dash else "solid",
                 headEnd="triangle" if both or (arrow and reverse) else "none",
                 tailEnd="triangle" if both or (arrow and not reverse) else "none")

    def group(self, name, members):
        self.add("group", name, shapes=",".join(
            f"/slide[1]/shape[@name={member}]" for member in members))

    def chip(self, name, label, x, y, size, fill):
        """A solid chip body, editable centered label and four banks of pins."""
        start = len(self.commands)
        pin, reach = size * .075, size * .10
        for i in range(5):
            pos = size * (.16 + .155*i)
            for side, px, py, pw, ph in (
                ("T", x+pos, y-reach, pin, reach),
                ("B", x+pos, y+size, pin, reach),
                ("L", x-reach, y+pos, reach, pin),
                ("R", x+size, y+pos, reach, pin)):
                self.shape(f"{name}.Pin{side}{i}", px, py, pw, ph, fill=NAVY)
        self.shape(name+".Body", x, y, size, size, preset="roundRect",
                   adj="adj:val 8000", fill=fill, line=f"{NAVY}:1.5")
        self.shape(name+".Label", x, y, size, size, text=label, bold="true", size=15)
        self.group(name, [c["props"]["name"] for c in self.commands[start:]])

    def wave(self, name, x, y, w, h, color, cycles=4):
        step = w / cycles
        points = [(x, y+h)]
        for i in range(cycles):
            a = x+i*step
            points.extend([(a+step*.25, y+h), (a+step*.25, y),
                           (a+step*.7, y), (a+step*.7, y+h), (a+step, y+h)])
        for i, (p, q) in enumerate(zip(points, points[1:])):
            self.line(f"{name}.{i}", *p, *q, color=color)

    def asset(self, name, filename, x, y, w, h, crop):
        visible_w = 1254 - crop[0] - crop[2]
        visible_h = 1254 - crop[1] - crop[3]
        fitted_w = min(w, h * visible_w / visible_h)
        fitted_h = fitted_w * visible_h / visible_w
        self.add("picture", name, src=str(ROOT/"figure/ppt-assets"/filename),
                 x=unit(x+(w-fitted_w)/2), y=unit(y+(h-fitted_h)/2),
                 width=unit(fitted_w), height=unit(fitted_h),
                 crop=",".join(str(100*v/1254) for v in crop), alt=name)


def build_commands():
    """Five main stages and two centered, parallel snapshot consumers."""
    d = Diagram()
    stages = [("RTL", .3, 3.1, "RTL Design"),
              ("Partition", 3.75, 3.1, "Automated\nPartitioning"),
              ("Deploy", 7.2, 3.7, "Multi-FPGA\nDeployment"),
              ("Cycle", 11.25, 3.9, "Cycle-Accurate\nExecution &\nGlobal Pause"),
              ("Snapshot", 15.5, 3.2, "Global Snapshot")]
    for i, (name, x, w, title) in enumerate(stages, 1):
        d.shape(name+".Panel", x, .35, w, 4.15, preset="roundRect",
                adj="adj:val 4500", fill="F1F8FB", line="8EB5CB:1.2")
        d.shape(name+".Number", x+w/2-.24, .08, .48, .48, preset="ellipse",
                fill=NAVY)
        d.shape(name+".NumberText", x+w/2-.24, .08, .48, .48,
                text=i, color="FFFFFF", bold="true", size=22)
        d.shape(name+".Title", x+.10, .58 if name == "Cycle" else .62,
                w-.20, 1.08 if name == "Cycle" else .90, text=title,
                bold="true", size=22 if name != "Cycle" else 18)
        if i < 5:
            d.shape(name+".Next", x+w-.03, 2.50, .41, .40,
                    preset="rightArrow", fill=AMBER)
    # Original source PNGs are embedded intact; only transparent margins cropped.
    d.asset("RTL.Asset", "rtl-design.png", .85, 1.68, 2.0, 2.65,
            (286, 233, 275, 180))
    d.asset("Partition.Asset", "circuit-partitioning.png", 4.02, 1.80, 2.56, 2.48,
            (199, 234, 198, 234))
    d.shape("Deploy.Host", 7.65, 1.67, 2.8, .58, preset="roundRect",
            adj="adj:val 7000", fill="DCE8EF", line="7D9DB2:1.2",
            text="Host Runtime", size=20, bold="true")
    d.line("Deploy.Host0", 8.05, 2.25, 8.05, 2.92, arrow=True)
    d.line("Deploy.Host1", 10.05, 2.25, 10.05, 2.92, arrow=True)
    d.chip("Deploy.FPGA0", "FPGA0", 7.49, 3.03, 1.12, BLUE)
    d.chip("Deploy.FPGA1", "FPGA1", 9.49, 3.03, 1.12, GREEN)
    d.line("Deploy.Link", 8.76, 3.58, 9.34, 3.58, both=True)
    d.shape("Deploy.LinkLabel", 8.30, 2.59, 1.50, .36, text="LI-TDM", size=16, bold="true")
    d.shape("Deploy.Fabric", 8.30, 4.12, 1.50, .36, text="Fabric", size=16, bold="true")
    for name, y, color, label in [("0", 1.72, "2584B8", "FPGA0"),
                                   ("1", 3.37, TEAL, "FPGA1")]:
        d.shape("Cycle.Box"+name, 11.52, y, 3.36, .90, preset="roundRect",
                adj="adj:val 5000", fill="FFFFFF", line=f"{color}:1.3")
        d.shape("Cycle.Label"+name, 11.66, y+.03, 1.3, .40,
                text=label, align="left", size=18, bold="true")
        d.wave("Cycle.Wave"+name, 11.72, y+.49, 2.70, .25, color)
    for x in (12.58, 13.82):
        d.line(f"Cycle.Sync{x}", x, 2.62, x, 3.37, dash=True)
    d.line("Cycle.SyncBar", 12.58, 2.99, 13.82, 2.99, dash=True)
    d.shape("Cycle.Pause", 12.87, 2.66, .66, .66, preset="ellipse", fill=AMBER)
    for i in (0, 1):
        d.shape(f"Cycle.PauseBar{i}", 13.075+i*.17, 2.82, .09, .34, fill="FFFFFF")
    d.chip("Snapshot.FPGA0", "FPGA0", 15.83, 1.88, .95, BLUE)
    d.chip("Snapshot.FPGA1", "FPGA1", 15.83, 3.17, .95, GREEN)
    # Separate orthogonal paths meet a shared snapshot; no implied FPGA serial chain.
    for i, y, dest in [(0, 2.35, 2.65), (1, 3.64, 3.23)]:
        d.line(f"Snapshot.In{i}A", 16.90, y, 17.16, y)
        d.line(f"Snapshot.In{i}B", 17.16, y, 17.16, dest)
        d.line(f"Snapshot.In{i}C", 17.16, dest, 17.48, dest, arrow=True)
    d.shape("Snapshot.Database", 17.50, 2.35, .88, 1.12,
            preset="can", fill=BLUE, line=f"{NAVY}:1.5")
    d.shape("Snapshot.Caption", 17.10, 3.52, 1.55, .78,
            text="Global\nSnapshot", size=18, bold="true")
    # Lower pair is centered on the figure, not aligned beneath the last stages.
    for name, x, title in [("Restore", 3.80, "FPGA Restore"),
                            ("Replay", 9.80, "Software RTL Replay")]:
        d.shape(name+".Panel", x, 5.30, 5.4, 2.0, preset="roundRect",
                adj="adj:val 6000", fill="F1F8FB", line="8EB5CB:1.2")
        d.shape(name+".Title", x+.2, 5.39, 5.0, .44, text=title, size=22, bold="true")
    d.line("Snapshot.Output", 17.10, 4.50, 17.10, 4.92)
    d.line("Snapshot.Bus", 6.50, 4.92, 17.10, 4.92)
    for name, x in [("Restore", 6.50), ("Replay", 12.50)]:
        d.line(name+".Input", x, 4.92, x, 5.30, arrow=True)
    d.chip("Restore.FPGA0", "FPGA0", 5.00, 6.00, 1.02, BLUE)
    d.chip("Restore.FPGA1", "FPGA1", 6.95, 6.00, 1.02, GREEN)
    d.shape("Replay.RTL", 10.38, 6.00, .82, 1.04, preset="foldedCorner",
            fill="FFFFFF", line=f"{NAVY}:1.5", text="RTL", size=20, bold="true")
    d.line("Replay.Arrow", 11.40, 6.51, 11.97, 6.51, arrow=True)
    d.shape("Replay.Monitor", 12.17, 5.98, 2.45, 1.08, preset="roundRect",
            adj="adj:val 7000", fill=BLUE, line=f"{NAVY}:1.5")
    d.shape("Replay.Screen", 12.27, 6.08, 2.25, .87, fill="FFFFFF")
    for i, color in enumerate(("2584B8", TEAL, AMBER)):
        d.wave(f"Replay.Trace{i}", 12.38, 6.20+i*.23, 2.02, .13, color, cycles=5)
    d.shape("Replay.Stand", 13.28, 7.06, .23, .12, fill=NAVY)
    d.shape("Replay.Foot", 12.95, 7.18, .89, .035, fill=NAVY)
    d.add("notes", "FigureNotes", text=(
        "Conceptual REMUS workflow, reconstructed from figure/FPGA与RTL全流程图.png. "
        "RTL and partitioning illustrations reuse figure/ppt-assets. All FPGA icons, "
        "labels, waveform traces and flow lines are editable native objects. "
        "Restore and software RTL replay are parallel uses of a global snapshot; "
        "this figure is not evidence of implementation or experimental completion."))
    return d.commands


def main():
    """Generate in build/, validate and render; publish only when requested."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--publish", action="store_true")
    parser.add_argument("--theme", choices=tuple(THEMES), default=DEFAULT_THEME)
    args = parser.parse_args()
    BUILD.mkdir(parents=True, exist_ok=True)
    pptx = BUILD / "REMUS_FPGA_RTL_Workflow.pptx"
    preview = BUILD / "fpga-rtl-workflow.png"
    cli_path = shutil.which("officecli") or "/home/hgh/.local/bin/officecli"
    env = dict(os.environ, OFFICECLI_NO_AUTO_RESIDENT="1")

    def cli(*argv):
        result = subprocess.run([cli_path, *map(str, argv)], env=env,
                                capture_output=True, text=True, check=True)
        if "UNSUPPORTED" in result.stdout + result.stderr:
            raise RuntimeError(result.stdout + result.stderr)
        return result.stdout

    if pptx.exists():
        pptx.unlink()
    cli("create", pptx)
    cli("set", pptx, "/", "--prop", "slideWidth="+unit(19),
        "--prop", "slideHeight="+unit(7.6))
    palette = THEMES[args.theme]
    cli("set", pptx, "/theme", "--prop", "headingFont=Arial", "--prop", "bodyFont=Arial",
        "--prop", f"accent1={palette['accent1']}", "--prop", f"accent2={palette['accent2']}",
        "--prop", f"accent3={palette['accent3']}")
    cli("add", pptx, "/", "--type", "slide", "--prop", "layout=blank", "--prop", "background=FFFFFF")
    (BUILD/"initial.txt").write_text(cli("get", pptx, "/slide[1]", "--depth", "1"))
    batch = BUILD / "commands.json"
    batch.write_text(json.dumps(recolor_commands(build_commands(), args.theme), indent=2))
    (BUILD/"batch.json").write_text(cli("batch", pptx, "--input", batch, "--json"))
    cli("save", pptx)
    for mode in ("text", "issues"):
        result = cli("view", pptx, mode)
        (BUILD/(mode+".txt")).write_text(result)
        print(result)
        if mode == "issues":
            issues_clean = "Found 0 issue(s)" in result
    result = cli("validate", pptx)
    (BUILD/"validate.txt").write_text(result)
    print(result)
    if preview.exists():
        preview.unlink()
    print(cli("view", pptx, "screenshot", "--page", "1", "--screenshot-width", "2400", "-o", preview))
    cli("close", pptx)
    if not issues_clean or "Validation passed" not in result:
        raise RuntimeError("Figure checks failed; inspect build reports and preview before publishing.")
    if args.publish:
        target = ROOT/"pptx/figures"/pptx.name
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(pptx, target)
        shutil.copy2(preview, ROOT/"figure"/preview.name)
    print(pptx)


if __name__ == "__main__":
    main()
