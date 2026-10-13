#!/usr/bin/env python3
"""Build REMUS background slides using OfficeCLI, outside the agent sandbox.

Run with the system Python; no third-party Python packages are required.
The default output stays in thesis/build/pptx until it has been reviewed.
"""

import argparse
import json
import os
from pathlib import Path
import shutil
import subprocess


THESIS = Path(__file__).resolve().parents[1]
BUILD = THESIS / "build" / "pptx"
TITLE = "1. From RTL Simulation to Multi-FPGA Prototyping"
TITLE_2 = "2. Multi-FPGA Prototyping Is Fast, but Hard to Debug"
TITLE_3 = "3. Key Challenges of Replayable Multi-FPGA Emulation"
TITLE_4 = "4. Research Gap and Goal"
NAVY = "183B56"
TEAL = "008C95"
AMBER = "DF973E"
INK = "20354A"


def inches(value):
    """Format explicit PowerPoint dimensions in inches."""
    return f"{value:.6f}in"


def shape(name, x, y, width, height, **props):
    """Describe one independently editable shape with explicit text defaults."""
    return {
        "command": "add", "parent": "/slide[1]", "type": "shape",
        "props": {
            "name": f"S01.{name}", "x": inches(x), "y": inches(y),
            "width": inches(width), "height": inches(height),
            "fill": "none", "line": "none", "shadow": "none",
            "font": "Arial", "size": "18", "color": INK,
            "margin": "0pt", "autoFit": "none",
            **{key: str(value) for key, value in props.items()},
        },
    }


def picture(name, asset, box, x, y, width):
    """Crop transparent margins in PPTX while preserving the artwork ratio.

    Bounds were measured from the visible artwork, with padding retained for
    anti-aliased edges. Source PNGs are embedded unchanged, never rewritten.
    """
    left, top, right, bottom = box
    height = width * (bottom - top) / (right - left)
    crop = [left, top, 1254 - right, 1254 - bottom]
    return {
        "command": "add", "parent": "/slide[1]", "type": "picture",
        "props": {
            "name": f"S01.{name}",
            "src": str(THESIS / "figure" / "ppt-assets" / asset),
            "alt": {"waveform-monitor.png": "Waveform monitor",
                    "global-snapshot.png": "Global snapshot",
                    "cycle-control.png": "Logical cycle progression",
                    "global-pause.png": "Coordinated pause",
                    "circuit-partitioning.png": "Circuit partitioning",
                    "restore-replay.png": "Restore and replay"}.get(asset, "FPGA chip"),
            "x": inches(x), "y": inches(y), "width": inches(width),
            "height": inches(height),
            "crop": ",".join(f"{100 * value / 1254:.6f}" for value in crop),
        },
    }


def slide_commands():
    """Reconstruct the three-stage reference with native shapes and two assets."""
    commands = [{
        "command": "set", "path": "/slide[1]/shape[1]",
        "props": {
            "name": "S01.Title", "x": "0.35in", "y": "0.14in",
            "width": "12.64in", "height": "0.54in", "font": "Arial",
            "size": "32", "bold": "true", "color": NAVY,
            "margin": "0pt", "autoFit": "none", "fill": "none",
            "line": "none", "shadow": "none",
        },
    }]
    commands.append(shape("TitleRule", 0.35, 0.78, 12.64, 2 / 72, fill=TEAL))
    rows = [
        (1.06, 1.75, "EAF4F3", "RTL Simulation",
         ["Full visibility", "Flexible debugging", "Low performance"]),
        (3.28, 1.75, "F1F5F8", "FPGA Prototyping",
         ["MHz-level execution", "Long software workloads", "Limited by single-FPGA capacity"]),
        (5.49, 1.70, "FCF4E8", "Multi-FPGA Prototyping",
         ["Partition large designs", "Extend capacity", "Enable large-scale SoC execution"]),
    ]
    for index, (y, height, fill, heading, bullets) in enumerate(rows, 1):
        prefix = f"Stage{index}"
        commands.append(shape(f"{prefix}.Panel", 0.35, y, 12.64, height,
                              fill=fill, preset="roundRect", adj="adj:val 10000"))
        commands.append(shape(f"{prefix}.Divider", 5.015, y + 0.17, 0.009, height - 0.34,
                              fill="BDCBD4"))
        commands.append(shape(f"{prefix}.Heading", 5.52, y + 0.20, 7.1, 0.40,
                              text=heading, size=22, bold="true", color=NAVY))
        for bullet_index, text in enumerate(bullets, 1):
            text_y = y + 0.64 + (bullet_index - 1) * 0.32
            commands.append(shape(f"{prefix}.Bullet{bullet_index}", 5.65, text_y + 0.085,
                                  0.105, 0.105, fill=TEAL, preset="ellipse"))
            commands.append(shape(f"{prefix}.Text{bullet_index}", 5.98, text_y, 6.70, 0.32,
                                  text=text))

    # Reference arrows fit within the reserved gap between each pair of panels.
    commands.append(shape("Progress1", 6.37, 2.815, 0.61, 0.455, fill=AMBER,
                          preset="downArrow", adj="adj1:val 48000,adj2:val 55000"))
    commands.append(shape("Progress2", 6.37, 5.035, 0.61, 0.445, fill="91A5B5",
                          preset="downArrow", adj="adj1:val 48000,adj2:val 55000"))

    chip_box = (268, 297, 987, 991)
    commands.append(picture("Monitor", "waveform-monitor.png", (154, 320, 1101, 1004),
                            1.90, 1.285, 1.84))
    commands.append(picture("SingleFPGA", "fpga-chip.png", chip_box, 2.15, 3.51, 1.34))
    commands.append(picture("MultiFPGA.Left", "fpga-chip.png", chip_box, 1.12, 5.82, 1.12))
    commands.append(picture("MultiFPGA.Right", "fpga-chip.png", chip_box, 3.32, 5.82, 1.12))
    commands.append(shape("MultiFPGA.Link", 2.29, 6.185, 0.98, 0.34, fill=AMBER,
                          preset="leftRightArrow", adj="adj1:val 44000,adj2:val 28000"))
    commands.append(shape("PageNumber", 12.72, 7.25, 0.25, 0.20,
                          text="1", size=10, color="607184", align="right"))
    commands.append({
        "command": "add", "parent": "/slide[1]", "type": "notes",
        "props": {"text": (
            "Introduce the capacity-versus-observability motivation. RTL simulation provides "
            "visibility and flexible debugging, but long software workloads are slow. FPGA "
            "prototyping accelerates execution, while one FPGA limits design capacity. "
            "Partitioning across multiple FPGAs extends capacity. The next slide introduces "
            "the need for coordinated debugging. MHz-level execution is a general prototype "
            "characteristic here, not a measured REMUS performance result. Layout reference: "
            "figure/presentation-reference/midterm-background-01.png."
        )},
    })
    return commands


def slide_two_commands():
    """Compare typical prototyping limits with the targeted replay workflow."""
    commands = [slide_commands()[0]]
    commands[0]["props"]["size"] = "30"
    commands.append(shape("TitleRule", 0.35, 0.78, 12.64, 2 / 72, fill=TEAL))
    for name, x, fill, heading, qualifier in [
        ("Prototype", 0.35, "FCF4E8", "Multi-FPGA Prototyping",
         "Typical strengths & limitations"),
        ("Replay", 6.77, "EAF4F3", "Replayable Multi-FPGA Emulation",
         "Target capabilities"),
    ]:
        commands.append(shape(f"{name}.Panel", x, 1.06, 6.22, 6.13, fill=fill,
                              preset="roundRect", adj="adj:val 3000"))
        commands.append(shape(f"{name}.Heading", x + 0.20, 1.32, 5.82, 0.42,
                              text=heading, size=22, bold="true", color=NAVY,
                              align="center"))
        commands.append(shape(f"{name}.Qualifier", x + 0.25, 1.82, 5.72, 0.30,
                              text=qualifier, size=15, color="607184", align="center"))
        commands.append(shape(f"{name}.Divider", x + 0.23, 4.87, 5.76, 0.012,
                              fill="BDCBD4"))

    def badge(name, x, y, positive=True):
        commands.append(shape(f"{name}.Badge", x, y, 0.34, 0.34,
                              fill=TEAL if positive else AMBER, preset="ellipse"))
        if positive:
            commands.append(shape(f"{name}.CheckShort", x + 0.080, y + 0.175,
                                  0.105, 0.043, fill="FFFFFF", rotation=45))
            commands.append(shape(f"{name}.CheckLong", x + 0.125, y + 0.147,
                                  0.160, 0.043, fill="FFFFFF", rotation=315))
        else:
            commands.append(shape(f"{name}.Minus", x + 0.080, y + 0.149,
                                  0.180, 0.043, fill="FFFFFF"))

    left_rows = ["Large design capacity", "High execution speed", "Long software workloads",
                 "Limited visibility", "Limited full-state replay"]
    right_rows = ["Run large RTL designs", "Cycle-consistent global pause",
                  "Full-state extraction", "State restore", "Deterministic replay",
                  "Waveform reconstruction"]
    for column, rows, x, spacing in [("Prototype", left_rows, 0.87, 0.50),
                                     ("Replay", right_rows, 7.17, 0.43)]:
        for index, text in enumerate(rows):
            y = 2.28 + index * spacing
            badge(f"{column}.Item{index + 1}", x, y, column == "Replay" or index < 3)
            commands.append(shape(f"{column}.Text{index + 1}", x + 0.53, y + 0.003,
                                  5.00, 0.34, text=text))

    chip_box = (268, 297, 987, 991)
    for i, x in enumerate((1.09, 2.99, 4.89), 1):
        commands.append(picture(f"Prototype.FPGA{i}", "fpga-chip.png", chip_box,
                                x, 5.36, 0.94))
    commands.append(shape("Prototype.Run", 2.66, 5.03, 1.6, 0.30,
                          text="Run", size=18, bold="true", color=NAVY, align="center"))
    for i, x in enumerate((2.09, 3.99), 1):
        commands.append(shape(f"Prototype.Link{i}", x, 5.67, 0.84, 0.26,
                              fill=AMBER, preset="rightArrow"))
    commands.append(shape("Prototype.VisibilityArrow", 3.31, 6.32, 0.30, 0.30,
                          fill="91A5B5", preset="downArrow"))
    commands.append(shape("Prototype.Visibility", 2.10, 6.64, 2.72, 0.40,
                          text="Limited visibility", size=18, bold="true", color=NAVY,
                          fill="E0E7EC", preset="roundRect", adj="adj:val 15000",
                          align="center", valign="center"))

    nodes = ["Run", "Pause", "Dump", "Restore", "Replay"]
    centers = [7.50 + 1.19 * i for i in range(5)]
    for name, x in zip(nodes, centers):
        commands.append(shape(f"Workflow.{name}", x - 0.52, 5.55, 1.04, 0.51,
                              text=name, size=16, bold="true", color=NAVY,
                              fill="FFF0D8" if name == "Pause" else "FFFFFF",
                              line=f"{AMBER if name == 'Pause' else TEAL}:1.2",
                              preset="roundRect", adj="adj:val 14000",
                              align="center", valign="center"))

    def connector(name, **props):
        commands.append({"command": "add", "parent": "/slide[1]", "type": "connector",
                         "props": {"name": f"S02.{name}", "shape": "straight",
                                   "color": NAVY, "lineWidth": "1.8pt", **props}})

    for start, end in zip(nodes, nodes[1:]):
        connector(f"Workflow.{start}To{end}", **{
            "from": f"/slide[1]/shape[@name=S02.Workflow.{start}]",
            "to": f"/slide[1]/shape[@name=S02.Workflow.{end}]",
            "fromSide": "right", "toSide": "left", "tailEnd": "triangle"})

    # Three editable segments keep the return loop above every workflow box.
    connector("Workflow.ReturnTop", x="7.50in", y="5.22in", width="4.76in",
              height="0in", color=AMBER, lineWidth="2.5pt")
    connector("Workflow.ReturnRight", x="12.26in", y="5.22in", width="0in",
              height="0.33in", color=AMBER, lineWidth="2.5pt")
    connector("Workflow.ReturnLeft", x="7.50in", y="5.22in", width="0in",
              height="0.33in", color=AMBER, lineWidth="2.5pt", tailEnd="triangle")

    commands.append(picture("Workflow.Snapshot", "global-snapshot.png",
                            (210, 206, 1044, 1104), 9.605, 6.28, 0.55))
    commands.append(picture("Workflow.Waveform", "waveform-monitor.png",
                            (154, 320, 1101, 1004), 11.86, 6.29, 0.80))
    for name, target in [("Dump", "Snapshot"), ("Replay", "Waveform")]:
        connector(f"Workflow.{name}Output", **{
            "from": f"/slide[1]/shape[@name=S02.Workflow.{name}]",
            "to": f"/slide[1]/picture[@name=S02.Workflow.{target}]",
            "fromSide": "bottom", "toSide": "top", "tailEnd": "triangle"})
    commands.append(shape("Workflow.SnapshotLabel", 8.88, 6.93, 2.0, 0.25,
                          text="Global snapshot", size=14, color=NAVY, align="center"))
    commands.append(shape("Workflow.WaveformLabel", 11.62, 6.93, 1.28, 0.25,
                          text="Waveform", size=14, color=NAVY, align="center"))
    commands.append(shape("PageNumber", 12.72, 7.25, 0.25, 0.20,
                          text="2", size=10, color="607184", align="right"))
    commands.append({"command": "add", "parent": "/slide[1]", "type": "notes",
                     "props": {"text": (
                         "Contrast typical prototyping strengths and common debug limitations with "
                         "the target capabilities of replayable multi-FPGA emulation. This is a "
                         "research motivation slide, not a completed-feature checklist or an empirical "
                         "comparison of every prototyping system. The right panel and workflow express "
                         "goals; REMUS implementation and validation status are reported later. Dump "
                         "represents collection and aggregation of distributed state into a global "
                         "snapshot. Restore and replay are conceptual stages; execution backends and "
                         "correctness conditions are explained on the technical slides. The return "
                         "loop represents another debugging iteration. Layout reference: "
                         "figure/presentation-reference/midterm-background-02.png."
                     )}})
    for command in commands:
        props = command.get("props", {})
        if "name" in props:
            props["name"] = props["name"].replace("S01.", "S02.")
    return commands


def slide_three_commands():
    """Build four challenge panels, with editable timing and state-flow links."""
    commands = [slide_commands()[0]]
    commands[0]["props"]["size"] = "30"
    commands.append(shape("TitleRule", 0.35, 0.78, 12.64, 2 / 72, fill=TEAL))
    panels = [
        ("Cycle", 0.35, 1.12, "EAF4F3", "Cycle-Accurate\nExecution",
         ["Align DUT cycles across\npartitions", "Account for cross-FPGA\ncommunication latency"]),
        ("Pause", 6.77, 1.12, "F1F5F8", "Cycle-Consistent\nGlobal Pause",
         ["Stop partitions at the\nsame logical cycle", "Drain links for a stable\nsnapshot boundary"]),
        ("State", 0.35, 4.02, "FCF4E8", "Distributed State\nManagement",
         ["Extract local states", "Form a global snapshot\nfor restore and replay"]),
        ("Partition", 6.77, 4.02, "EAF4F3", "Automated\nPartitioning",
         ["Balance resources and\ncut size", "Control Partition\nPropagation Depth (PPD)\nthrough granularity"]),
    ]
    for name, x, y, fill, heading, bullets in panels:
        commands.append(shape(f"{name}.Panel", x, y, 6.22, 2.63, fill=fill,
                              preset="roundRect", adj="adj:val 6500"))
        commands.append(shape(f"{name}.Divider", x + 2.18, y + 0.25, 0.009, 2.13,
                              fill="BDCBD4"))
        commands.append(shape(f"{name}.Heading", x + 2.42, y + 0.23, 3.57, 0.70,
                              text=heading, size=20, bold="true", color=NAVY))
        for i, text in enumerate(bullets):
            top = y + 1.04 + i * 0.68
            commands.append(shape(f"{name}.Bullet{i + 1}", x + 2.46, top + 0.085,
                                  0.10, 0.10, fill=TEAL, preset="ellipse"))
            commands.append(shape(f"{name}.Text{i + 1}", x + 2.72, top, 3.30,
                                  0.82 if name == "Partition" and i == 1 else 0.61,
                                  text=text, size=17))

    chip_box = (268, 297, 987, 991)

    def chip(name, x, y, width):
        commands.append(picture(name, "fpga-chip.png", chip_box, x, y, width))

    def connector(name, **props):
        commands.append({"command": "add", "parent": "/slide[1]", "type": "connector",
                         "props": {"name": f"S03.{name}", "shape": "straight",
                                   "color": AMBER, "lineWidth": "2pt", **props}})

    def link(name, start, end, start_side, end_side, **props):
        connector(name, **{"from": f"/slide[1]/picture[@name=S03.{start}]",
                           "to": f"/slide[1]/picture[@name=S03.{end}]",
                           "fromSide": start_side, "toSide": end_side, **props})

    # Shared logical-cycle progress: two chips joined by editable pulse segments.
    chip("Cycle.Left", 0.55, 2.22, 0.66)
    chip("Cycle.Right", 1.77, 2.22, 0.66)
    commands.append(picture("Cycle.Clock", "cycle-control.png", (164, 126, 1092, 1122),
                            1.25, 1.57, 0.48))
    points = [(1.24, 2.60), (1.33, 2.60), (1.33, 2.35), (1.46, 2.35),
              (1.46, 2.60), (1.59, 2.60), (1.59, 2.35), (1.71, 2.35),
              (1.71, 2.60), (1.74, 2.60)]
    for i, ((x1, y1), (x2, y2)) in enumerate(zip(points, points[1:])):
        connector(f"Cycle.Pulse{i}", x=inches(min(x1, x2)), y=inches(min(y1, y2)),
                  width=inches(abs(x2 - x1)), height=inches(abs(y2 - y1)),
                  lineWidth="2.3pt")
    commands.append(shape("Cycle.Label", 0.52, 3.13, 1.94, 0.28,
                          text="DUT cycle n", size=14, color=NAVY, align="center"))

    # Triangular multi-partition diagram: the pause glyph alone is not sufficient.
    chip("Pause.Top", 7.57, 1.48, 0.59)
    chip("Pause.Left", 7.01, 2.64, 0.59)
    chip("Pause.Right", 8.13, 2.64, 0.59)
    link("Pause.SyncLeft", "Pause.Top", "Pause.Left", "bottom", "top")
    link("Pause.SyncRight", "Pause.Top", "Pause.Right", "bottom", "top")
    link("Pause.SyncBottom", "Pause.Left", "Pause.Right", "right", "left")
    commands.append(picture("Pause.Symbol", "global-pause.png", (140, 142, 1119, 1121),
                            7.62, 2.14, 0.49))
    commands.append(shape("Pause.Label", 6.97, 3.35, 1.80, 0.28,
                          text="Same DUT cycle n", size=13, color=NAVY, align="center"))

    # Each partition contributes a local dump to the aggregate global snapshot.
    for i, x in enumerate((0.53, 1.21, 1.89), 1):
        chip(f"State.FPGA{i}", x, 4.65, 0.55)
    commands.append(shape("State.LocalLabel", 0.52, 4.25, 1.94, 0.27,
                          text="Local states", size=14, color=NAVY, align="center"))
    commands.append(picture("State.Snapshot", "global-snapshot.png",
                            (210, 206, 1044, 1104), 1.235, 5.68, 0.50))
    # A bus gathers the three drops; the final arrow enters the snapshot.
    for i, center in enumerate((0.805, 1.485, 2.165), 1):
        connector(f"State.Drop{i}", x=inches(center), y="5.18in", width="0in",
                  height="0.35in", color=TEAL)
    connector("State.Bus", x="0.805in", y="5.53in", width="1.36in", height="0in", color=TEAL)
    connector("State.Aggregate", x="1.485in", y="5.53in", width="0in", height="0.15in",
              color=TEAL, tailEnd="triangle")
    commands.append(shape("State.GlobalLabel", 0.52, 6.30, 1.94, 0.25,
                          text="Global snapshot", size=13, color=NAVY, align="center"))

    commands.append(picture("Partition.Circuit", "circuit-partitioning.png",
                            (199, 234, 1056, 1020), 7.06, 4.69, 1.62))
    commands.append(shape("Partition.Label", 6.97, 6.40, 1.84, 0.27,
                          text="Partitioned design", size=13, color=NAVY, align="center"))
    commands.append(shape("Takeaway", 0.55, 6.95, 12.20, 0.35,
                          text="Replayable emulation requires scalable deployment and globally coordinated debugging.",
                          size=18, color=NAVY, bold="true", align="center"))
    commands.append(shape("PageNumber", 12.72, 7.25, 0.25, 0.20,
                          text="3", size=10, color="607184", align="right"))
    commands.append({"command": "add", "parent": "/slide[1]", "type": "notes",
                     "props": {"text": (
                         "This slide introduces research challenges, not completed REMUS results. "
                         "DUT logical cycles must remain aligned despite cross-FPGA communication "
                         "latency; the pulse is conceptual, not a measured clock waveform. Global "
                         "pause requires all partitions at the same DUT cycle and drained links, "
                         "providing a stable boundary. Local partition states must be mapped and "
                         "aggregated into a global snapshot for restoration and deterministic replay. "
                         "Partitioning must balance resources and cut size while controlling Partition "
                         "Propagation Depth (PPD) through granularity. Multiple chip icons and the "
                         "partitioned circuit illustrate the problem, not an experimentally verified "
                         "FPGA count. Reference: figure/presentation-reference/midterm-background-03.png."
                     )}})
    for command in commands:
        props = command.get("props", {})
        if "name" in props:
            props["name"] = props["name"].replace("S01.", "S03.")
    return commands


def slide_four_commands():
    """Compare deployment and replay capabilities without implying universal gaps."""
    commands = [slide_commands()[0]]
    commands.append(shape("TitleRule", 0.35, 0.78, 12.64, 2 / 72, fill=TEAL))
    columns = [
        ("Prototype", 0.35, "EAF4F3", "Multi-FPGA\nPrototyping", "Primary focus: capacity & speed"),
        ("Single", 4.64, "F1F5F8", "Single-FPGA\nReplayable Emulation", "Scan-based state & replay"),
        ("REMUS", 8.93, "FCF4E8", "This Work: REMUS", "Research Goal"),
    ]
    common_rows = ["Scalable deployment", "Fast execution", "Cycle-consistent pause",
                   "Global snapshot", "Deterministic replay", "Waveform reconstruction"]
    for name, x, fill, heading, qualifier in columns:
        commands.append(shape(f"{name}.Panel", x, 1.06, 4.06, 5.35, fill=fill,
                              preset="roundRect", adj="adj:val 4500"))
        commands.append(shape(f"{name}.Heading", x + 0.14,
                              1.40 if name == "REMUS" else 1.22, 3.78, 0.70,
                              text=heading, size=21, color=NAVY, bold="true", align="center"))
        commands.append(shape(f"{name}.Qualifier", x + 0.18, 2.04, 3.70, 0.27,
                              text=qualifier, size=14, color=TEAL if name == "REMUS" else "607184",
                              bold="true" if name == "REMUS" else "false", align="center"))
        commands.append(shape(f"{name}.Divider", x + 0.20, 3.48, 3.66, 0.012, fill="BDCBD4"))
        rows = list(common_rows)
        if name == "Single":
            rows[0] = "Limited by one FPGA"
            rows[2] = "Cycle-controlled pause"
            rows[3] = "Full-state snapshot"
        for i, text in enumerate(rows):
            y = 3.68 + i * 0.40
            variable = name == "Prototype" and i >= 2
            limited = name == "Single" and i == 0
            badge_x = x + 0.25
            commands.append(shape(f"{name}.Status{i + 1}", badge_x, y, 0.29, 0.29,
                                  fill=AMBER if variable or limited else TEAL, preset="ellipse"))
            if variable:
                commands.append(shape(f"{name}.Variable{i + 1}", badge_x, y - 0.002,
                                      0.29, 0.29, text="?", size=17, bold="true",
                                      color="FFFFFF", align="center", valign="center"))
            elif limited:
                commands.append(shape(f"{name}.Minus{i + 1}", badge_x + 0.065, y + 0.124,
                                      0.16, 0.042, fill="FFFFFF"))
            else:
                commands.append(shape(f"{name}.CheckShort{i + 1}", badge_x + 0.067, y + 0.151,
                                      0.092, 0.037, fill="FFFFFF", rotation=45))
                commands.append(shape(f"{name}.CheckLong{i + 1}", badge_x + 0.108, y + 0.127,
                                      0.137, 0.037, fill="FFFFFF", rotation=315))
            commands.append(shape(f"{name}.Text{i + 1}", x + 0.70, y - 0.007, 3.19, 0.34,
                                  text=text, size=17))
        footnote = {"Prototype": "Debug support varies by system",
                    "Single": "Replay within single-FPGA capacity",
                    "REMUS": "Target capabilities; validation follows"}[name]
        commands.append(shape(f"{name}.Scope", x + 0.18, 6.10, 3.70, 0.25,
                              text=footnote, size=12, color="607184", align="center"))

    chip_box = (268, 297, 987, 991)
    commands.append(picture("Prototype.Left", "fpga-chip.png", chip_box, 0.91, 2.44, 0.91))
    commands.append(picture("Prototype.Right", "fpga-chip.png", chip_box, 2.94, 2.44, 0.91))
    commands.append(shape("Prototype.Link", 1.91, 2.75, 0.94, 0.27, fill=AMBER,
                          preset="leftRightArrow"))

    commands.append(picture("Single.FPGA", "fpga-chip.png", chip_box, 5.18, 2.44, 0.91))
    # Native monitor frame keeps the host-state illustration editable.
    commands.append(shape("Single.Host", 6.74, 2.55, 1.17, 0.65, fill="FFFFFF",
                          line=f"{NAVY}:2.5", preset="roundRect", adj="adj:val 6500"))
    commands.append(shape("Single.HostStand", 7.265, 3.21, 0.12, 0.12, fill=NAVY))
    commands.append(shape("Single.HostFoot", 7.065, 3.33, 0.52, 0.045, fill=NAVY))
    commands.append(picture("Single.Snapshot", "global-snapshot.png",
                            (210, 206, 1044, 1104), 7.105, 2.63, 0.44))
    commands.append({"command": "add", "parent": "/slide[1]", "type": "connector",
                     "props": {"name": "S04.Single.StateTransfer", "shape": "straight",
                               "from": "/slide[1]/picture[@name=S04.Single.FPGA]",
                               "to": "/slide[1]/shape[@name=S04.Single.Host]",
                               "fromSide": "right", "toSide": "left",
                               "color": NAVY, "lineWidth": "2pt",
                               "headEnd": "triangle", "tailEnd": "triangle"}})
    commands.append(picture("REMUS.Left", "fpga-chip.png", chip_box, 9.18, 2.55, 0.70))
    commands.append(picture("REMUS.Right", "fpga-chip.png", chip_box, 10.34, 2.55, 0.70))
    commands.append(shape("REMUS.Link", 9.925, 2.79, 0.37, 0.20, fill=AMBER,
                          preset="leftRightArrow"))
    commands.append(picture("REMUS.Replay", "restore-replay.png", (169, 159, 1101, 1088),
                            11.26, 2.61, 0.57))
    commands.append(picture("REMUS.Snapshot", "global-snapshot.png",
                            (210, 206, 1044, 1104), 12.09, 2.59, 0.55))

    commands.append(shape("Goal.Panel", 0.35, 6.58, 12.64, 0.63, fill="EAF4F3",
                          preset="roundRect", adj="adj:val 15000"))
    for i, (diameter, fill) in enumerate([(0.47, AMBER), (0.35, "FFFFFF"),
                                         (0.25, AMBER), (0.13, "FFFFFF"), (0.065, AMBER)]):
        commands.append(shape(f"Goal.Target{i}", 1.22 - diameter / 2,
                              6.895 - diameter / 2, diameter, diameter,
                              fill=fill, preset="ellipse"))
    commands.append(shape("Goal.Arrow", 1.245, 6.66, 0.29, 0.10, fill=AMBER,
                          preset="rightArrow", rotation=315))
    commands.append(shape("Goal.Divider", 1.97, 6.69, 0.009, 0.40, fill="BDCBD4"))
    commands.append(shape("Goal.Text", 2.26, 6.63, 10.39, 0.55,
                          text="Goal: combine multi-FPGA scalability with replayable emulation\nfor large-scale SoC debugging.",
                          size=18, color=NAVY))
    commands.append(shape("PageNumber", 12.72, 7.25, 0.25, 0.20,
                          text="4", size=10, color="607184", align="right"))
    commands.append({"command": "add", "parent": "/slide[1]", "type": "notes",
                     "props": {"text": (
                         "Research motivation: combine multi-FPGA deployment with replayable "
                         "emulation. The prototype column indicates typical focus; amber marks "
                         "system-dependent debug capabilities, not universal absence. The middle "
                         "column represents scan-based single-FPGA replayable emulation such as "
                         "the REMU foundation described in docs/thesis-writing-guidelines.md and "
                         "src/proposal/significance_and_related_work.tex. A full-state snapshot in "
                         "that setting fits within one FPGA's capacity. REMUS is explicitly a "
                         "Research Goal: its checks are target capabilities, not measured results "
                         "or a completed-feature checklist. The diagram is conceptual and does "
                         "not establish restoration backend or a tested FPGA count. No exhaustive "
                         "prior-art or novelty claim is made by this qualitative comparison. "
                         "Layout: figure/presentation-reference/midterm-background-04.png."
                     )}})
    for command in commands:
        props = command.get("props", {})
        if "name" in props:
            props["name"] = props["name"].replace("S01.", "S04.")
    return commands


def main():
    """Build, inspect, and render one slide through OfficeCLI outside the sandbox."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--slide", type=int, choices=(1, 2, 3, 4), default=1)
    parser.add_argument("--output", type=Path)
    parser.add_argument("--preview", type=Path)
    parser.add_argument("--officecli", default=shutil.which("officecli") or "/home/hgh/.local/bin/officecli")
    args = parser.parse_args()
    args.output = (args.output or BUILD / f"REMUS_Background_Slide_{args.slide}.pptx").resolve()
    args.preview = (args.preview or BUILD / f"midterm-background-{args.slide:02}.png").resolve()
    title, build_commands = {1: (TITLE, slide_commands), 2: (TITLE_2, slide_two_commands),
                             3: (TITLE_3, slide_three_commands),
                             4: (TITLE_4, slide_four_commands)}[args.slide]
    commands = build_commands()
    log_prefix = f"slide-{args.slide:02}"
    BUILD.mkdir(parents=True, exist_ok=True)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.preview.parent.mkdir(parents=True, exist_ok=True)
    env = dict(os.environ, OFFICECLI_NO_AUTO_RESIDENT="1")

    def cli(*arguments):
        result = subprocess.run([args.officecli, *map(str, arguments)], env=env,
                                capture_output=True, text=True, check=True)
        if "UNSUPPORTED" in result.stdout + result.stderr:
            raise RuntimeError(result.stdout + result.stderr)
        return result.stdout

    # Only the chosen build output is replaced; source assets and old decks stay intact.
    if args.output.exists():
        args.output.unlink()
    cli("create", args.output)
    cli("set", args.output, "/", "--prop", "slideSize=widescreen")
    cli("set", args.output, "/theme", "--prop", "headingFont=Arial", "--prop", "bodyFont=Arial",
        "--prop", f"accent1={NAVY}", "--prop", f"accent2={TEAL}", "--prop", f"accent3={AMBER}")
    cli("add", args.output, "/", "--type", "slide", "--prop", "layout=blank",
        "--prop", "background=FFFFFF", "--prop", f"title={title}")
    (BUILD / f"{log_prefix}-initial.txt").write_text(cli("get", args.output, "/slide[1]", "--depth", "1"))
    commands_path = BUILD / f"{log_prefix}.json"
    commands_path.write_text(json.dumps(commands, indent=2) + "\n")
    (BUILD / f"{log_prefix}-batch.json").write_text(cli("batch", args.output, "--input", commands_path, "--json"))
    cli("save", args.output)
    for mode in ("text", "issues", "outline"):
        report = cli("view", args.output, mode)
        (BUILD / f"{log_prefix}-{mode}.txt").write_text(report)
        print(report.strip())
    print(cli("validate", args.output).strip())
    if args.preview.exists():
        args.preview.unlink()
    print(cli("view", args.output, "screenshot", "--page", "1", "-o", args.preview).strip())
    cli("close", args.output)
    print(args.output)


if __name__ == "__main__":
    main()
