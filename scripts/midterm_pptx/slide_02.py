"""Page 2: Multi-FPGA Prototyping Is Fast, but Hard to Debug."""

from .common import apply_layout_edits, SlideAPI, NAVY, TEAL, AMBER

TITLE = 'Motivation: Multi-FPGA Prototyping Is Fast, but Hard to Debug'
slide = SlideAPI(2)


# Final reviewed layout for this page. These properties override the base
# component layout below; edit revised text, geometry and rich text here.
LAYOUT_EDITS = {'remove': ['S02.Prototype.Qualifier',
            'S02.Replay.Qualifier',
            'S02.Prototype.Link2',
            'S02.Prototype.Link1'],
 'objects': {'S02.Title': {'props': {'font': 'Arial',
                                     'size': '30pt',
                                     'color': '#183B56',
                                     'bold': 'true',
                                     'align': 'left',
                                     'name': 'S02.Title',
                                     'x': '25.2pt',
                                     'y': '10.08pt',
                                     'width': '910.08pt',
                                     'height': '38.88pt',
                                     'fill': 'none',
                                     'font.latin': 'Arial',
                                     'line': 'none',
                                     'margin': '0cm',
                                     'autoFit': 'none'},
                           'paragraphs': [{'command': 'set',
                                           'path': '{object}/paragraph[1]',
                                           'props': {'font.latin': 'Arial',
                                                     'size': '30pt',
                                                     'bold': 'true',
                                                     'color': '#183B56',
                                                     'text': 'Motivation: Multi-FPGA Prototyping '
                                                             'Is Fast, but Hard to Debug'}}]},
             'S02.Replay.Heading': {'props': {'font': 'Arial',
                                              'size': '22pt',
                                              'color': '#183B56',
                                              'bold': 'true',
                                              'align': 'center',
                                              'name': 'S02.Replay.Heading',
                                              'x': '501.84pt',
                                              'y': '95.04pt',
                                              'width': '419.04pt',
                                              'height': '30.24pt',
                                              'fill': 'none',
                                              'font.latin': 'Arial',
                                              'line': 'none',
                                              'margin': '0cm',
                                              'autoFit': 'none'},
                                    'paragraphs': [{'command': 'set',
                                                    'path': '{object}/paragraph[1]',
                                                    'props': {'align': 'center'}},
                                                   {'command': 'add',
                                                    'parent': '{object}/paragraph[1]',
                                                    'type': 'run',
                                                    'props': {'font.latin': 'Arial',
                                                              'size': '22pt',
                                                              'bold': 'true',
                                                              'color': '#183B56',
                                                              'text': 'Replayable'}},
                                                   {'command': 'add',
                                                    'parent': '{object}/paragraph[1]',
                                                    'type': 'run',
                                                    'props': {'font.latin': 'Arial',
                                                              'size': '22pt',
                                                              'bold': 'true',
                                                              'color': '#183B56',
                                                              'text': ' Multi-FPGA Emulation'}}]},
             'S02.Prototype.Item1.Badge': {'props': {'y': '1887885emu'}},
             'S02.Prototype.Item1.CheckShort': {'props': {'y': '2047905emu'}},
             'S02.Prototype.Item1.CheckLong': {'props': {'y': '2022302emu'}},
             'S02.Prototype.Text1': {'props': {'y': '1890628emu'}},
             'S02.Prototype.Item2.Badge': {'props': {'y': '2345085emu'}},
             'S02.Prototype.Item2.CheckShort': {'props': {'y': '2505105emu'}},
             'S02.Prototype.Item2.CheckLong': {'props': {'y': '2479502emu'}},
             'S02.Prototype.Text2': {'props': {'y': '2347828emu'}},
             'S02.Prototype.Item3.Badge': {'props': {'y': '2802285emu'}},
             'S02.Prototype.Item3.CheckShort': {'props': {'y': '2962305emu'}},
             'S02.Prototype.Item3.CheckLong': {'props': {'y': '2936702emu'}},
             'S02.Prototype.Text3': {'props': {'y': '2805028emu'}},
             'S02.Prototype.Item4.Badge': {'props': {'y': '3259485emu'}},
             'S02.Prototype.Item4.Minus': {'props': {'y': '3395731emu'}},
             'S02.Prototype.Text4': {'props': {'y': '3262228emu'}},
             'S02.Prototype.Item5.Badge': {'props': {'y': '3716685emu'}},
             'S02.Prototype.Item5.Minus': {'props': {'y': '3852931emu'}},
             'S02.Prototype.Text5': {'props': {'y': '3719428emu'}},
             'S02.Replay.Item1.Badge': {'props': {'x': '6640656emu', 'y': '1887881emu'}},
             'S02.Replay.Item1.CheckShort': {'props': {'x': '6713808emu', 'y': '2047901emu'}},
             'S02.Replay.Item1.CheckLong': {'props': {'x': '6754956emu', 'y': '2022298emu'}},
             'S02.Replay.Text1': {'props': {'x': '7125288emu', 'y': '1890624emu'}},
             'S02.Replay.Item2.Badge': {'props': {'x': '6640656emu', 'y': '2281073emu'}},
             'S02.Replay.Item2.CheckShort': {'props': {'x': '6713808emu', 'y': '2441093emu'}},
             'S02.Replay.Item2.CheckLong': {'props': {'x': '6754956emu', 'y': '2415490emu'}},
             'S02.Replay.Text2': {'props': {'x': '7125288emu', 'y': '2283816emu'}},
             'S02.Replay.Item3.Badge': {'props': {'x': '6640656emu', 'y': '2674265emu'}},
             'S02.Replay.Item3.CheckShort': {'props': {'x': '6713808emu', 'y': '2834285emu'}},
             'S02.Replay.Item3.CheckLong': {'props': {'x': '6754956emu', 'y': '2808682emu'}},
             'S02.Replay.Text3': {'props': {'x': '7125288emu', 'y': '2677008emu'}},
             'S02.Replay.Item4.Badge': {'props': {'x': '6640656emu', 'y': '3067457emu'}},
             'S02.Replay.Item4.CheckShort': {'props': {'x': '6713808emu', 'y': '3227477emu'}},
             'S02.Replay.Item4.CheckLong': {'props': {'x': '6754956emu', 'y': '3201874emu'}},
             'S02.Replay.Text4': {'props': {'x': '7125288emu', 'y': '3084268emu'}},
             'S02.Replay.Item5.Badge': {'props': {'x': '6640656emu', 'y': '3460649emu'}},
             'S02.Replay.Item5.CheckShort': {'props': {'x': '6713808emu', 'y': '3620669emu'}},
             'S02.Replay.Item5.CheckLong': {'props': {'x': '6754956emu', 'y': '3595066emu'}},
             'S02.Replay.Text5': {'props': {'x': '7125288emu', 'y': '3463392emu'}},
             'S02.Replay.Item6.Badge': {'props': {'x': '6640656emu', 'y': '3853841emu'}},
             'S02.Replay.Item6.CheckShort': {'props': {'x': '6713808emu', 'y': '4013861emu'}},
             'S02.Replay.Item6.CheckLong': {'props': {'x': '6754956emu', 'y': '3988258emu'}},
             'S02.Replay.Text6': {'props': {'x': '7125288emu', 'y': '3856584emu'}},
             'S02.Prototype.DoubleArrow1': {'add': 'shape',
                                            'props': {'name': 'S02.Prototype.DoubleArrow1',
                                                      'x': '1892103emu',
                                                      'y': '5152629emu',
                                                      'width': '829549emu',
                                                      'height': '287803emu',
                                                      'fill': '#DF973E',
                                                      'geometry': 'leftRightArrow',
                                                      'adj': 'adj1:val 44000,adj2:val 28000',
                                                      'font': 'Arial',
                                                      'font.latin': 'Arial',
                                                      'size': '18pt',
                                                      'color': '#20354A',
                                                      'line': 'none',
                                                      'margin': '0cm',
                                                      'autoFit': 'none'},
                                            'paragraphs': [{'command': 'set',
                                                            'path': '{object}/paragraph[1]',
                                                            'props': {'size': '18pt'}}]},
             'S02.Prototype.DoubleArrow2': {'add': 'shape',
                                            'props': {'name': 'S02.Prototype.DoubleArrow2',
                                                      'x': '3641867emu',
                                                      'y': '5164190emu',
                                                      'width': '829549emu',
                                                      'height': '287803emu',
                                                      'fill': '#DF973E',
                                                      'geometry': 'leftRightArrow',
                                                      'adj': 'adj1:val 44000,adj2:val 28000',
                                                      'font': 'Arial',
                                                      'font.latin': 'Arial',
                                                      'size': '18pt',
                                                      'color': '#20354A',
                                                      'line': 'none',
                                                      'margin': '0cm',
                                                      'autoFit': 'none'},
                                            'paragraphs': [{'command': 'set',
                                                            'path': '{object}/paragraph[1]',
                                                            'props': {'size': '18pt'}}]}}}


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
    commands = apply_layout_edits(commands, LAYOUT_EDITS)
    # Explicit title spacing and page-specific finishing objects.
    commands.extend([{'command': 'set', 'path': '/slide[1]/shape[@name=S02.Title]', 'props': {'lineSpacing': '0.9x'}}])
    return commands
