"""Page 1: From RTL Simulation to Multi-FPGA Prototyping."""

from .common import apply_layout_edits, SlideAPI, NAVY, TEAL, AMBER

TITLE = 'Intro: From RTL Simulation to Multi-FPGA Prototyping'
slide = SlideAPI(1)


# Final reviewed layout for this page. These properties override the base
# component layout below; edit revised text, geometry and rich text here.
LAYOUT_EDITS = {'remove': [],
 'objects': {'S01.Title': {'props': {'font': 'Arial',
                                     'size': '32pt',
                                     'color': '#183B56',
                                     'bold': 'true',
                                     'align': 'left',
                                     'name': 'S01.Title',
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
                                                     'size': '32pt',
                                                     'bold': 'true',
                                                     'color': '#183B56',
                                                     'text': 'Intro: From RTL Simulation to '
                                                             'Multi-FPGA Prototyping'}}]}}}


def build_commands():
    """Reconstruct the three-stage reference with native shapes and two assets."""
    commands = [slide.title(size=32)]
    commands.append(slide.shape("TitleRule", 0.35, 0.78, 12.64, 2 / 72, fill=TEAL))
    rows = [
        (1.06, 1.75, "EAF4F3", "RTL Simulation",
         ["Full visibility", "Flexible debugging", "Low performance"]),
        (3.28, 1.75, "F1F5F8", "FPGA Prototyping",
         ["MHz-level execution", "Long software workloads", "Limited by single-FPGA capacity"]),
        (5.49, 1.70, "FCF4E8", "Multi-FPGA Prototyping",
         ["Partition large designs", "Extend capacity", "Enable large-scale SoC execution"]),
    ]
    for index, (y, height, fill, heading, bullets) in enumerate(rows, 1):
        prefix = f"Stage{index}"
        commands.append(slide.shape(f"{prefix}.Panel", 0.35, y, 12.64, height,
                              fill=fill, preset="roundRect", adj="adj:val 10000"))
        commands.append(slide.shape(f"{prefix}.Divider", 5.015, y + 0.17, 0.009, height - 0.34,
                              fill="BDCBD4"))
        commands.append(slide.shape(f"{prefix}.Heading", 5.52, y + 0.20, 7.1, 0.40,
                              text=heading, size=22, bold="true", color=NAVY))
        for bullet_index, text in enumerate(bullets, 1):
            text_y = y + 0.64 + (bullet_index - 1) * 0.32
            commands.append(slide.shape(f"{prefix}.Bullet{bullet_index}", 5.65, text_y + 0.085,
                                  0.105, 0.105, fill=TEAL, preset="ellipse"))
            commands.append(slide.shape(f"{prefix}.Text{bullet_index}", 5.98, text_y, 6.70, 0.32,
                                  text=text))

    # Reference arrows fit within the reserved gap between each pair of panels.
    commands.append(slide.shape("Progress1", 6.37, 2.815, 0.61, 0.455, fill=AMBER,
                          preset="downArrow", adj="adj1:val 48000,adj2:val 55000"))
    commands.append(slide.shape("Progress2", 6.37, 5.035, 0.61, 0.445, fill="91A5B5",
                          preset="downArrow", adj="adj1:val 48000,adj2:val 55000"))

    chip_box = (268, 297, 987, 991)
    commands.append(slide.picture("Monitor", "waveform-monitor.png", (154, 320, 1101, 1004),
                            1.90, 1.285, 1.84))
    commands.append(slide.picture("SingleFPGA", "fpga-chip.png", chip_box, 2.15, 3.51, 1.34))
    commands.append(slide.picture("MultiFPGA.Left", "fpga-chip.png", chip_box, 1.12, 5.82, 1.12))
    commands.append(slide.picture("MultiFPGA.Right", "fpga-chip.png", chip_box, 3.32, 5.82, 1.12))
    commands.append(slide.shape("MultiFPGA.Link", 2.29, 6.185, 0.98, 0.34, fill=AMBER,
                          preset="leftRightArrow", adj="adj1:val 44000,adj2:val 28000"))
    commands.append(slide.shape("PageNumber", 12.72, 7.25, 0.25, 0.20,
                          text="1", size=10, color="607184", align="right"))
    commands.append({
        "command": "add", "parent": "/slide[1]", "type": "notes",
        "props": {"text": (
            "Introduce the capacity-versus-observability motivation. RTL simulation provides "
            "visibility and flexible debugging, but long software workloads are slow. FPGA "
            "prototyping accelerates execution, while one FPGA limits design capacity. "
            "Partitioning across multiple FPGAs extends capacity. The next slide introduces "
            "the need for coordinated debugging. MHz-level execution is a general prototype "
            "characteristic here, not a measured REMUS performance result. Layout reference: "
            "figure/presentation-reference/midterm-background-01.png."
        )},
    })
    commands = apply_layout_edits(commands, LAYOUT_EDITS)
    # Explicit title spacing and page-specific finishing objects.
    commands.extend([{'command': 'set', 'path': '/slide[1]/shape[@name=S01.Title]', 'props': {'lineSpacing': '0.9x'}}])
    return commands
