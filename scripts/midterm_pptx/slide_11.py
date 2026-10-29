"""Page 11: future work, with compact numbered headings and editable prose."""

from .common import SlideAPI, NAVY, TEAL

TITLE = "11. Future Work"
OUTPUT_STEM = "REMUS_Future_Work_Slide_11"
PREVIEW_STEM = "midterm-future-work-11"
slide = SlideAPI(11)


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
            "This page combines the remaining problems with the work that addresses "
            "them; it does not repeat a separate problem list. First complete Fabric "
            "board-level integration and validation, then assemble a four-FPGA "
            "emulation system. That platform will support analysis of execution and "
            "communication overheads. Use the measurements to guide runtime changes, "
            "including interrupt-driven control to reduce Fabric polling overhead. "
            "Optimize partitioning for multiple resource types and communication cost, "
            "then evaluate whether those changes improve actual emulation performance. "
            "Do not promise a performance gain before the experiments. These technical "
            "activities may iterate rather than forming a strict one-pass sequence. "
            "Finally consolidate experimental results and complete the thesis. "
            "Fabric board validation, four-FPGA deployment and interrupt-driven control "
            "are future work, not completed results. No defense date is implied. "
            "Sources: src/midterm/problems.tex and src/midterm/next_plan.tex; wording "
            "and ordering follow the user's approved four-item plan. Design reference: "
            "figure/presentation-reference/midterm-future-work-11-v1.png. The user "
            "requested smaller 1., 2., 3., 4. numbering at the heading font size, "
            "replacing the large 01–04 in that image. All visible objects are native "
            "editable PowerPoint shapes, not an embedded design screenshot."
        )},
    })
    return commands
