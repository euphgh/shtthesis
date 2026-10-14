"""Page 2: Multi-FPGA Prototyping Is Fast, but Hard to Debug."""

from .common import SlideAPI, NAVY, TEAL, AMBER

TITLE = '2. Multi-FPGA Prototyping Is Fast, but Hard to Debug'
slide = SlideAPI(2)


def build_commands():
    """Compare typical prototyping limits with the targeted replay workflow."""
    commands = [slide.title(size=30)]
    commands.append(slide.shape("TitleRule", 0.35, 0.78, 12.64, 2 / 72, fill=TEAL))
    for name, x, fill, heading, qualifier in [
        ("Prototype", 0.35, "FCF4E8", "Multi-FPGA Prototyping",
         "Typical strengths & limitations"),
        ("Replay", 6.77, "EAF4F3", "Replayable Multi-FPGA Emulation",
         "Target capabilities"),
    ]:
        commands.append(slide.shape(f"{name}.Panel", x, 1.06, 6.22, 6.13, fill=fill,
                              preset="roundRect", adj="adj:val 3000"))
        commands.append(slide.shape(f"{name}.Heading", x + 0.20, 1.32, 5.82, 0.42,
                              text=heading, size=22, bold="true", color=NAVY,
                              align="center"))
        commands.append(slide.shape(f"{name}.Qualifier", x + 0.25, 1.82, 5.72, 0.30,
                              text=qualifier, size=15, color="607184", align="center"))
        commands.append(slide.shape(f"{name}.Divider", x + 0.23, 4.87, 5.76, 0.012,
                              fill="BDCBD4"))

    def badge(name, x, y, positive=True):
        commands.append(slide.shape(f"{name}.Badge", x, y, 0.34, 0.34,
                              fill=TEAL if positive else AMBER, preset="ellipse"))
        if positive:
            commands.append(slide.shape(f"{name}.CheckShort", x + 0.080, y + 0.175,
                                  0.105, 0.043, fill="FFFFFF", rotation=45))
            commands.append(slide.shape(f"{name}.CheckLong", x + 0.125, y + 0.147,
                                  0.160, 0.043, fill="FFFFFF", rotation=315))
        else:
            commands.append(slide.shape(f"{name}.Minus", x + 0.080, y + 0.149,
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
            commands.append(slide.shape(f"{column}.Text{index + 1}", x + 0.53, y + 0.003,
                                  5.00, 0.34, text=text))

    chip_box = (268, 297, 987, 991)
    for i, x in enumerate((1.09, 2.99, 4.89), 1):
        commands.append(slide.picture(f"Prototype.FPGA{i}", "fpga-chip.png", chip_box,
                                x, 5.36, 0.94))
    commands.append(slide.shape("Prototype.Run", 2.66, 5.03, 1.6, 0.30,
                          text="Run", size=18, bold="true", color=NAVY, align="center"))
    for i, x in enumerate((2.09, 3.99), 1):
        commands.append(slide.shape(f"Prototype.Link{i}", x, 5.67, 0.84, 0.26,
                              fill=AMBER, preset="rightArrow"))
    commands.append(slide.shape("Prototype.VisibilityArrow", 3.31, 6.32, 0.30, 0.30,
                          fill="91A5B5", preset="downArrow"))
    commands.append(slide.shape("Prototype.Visibility", 2.10, 6.64, 2.72, 0.40,
                          text="Limited visibility", size=18, bold="true", color=NAVY,
                          fill="E0E7EC", preset="roundRect", adj="adj:val 15000",
                          align="center", valign="center"))

    nodes = ["Run", "Pause", "Dump", "Restore", "Replay"]
    centers = [7.50 + 1.19 * i for i in range(5)]
    for name, x in zip(nodes, centers):
        commands.append(slide.shape(f"Workflow.{name}", x - 0.52, 5.55, 1.04, 0.51,
                              text=name, size=16, bold="true", color=NAVY,
                              fill="FFF0D8" if name == "Pause" else "FFFFFF",
                              line=f"{AMBER if name == 'Pause' else TEAL}:1.2",
                              preset="roundRect", adj="adj:val 14000",
                              align="center", valign="center"))

    def connector(name, **props):
        commands.append(slide.connector(name, **{"color": NAVY, "lineWidth": "1.8pt", **props}))

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

    commands.append(slide.picture("Workflow.Snapshot", "global-snapshot.png",
                            (210, 206, 1044, 1104), 9.605, 6.28, 0.55))
    commands.append(slide.picture("Workflow.Waveform", "waveform-monitor.png",
                            (154, 320, 1101, 1004), 11.86, 6.29, 0.80))
    for name, target in [("Dump", "Snapshot"), ("Replay", "Waveform")]:
        connector(f"Workflow.{name}Output", **{
            "from": f"/slide[1]/shape[@name=S02.Workflow.{name}]",
            "to": f"/slide[1]/picture[@name=S02.Workflow.{target}]",
            "fromSide": "bottom", "toSide": "top", "tailEnd": "triangle"})
    commands.append(slide.shape("Workflow.SnapshotLabel", 8.88, 6.93, 2.0, 0.25,
                          text="Global snapshot", size=14, color=NAVY, align="center"))
    commands.append(slide.shape("Workflow.WaveformLabel", 11.62, 6.93, 1.28, 0.25,
                          text="Waveform", size=14, color=NAVY, align="center"))
    commands.append(slide.shape("PageNumber", 12.72, 7.25, 0.25, 0.20,
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
    return commands
