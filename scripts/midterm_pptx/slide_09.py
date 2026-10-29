"""Page 9: direct PCIe versus Fabric access, using editable diagrams."""

from .common import apply_layout_edits, SlideAPI, NAVY, TEAL

TITLE = 'Progress4: Scalable Multi-FPGA Runtime'
OUTPUT_STEM = "REMUS_Progress_Slide_9"
PREVIEW_STEM = "midterm-progress-09"
slide = SlideAPI(9)


# Final reviewed layout for this page. These properties override the base
# component layout below; edit revised text, geometry and rich text here.
LAYOUT_EDITS = {'remove': ['S09.Direct.LinkCaption'],
 'objects': {'S09.Title': {'props': {'font': 'Arial',
                                     'size': '30pt',
                                     'color': '#183B56',
                                     'bold': 'true',
                                     'align': 'left',
                                     'name': 'S09.Title',
                                     'x': '25.2pt',
                                     'y': '10.08pt',
                                     'width': '910.08pt',
                                     'height': '38.88pt',
                                     'fill': 'none',
                                     'line': 'none',
                                     'margin': '0cm',
                                     'autoFit': 'none'},
                           'paragraphs': [{'command': 'add',
                                           'parent': '{object}/paragraph[1]',
                                           'type': 'run',
                                           'props': {'size': '30pt',
                                                     'bold': 'true',
                                                     'color': '#183B56',
                                                     'text': 'Progress4: Scalable '}},
                                          {'command': 'add',
                                           'parent': '{object}/paragraph[1]',
                                           'type': 'run',
                                           'props': {'font.latin': 'Arial',
                                                     'size': '30pt',
                                                     'bold': 'true',
                                                     'color': '#183B56',
                                                     'text': 'Multi-FPGA Runtime'}}]},
             'S09.Direct.Text1': {'props': {'y': '5456237emu'}}}}


def build_commands():
    """Rebuild the approved comparison with native shapes and enlarged bullets.

    Both panels share geometry so that the number of Host connections is the
    primary visible difference. Implementation status and topology caveats stay
    in speaker notes, as requested; the drawing describes architecture only.
    """
    commands = [slide.title(size=30)]
    commands.append(slide.shape("TitleRule", 0.35, 0.78, 12.64, 2 / 72, fill=TEAL))
    for prefix, x, fabric in (("Direct", 0.35, False), ("Fabric", 6.87, True)):
        commands.append(slide.shape(f"{prefix}.Panel", x, 1.08, 6.12, 3.95,
                                    fill="EAF4F3" if fabric else "F1F5F8",
                                    preset="roundRect", adj="adj:val 4000"))
        commands.append(slide.shape(f"{prefix}.Heading", x + 0.18, 1.23, 5.76, 0.45,
                                    text="Fabric-Based Access" if fabric else "Direct PCIe Access",
                                    size=24, bold="true", color=NAVY))
        commands.append(slide.shape(f"{prefix}.Host", x + 0.20, 1.88, 5.72, 0.65,
                                    text="Host", size=24, bold="true", color=NAVY,
                                    fill="FFFFFF", line=f"{NAVY}:2", align="center", valign="middle"))
        for index, label in enumerate(("Ref FPGA" if fabric else "FPGA A", "FPGA B", "FPGA C")):
            node_x = x + 0.18 + index * 2.11
            color = TEAL if fabric and index == 0 else NAVY
            commands.append(slide.shape(f"{prefix}.Node{index}", node_x, 3.42, 1.54, 1.18,
                                        fill="FFFFFF", line=f"{color}:2"))
            commands.append(slide.shape(f"{prefix}.Node{index}.Label", node_x + 0.04, 3.56,
                                        1.46, 0.30, text=label, size=17, bold="true",
                                        color=color, align="center"))
            commands.append(slide.shape(f"{prefix}.Node{index}.Resources", node_x + 0.10, 3.96,
                                        1.34, 0.52, text="Registers\nMemory", size=14,
                                        fill="F1F5F8", line="BDCBD4:0.7", align="center", valign="middle"))
            if not fabric or index == 0:
                center = node_x + 0.77
                commands.append(slide.shape(f"{prefix}.PCIe{index}", center - 0.075, 2.55,
                                            0.15, 0.85, fill=NAVY, preset="upDownArrow"))
                commands.append(slide.shape(f"{prefix}.PCIe{index}.Label", center + 0.12, 2.82,
                                            0.72, 0.30, text="PCIe", size=16, bold="true", color=NAVY))
            if index < 2:
                link_x = node_x + 1.56
                commands.append(slide.shape(f"{prefix}.Link{index}", link_x, 4.05, 0.53, 0.15,
                                            preset="leftRightArrow", fill=TEAL if fabric else "91A5B5"))
                if fabric:
                    commands.append(slide.shape(f"{prefix}.Link{index}.Label", link_x - 0.04,
                                                3.77, 0.61, 0.24, text="Fabric", size=12,
                                                bold="true", color=TEAL, align="center"))
        if not fabric:
            commands.append(slide.shape("Direct.LinkCaption", x + 1.40, 4.73, 3.32, 0.25,
                                        text="DUT communication", size=14,
                                        color="607184", align="center"))
        bullets = (["One Host entry via Ref",
                    "Unified register and memory access",
                    "Extend through inter-FPGA links"] if fabric else
                   ["Separate Host connection per FPGA",
                    "Limited by Host PCIe connectivity"])
        for index, text in enumerate(bullets):
            y = 5.43 + index * 0.55
            commands.append(slide.shape(f"{prefix}.Bullet{index}", x + 0.06, y + 0.13,
                                        0.10, 0.10, fill=TEAL, preset="ellipse"))
            commands.append(slide.shape(f"{prefix}.Text{index}", x + 0.36, y, 5.76, 0.52,
                                        text=text, size=22))
    commands.append(slide.shape("PageNumber", 12.72, 7.25, 0.25, 0.20,
                                text="9", size=10, color="607184", align="right"))
    commands.append({
        "command": "add", "parent": "/slide[1]", "type": "notes",
        "props": {"text": (
            "Runtime operations such as global pause and state management require Host "
            "access to each FPGA's registers and memory. The baseline dual-board "
            "prototype uses a separate PCIe connection to each FPGA. Fabric provides "
            "a shared Host entry through the Ref node and carries resource requests "
            "over inter-FPGA links. Ref also retains its local DUT and resources. "
            "The diagrams illustrate architecture; three nodes and chain links do not "
            "claim a validated three-FPGA deployment. Access bandwidth is shared at Ref, "
            "and supported scale still depends on links and implementation constraints. "
            "Fabric components and the Driver backend are implemented; the dual-node "
            "Cosim environment is established. Current documented evidence does not "
            "establish complete end-to-end or Fabric board-level validation. "
            "At the user's request, these status lines and the illustrative-topology "
            "caption are omitted from the visible slide, not converted into success claims. "
            "Sources: src/midterm/progress/runtime.tex; "
            "../docs/source/project-notes/fabric/status.md. "
            "Design reference: figure/presentation-reference/midterm-runtime-09-v1.png. "
            "All visible text, diagrams, and arrows are native editable PowerPoint elements."
        )},
    })
    commands = apply_layout_edits(commands, LAYOUT_EDITS)
    # Explicit title spacing and page-specific finishing objects.
    commands.extend([{'command': 'set', 'path': '/slide[1]/shape[@name=S09.Title]', 'props': {'lineSpacing': '0.9x'}}])
    return commands
