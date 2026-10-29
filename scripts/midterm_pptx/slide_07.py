"""Page 7: distributed state capture and the two restoration paths."""

from .common import SlideAPI, THESIS, NAVY, TEAL, inches

TITLE = "7. Distributed State Capture, Restore and Replay"
OUTPUT_STEM = "REMUS_Progress_Slide_7"
PREVIEW_STEM = "midterm-progress-07"
slide = SlideAPI(7)


def build_commands():
    """Build the approved method-first layout with the original experiment image.

    Each text block is a native shape. Emphasis is applied to matching runs,
    rather than placing fragments manually. The screenshot is embedded without
    resampling or cropping; it remains independent of the editable caption.
    """
    commands = [slide.title(size=30)]
    commands.append(slide.shape("TitleRule", 0.35, 0.78, 12.64, 2 / 72, fill=TEAL))

    sections = [
        ("Snapshot", "01", "Global Snapshot", 1.40,
         "Capture partition states at the same DUT cycle.",
         "Reuse REMU's Scan Dump mechanism."),
        ("Restore", "02", "FPGA Restore", 3.35,
         "Write back scan data by partition.",
         "Restore local registers, SRAM and memory."),
        ("Replay", "03", "Software RTL Replay", 5.30,
         "Decode partition data through state mapping.",
         "Load RTL states and replay recorded inputs."),
    ]
    for name, number, heading, y, first, second in sections:
        commands.append(slide.shape(f"{name}.Number", 0.40, y, 0.50, 0.52,
                                    text=number, size=24, bold="true", color=TEAL))
        commands.append(slide.shape(f"{name}.Heading", 1.05, y, 4.95, 0.52,
                                    text=heading, size=24, bold="true", color=NAVY))
        for index, text in enumerate((first, second), 1):
            commands.append(slide.shape(f"{name}.Text{index}", 0.40,
                                        y + 0.63 + (index - 1) * 0.62,
                                        5.55, 0.60, text=text, size=18))

    for name, phrase in (("Restore", "by partition"), ("Replay", "state mapping")):
        commands.append({
            "command": "set",
            "path": f"/slide[1]/shape[@name=S07.{name}.Text1]",
            "props": {"find": phrase, "bold": "true", "color": NAVY},
        })

    # This is a Cosim screenshot, not a photograph/log of physical FPGA execution.
    # Keep its identity visible while leaving detailed evidence scope in notes.
    x, y, width = 6.35, 2.15, 6.64
    height = width * 522 / 1275
    commands.append(slide.shape("Evidence.Source", x, y - 0.35, width, 0.25,
                                text="Cosim checkpoint / RTL replay", size=12,
                                color="607184"))
    commands.append({
        "command": "add", "parent": "/slide[1]", "type": "picture",
        "props": {
            "name": "S07.Evidence.Waveform",
            "src": str(THESIS / "experiments/figure/picorv32-cosim-vs-replay-state-tick42080.png"),
            "x": inches(x), "y": inches(y),
            "width": inches(width), "height": inches(height),
            "alt": "PicoRV32 two-partition Cosim checkpoint values at DUT cycle 42080 "
                   "above the software RTL replay waveform, restored from cycle 2048. "
                   "Six selected signal values match at the comparison point.",
        },
    })
    commands.append(slide.shape("Evidence.Conclusion", x, y + height + 0.28,
                                width, 1.10,
                                text="Waveform replay reproduces the same signal\n"
                                     "values as FPGA execution.",
                                size=20, color=NAVY))
    commands.append(slide.shape("PageNumber", 12.72, 7.25, 0.25, 0.20,
                                text="7", size=10, color="607184", align="right"))
    commands.append({
        "command": "add", "parent": "/slide[1]", "type": "notes",
        "props": {"text": (
            "The previous slide establishes a common DUT cycle. REMUS reuses REMU's "
            "local Scan Dump and organizes per-partition scan files as a Global Snapshot. "
            "Memory and input management retain the existing REMU mechanisms. "
            "FPGA Restore writes each partition's scan data back to the corresponding "
            "FPGA with the matching design and scan layout, restoring local registers "
            "and SRAM plus the memory-model data before execution resumes. "
            "Software restoration instead decodes local scan positions through state "
            "mapping and loads the corresponding RTL objects. Recorded inputs are "
            "replayed by logical cycle, enabling waveform observation. "
            "The user-approved conclusion summarizes reported tested functionality; "
            "it is not an all-state or all-cycle equivalence assertion. "
            "The displayed image specifically compares a TWO-PARTITION COSIM checkpoint "
            "at cycle 42080 with Icarus Verilog software RTL replay from checkpoint 2048. "
            "Six selected signals match at relative cycle 40032. Inputs remain unchanged "
            "after 2048 in this example. It is not a physical-board restore screenshot. "
            "The author separately confirmed board-vs-Cosim checkpoint consistency and "
            "FPGA restoration/replay results; original board comparison records are still "
            "being archived. Do not present this software example as direct evidence "
            "of physical FPGA restore or merge different observation sets into a full "
            "equivalence claim. Sources: src/midterm/progress/state_replay.tex; "
            "experiments/picorv32-cosim-replay.md; experiments/board-execution.md. "
            "Design: figure/presentation-reference/midterm-state-replay-07-v2.png. "
            "All slide text is editable; the experiment screenshot is an unchanged raster."
        )},
    })
    return commands
