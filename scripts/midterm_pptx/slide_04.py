"""Page 4: Research Gap and Goal."""

from .common import SlideAPI, NAVY, TEAL, AMBER

TITLE = '4. Research Gap and Goal'
slide = SlideAPI(4)


def build_commands():
    """Compare deployment and replay capabilities without implying universal gaps."""
    commands = [slide.title(size=32)]
    commands.append(slide.shape("TitleRule", 0.35, 0.78, 12.64, 2 / 72, fill=TEAL))
    columns = [
        ("Prototype", 0.35, "EAF4F3", "Multi-FPGA\nPrototyping", "Primary focus: capacity & speed"),
        ("Single", 4.64, "F1F5F8", "Single-FPGA\nReplayable Emulation", "Scan-based state & replay"),
        ("REMUS", 8.93, "FCF4E8", "This Work: REMUS", "Research Goal"),
    ]
    common_rows = ["Scalable deployment", "Fast execution", "Cycle-consistent pause",
                   "Global snapshot", "Deterministic replay", "Waveform reconstruction"]
    for name, x, fill, heading, qualifier in columns:
        commands.append(slide.shape(f"{name}.Panel", x, 1.06, 4.06, 5.35, fill=fill,
                              preset="roundRect", adj="adj:val 4500"))
        commands.append(slide.shape(f"{name}.Heading", x + 0.14,
                              1.40 if name == "REMUS" else 1.22, 3.78, 0.70,
                              text=heading, size=21, color=NAVY, bold="true", align="center"))
        commands.append(slide.shape(f"{name}.Qualifier", x + 0.18, 2.04, 3.70, 0.27,
                              text=qualifier, size=14, color=TEAL if name == "REMUS" else "607184",
                              bold="true" if name == "REMUS" else "false", align="center"))
        commands.append(slide.shape(f"{name}.Divider", x + 0.20, 3.48, 3.66, 0.012, fill="BDCBD4"))
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
            commands.append(slide.shape(f"{name}.Status{i + 1}", badge_x, y, 0.29, 0.29,
                                  fill=AMBER if variable or limited else TEAL, preset="ellipse"))
            if variable:
                commands.append(slide.shape(f"{name}.Variable{i + 1}", badge_x, y - 0.002,
                                      0.29, 0.29, text="?", size=17, bold="true",
                                      color="FFFFFF", align="center", valign="center"))
            elif limited:
                commands.append(slide.shape(f"{name}.Minus{i + 1}", badge_x + 0.065, y + 0.124,
                                      0.16, 0.042, fill="FFFFFF"))
            else:
                commands.append(slide.shape(f"{name}.CheckShort{i + 1}", badge_x + 0.067, y + 0.151,
                                      0.092, 0.037, fill="FFFFFF", rotation=45))
                commands.append(slide.shape(f"{name}.CheckLong{i + 1}", badge_x + 0.108, y + 0.127,
                                      0.137, 0.037, fill="FFFFFF", rotation=315))
            commands.append(slide.shape(f"{name}.Text{i + 1}", x + 0.70, y - 0.007, 3.19, 0.34,
                                  text=text, size=17))
        footnote = {"Prototype": "Debug support varies by system",
                    "Single": "Replay within single-FPGA capacity",
                    "REMUS": "Target capabilities; validation follows"}[name]
        commands.append(slide.shape(f"{name}.Scope", x + 0.18, 6.10, 3.70, 0.25,
                              text=footnote, size=12, color="607184", align="center"))

    chip_box = (268, 297, 987, 991)
    commands.append(slide.picture("Prototype.Left", "fpga-chip.png", chip_box, 0.91, 2.44, 0.91))
    commands.append(slide.picture("Prototype.Right", "fpga-chip.png", chip_box, 2.94, 2.44, 0.91))
    commands.append(slide.shape("Prototype.Link", 1.91, 2.75, 0.94, 0.27, fill=AMBER,
                          preset="leftRightArrow"))

    commands.append(slide.picture("Single.FPGA", "fpga-chip.png", chip_box, 5.18, 2.44, 0.91))
    # Native monitor frame keeps the host-state illustration editable.
    commands.append(slide.shape("Single.Host", 6.74, 2.55, 1.17, 0.65, fill="FFFFFF",
                          line=f"{NAVY}:2.5", preset="roundRect", adj="adj:val 6500"))
    commands.append(slide.shape("Single.HostStand", 7.265, 3.21, 0.12, 0.12, fill=NAVY))
    commands.append(slide.shape("Single.HostFoot", 7.065, 3.33, 0.52, 0.045, fill=NAVY))
    commands.append(slide.picture("Single.Snapshot", "global-snapshot.png",
                            (210, 206, 1044, 1104), 7.105, 2.63, 0.44))
    commands.append({"command": "add", "parent": "/slide[1]", "type": "connector",
                     "props": {"name": "S04.Single.StateTransfer", "shape": "straight",
                               "from": "/slide[1]/picture[@name=S04.Single.FPGA]",
                               "to": "/slide[1]/shape[@name=S04.Single.Host]",
                               "fromSide": "right", "toSide": "left",
                               "color": NAVY, "lineWidth": "2pt",
                               "headEnd": "triangle", "tailEnd": "triangle"}})
    commands.append(slide.picture("REMUS.Left", "fpga-chip.png", chip_box, 9.18, 2.55, 0.70))
    commands.append(slide.picture("REMUS.Right", "fpga-chip.png", chip_box, 10.34, 2.55, 0.70))
    commands.append(slide.shape("REMUS.Link", 9.925, 2.79, 0.37, 0.20, fill=AMBER,
                          preset="leftRightArrow"))
    commands.append(slide.picture("REMUS.Replay", "restore-replay.png", (169, 159, 1101, 1088),
                            11.26, 2.61, 0.57))
    commands.append(slide.picture("REMUS.Snapshot", "global-snapshot.png",
                            (210, 206, 1044, 1104), 12.09, 2.59, 0.55))

    commands.append(slide.shape("Goal.Panel", 0.35, 6.58, 12.64, 0.63, fill="EAF4F3",
                          preset="roundRect", adj="adj:val 15000"))
    for i, (diameter, fill) in enumerate([(0.47, AMBER), (0.35, "FFFFFF"),
                                         (0.25, AMBER), (0.13, "FFFFFF"), (0.065, AMBER)]):
        commands.append(slide.shape(f"Goal.Target{i}", 1.22 - diameter / 2,
                              6.895 - diameter / 2, diameter, diameter,
                              fill=fill, preset="ellipse"))
    commands.append(slide.shape("Goal.Arrow", 1.245, 6.66, 0.29, 0.10, fill=AMBER,
                          preset="rightArrow", rotation=315))
    commands.append(slide.shape("Goal.Divider", 1.97, 6.69, 0.009, 0.40, fill="BDCBD4"))
    commands.append(slide.shape("Goal.Text", 2.26, 6.63, 10.39, 0.55,
                          text="Goal: combine multi-FPGA scalability with replayable emulation\nfor large-scale SoC debugging.",
                          size=18, color=NAVY))
    commands.append(slide.shape("PageNumber", 12.72, 7.25, 0.25, 0.20,
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
    return commands
