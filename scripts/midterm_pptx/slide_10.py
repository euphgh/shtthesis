"""Page 10: physical dual-FPGA platform, Linux execution and recorded metrics."""

from .common import SlideAPI, THESIS, NAVY, TEAL, AMBER, inches

TITLE = "10. Dual-FPGA Prototype and Evaluation"
OUTPUT_STEM = "REMUS_Prototype_Slide_10"
PREVIEW_STEM = "midterm-prototype-10"
slide = SlideAPI(10)


def cropped_picture(name, source, source_size, bounds, x, y, width, alt):
    """Embed the original image and apply an aspect-preserving PowerPoint crop."""
    source_width, source_height = source_size
    left, top, right, bottom = bounds
    height = width * (bottom - top) / (right - left)
    crop = (100 * left / source_width, 100 * top / source_height,
            100 * (source_width - right) / source_width,
            100 * (source_height - bottom) / source_height)
    return {
        "command": "add", "parent": "/slide[1]", "type": "picture",
        "props": {
            "name": f"S10.{name}", "src": str(THESIS / source),
            "x": inches(x), "y": inches(y),
            "width": inches(width), "height": inches(height),
            "crop": ",".join(f"{value:.6f}" for value in crop), "alt": alt,
        },
    }


def build_commands():
    """Use native text/table cells around two unmodified photographic sources.

    The left crop removes the oscilloscope. The right crop retains the continuous
    Linux shell region, including cpuinfo and uname; it does not reconstruct logs.
    The workload table uses editable cell shapes, with statistics kept separate
    from photos so measurement conditions remain readable and maintainable.
    """
    commands = [slide.title(size=30)]
    commands.append(slide.shape("TitleRule", 0.35, 0.78, 12.64, 2 / 72, fill=TEAL))
    for name, text, x, width in [
        ("Platform", "Experimental Platform", 0.35, 4.65),
        ("Workloads", "DUTs and Workloads", 5.45, 7.54),
    ]:
        commands.append(slide.shape(f"{name}.Heading", x, 1.04, width, 0.46,
                                    text=text, size=22, bold="true", color=NAVY))

    commands.append(cropped_picture(
        "Platform.Photo", "figure/remus-2fpga-hw.jpg", (1279, 1706),
        (70, 600, 1220, 1410), 0.35, 1.62, 4.65,
        "Two NM37 VU37P FPGA boards inside the shared PCIe Host; "
        "real dual-FPGA setup with board-to-board optical connections."))
    commands.append(slide.shape("Platform.PhotoLabel", 0.48, 1.76, 2.66, 0.36,
                                text="Two NM37 FPGA boards", size=13, bold="true",
                                color="FFFFFF", fill=NAVY, margin="3pt"))
    for index, text in enumerate([
        "Two NM37 boards with VU37P FPGAs",
        "PCIe access from a shared Host",
        "QSFP/Aurora links between FPGAs",
    ], 1):
        commands.append(slide.shape(f"Platform.Text{index}", 0.35,
                                    5.10 + (index - 1) * 0.36, 4.65, 0.35,
                                    text=text, size=17))

    # Separate cell text and rules make the workload table fully editable.
    x, width, split = 5.45, 7.54, 3.45
    commands.append(slide.shape("Workloads.HeaderPanel", x, 1.62, width, 0.35,
                                fill="EAF4F3"))
    for name, text, dx, cell_width in [
        ("DUTs", "DUTs", 0.15, split - 0.30),
        ("Programs", "Workloads", split + 0.15, width - split - 0.30),
    ]:
        commands.append(slide.shape(f"Workloads.{name}.Header", x + dx, 1.66,
                                    cell_width, 0.28, text=text, size=14,
                                    bold="true", color=TEAL))
    for index, (dut, workload) in enumerate([
        ("PicoRV32 · Rocket", "Bare-metal programs"),
        ("Nanhu · KMH", "OpenSBI and Linux"),
    ], 1):
        y = 2.02 + (index - 1) * 0.43
        commands.append(slide.shape(f"Workloads.DUT{index}", x + 0.15, y,
                                    split - 0.30, 0.36, text=dut, size=17,
                                    bold="true", color=NAVY))
        commands.append(slide.shape(f"Workloads.Program{index}", x + split + 0.15,
                                    y, width - split - 0.30, 0.36,
                                    text=workload, size=17))
        commands.append(slide.shape(f"Workloads.Rule{index}", x, y + 0.40,
                                    width, 0.008, fill="D8E3E9"))

    commands.append(cropped_picture(
        "Linux.Console", "experiments/figure/kmh-2fpga-linux-cli.png", (1370, 1249),
        (0, 764, 1370, 1222), 5.45, 3.04, 7.54,
        "KMH physical dual-FPGA Linux shell: cat /proc/cpuinfo, "
        "processor and hart 0, ICT xiangshan, uname -a and Linux 6.12.0+ riscv64."))
    commands.append(slide.shape("Linux.Caption", 5.45, 5.79, 7.54, 0.56,
                                text="KMH boots Linux and supports interactive shell commands.",
                                size=18, color=NAVY))

    # Observed logical execution rates / Host pause time, not physical clock specs.
    commands.append(slide.shape("Metrics.Panel", 0.35, 6.43, 12.64, 0.66,
                                fill="EAF4F3"))
    metrics = [
        ("PicoRV32 · Effective Rate", "≈0.327 MHz", TEAL),
        ("KMH · Effective Rate", "≈0.322 MHz", TEAL),
        ("Global Pause · Host-Observed", "≈0.8–1.1 ms", AMBER),
    ]
    for index, (label, value, color) in enumerate(metrics):
        x = 0.35 + index * (12.64 / 3)
        if index:
            commands.append(slide.shape(f"Metrics.Divider{index}", x, 6.51,
                                        0.009, 0.50, fill="BDCBD4"))
        commands.append(slide.shape(f"Metrics.Label{index}", x + 0.18, 6.48,
                                    3.85, 0.22, text=label, size=12, color=NAVY))
        commands.append(slide.shape(f"Metrics.Value{index}", x + 0.18, 6.72,
                                    3.85, 0.37, text=value, size=22,
                                    color=color, bold="true"))
    commands.append(slide.shape("Metrics.Scope", 0.35, 7.18, 11.90, 0.22,
                                text="Measured run windows; KMH measured before checkpoint save. "
                                     "Pause latency includes Host control.",
                                size=10, color="607184"))
    commands.append(slide.shape("PageNumber", 12.63, 7.25, 0.34, 0.20,
                                text="10", size=10, color="607184", align="right"))
    commands.append({
        "command": "add", "parent": "/slide[1]", "type": "notes",
        "props": {"text": (
            "This is the real dual-FPGA PCIe-direct prototype, not a completed Fabric "
            "board deployment. Two NM37 boards use VU37P devices with separate PCIe "
            "Host access and QSFP/Aurora board communication. The real photo is "
            "figure/remus-2fpga-hw.jpg; its oscilloscope is cropped away. "
            "PicoRV32 and Rocket run hand-written bare-metal workloads; Nanhu and "
            "single-core KMH run OpenSBI/Linux, as confirmed by the author in "
            "src/midterm/progress/prototype.tex. The terminal specifically belongs "
            "to KMH, not all four DUTs. The crop shows shell commands, cpuinfo and "
            "uname for Linux 6.12.0+. Image timestamps are not Host elapsed time. "
            "Performance comes from experiments/board-performance.md and raw/perf.txt. "
            "PicoRV32's longer runs are 0.326741 and 0.327423 MHz; combined cycles/time "
            "gives about 0.326834 MHz, rounded here to 0.327. KMH's 0.322073 MHz is "
            "a 1095817-cycle, 3.40238-second window BEFORE checkpoint save, not the "
            "full Linux boot or post-CLI rate. These are logical progress over Host "
            "time, not FPGA physical clocks. Pause records include 23 PicoRV32 "
            "observations from 0.803824 to 0.925013 ms and one KMH observation of "
            "1.04744 ms, rounded to approximately 0.8–1.1 ms. They are Host-visible "
            "synchronized-pause times, not pure hardware barrier latency, independent "
            "repeat trials or a success-rate measurement. Detailed checkpoint timings "
            "and resources are intentionally omitted. Sources: "
            "src/midterm/progress/prototype.tex; experiments/board-execution.md; "
            "experiments/board-performance.md. Original photos are embedded unchanged "
            "and cropped only through PPT properties; all slide text/cells are editable."
        )},
    })
    return commands
