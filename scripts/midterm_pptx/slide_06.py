"""Page 6: concise execution summary and a cropped global-pause illustration."""

from .common import SlideAPI, THESIS, NAVY, TEAL, inches

TITLE = "6. Cycle-Accurate Execution and Global Pause"
OUTPUT_STEM = "REMUS_Progress_Slide_6"
PREVIEW_STEM = "midterm-progress-06"
slide = SlideAPI(6)


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
            "REMUS builds on DUOHUAFEN's LI-TDM for cycle-accurate execution. "
            "The first-stage receive and last-stage send are omitted to reduce "
            "redundant communication; this is a protocol optimization, not a measured "
            "percentage speedup. Keep these implementation details in the narration. "
            "For global pause, the Host collects all receive-barrier acknowledgements "
            "before sampling stable counters. Barrier acknowledgement alone is not "
            "a valid global pause. In the illustrative example, B is at 41 and A at 42. "
            "The common target is 43; configure two steps for B and one for A while "
            "barriers remain held, then release B before A. LI-TDM dependencies still "
            "apply. Finally check stopped/pause status and final counters on all "
            "partitions. Equal logical cycles do not imply simultaneous physical "
            "stops or prove all-state equivalence. Required propagation must finish. "
            "The diagram's shared arrows are a simplified visual summary of Host "
            "operations on each partition, not FPGA-to-FPGA forwarding of Host commands. "
            "The cycle numbers are illustrative, not experimental data. "
            "Source: src/midterm/progress/cycle_control.tex. The right illustration "
            "is intentionally a raster crop per user request; the title, left text "
            "and page number are editable. The three requested supplementary "
            "callouts from the design reference are omitted."
        )},
    })
    return commands
