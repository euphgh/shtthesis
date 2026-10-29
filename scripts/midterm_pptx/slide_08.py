"""Page 8: automated partitioning and measured per-Part resource distribution."""

from .common import SlideAPI, NAVY, TEAL, inches

TITLE = 'Progress3: Automated Multi-FPGA Circuit Partitioning'
OUTPUT_STEM = "REMUS_Progress_Slide_8"
PREVIEW_STEM = "midterm-progress-08"
slide = SlideAPI(8)

# Vivado 2024.2, KMH two-part EMU_SYSTEM hierarchy. Values are percentages
# of the device capacity reported by Vivado, not percentages of both Parts.
# Source: experiments/synthesis-utilization.md, section 3.2.
RESOURCES = ("LUT", "FF", "BRAM")
PART0 = (73.18, 17.66, 14.31)
PART1 = (75.77, 8.17, 0.00)


def build_commands():
    """Use an editable chart for resource evidence and qualify early efficiency observations.

    The native chart embeds the measured data. Unfinished netlist-baseline
    comparisons and provisional ratios are deliberately not charted as results.
    """
    commands = [slide.title(size=30)]
    commands.append(slide.shape("TitleRule", 0.35, 0.78, 12.64, 2 / 72, fill=TEAL))
    commands.append(slide.shape("Method.Heading", 0.40, 1.20, 3.95, 0.5,
                                text="Automated Partitioning", size=22,
                                bold="true", color=NAVY))
    for index, text in enumerate([
        "Adaptive-granularity\nRTL partitioning",
        "KaHyPar-based\nhypergraph partitioning",
        "Path-cut analysis\nfor LI-TDM",
    ], 1):
        y = 2.00 + (index - 1) * 1.02
        commands.append(slide.shape(f"Method.Number{index}", 0.42, y + 0.04,
                                    0.33, 0.33, text=str(index), size=14, bold="true",
                                    color="FFFFFF", fill=TEAL, preset="ellipse",
                                    align="center", valign="middle"))
        commands.append(slide.shape(f"Method.Text{index}", 0.92, y, 3.35, 0.78,
                                    text=text, size=19))
    commands.append(slide.shape("Efficiency.Status", 0.40, 5.43, 3.95, 0.35,
                                text="Preliminary observation", size=14, color="607184"))
    commands.append(slide.shape("Efficiency.Text", 0.40, 5.87, 3.95, 1.05,
                                text="Smaller graphs and faster solving\non well-structured RTL.",
                                size=18, color=NAVY))

    commands.append(slide.shape("Results.Heading", 4.78, 1.20, 8.18, 0.5,
                                text="Post-Synthesis Resource Utilization", size=22,
                                bold="true", color=NAVY))
    commands.append(slide.shape("Results.Context", 4.78, 1.76, 8.18, 0.35,
                                text="KMH · Two partitions · Utilization (%)", size=16,
                                color="607184"))
    commands.append({
        "command": "add", "parent": "/slide[1]", "type": "chart",
        "props": {
            "name": "S08.Resources.Chart", "chartType": "column",
            "x": inches(4.72), "y": inches(2.18),
            "width": inches(8.25), "height": inches(3.80),
            "categories": ",".join(RESOURCES),
            "series1.name": "Part 0", "series1.values": ",".join(f"{v:.2f}" for v in PART0),
            "series1.color": NAVY,
            "series2.name": "Part 1", "series2.values": ",".join(f"{v:.2f}" for v in PART1),
            "series2.color": TEAL,
            "title": "none", "legend": "top", "legendFont": "15:20354A:Arial",
            "axisfont": "16:20354A:Arial", "axismin": "0", "axismax": "90",
            "majorunit": "20", "axisnumfmt": "0",
            "dataLabels": "value", "labelPos": "outsideEnd",
            "labelfont": "18:20354A:Arial", "gapwidth": "90", "overlap": "-15",
            "gridlines": "DDE5EA:0.5", "chartareafill": "FFFFFF",
            "plotFill": "FFFFFF", "plotborder": "none", "chartborder": "none",
            "seriesoutline": "none",
        },
    })
    commands.append(slide.shape("Results.Observation", 4.78, 6.22, 8.18, 0.65,
                                text="Similar LUT usage, uneven FF and BRAM distribution.",
                                size=20, color=NAVY))
    commands.append(slide.shape("Results.Scope", 4.78, 6.92, 8.18, 0.28,
                                text="EMU_SYSTEM synthesis; percentages of device capacity.",
                                size=12, color="607184"))
    commands.append(slide.shape("PageNumber", 12.72, 7.25, 0.25, 0.20,
                                text="8", size=10, color="607184", align="right"))
    commands.append({
        "command": "add", "parent": "/slide[1]", "type": "notes",
        "props": {"text": (
            "REMUS implements adaptive RTL granularity selection, weighted hypergraph "
            "partitioning using KaHyPar, and path-cut analysis for LI-TDM configuration. "
            "The author's revised slide reports graph size around one tenth of the "
            "netlist-level baseline, with no significant change in cut-size and "
            "path-cut number. These are author-reported comparisons; this slide "
            "synchronization does not independently validate the baseline runs. "
            "Confirm matched DUTs, configurations and graph-size definitions when "
            "finalizing the experimental record. "
            "The main chart uses archived KMH two-Part Vivado 2024.2 synthesis results: "
            "Part 0 LUT/FF/BRAM utilization 73.18/17.66/14.31 percent; Part 1 "
            "75.77/8.17/0.00 percent. BRAM counts are 288.5 and 0 tiles. URAM "
            "is 13 versus 0, omitted from the plot for focus. The scope is "
            "role_i/ClockResetCore_0/emu_system, including inserted infrastructure; "
            "not pure DUT, full board consumption, or post-route utilization. "
            "The denominator is whole-device capacity, not the remaining Part budget. "
            "The observed resource asymmetry does not isolate adaptive granularity or "
            "scalar weights as its sole cause. Constraints, module grouping and synthesis "
            "mapping may also matter. Exact build matching between partition summaries "
            "and synthesis reports remains to be completed, so no estimation-error or "
            "baseline-gain inference is made from their combination. "
            "Sources: experiments/synthesis-utilization.md (3.2); "
            "src/midterm/progress/partitioning.tex; src/midterm/problems.tex."
        )},
    })
    return commands
