"""Page 3: Key Challenges of Replayable Multi-FPGA Emulation."""

from .common import apply_layout_edits, SlideAPI, NAVY, TEAL, AMBER, inches

TITLE = 'Key Challenges of Replayable Multi-FPGA Emulation'
slide = SlideAPI(3)


# Final reviewed layout for this page. These properties override the base
# component layout below; edit revised text, geometry and rich text here.
LAYOUT_EDITS = {'remove': [],
 'objects': {'S03.Title': {'props': {'font': 'Arial',
                                     'size': '30pt',
                                     'color': '#183B56',
                                     'bold': 'true',
                                     'align': 'left',
                                     'name': 'S03.Title',
                                     'x': '25.2pt',
                                     'y': '10.08pt',
                                     'width': '910.08pt',
                                     'height': '38.88pt',
                                     'fill': 'none',
                                     'font.latin': 'Arial',
                                     'line': 'none',
                                     'margin': '0cm',
                                     'autoFit': 'none'},
                           'paragraphs': [{'command': 'add',
                                           'parent': '{object}/paragraph[1]',
                                           'type': 'run',
                                           'props': {'font.latin': 'Arial',
                                                     'size': '30pt',
                                                     'bold': 'true',
                                                     'color': '#183B56',
                                                     'text': 'Key Challenges of '}},
                                          {'command': 'add',
                                           'parent': '{object}/paragraph[1]',
                                           'type': 'run',
                                           'props': {'font.latin': 'Arial',
                                                     'size': '30pt',
                                                     'bold': 'true',
                                                     'color': '#183B56',
                                                     'text': 'Replayable'}},
                                          {'command': 'add',
                                           'parent': '{object}/paragraph[1]',
                                           'type': 'run',
                                           'props': {'font.latin': 'Arial',
                                                     'size': '30pt',
                                                     'bold': 'true',
                                                     'color': '#183B56',
                                                     'text': ' Multi-FPGA Emulation'}}]},
             'S03.Cycle.Panel': {'props': {'y': '939720emu'}},
             'S03.Cycle.Heading': {'props': {'font': 'Arial',
                                             'size': '20pt',
                                             'color': '#183B56',
                                             'bold': 'true',
                                             'align': 'left',
                                             'name': 'S03.Cycle.Heading',
                                             'x': '2504542emu',
                                             'y': '97.2pt',
                                             'width': '257.04pt',
                                             'height': '50.4pt',
                                             'fill': 'none',
                                             'font.latin': 'Arial',
                                             'line': 'none',
                                             'margin': '0cm',
                                             'autoFit': 'none'},
                                   'paragraphs': [{'command': 'set',
                                                   'path': '{object}/paragraph[1]',
                                                   'props': {'font.latin': 'Arial',
                                                             'size': '20pt',
                                                             'bold': 'true',
                                                             'color': '#183B56',
                                                             'text': 'Cycle-Accurate Execution'}}]},
             'S03.Cycle.Bullet1': {'props': {'y': '1968420emu'}},
             'S03.Cycle.Text1': {'props': {'y': '1890696emu'}},
             'S03.Pause.Panel': {'props': {'y': '946638emu'}},
             'S03.Pause.Divider': {'props': {'y': '1175238emu'}},
             'S03.Pause.Heading': {'props': {'y': '1156950emu'}},
             'S03.Pause.Bullet1': {'props': {'y': '1975338emu'}},
             'S03.Pause.Text1': {'props': {'y': '1897614emu'}},
             'S03.Pause.Bullet2': {'props': {'y': '2597130emu'}},
             'S03.Pause.Text2': {'props': {'font': 'Arial',
                                           'size': '17pt',
                                           'color': '#20354A',
                                           'bold': 'false',
                                           'align': 'left',
                                           'name': 'S03.Pause.Text2',
                                           'x': '683.28pt',
                                           'y': '2519406emu',
                                           'width': '237.6pt',
                                           'height': '43.92pt',
                                           'fill': 'none',
                                           'line': 'none',
                                           'margin': '0cm',
                                           'autoFit': 'none'},
                                 'paragraphs': [{'command': 'add',
                                                 'parent': '{object}/paragraph[1]',
                                                 'type': 'run',
                                                 'props': {'size': '17pt',
                                                           'color': '#20354A',
                                                           'text': 'Internal states from different '
                                                                   'cycle'}},
                                                {'command': 'add',
                                                 'parent': '{object}/paragraph[1]',
                                                 'type': 'run',
                                                 'props': {'size': '17pt',
                                                           'color': '#20354A',
                                                           'text': ' '}},
                                                {'command': 'add',
                                                 'parent': '{object}/paragraph[1]',
                                                 'type': 'run',
                                                 'props': {'size': '17pt',
                                                           'color': '#20354A',
                                                           'text': 'can not be replayed'}}]},
             'S03.State.Panel': {'props': {'y': '3644892emu'}},
             'S03.State.Divider': {'props': {'y': '3873492emu'}},
             'S03.State.Heading': {'props': {'y': '3855204emu'}},
             'S03.State.Bullet1': {'props': {'y': '4828340emu'}},
             'S03.State.Text1': {'props': {'y': '4750616emu'}},
             'S03.State.Bullet2': {'props': {'y': '5295384emu'}},
             'S03.State.Text2': {'props': {'y': '5217660emu'}},
             'S03.Partition.Panel': {'props': {'y': '3644892emu'}},
             'S03.Partition.Divider': {'props': {'y': '3873492emu'}},
             'S03.Partition.Heading': {'props': {'font': 'Arial',
                                                 'size': '20pt',
                                                 'color': '#183B56',
                                                 'bold': 'true',
                                                 'align': 'left',
                                                 'name': 'S03.Partition.Heading',
                                                 'x': '661.68pt',
                                                 'y': '3855204emu',
                                                 'width': '257.04pt',
                                                 'height': '50.4pt',
                                                 'fill': 'none',
                                                 'font.latin': 'Arial',
                                                 'line': 'none',
                                                 'margin': '0cm',
                                                 'autoFit': 'none'},
                                       'paragraphs': [{'command': 'set',
                                                       'path': '{object}/paragraph[1]',
                                                       'props': {'font.latin': 'Arial',
                                                                 'size': '20pt',
                                                                 'bold': 'true',
                                                                 'color': '#183B56',
                                                                 'text': 'Automated '
                                                                         'Partitioning'}}]},
             'S03.Partition.Bullet1': {'props': {'y': '4504781emu'}},
             'S03.Partition.Text1': {'props': {'y': '4427057emu'}},
             'S03.Partition.Bullet2': {'props': {'y': '5126573emu'}},
             'S03.Partition.Text2': {'props': {'font': 'Arial',
                                               'size': '17pt',
                                               'color': '#20354A',
                                               'bold': 'false',
                                               'align': 'left',
                                               'name': 'S03.Partition.Text2',
                                               'x': '683.28pt',
                                               'y': '5048849emu',
                                               'width': '237.6pt',
                                               'height': '59.04pt',
                                               'fill': 'none',
                                               'font.latin': 'Arial',
                                               'line': 'none',
                                               'margin': '0cm',
                                               'autoFit': 'none'},
                                     'paragraphs': [{'command': 'set',
                                                     'path': '{object}/paragraph[1]',
                                                     'props': {'font.latin': 'Arial',
                                                               'size': '17pt',
                                                               'color': '#20354A',
                                                               'text': 'Limit Maximum Path-Cut '
                                                                       'Number through '
                                                                       'granularity'}}]},
             'S03.Cycle.Label': {'props': {'font': 'Arial',
                                           'size': '14pt',
                                           'color': '#183B56',
                                           'bold': 'false',
                                           'align': 'center',
                                           'name': 'S03.Cycle.Label',
                                           'x': '37.44pt',
                                           'y': '225.36pt',
                                           'width': '139.68pt',
                                           'height': '20.16pt',
                                           'fill': 'none',
                                           'font.latin': 'Arial',
                                           'line': 'none',
                                           'margin': '0cm',
                                           'autoFit': 'none'},
                                 'paragraphs': [{'command': 'set',
                                                 'path': '{object}/paragraph[1]',
                                                 'props': {'align': 'center',
                                                           'font.latin': 'Arial',
                                                           'size': '14pt',
                                                           'color': '#183B56',
                                                           'text': 'Same DUT cycle n'}}]},
             'S03.Pause.Top': {'props': {'y': '1275822emu'}},
             'S03.Pause.Left': {'props': {'y': '2336526emu'}},
             'S03.Pause.Right': {'props': {'y': '2336526emu'}},
             'S03.Pause.Symbol': {'props': {'y': '2020006emu'}},
             'S03.Pause.Label': {'props': {'y': '2985750emu'}},
             'S03.State.FPGA1': {'props': {'y': '4220964emu'}},
             'S03.State.FPGA2': {'props': {'y': '4220964emu'}},
             'S03.State.FPGA3': {'props': {'y': '4220964emu'}},
             'S03.State.LocalLabel': {'props': {'y': '3855204emu'}},
             'S03.State.Snapshot': {'props': {'y': '5162796emu'}},
             'S03.State.GlobalLabel': {'props': {'y': '5729724emu'}},
             'S03.Partition.Circuit': {'props': {'y': '4074660emu'}},
             'S03.Partition.Label': {'props': {'y': '5638280emu'}},
             'S03.Takeaway': {'props': {'font': 'Arial',
                                        'size': '18pt',
                                        'color': '#183B56',
                                        'bold': 'true',
                                        'align': 'left',
                                        'name': 'S03.Takeaway',
                                        'x': '63.36pt',
                                        'y': '496.8pt',
                                        'width': '878.4pt',
                                        'height': '25.2pt',
                                        'fill': 'none',
                                        'line': 'none',
                                        'margin': '0cm',
                                        'autoFit': 'none'},
                              'paragraphs': [{'command': 'add',
                                              'parent': '{object}/paragraph[1]',
                                              'type': 'run',
                                              'props': {'bold': 'true',
                                                        'color': '#183B56',
                                                        'text': 'Academe'}},
                                             {'command': 'add',
                                              'parent': '{object}/paragraph[1]',
                                              'type': 'run',
                                              'props': {'bold': 'true',
                                                        'color': '#183B56',
                                                        'text': ' '}},
                                             {'command': 'add',
                                              'parent': '{object}/paragraph[1]',
                                              'type': 'run',
                                              'props': {'bold': 'true',
                                                        'color': '#183B56',
                                                        'text': 'have made progress in individual '
                                                                'fields, still gaps in Multi-FPGA '
                                                                'Emulation system.'}}]},
             'S03.Pause.SyncLeft': {'props': {'y': '1796559emu'}},
             'S03.Pause.SyncRight': {'props': {'y': '1796559emu'}},
             'S03.Pause.SyncBottom': {'props': {'y': '2596894emu'}},
             'S03.State.Drop1': {'props': {'y': '4705596emu'}},
             'S03.State.Drop2': {'props': {'y': '4705596emu'}},
             'S03.State.Drop3': {'props': {'y': '4705596emu'}},
             'S03.State.Bus': {'props': {'y': '5025636emu'}},
             'S03.State.Aggregate': {'props': {'y': '5025636emu'}}}}


def build_commands():
    """Build four challenge panels, with editable timing and state-flow links."""
    commands = [slide.title(size=30)]
    commands.append(slide.shape("TitleRule", 0.35, 0.78, 12.64, 2 / 72, fill=TEAL))
    panels = [
        ("Cycle", 0.35, 1.12, "EAF4F3", "Cycle-Accurate\nExecution",
         ["Align DUT cycles across\npartitions", "Account for cross-FPGA\ncommunication latency"]),
        ("Pause", 6.77, 1.12, "F1F5F8", "Cycle-Consistent\nGlobal Pause",
         ["Stop partitions at the\nsame logical cycle", "Drain links for a stable\nsnapshot boundary"]),
        ("State", 0.35, 4.02, "FCF4E8", "Distributed State\nManagement",
         ["Extract local states", "Form a global snapshot\nfor restore and replay"]),
        ("Partition", 6.77, 4.02, "EAF4F3", "Automated\nPartitioning",
         ["Balance resources and\ncut size", "Limit Maximum\nPath-Cut Number\nthrough granularity"]),
    ]
    for name, x, y, fill, heading, bullets in panels:
        commands.append(slide.shape(f"{name}.Panel", x, y, 6.22, 2.63, fill=fill,
                              preset="roundRect", adj="adj:val 6500"))
        commands.append(slide.shape(f"{name}.Divider", x + 2.18, y + 0.25, 0.009, 2.13,
                              fill="BDCBD4"))
        commands.append(slide.shape(f"{name}.Heading", x + 2.42, y + 0.23, 3.57, 0.70,
                              text=heading, size=20, bold="true", color=NAVY))
        for i, text in enumerate(bullets):
            top = y + 1.04 + i * 0.68
            commands.append(slide.shape(f"{name}.Bullet{i + 1}", x + 2.46, top + 0.085,
                                  0.10, 0.10, fill=TEAL, preset="ellipse"))
            commands.append(slide.shape(f"{name}.Text{i + 1}", x + 2.72, top, 3.30,
                                  0.82 if name == "Partition" and i == 1 else 0.61,
                                  text=text, size=17))

    chip_box = (268, 297, 987, 991)

    def chip(name, x, y, width):
        commands.append(slide.picture(name, "fpga-chip.png", chip_box, x, y, width))

    def connector(name, **props):
        commands.append(slide.connector(name, **{"color": AMBER, "lineWidth": "2pt", **props}))

    def link(name, start, end, start_side, end_side, **props):
        connector(name, **{"from": f"/slide[1]/picture[@name=S03.{start}]",
                           "to": f"/slide[1]/picture[@name=S03.{end}]",
                           "fromSide": start_side, "toSide": end_side, **props})

    # Shared logical-cycle progress: two chips joined by editable pulse segments.
    chip("Cycle.Left", 0.55, 2.22, 0.66)
    chip("Cycle.Right", 1.77, 2.22, 0.66)
    commands.append(slide.picture("Cycle.Clock", "cycle-control.png", (164, 126, 1092, 1122),
                            1.25, 1.57, 0.48))
    points = [(1.24, 2.60), (1.33, 2.60), (1.33, 2.35), (1.46, 2.35),
              (1.46, 2.60), (1.59, 2.60), (1.59, 2.35), (1.71, 2.35),
              (1.71, 2.60), (1.74, 2.60)]
    for i, ((x1, y1), (x2, y2)) in enumerate(zip(points, points[1:])):
        connector(f"Cycle.Pulse{i}", x=inches(min(x1, x2)), y=inches(min(y1, y2)),
                  width=inches(abs(x2 - x1)), height=inches(abs(y2 - y1)),
                  lineWidth="2.3pt")
    commands.append(slide.shape("Cycle.Label", 0.52, 3.13, 1.94, 0.28,
                          text="DUT cycle n", size=14, color=NAVY, align="center"))

    # Triangular multi-partition diagram: the pause glyph alone is not sufficient.
    chip("Pause.Top", 7.57, 1.48, 0.59)
    chip("Pause.Left", 7.01, 2.64, 0.59)
    chip("Pause.Right", 8.13, 2.64, 0.59)
    link("Pause.SyncLeft", "Pause.Top", "Pause.Left", "bottom", "top")
    link("Pause.SyncRight", "Pause.Top", "Pause.Right", "bottom", "top")
    link("Pause.SyncBottom", "Pause.Left", "Pause.Right", "right", "left")
    commands.append(slide.picture("Pause.Symbol", "global-pause.png", (140, 142, 1119, 1121),
                            7.62, 2.14, 0.49))
    commands.append(slide.shape("Pause.Label", 6.97, 3.35, 1.80, 0.28,
                          text="Same DUT cycle n", size=13, color=NAVY, align="center"))

    # Each partition contributes a local dump to the aggregate global snapshot.
    for i, x in enumerate((0.53, 1.21, 1.89), 1):
        chip(f"State.FPGA{i}", x, 4.65, 0.55)
    commands.append(slide.shape("State.LocalLabel", 0.52, 4.25, 1.94, 0.27,
                          text="Local states", size=14, color=NAVY, align="center"))
    commands.append(slide.picture("State.Snapshot", "global-snapshot.png",
                            (210, 206, 1044, 1104), 1.235, 5.68, 0.50))
    # A bus gathers the three drops; the final arrow enters the snapshot.
    for i, center in enumerate((0.805, 1.485, 2.165), 1):
        connector(f"State.Drop{i}", x=inches(center), y="5.18in", width="0in",
                  height="0.35in", color=TEAL)
    connector("State.Bus", x="0.805in", y="5.53in", width="1.36in", height="0in", color=TEAL)
    connector("State.Aggregate", x="1.485in", y="5.53in", width="0in", height="0.15in",
              color=TEAL, tailEnd="triangle")
    commands.append(slide.shape("State.GlobalLabel", 0.52, 6.30, 1.94, 0.25,
                          text="Global snapshot", size=13, color=NAVY, align="center"))

    commands.append(slide.picture("Partition.Circuit", "circuit-partitioning.png",
                            (199, 234, 1056, 1020), 7.06, 4.69, 1.62))
    commands.append(slide.shape("Partition.Label", 6.97, 6.40, 1.84, 0.27,
                          text="Partitioned design", size=13, color=NAVY, align="center"))
    commands.append(slide.shape("Takeaway", 0.55, 6.95, 12.20, 0.35,
                          text="Replayable emulation requires scalable deployment and globally coordinated debugging.",
                          size=18, color=NAVY, bold="true", align="center"))
    commands.append(slide.shape("PageNumber", 12.72, 7.25, 0.25, 0.20,
                          text="3", size=10, color="607184", align="right"))
    commands.append({"command": "add", "parent": "/slide[1]", "type": "notes",
                     "props": {"text": (
                         "This slide introduces research challenges, not completed REMUS results. "
                         "DUT logical cycles must remain aligned despite cross-FPGA communication "
                         "latency; the pulse is conceptual, not a measured clock waveform. Global "
                         "pause requires all partitions at the same DUT cycle and drained links, "
                         "providing a stable boundary. Local partition states must be mapped and "
                         "aggregated into a global snapshot for restoration and deterministic replay. "
                         "Partitioning must balance resources and cut size while limiting the maximum "
                         "path-cut number through granularity selection. Multiple chip icons and the "
                         "partitioned circuit illustrate the problem, not an experimentally verified "
                         "FPGA count. Reference: figure/presentation-reference/midterm-background-03.png."
                     )}})
    commands = apply_layout_edits(commands, LAYOUT_EDITS)
    # Explicit title spacing and page-specific finishing objects.
    commands.extend([{'command': 'set', 'path': '/slide[1]/shape[@name=S03.Title]', 'props': {'lineSpacing': '0.9x'}}])
    return commands
