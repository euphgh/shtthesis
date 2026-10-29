"""Page 11: future work, with compact numbered headings and editable prose."""

from .common import apply_layout_edits, SlideAPI, NAVY, TEAL

TITLE = "11. Future Work"
OUTPUT_STEM = "REMUS_Future_Work_Slide_11"
PREVIEW_STEM = "midterm-future-work-11"
slide = SlideAPI(11)


# Final reviewed layout for this page. These properties override the base
# component layout below; edit revised text, geometry and rich text here.
LAYOUT_EDITS = {'remove': ['S11.Item3.Body', 'S11.Item2.Separator', 'S11.Item3.Number', 'S11.Item3.Heading'],
 'objects': {'S11.Item2.Body': {'props': {'font': 'Arial',
                                          'size': '18pt',
                                          'color': '#20354A',
                                          'bold': 'false',
                                          'align': 'left',
                                          'name': 'S11.Item2.Body',
                                          'x': '399.6pt',
                                          'y': '211.68pt',
                                          'width': '535.68pt',
                                          'height': '666528emu',
                                          'fill': 'none',
                                          'font.latin': 'Arial',
                                          'line': 'none',
                                          'margin': '0cm',
                                          'autoFit': 'none',
                                          'lineSpacing': '1.25x',
                                          'spaceBefore': '0pt',
                                          'spaceAfter': '0pt'},
                                'paragraphs': [{'command': 'set',
                                                'path': '{object}/paragraph[1]',
                                                'props': {'lineSpacing': '1.25x',
                                                          'spaceBefore': '0pt',
                                                          'spaceAfter': '0pt',
                                                          'font.latin': 'Arial',
                                                          'size': '18pt',
                                                          'color': '#20354A',
                                                          'text': 'Analyze execution and '
                                                                  'communication overheads on four '
                                                                  'FPGAs.'}}]},
             'S11.Item3.Separator': {'props': {'y': '3609067emu'}},
             'S11.Item4.Number': {'props': {'font': 'Arial',
                                            'size': '22pt',
                                            'color': '#008C95',
                                            'bold': 'true',
                                            'align': 'left',
                                            'name': 'S11.Item4.Number',
                                            'x': '34.56pt',
                                            'y': '3892531emu',
                                            'width': '27.36pt',
                                            'height': '34.56pt',
                                            'fill': 'none',
                                            'font.latin': 'Arial',
                                            'line': 'none',
                                            'margin': '0cm',
                                            'autoFit': 'none'},
                                  'paragraphs': [{'command': 'set',
                                                  'path': '{object}/paragraph[1]',
                                                  'props': {'font.latin': 'Arial',
                                                            'size': '22pt',
                                                            'bold': 'true',
                                                            'color': '#008C95',
                                                            'text': '3.'}}]},
             'S11.Item4.Heading': {'props': {'y': '3892531emu'}},
             'S11.Item4.Body': {'props': {'y': '3874243emu'}}}}


def build_commands():
    """Build four aligned text rows, retaining future-work status throughout.

    Numbers use the same font size and baseline as each heading, per the user's
    correction to the design reference. Separate native text boxes keep the
    wording and alignment editable without rasterizing the reference image.
    """
    commands = [slide.title(size=32)]
    commands.append(slide.shape("TitleRule", 0.35, 0.78, 12.64, 2 / 72, fill=TEAL))
    rows = [
        (1.36, "Fabric Deployment &\nFour-FPGA Integration", [
            "Complete board-level Fabric integration and validation.",
            "Build a four-FPGA emulation system.",
        ]),
        (2.96, "Performance Analysis &\nRuntime Optimization", [
            "Analyze execution and communication overheads on four FPGAs.",
            "Reduce polling overhead with interrupt-driven control.",
        ]),
        (4.56, "Partitioning Optimization\n& Evaluation", [
            "Improve multi-resource balance and reduce communication cost.",
            "Evaluate the impact on emulation performance.",
        ]),
        (6.18, "Thesis Writing", [
            "Consolidate experimental results and complete the thesis.",
        ]),
    ]
    heading_size = 22
    for index, (y, heading, lines) in enumerate(rows, 1):
        commands.append(slide.shape(f"Item{index}.Number", 0.48, y, 0.38, 0.48,
                                    text=f"{index}.", size=heading_size,
                                    bold="true", color=TEAL))
        commands.append(slide.shape(f"Item{index}.Heading", 1.00, y, 4.38, 0.92,
                                    text=heading, size=heading_size,
                                    bold="true", color=NAVY))
        commands.append(slide.shape(f"Item{index}.Body", 5.55, y - 0.02,
                                    7.44, 1.12, text="\n".join(lines), size=18,
                                    lineSpacing="1.25x", spaceBefore="0pt", spaceAfter="0pt"))
        if index < 4:
            commands.append(slide.shape(f"Item{index}.Separator", 0.48, y + 1.31,
                                        12.51, 0.012, fill="D8E3E9"))
    commands.append(slide.shape("PageNumber", 12.63, 7.25, 0.34, 0.20,
                                text="11", size=10, color="607184", align="right"))
    commands.append({
        "command": "add", "parent": "/slide[1]", "type": "notes",
        "props": {"text": (
            "The author's revised plan contains three items: Fabric board-level integration and validation followed by a four-FPGA system; execution and communication overhead analysis on that system; consolidation of results and thesis writing. These are future work. The separate partitioning-optimization item and interrupt-driven-control sentence were removed in the author's 2026-10-29 revision."
        )},
    })
    commands = apply_layout_edits(commands, LAYOUT_EDITS)
    # Explicit title spacing and page-specific finishing objects.
    commands.extend([{'command': 'set', 'path': '/slide[1]/shape[@name=S11.Title]', 'props': {'lineSpacing': '0.9x'}}])
    return commands
