"""Shared styles and pure OfficeCLI command builders.

SlideAPI names objects by presentation page while targeting slide[1] in each
standalone PPTX. These helpers do not run OfficeCLI or write presentation files.
"""

from copy import deepcopy
from .theme import DEFAULT_THEME, THEMES, recolor_commands
from pathlib import Path

THESIS = Path(__file__).resolve().parents[2]
BUILD = THESIS / "build" / "pptx"
NAVY = "183B56"
TEAL = "008C95"
AMBER = "DF973E"
INK = "20354A"


def inches(value):
    """Format explicit PowerPoint dimensions in inches."""
    return f"{value:.6f}in"


class SlideAPI:
    """Create native slide commands with a page-specific object namespace."""

    def __init__(self, page_number):
        self.prefix = f"S{page_number:02}"

    def title(self, size=32):
        """Format the title shape created by the command-line runner."""
        return {
            "command": "set",
            "path": "/slide[1]/shape[1]",
            "props": {
                "name": f"{self.prefix}.Title",
                "x": "0.35in",
                "y": "0.14in",
                "width": "12.64in",
                "height": "0.54in",
                "font": "Arial",
                "size": str(size),
                "bold": "true",
                "color": NAVY,
                "margin": "0pt",
                "autoFit": "none",
                "fill": "none",
                "line": "none",
                "shadow": "none",
            },
        }

    def shape(self, name, x, y, width, height, **props):
        """Describe one independently editable shape with explicit text defaults."""
        return {
            "command": "add",
            "parent": "/slide[1]",
            "type": "shape",
            "props": {
                "name": f"{self.prefix}.{name}",
                "x": inches(x),
                "y": inches(y),
                "width": inches(width),
                "height": inches(height),
                "fill": "none",
                "line": "none",
                "shadow": "none",
                "font": "Arial",
                "size": "18",
                "color": INK,
                "margin": "0pt",
                "autoFit": "none",
                **{key: str(value) for key, value in props.items()},
            },
        }

    def picture(self, name, asset, box, x, y, width):
        """Crop transparent margins in PPTX while preserving the artwork ratio.

        Bounds were measured from the visible artwork, with padding retained for
        anti-aliased edges. Source PNGs are embedded unchanged, never rewritten.
        """
        left, top, right, bottom = box
        height = width * (bottom - top) / (right - left)
        crop = [left, top, 1254 - right, 1254 - bottom]
        return {
            "command": "add",
            "parent": "/slide[1]",
            "type": "picture",
            "props": {
                "name": f"{self.prefix}.{name}",
                "src": str(THESIS / "figure" / "ppt-assets" / asset),
                "alt": {
                    "waveform-monitor.png": "Waveform monitor",
                    "global-snapshot.png": "Global snapshot",
                    "cycle-control.png": "Logical cycle progression",
                    "global-pause.png": "Coordinated pause",
                    "circuit-partitioning.png": "Circuit partitioning",
                    "restore-replay.png": "Restore and replay",
                    "rtl-design.png": "Hierarchical RTL design",
                }.get(asset, "FPGA chip"),
                "x": inches(x),
                "y": inches(y),
                "width": inches(width),
                "height": inches(height),
                "crop": ",".join(f"{100 * value / 1254:.6f}" for value in crop),
            },
        }

    def connector(self, name, **props):
        """Create an editable connector; callers supply color, width and endpoints."""
        return {
            "command": "add",
            "parent": "/slide[1]",
            "type": "connector",
            "props": {"name": f"{self.prefix}.{name}", "shape": "straight", **props},
        }


def apply_layout_edits(commands, edits):
    """Apply stable-name deltas after the original page has been constructed.

    Rich text is rebuilt through OfficeCLI paragraph/run commands. Only the
    paragraph container is reset with raw-set; this avoids inheriting obsolete
    bullets and preserves superscript citations, line breaks and mixed weights.
    """
    commands = deepcopy(commands)
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

    return commands
