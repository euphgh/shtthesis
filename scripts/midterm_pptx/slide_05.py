"""Page 5: REMUS: Overall Workflow and Mid-Term Scope."""

from .common import SlideAPI, NAVY, TEAL, AMBER, INK, inches

TITLE = '5. REMUS: Overall Workflow and Mid-Term Scope'
slide = SlideAPI(5)


def build_commands():
    """Rebuild the updated five-stage reference; state capture uses the blue theme."""
    commands = [slide.title(size=30)]
    commands.append(slide.shape("TitleRule", 0.35, 0.78, 12.64, 2 / 72, fill=TEAL))
    commands.append(
        slide.shape(
            "Workflow.Heading",
            0.35,
            1.05,
            8.0,
            0.40,
            text="Overall Workflow",
            size=22,
            bold="true",
            color=NAVY,
        )
    )
    stages = [
        ("RTL", 0.35, 2.12, "RTL Design", ""),
        ("Partition", 2.68, 2.25, "Automated\nPartitioning", ""),
        (
            "Deploy",
            5.14,
            2.36,
            "Multi-FPGA\nDeployment",
            "Fabric routing &\nruntime control",
        ),
        (
            "Cycle",
            7.71,
            2.85,
            "Cycle-Accurate\nExecution & Global Pause",
            "Synchronized DUT cycles",
        ),
        (
            "State",
            10.77,
            2.22,
            "State Capture,\nRestore & Replay",
            "Debug and replay support",
        ),
    ]
    for i, (name, x, width, title, caption) in enumerate(stages, 1):
        center = x + width / 2
        commands.append(
            slide.shape(
                f"{name}.Panel",
                x,
                1.60,
                width,
                3.36,
                fill="EAF4F3",
                preset="roundRect",
                adj="adj:val 6500",
            )
        )
        commands.append(
            slide.shape(
                f"{name}.Number",
                center - 0.235,
                1.76,
                0.47,
                0.47,
                text=str(i),
                size=21,
                bold="true",
                color="FFFFFF",
                fill=TEAL,
                preset="ellipse",
                align="center",
                valign="center",
            )
        )
        commands.append(
            slide.shape(
                f"{name}.Title",
                x + 0.10,
                2.34,
                width - 0.20,
                0.84,
                text=title,
                size=17,
                bold="true",
                color=NAVY,
                align="center",
            )
        )
        if caption:
            commands.append(
                slide.shape(
                    f"{name}.Caption",
                    x + 0.10,
                    3.26 if name == "Cycle" else 3.06,
                    width - 0.20,
                    0.51,
                    text=caption,
                    size=14,
                    color=INK,
                    align="center",
                )
            )
    # Add progression arrows after every panel so the next panel cannot hide their tips.
    for i, (_, x, width, _, _) in enumerate(stages[:-1], 1):
        commands.append(
            slide.shape(
                f"Workflow.Arrow{i}",
                x + width - 0.09,
                3.20,
                0.39,
                0.30,
                fill=AMBER,
                preset="rightArrow",
            )
        )

    commands.append(
        slide.picture(
            "RTL.Document", "rtl-design.png", (286, 233, 979, 1074), 0.855, 3.52, 1.11
        )
    )
    commands.append(
        slide.picture(
            "Partition.Circuit",
            "circuit-partitioning.png",
            (199, 234, 1056, 1020),
            3.08,
            3.58,
            1.45,
        )
    )
    chip_box = (268, 297, 987, 991)
    for name, x, y in [
        ("TL", 5.62, 3.62),
        ("TR", 6.52, 3.62),
        ("BL", 5.62, 4.18),
        ("BR", 6.52, 4.18),
    ]:
        commands.append(
            slide.picture(f"Deploy.{name}", "fpga-chip.png", chip_box, x, y, 0.50)
        )

    def connector(name, **props):
        commands.append(slide.connector(name, **{"color": NAVY, "lineWidth": "1.6pt", **props}))

    for start, end, side1, side2 in [
        ("TL", "TR", "right", "left"),
        ("BL", "BR", "right", "left"),
        ("TL", "BL", "bottom", "top"),
        ("TR", "BR", "bottom", "top"),
    ]:
        connector(
            f"Deploy.Link{start}{end}",
            **{
                "from": f"/slide[1]/picture[@name=S05.Deploy.{start}]",
                "to": f"/slide[1]/picture[@name=S05.Deploy.{end}]",
                "fromSide": side1,
                "toSide": side2,
                "color": AMBER,
            },
        )
    commands.append(
        slide.shape(
            "Deploy.Scope",
            5.26,
            4.74,
            2.12,
            0.20,
            text="Illustrative topology",
            size=11,
            color="607184",
            align="center",
        )
    )

    # Native clock/pause icons and a dashed sync bus preserve the reference's semantics.
    clock_centers = [8.25, 9.135, 10.02]
    for i, center in enumerate(clock_centers):
        commands.append(
            slide.shape(
                f"Cycle.Icon{i}",
                center - 0.24,
                3.78,
                0.48,
                0.48,
                fill="FFFFFF",
                line=f"{TEAL if i == 1 else NAVY}:2.2",
                preset="ellipse",
            )
        )
        if i == 1:
            for j, offset in enumerate((-0.092, 0.035)):
                commands.append(
                    slide.shape(
                        f"Cycle.PauseBar{j}",
                        center + offset,
                        3.905,
                        0.057,
                        0.23,
                        fill=TEAL,
                        preset="roundRect",
                    )
                )
        else:
            connector(
                f"Cycle.Clock{i}.Minute",
                x=inches(center),
                y="3.865in",
                width="0in",
                height="0.155in",
                lineWidth="2pt",
            )
            connector(
                f"Cycle.Clock{i}.Hour",
                x=inches(center),
                y="4.02in",
                width="0.105in",
                height="0.09in",
                lineWidth="2pt",
            )
        connector(
            f"Cycle.SyncDrop{i}",
            x=inches(center),
            y="4.34in",
            width="0in",
            height="0.18in",
            lineDash="dash",
        )
    for i in range(2):
        connector(
            f"Cycle.Progress{i}",
            **{
                "from": f"/slide[1]/shape[@name=S05.Cycle.Icon{i}]",
                "to": f"/slide[1]/shape[@name=S05.Cycle.Icon{i + 1}]",
                "fromSide": "right",
                "toSide": "left",
                "tailEnd": "triangle",
            },
        )
    connector(
        "Cycle.SyncBus",
        x="8.25in",
        y="4.52in",
        width="1.77in",
        height="0in",
        lineDash="dash",
    )
    commands.append(
        slide.shape(
            "Cycle.SyncLabel",
            7.93,
            4.61,
            2.41,
            0.24,
            text="Synchronized",
            size=13,
            color=NAVY,
            align="center",
        )
    )

    # Stage 5 deliberately has no amber/yellow: panel, badge and state arrow match blue stages.
    commands.append(
        slide.picture(
            "State.Snapshot",
            "global-snapshot.png",
            (210, 206, 1044, 1104),
            11.02,
            3.77,
            0.53,
        )
    )
    commands.append(
        slide.picture(
            "State.Waveform",
            "waveform-monitor.png",
            (154, 320, 1101, 1004),
            12.00,
            3.78,
            0.77,
        )
    )
    commands.append(
        slide.shape("State.ToReplay", 11.61, 3.97, 0.32, 0.18, fill=TEAL, preset="rightArrow")
    )
    commands.append(
        slide.shape(
            "State.Scope",
            10.87,
            4.43,
            2.02,
            0.43,
            text="Restore / replay\nPlanned",
            size=12,
            color="607184",
            align="center",
        )
    )

    commands.append(
        slide.shape(
            "Scope.Heading",
            0.35,
            5.29,
            4.0,
            0.40,
            text="Mid-Term Scope",
            size=22,
            bold="true",
            color=NAVY,
        )
    )
    commands.append(slide.shape("Scope.Rule", 3.55, 5.51, 9.44, 0.012, fill="BDCBD4"))
    commands.append(
        slide.shape(
            "Scope.Panel",
            0.35,
            5.87,
            12.64,
            1.20,
            fill="EAF4F3",
            preset="roundRect",
            adj="adj:val 8000",
        )
    )
    scopes = [
        ("Partitioning\nframework", "RTL partitioning\nand mapping"),
        ("Cycle-accurate\nexecution", "Multi-FPGA runs\nwith cycle control"),
        ("Global pause &\nstate dump", "Global snapshots\nacross FPGAs"),
        ("Restore & replay", "Planned: restore\n& replay checks"),
        ("Dual-FPGA\nprototype", "Initial evaluation\nand system tests"),
    ]
    for i, (heading, text) in enumerate(scopes):
        x = 0.35 + i * 2.528
        if i:
            commands.append(
                slide.shape(f"Scope.Divider{i}", x, 6.05, 0.009, 0.84, fill="BDCBD4")
            )
        commands.append(
            slide.shape(
                f"Scope.Bullet{i}",
                x + 0.17,
                6.105,
                0.095,
                0.095,
                fill=TEAL,
                preset="ellipse",
            )
        )
        commands.append(
            slide.shape(
                f"Scope.Title{i}",
                x + 0.37,
                6.02,
                2.04,
                0.48,
                text=heading,
                size=15,
                bold="true",
                color=NAVY,
            )
        )
        commands.append(
            slide.shape(
                f"Scope.Text{i}",
                x + 0.37,
                6.53,
                2.04,
                0.46,
                text=text,
                size=13,
                color=INK,
            )
        )
    commands.append(
        slide.shape(
            "PageNumber",
            12.72,
            7.25,
            0.25,
            0.20,
            text="5",
            size=10,
            color="607184",
            align="right",
        )
    )
    commands.append(
        {
            "command": "add",
            "parent": "/slide[1]",
            "type": "notes",
            "props": {
                "text": (
                    "Overall target workflow and mid-term work areas, based on the user's updated "
                    "five-stage reference figure/presentation-reference/midterm-background-05.png. "
                    "The State Capture, Restore & Replay card deliberately uses the same blue/teal "
                    "styling as preceding stages, not yellow. Fabric routing and runtime control "
                    "are folded into deployment; cycle execution and global pause form one stage. "
                    "The four FPGA icons are an illustrative topology, not evidence of a tested "
                    "four-FPGA system. State capture aggregates local states into a global snapshot; "
                    "the final icon depicts the intended path from snapshot through restoration "
                    "and replay to waveform reconstruction, not direct conversion of a dump into "
                    "a waveform. Restore/replay is planned for further development and validation "
                    "according to src/midterm/outline.md sections 1.1 and 1.7. Scope bullets are "
                    "work areas, not completed-feature checks; implementation and experiment "
                    "evidence belong on the later progress slides."
                )
            },
        }
    )
    return commands
