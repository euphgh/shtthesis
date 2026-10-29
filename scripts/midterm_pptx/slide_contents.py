"""Contents page introducing the four sections of the midterm defense."""

from .common import SlideAPI, NAVY, TEAL

TITLE = "Contents"
OUTPUT_STEM = "REMUS_Midterm_Contents"
PREVIEW_STEM = "midterm-contents"
slide = SlideAPI(0)


def build_commands():
    """Show the narrative as four numbered stops with one short description each.

    The page is separate from the numbered technical slides. No physical page
    references are shown, so adding a cover or merging the deck does not make
    the contents stale. All elements remain native PowerPoint shapes.
    """
    commands = [slide.title(size=32)]
    commands.append(slide.shape("TitleRule", 0.35, 0.78, 12.64, 2 / 72, fill=TEAL))
    rows = [
        ("Background & Research Goal",
         "Motivation, research gap and REMUS overview"),
        ("Research Progress",
         "Execution & pause · State & replay · Partitioning · Runtime"),
        ("Prototype & Evaluation",
         "Dual-FPGA platform, workloads and experimental results"),
        ("Current Challenges & Future Work",
         "Remaining limitations and the next research steps"),
    ]
    # The vertical path expresses presentation order; place it behind the stops.
    commands.append(slide.shape("NarrativePath", 1.075, 1.68, 0.025, 4.14,
                                fill="BDCBD4"))
    for index, (heading, description) in enumerate(rows, 1):
        y = 1.40 + (index - 1) * 1.38
        commands.append(slide.shape(f"Section{index}.Number", 0.77, y + 0.04,
                                    0.64, 0.64, text=f"{index:02}", size=22,
                                    bold="true", color="FFFFFF", fill=TEAL,
                                    preset="ellipse", align="center", valign="middle"))
        commands.append(slide.shape(f"Section{index}.Heading", 1.84, y, 10.65, 0.52,
                                    text=heading, size=27, bold="true", color=NAVY))
        commands.append(slide.shape(f"Section{index}.Description", 1.84, y + 0.64,
                                    10.65, 0.48, text=description, size=19,
                                    color="607184"))
    commands.append({
        "command": "add", "parent": "/slide[1]", "type": "notes",
        "props": {"text": (
            "Place this page after the cover and before the background section. "
            "Introduce the defense in four parts. First, motivate replayable multi-FPGA "
            "emulation, identify the research gap and outline REMUS. Second, explain "
            "cycle-accurate execution and consistent pause, distributed state capture "
            "and replay, automated partitioning, and the scalable Runtime/Fabric design. "
            "Third, present the dual-FPGA direct-PCIe prototype and measured results. "
            "Finally, connect observed limitations to future work on resource balance, "
            "execution performance, runtime control and system expansion. "
            "The current content mapping is background 1-5, progress 6-9, prototype 10 "
            "and future work 11. These are content identifiers rather than final deck "
            "page numbers. Source: docs/midterm-presentation-outline.md. "
            "This contents page does not assert completion of all technical goals."
        )},
    })
    return commands
