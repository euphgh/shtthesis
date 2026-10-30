#!/usr/bin/env python3
"""Build an editable, standalone checkpoint/replay figure using OfficeCLI.

Run outside the sandbox. The source PNG and report references are not changed.
The pure shape helpers are reused from the standalone workflow figure; this
module owns all checkpoint-specific geometry, wording and export paths.
"""

import argparse
import json
import os
from pathlib import Path
import shutil
import subprocess
from midterm_pptx.theme import DEFAULT_THEME, THEMES, recolor_commands

from build_fpga_rtl_workflow import Diagram, ROOT, NAVY, TEAL, AMBER, BLUE, GREEN, unit

BUILD = ROOT / "build/pptx/checkpoint-replay"
STEM = "REMUS_Checkpoint_and_Replay"


class CheckpointDiagram(Diagram):
    """Reusable native folder, file and staggered-chip components."""

    def panel(self, name, x, y, w, h, fill="FFFFFF", border="8EB5CB"):
        self.shape(name, x, y, w, h, preset="roundRect", adj="adj:val 4500",
                   fill=fill, line=f"{border}:1.2")

    def folder(self, name, x, y, scale=.45):
        self.shape(name+".Tab", x+.03, y, scale*.45, scale*.27,
                   fill=BLUE, line=f"{NAVY}:1.1", preset="roundRect")
        self.shape(name+".Body", x, y+scale*.16, scale, scale*.64,
                   fill=BLUE, line=f"{NAVY}:1.1", preset="roundRect",
                   adj="adj:val 7000")
        self.group(name, [name+".Tab", name+".Body"])

    def file(self, name, x, y, w, h, text, fill, font=18):
        self.shape(name+".Page", x, y, w, h, preset="foldedCorner",
                   fill=fill, line=f"{NAVY}:1.2")
        # Text is independent of the foldedCorner preset's inset text area.
        self.shape(name+".Text", x+.06, y+.24, w-.12, h-.30,
                   text=text, size=font, bold="true")
        self.group(name, [name+".Page", name+".Text"])

    def chip_stack(self, name, x, y, size=1.22):
        """Three complete chip silhouettes with transparent space around the pins.

        Each chip is a native group containing only pins, body and label.
        No backing rectangle masks the other chips in the staggered stack.
        All chips use equal size and equal diagonal offset; no internal partitions.
        """
        groups = []
        for depth, fill in [(2, "DCEEEA"), (1, "BCDCD5"), (0, GREEN)]:
            px, py = x+depth*.34, y-depth*.34
            part = f"{name}.Chip{depth}"
            start = len(self.commands)
            for i in range(5):
                at = size*(.15+i*.155)
                for side, a, b, w, h in (
                    ("Top", px+at, py-.10, .07, .10),
                    ("Bottom", px+at, py+size, .07, .10),
                    ("Left", px-.10, py+at, .10, .07),
                    ("Right", px+size, py+at, .10, .07)):
                    self.shape(f"{part}.{side}{i}", a, b, w, h, fill=NAVY)
            self.shape(part+".Body", px, py, size, size, fill=fill,
                       line=f"{NAVY}:1.5", preset="roundRect", adj="adj:val 7000")
            if depth == 0:
                self.shape(part+".Label", px, py, size, size,
                           text="FPGA", bold="true", size=21)
            members = [c["props"]["name"] for c in self.commands[start:]]
            self.group(part, members)
            groups.append(f"/slide[1]/group[@name={part}]")
        self.add("group", name, shapes=",".join(groups))


def build_commands():
    """Same-cycle collection, one expanded checkpoint, two restore paths."""
    d = CheckpointDiagram()
    for name, x, w, title, fill in (
        ("Distributed", .25, 6.15, "Distributed FPGA State", "F1F8FB"),
        ("Host", 7.35, 6.00, "Global Snapshot on Host", "FFFAF0"),
        ("Paths", 14.30, 5.45, "Restore / Replay Paths", "F1F8FB")):
        d.panel(name+".Panel", x, .25, w, 9.50, fill)
        d.shape(name+".Title", x+.12, .52, w-.24, .58,
                text=title, size=23, bold="true")

    # The scan-state boundary encloses registers and SRAM only.
    for i, y in [(0, 1.50), (1, 5.60)]:
        name = f"FPGA{i}"
        d.panel(name+".Panel", .50, y, 5.65, 3.55)
        d.shape(name+".Title", .70, y+.12, 2.0, .45,
                text=f"FPGA {i}", size=22, bold="true", align="left")
        d.panel(name+".Partition", .72, y+.65, 2.65, 2.67, "EEF6FB")
        d.shape(name+".PartTitle", .82, y+.70, 2.45, .40,
                text=f"Partition {i}", size=19, bold="true")
        d.shape(name+".PartRTL", .82, y+1.10, 2.45, .36,
                text="Partial DUT RTL", size=17)
        d.shape(name+".ScanBoundary", .87, y+1.52, 2.35, 1.00,
                preset="roundRect", adj="adj:val 4500", fill="FFFFFF", line=f"{TEAL}:1.3:dash")
        for label, dy in [("Registers", 1.62), ("SRAM", 2.04)]:
            d.shape(name+"."+label, .98, y+dy, 2.13, .36,
                    fill="EAF4F3", text=label, size=18)
        d.shape(name+".Combinational", .98, y+2.57, 2.13, .68,
                text="Combinational Logic", size=16, fill="C5D7E5", line="8BA7BC:1")
        d.panel(name+".DDR", 3.70, y+.65, 2.23, 2.67, "FFF6E5", AMBER)
        d.shape(name+".DDRTitle", 3.81, y+.75, 2.01, .42,
                text=f"DDR {i}", size=21, bold="true")
        d.panel(name+".ScanData", 3.86, y+1.25, 1.91, 1.19, "DCEEF9", "2584B8")
        d.shape(name+".ScanText", 3.90, y+1.28, 1.83, 1.13,
                text=f"Scan Chain\nData\n(part {i})", size=16, bold="true")
        d.line(name+".ScanOut", 3.22, y+1.82, 3.86, y+1.82, color=TEAL, arrow=True)
        if i == 0:
            d.panel(name+".Memory", 3.86, y+2.52, 1.91, .70, "EAF4F3", TEAL)
            d.shape(name+".MemoryText", 3.90, y+2.53, 1.83, .68,
                    text="RAM Model\nData", size=16, bold="true")
        # DDR-level outputs include all local payloads, not only Scan Chain Data.
        d.line(name+".Collect", 5.93, y+1.82, 6.88, y+1.82)
    d.shape("Distributed.More", 2.85, 5.07, 1.0, .46, text="...", size=22, bold="true")
    d.shape("Distributed.ScanLegend", .65, 9.23, 5.35, .34,
            text="Dashed boundary: scanned state", size=16, color=TEAL)
    d.line("Host.CollectBus", 6.88, 3.32, 6.88, 7.42)
    d.line("Host.CollectArrow", 6.88, 5.35, 7.68, 5.35, arrow=True)

    # Only cycle 0 is expanded. Header strips of later cycles remain visible.
    d.folder("Host.RootFolder", 7.72, 1.34, .48)
    d.shape("Host.RootLabel", 8.32, 1.29, 3.70, .48, text="ckpt/",
            size=22, bold="true", align="left")
    d.panel("Checkpoint.Cycle100", 8.20, 2.00, 4.85, 3.92, "E7EEF3", "8CA4B5")
    d.shape("Checkpoint.Cycle100Label", 8.44, 2.04, 4.35, .40,
            text="DUT Cycle 100   ...", size=18, bold="true", align="left")
    d.panel("Checkpoint.Cycle20", 7.94, 2.55, 4.85, 3.70, "E3F0F6", "6B9DBB")
    d.shape("Checkpoint.Cycle20Label", 8.18, 2.59, 4.35, .40,
            text="DUT Cycle 20", size=18, bold="true", align="left")
    d.panel("Checkpoint.Cycle0", 7.68, 3.10, 5.20, 3.48, "FFFFFF", "2584B8")
    d.folder("Checkpoint.Cycle0Folder", 7.92, 3.32, .42)
    d.shape("Checkpoint.Cycle0Label", 8.47, 3.24, 3.80, .50,
            text="0/  ·  DUT Cycle 0", size=20, bold="true", align="left")
    for name, x, text, color in (
        ("Part0", 7.90, "scanchain\npart_0", "DCEEF9"),
        ("Part1", 9.57, "scanchain\npart_1", "DCEEF9"),
        ("Memory", 11.24, "RAM Model\nData", "EAF4F3")):
        d.file("Checkpoint."+name, x, 4.03, 1.43, 1.78, text, color, font=15)
    d.shape("Checkpoint.SameCycle", 7.90, 5.98, 4.76, .44,
            text="All partitions · same cycle", size=16, bold="true")

    # Auxiliary files are distinct from cycle snapshots. Avoid input-arrow clutter.
    d.file("Aux.Input", 7.85, 7.65, 2.12, 1.53, "Input Traces", "FFF0D9", font=18)
    d.file("Aux.Mapping", 10.45, 7.65, 2.48, 1.53,
           "State Mapping\nMetadata", "EDF0F3", font=18)
    d.shape("Aux.Heading", 7.73, 7.18, 5.15, .35,
            text="Supporting records and metadata", size=17, align="left")

    # A single selected snapshot feeds both paths; routing never crosses labels.
    d.line("Restore.SelectedSnapshot", 12.88, 5.35, 13.78, 5.35)
    d.line("Restore.PathBus", 13.78, 3.36, 13.78, 7.28)
    d.line("Restore.HardwareArrow", 13.78, 3.36, 14.60, 3.36, arrow=True)
    d.line("Restore.SoftwareArrow", 13.78, 7.28, 14.60, 7.28, arrow=True)

    d.panel("Restore.Panel", 14.60, 1.53, 4.85, 3.90, "EAF4F3", TEAL)
    d.shape("Restore.Title", 14.80, 1.75, 4.45, .52,
            text="FPGA Restore", size=23, bold="true")
    d.chip_stack("Restore.Chips", 16.05, 3.05, size=1.18)
    d.shape("Restore.Description", 14.87, 4.43, 4.30, .77,
            text="Write back by partition\nRestore local states", size=19)

    d.panel("Replay.Panel", 14.60, 6.00, 4.85, 3.31, "F1F5F8", "6B8AA0")
    d.shape("Replay.Title", 14.80, 6.22, 4.45, .52,
            text="Software RTL Replay", size=23, bold="true")
    d.panel("Replay.Monitor", 15.91, 6.99, 2.23, 1.10, BLUE, NAVY)
    d.shape("Replay.Screen", 16.01, 7.09, 2.03, .86, fill="FFFFFF")
    d.wave("Replay.Trace0", 16.16, 7.25, 1.73, .18, "2584B8", cycles=3)
    d.wave("Replay.Trace1", 16.16, 7.62, 1.73, .18, TEAL, cycles=3)
    d.shape("Replay.Stand", 16.92, 8.09, .22, .15, fill=NAVY)
    d.shape("Replay.Foot", 16.54, 8.24, .98, .045, fill=NAVY)
    d.shape("Replay.Description", 14.87, 8.40, 4.30, .73,
            text="Decode by state mapping\nRestore and replay", size=19)
    # The one auxiliary edge is the mapping dependency of software RTL decoding.
    d.line("Mapping.AuxA", 12.93, 8.52, 13.55, 8.52, color="607184", dash=True)
    d.line("Mapping.AuxB", 13.55, 8.52, 13.55, 8.95, color="607184", dash=True)
    d.line("Mapping.AuxC", 13.55, 8.95, 14.60, 8.95, color="607184", dash=True, arrow=True)
    d.add("notes", "FigureNotes", text=(
        "Standalone thesis figure rebuilt from figure/ckpt-and-replay.png. "
        "Dashed partition boundaries include registers and SRAM, not combinational logic. "
        "Host collects all partition data for the same DUT cycle. Only illustrative "
        "cycle 0 is expanded; cycles 20 and 100 are compact overlapping cards. "
        "Input Traces are supporting records for hardware/software restoration and replay; "
        "their dependencies are described in the report rather than drawn as extra arrows. "
        "State mapping metadata is used to decode partition state for software RTL replay. "
        "The three-chip stack indicates multiple FPGA targets, not a measured platform size. "
        "File labels are conceptual, not a complete on-disk schema."))
    return d.commands


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--publish", action="store_true",
                        help="Copy output to delivery paths after checks; review PNG first.")
    parser.add_argument("--theme", choices=tuple(THEMES), default=DEFAULT_THEME)
    args = parser.parse_args()
    BUILD.mkdir(parents=True, exist_ok=True)
    pptx = BUILD / f"{STEM}.pptx"
    preview = BUILD / "checkpoint-and-replay.png"
    executable = shutil.which("officecli") or "/home/hgh/.local/bin/officecli"
    env = dict(os.environ, OFFICECLI_NO_AUTO_RESIDENT="1")

    def cli(*arguments):
        result = subprocess.run([executable, *map(str, arguments)], env=env,
                                capture_output=True, text=True, check=True)
        if "UNSUPPORTED" in result.stdout + result.stderr:
            raise RuntimeError(result.stdout + result.stderr)
        return result.stdout

    if pptx.exists():
        pptx.unlink()
    cli("create", pptx)
    cli("set", pptx, "/", "--prop", "slideWidth="+unit(20),
        "--prop", "slideHeight="+unit(10))
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
        report = cli("view", pptx, mode)
        (BUILD/(mode+".txt")).write_text(report)
        print(report)
        if mode == "issues":
            clean = "Found 0 issue(s)" in report
    validation = cli("validate", pptx)
    (BUILD/"validate.txt").write_text(validation)
    print(validation)
    if preview.exists():
        preview.unlink()
    print(cli("view", pptx, "screenshot", "--page", "1", "-o", preview))
    cli("close", pptx)
    if not clean or "Validation passed" not in validation:
        raise RuntimeError("Figure checks failed; inspect reports and preview.")
    if args.publish:
        shutil.copy2(pptx, ROOT/"pptx/figures"/pptx.name)
        shutil.copy2(preview, ROOT/"figure"/preview.name)
    print(pptx)


if __name__ == "__main__":
    main()
