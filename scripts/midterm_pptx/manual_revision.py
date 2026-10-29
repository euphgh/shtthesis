"""Replay the author's editable, object-level revisions and add references."""

from copy import deepcopy

from .common import SlideAPI
from .manual_adjustments import ADJUSTMENTS


def apply_manual_adjustments(page, commands):
    """Apply stable-name deltas after the original page has been constructed.

    Rich text is rebuilt through OfficeCLI paragraph/run commands. Only the
    paragraph container is reset with raw-set; this avoids inheriting obsolete
    bullets and preserves superscript citations, line breaks and mixed weights.
    """
    commands = deepcopy(commands)
    edits = ADJUSTMENTS.get(page, {})
    kinds = {
        c.get("props", {}).get("name"): c.get("type", "shape")
        for c in commands if c.get("props", {}).get("name")
    }

    def path_for(name, kind=None):
        kind = kind or kinds.get(name, "shape")
        kind = kind if kind in ("picture", "chart", "table", "connector") else "shape"
        return f"/slide[1]/{kind}[@name={name}]"

    for name in edits.get("remove", []):
        commands.append({"command": "remove", "path": path_for(name)})
    for name, edit in edits.get("objects", {}).items():
        path = path_for(name, edit.get("add"))
        props = deepcopy(edit["props"])
        if "add" in edit:
            commands.append({"command": "add", "parent": "/slide[1]",
                             "type": edit["add"], "props": props})
        if "paragraphs" in edit:
            body = f"//p:sp[p:nvSpPr/p:cNvPr[@name='{name}']]/p:txBody"
            commands.extend([
                {"command": "raw-set", "part": "/slide[1]", "xpath": body + "/a:p",
                 "action": "remove"},
                {"command": "raw-set", "part": "/slide[1]", "xpath": body,
                 "action": "append", "xml": "<a:p/>"},
            ])
        commands.append({"command": "set", "path": path, "props": props})
        for child in edit.get("paragraphs", []):
            cmd = deepcopy(child)
            for key in ("path", "parent"):
                if key in cmd:
                    cmd[key] = cmd[key].replace("{object}", path)
            commands.append(cmd)

    # PowerPoint's imported title masters use 90% line spacing. Make that
    # inherited style explicit so standalone regeneration has the same baseline.
    commands.append({"command": "set", "path": f"/slide[1]/shape[@name=S{page:02}.Title]",
                     "props": {"lineSpacing": "0.9x"}})
    if page == 8:
        # Preserve the author's chart-level label settings in addition to the
        # series-level label formats; OfficeCLI's default would enlarge them.
        commands.append({
            "command": "raw-set", "part": "/ppt/slides/charts/chart1.xml",
            "xpath": "//c:barChart/c:gapWidth", "action": "insertbefore",
            "xml": '<c:dLbls><c:dLblPos val="outEnd"/><c:showLegendKey val="0"/>'
                   '<c:showVal val="1"/><c:showCatName val="0"/><c:showSerName val="0"/>'
                   '<c:showPercent val="0"/><c:showBubbleSize val="1"/></c:dLbls>',
        })

    # References correspond to [1] on final pages 8 and 9 (body pages 6 and 7).
    # Metadata: reference.bib, zhu_duohuafen_2024 and chen_remu_2023.
    references = {
        6: ("[1] G. Zhu. Cross-Node Deployment of Digital Logic Design for FPGA Cloud. "
            "Master's thesis, ShanghaiTech University, 2024."),
        7: ("[1] Y. Chen et al. REMU: Enabling Cost-Effective Checkpointing and Deterministic "
            "Replay in FPGA-based Emulation. ICCD, 2023, pp. 21–29."),
    }
    if page in references:
        commands.append(SlideAPI(page).shape(
            "Reference1", 0.40, 7.06, 12.15, 0.28, text=references[page],
            size=10, color="607184"))
        for command in commands:
            if command.get("type") == "notes":
                command["props"]["text"] += " Reference [1]: " + references[page][4:]
                if page == 7:
                    command["props"]["text"] += " DOI: 10.1109/ICCD58817.2023.00014."
    if page == 11:
        for command in commands:
            if command.get("type") == "notes":
                command["props"]["text"] = (
                    "The author's revised plan contains three items: Fabric board-level "
                    "integration and validation followed by a four-FPGA system; execution "
                    "and communication overhead analysis on that system; consolidation "
                    "of results and thesis writing. These are future work. The separate "
                    "partitioning-optimization item and interrupt-driven-control sentence "
                    "were removed in the author's 2026-10-29 revision."
                )
    return commands
