"""Page 6: concise execution summary and a cropped global-pause illustration."""

from .common import apply_layout_edits, SlideAPI, THESIS, NAVY, TEAL, inches

TITLE = 'Pregress1:  Cycle-Accurate Execution and Global Pause'
OUTPUT_STEM = "REMUS_Progress_Slide_6"
PREVIEW_STEM = "midterm-progress-06"
slide = SlideAPI(6)


# Final reviewed layout for this page. These properties override the base
# component layout below; edit revised text, geometry and rich text here.
LAYOUT_EDITS = {'remove': ['S06.Execution.Bullet2', 'S06.Execution.Attribution', 'S06.Execution.Bullet1'],
 'objects': {'S06.Title': {'props': {'font': 'Arial',
                                     'size': '30pt',
                                     'color': '#183B56',
                                     'bold': 'true',
                                     'align': 'left',
                                     'name': 'S06.Title',
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
                                                     'text': 'Pregress1:  Cycle-Accurate Execution '
                                                             'and Global Pause'}}]},
             'S06.Execution.Text1': {'props': {'font': 'Arial',
                                               'size': '18pt',
                                               'color': '#20354A',
                                               'bold': 'false',
                                               'align': 'left',
                                               'name': 'S06.Execution.Text1',
                                               'x': '424844emu',
                                               'y': '146.16pt',
                                               'width': '3642111emu',
                                               'height': '43.2pt',
                                               'fill': 'none',
                                               'bulletRaw': '<a:buFont '
                                                            'xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main" '
                                                            'charset="0" '
                                                            'panose="020B0604020202020204" '
                                                            'pitchFamily="34" typeface="Arial" '
                                                            '/><a:buChar '
                                                            'xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main" '
                                                            'char="•" />',
                                               'font.latin': 'Arial',
                                               'line': 'none',
                                               'margin': '0cm',
                                               'autoFit': 'none',
                                               'indent': '-22.5pt',
                                               'marginLeft': '22.5pt'},
                                     'paragraphs': [{'command': 'set',
                                                     'path': '{object}/paragraph[1]',
                                                     'props': {'indent': '-22.5pt',
                                                               'marginLeft': '22.5pt',
                                                               'bulletRaw': '<a:buFont '
                                                                            'xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main" '
                                                                            'charset="0" '
                                                                            'panose="020B0604020202020204" '
                                                                            'pitchFamily="34" '
                                                                            'typeface="Arial" '
                                                                            '/><a:buChar '
                                                                            'xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main" '
                                                                            'char="•" />'}},
                                                    {'command': 'add',
                                                     'parent': '{object}/paragraph[1]',
                                                     'type': 'run',
                                                     'props': {'font.latin': 'Arial',
                                                               'color': '#20354A',
                                                               'text': 'Execution b'}},
                                                    {'command': 'add',
                                                     'parent': '{object}/paragraph[1]',
                                                     'type': 'run',
                                                     'props': {'font.latin': 'Arial',
                                                               'size': '18pt',
                                                               'color': '#20354A',
                                                               'text': 'ased on DUOHUAFEN LI-TDM'}},
                                                    {'command': 'add',
                                                     'parent': '{object}/paragraph[1]',
                                                     'type': 'run',
                                                     'props': {'font.latin': 'Arial',
                                                               'baseline': '30%',
                                                               'color': '#20354A',
                                                               'text': '[1]'}}]},
             'S06.Execution.Text2': {'props': {'font': 'Arial',
                                               'size': '18pt',
                                               'color': '#20354A',
                                               'bold': 'false',
                                               'align': 'left',
                                               'name': 'S06.Execution.Text2',
                                               'x': '406556emu',
                                               'y': '2589160emu',
                                               'width': '3552795emu',
                                               'height': '43.2pt',
                                               'fill': 'none',
                                               'bulletRaw': '<a:buFont '
                                                            'xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main" '
                                                            'charset="0" '
                                                            'panose="020B0604020202020204" '
                                                            'pitchFamily="34" typeface="Arial" '
                                                            '/><a:buChar '
                                                            'xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main" '
                                                            'char="•" />',
                                               'font.latin': 'Arial',
                                               'line': 'none',
                                               'margin': '0cm',
                                               'autoFit': 'none',
                                               'indent': '-22.5pt',
                                               'marginLeft': '22.5pt'},
                                     'paragraphs': [{'command': 'set',
                                                     'path': '{object}/paragraph[1]',
                                                     'props': {'indent': '-22.5pt',
                                                               'marginLeft': '22.5pt',
                                                               'bulletRaw': '<a:buFont '
                                                                            'xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main" '
                                                                            'charset="0" '
                                                                            'panose="020B0604020202020204" '
                                                                            'pitchFamily="34" '
                                                                            'typeface="Arial" '
                                                                            '/><a:buChar '
                                                                            'xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main" '
                                                                            'char="•" />',
                                                               'font.latin': 'Arial',
                                                               'size': '18pt',
                                                               'color': '#20354A',
                                                               'text': 'Optimized communication '
                                                                       'flow'}}]},
             'S06.Pause.Heading': {'props': {'y': '4028585emu'}},
             'S06.Pause.Number1': {'props': {'y': '4760105emu'}},
             'S06.Pause.Text1': {'props': {'y': '4750961emu'}},
             'S06.Pause.Number2': {'props': {'y': '5272169emu'}},
             'S06.Pause.Text2': {'props': {'y': '5263025emu'}},
             'S06.Pause.Number3': {'props': {'y': '5784233emu'}},
             'S06.Pause.Text3': {'props': {'y': '5775089emu'}},
             'S06.Pause.Illustration': {'props': {'x': '324.72pt',
                                                  'y': '1186107emu',
                                                  'height': '5052713emu',
                                                  'crop': '35.526,12.752,1.076,13.846'}},
             'S06.Execution.Reduction': {'add': 'textbox',
                                         'props': {'name': 'S06.Execution.Reduction',
                                                   'x': '406556emu',
                                                   'y': '249.12pt',
                                                   'width': '3552795emu',
                                                   'height': '43.2pt',
                                                   'fill': 'none',
                                                   'bulletRaw': '<a:buFont '
                                                                'xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main" '
                                                                'charset="0" '
                                                                'panose="020B0604020202020204" '
                                                                'pitchFamily="34" typeface="Arial" '
                                                                '/><a:buChar '
                                                                'xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main" '
                                                                'char="•" />',
                                                   'color': '#20354A',
                                                   'line': 'none',
                                                   'margin': '0cm',
                                                   'autoFit': 'none',
                                                   'indent': '-22.5pt',
                                                   'marginLeft': '22.5pt'},
                                         'paragraphs': [{'command': 'set',
                                                         'path': '{object}/paragraph[1]',
                                                         'props': {'indent': '-22.5pt',
                                                                   'marginLeft': '22.5pt',
                                                                   'bulletRaw': '<a:buFont '
                                                                                'xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main" '
                                                                                'charset="0" '
                                                                                'panose="020B0604020202020204" '
                                                                                'pitchFamily="34" '
                                                                                'typeface="Arial" '
                                                                                '/><a:buChar '
                                                                                'xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main" '
                                                                                'char="•" />'}},
                                                        {'command': 'add',
                                                         'parent': '{object}/paragraph[1]',
                                                         'type': 'run',
                                                         'props': {'color': '#20354A',
                                                                   'text': 'Reduce once'}},
                                                        {'command': 'add',
                                                         'parent': '{object}/paragraph[1]',
                                                         'type': 'run',
                                                         'props': {'color': '#20354A',
                                                                   'text': ' '}},
                                                        {'command': 'add',
                                                         'parent': '{object}/paragraph[1]',
                                                         'type': 'run',
                                                         'props': {'color': '#20354A',
                                                                   'text': 'data exchange  per '
                                                                           'cycle'}}]}}}


def build_commands():
    """Keep the text editable and reuse the approved diagram without redrawing it.

    Crop the reference inside PowerPoint, preserving the original PNG pixels.
    The crop excludes the reference title, left column and bottom takeaway.
    """
    commands = [slide.title(size=30)]
    commands.append(slide.shape("TitleRule", 0.35, 0.78, 12.64, 2 / 72,
                                fill=TEAL))

    commands.append(slide.shape("Execution.Heading", 0.35, 1.25, 4.0, 0.7,
                                text="Cycle-Accurate Execution", size=22,
                                bold="true", color=NAVY))
    for index, (y, text) in enumerate([
        (2.03, "LI-TDM-based execution"),
        (2.55, "Optimized communication flow"),
    ], 1):
        commands.append(slide.shape(f"Execution.Bullet{index}", 0.45, y + 0.11,
                                    0.09, 0.09, fill=TEAL, preset="ellipse"))
        commands.append(slide.shape(f"Execution.Text{index}", 0.68, y, 3.58, 0.6,
                                    text=text, size=18))
    commands.append(slide.shape("Execution.Attribution", 0.68, 3.13, 3.58, 0.38,
                                text="Based on DUOHUAFEN", size=14,
                                color="607184"))

    commands.append(slide.shape("Pause.Heading", 0.35, 4.12, 4.0, 0.7,
                                text="Cycle-Consistent Pause", size=22,
                                bold="true", color=NAVY))
    for index, text in enumerate([
        "Stabilize progress", "Set a common target", "Advance and verify",
    ], 1):
        y = 4.92 + (index - 1) * 0.56
        commands.append(slide.shape(f"Pause.Number{index}", 0.43, y, 0.32, 0.32,
                                    text=str(index), size=14, bold="true",
                                    color="FFFFFF", fill=TEAL, preset="ellipse",
                                    align="center", valign="middle"))
        commands.append(slide.shape(f"Pause.Text{index}", 0.91, y - 0.01,
                                    3.33, 0.48, text=text, size=18))

    # Pixel coordinates of the complete right-hand panel in the 1672 x 941 PNG.
    left, top, right, bottom = 594, 120, 1654, 850
    source_width, source_height = 1672, 941
    width = 8.48
    height = width * (bottom - top) / (right - left)
    crop = (100 * left / source_width, 100 * top / source_height,
            100 * (source_width - right) / source_width,
            100 * (source_height - bottom) / source_height)
    commands.append({
        "command": "add", "parent": "/slide[1]", "type": "picture",
        "props": {
            "name": "S06.Pause.Illustration",
            "src": str(THESIS / "figure/presentation-reference/midterm-progress-06-v1.png"),
            "x": inches(4.50), "y": inches(1.12),
            "width": inches(width), "height": inches(height),
            "crop": ",".join(f"{value:.6f}" for value in crop),
            "alt": "Illustrative global-pause coordination: receive barriers stabilize "
                   "FPGA B at cycle 41 and FPGA A at 42; Host configures target 43, "
                   "releases B before A, and verifies both stopped at cycle 43.",
        },
    })
    commands.append(slide.shape("PageNumber", 12.72, 7.25, 0.25, 0.20,
                                text="6", size=10, color="607184", align="right"))
    commands.append({
        "command": "add", "parent": "/slide[1]", "type": "notes",
        "props": {"text": (
            "REMUS builds on DUOHUAFEN's LI-TDM for cycle-accurate execution. The first-stage "
            'receive and last-stage send are omitted to reduce redundant communication; this is a '
            'protocol optimization, not a measured percentage speedup. Keep these implementation '
            'details in the narration. For global pause, the Host collects all receive-barrier '
            'acknowledgements before sampling stable counters. Barrier acknowledgement alone is not'
            ' a valid global pause. In the illustrative example, B is at 41 and A at 42. The common'
            ' target is 43; configure two steps for B and one for A while barriers remain held, '
            'then release B before A. LI-TDM dependencies still apply. Finally check stopped/pause '
            'status and final counters on all partitions. Equal logical cycles do not imply '
            'simultaneous physical stops or prove all-state equivalence. Required propagation must '
            "finish. The diagram's shared arrows are a simplified visual summary of Host operations"
            ' on each partition, not FPGA-to-FPGA forwarding of Host commands. The cycle numbers '
            'are illustrative, not experimental data. Source: '
            'src/midterm/progress/cycle_control.tex. The right illustration is intentionally a '
            'raster crop per user request; the title, left text and page number are editable. The '
            'three requested supplementary callouts from the design reference are omitted. '
            'Reference [1]: G. Zhu. Cross-Node Deployment of Digital Logic Design for FPGA Cloud. '
            "Master's thesis, ShanghaiTech University, 2024."
        )},
    })
    commands = apply_layout_edits(commands, LAYOUT_EDITS)
    # Explicit title spacing and page-specific finishing objects.
    commands.extend([{'command': 'set', 'path': '/slide[1]/shape[@name=S06.Title]', 'props': {'lineSpacing': '0.9x'}},
     {'command': 'add',
      'parent': '/slide[1]',
      'type': 'shape',
      'props': {'name': 'S06.Reference1',
                'x': '0.400000in',
                'y': '7.060000in',
                'width': '12.150000in',
                'height': '0.280000in',
                'fill': 'none',
                'line': 'none',
                'shadow': 'none',
                'font': 'Arial',
                'size': '10',
                'color': '607184',
                'margin': '0pt',
                'autoFit': 'none',
                'text': '[1] G. Zhu. Cross-Node Deployment of Digital Logic Design for FPGA Cloud. '
                        "Master's thesis, ShanghaiTech University, 2024."}}])
    return commands
