"""Switch REMUS slide colors without modifying photographs or raster diagrams.

Recolor commands AFTER layout edits, so even hard-coded rich text and charts
obey the chosen palette. Keep the original blue theme for comparison.
"""
from copy import deepcopy
import re

DEFAULT_THEME = "academic-red"
THEMES = {
    "academic-red": dict(title="C00000", rule="C55A11", body="1F1F1F",
                         outline="333333", accent1="C00000", accent2="70AD47",
                         accent3="ED7D31", surface="F1F7EC", neutral="F5F5F5",
                         muted="898989", background="FFFFFF"),
    "navy-teal": dict(title="183B56", rule="008C95", body="20354A",
                      outline="183B56", accent1="183B56", accent2="008C95",
                      accent3="DF973E", surface="EAF4F3", neutral="F1F5F8",
                      muted="607184", background="FFFFFF"),
}

# Legacy-to-academic-red mapping. Structural navy becomes dark gray; only
# the main slide title becomes red, and the title rule becomes rust orange.
RED_MAP = {
    "183B56": "333333", "008C95": "70AD47", "DF973E": "ED7D31",
    "20354A": "1F1F1F", "607184": "898989",
    "EAF4F3": "F1F7EC", "F1F5F8": "F5F5F5", "FCF4E8": "FFF3EF",
    "FFF0D8": "FFF3EF", "FFF0D9": "FFF3EF", "FFF6E5": "FFF3EF",
    "FFFAF0": "FFF8F3", "F1F8FB": "F5F5F5", "EEF6FB": "F5F5F5",
    "E3F0F6": "F1F7EC", "E7EEF3": "F5F5F5", "EDF0F3": "F5F5F5",
    "DCE8EF": "E8E8E8", "DCEEF9": "F1F7EC", "C5D7E5": "E5E5E5",
    "D8E3E9": "DEDEDE", "BDCBD4": "D1D1D1", "DDE5EA": "DEDEDE",
    "E0E7EC": "E5E5E5", "91A5B5": "A0A0A0", "8EB5CB": "B4B4B4",
    "8BA7BC": "B4B4B4", "8CA4B5": "B4B4B4", "7D9DB2": "A0A0A0",
    "6B9DBB": "93AD8A", "6B8AA0": "9E9E9E", "2584B8": "70AD47",
    "A9D3EC": "FFE4CD", "ACE0D4": "E1EED8", "DCEEEA": "F1F7EC",
    "BCDCD5": "E1EED8",
}
_COLOR = re.compile(r"(?<![a-zA-Z0-9])(#?)([a-fA-F0-9]{6})(?![a-zA-Z0-9])")
SKIP_KEYS = {"text", "alt", "src", "path", "part", "parent", "name",
             "title", "command", "type", "notes"}


def recolor_commands(commands, theme=DEFAULT_THEME):
    """Transform editable OfficeCLI commands, preserving raster picture bytes."""
    if theme not in THEMES:
        raise ValueError(f"Unknown theme: {theme}")
    if theme == "navy-teal":
        return deepcopy(commands)

    def walk(obj, owner="", key=""):
        if isinstance(obj, list):
            return [walk(v, owner, key) for v in obj]
        if isinstance(obj, dict):
            name = obj.get("name", owner)
            # Layout edits can issue standalone paragraph/run commands. They
            # have no props.name; recover ownership from their OfficeCLI path.
            selector = obj.get("path") or obj.get("parent")
            if not name and isinstance(selector, str):
                found = re.search(r"\[@name=['\"]?(S\d{2}\.[^\]'\"]+)['\"]?\]", selector)
                if found:
                    name = found.group(1)
            return {k: walk(v, name, k) for k, v in obj.items()}
        if not isinstance(obj, str) or key in SKIP_KEYS:
            return obj
        val = _COLOR.sub(
            lambda m: m.group(1) + RED_MAP.get(m.group(2).upper(), m.group(2)),
            obj)
        if key == "color" and re.fullmatch(r"S\d{2}\.Title", owner):
            return ("#" if obj.startswith("#") else "") + THEMES[theme]["title"]
        if key in ("fill", "line", "color") and owner.endswith(".TitleRule"):
            return ("#" if obj.startswith("#") else "") + THEMES[theme]["rule"]
        return val

    return walk(commands)
