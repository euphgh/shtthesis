"""Apply REMUS colors to the existing cover, contents and thanks slides.

Run outside the sandbox, as required for all OfficeCLI invocations. The source
is copied into build/pptx before editing; text, logos and geometry are retained.
"""

import argparse
import json
from midterm_pptx.theme import DEFAULT_THEME, THEMES, RED_MAP
from pathlib import Path
import shutil
import subprocess
from zipfile import ZipFile
import xml.etree.ElementTree as ET


ROOT = Path(__file__).resolve().parents[1]
WORK = ROOT / "build/pptx/restyle-midterm"
SOURCE = ROOT / "pptx/midterm/REMUS-midterm.pptx"
BACKUP = WORK / "REMUS-midterm-original.pptx"
OUTPUT = WORK / "REMUS-midterm.pptx"
CLI = shutil.which("officecli") or "/home/hgh/.local/bin/officecli"
NS = {"a": "http://schemas.openxmlformats.org/drawingml/2006/main"}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--theme", choices=tuple(THEMES), default=DEFAULT_THEME)
    parser.add_argument("--officecli", default=CLI)
    args = parser.parse_args()
    palette = THEMES[args.theme]
    WORK.mkdir(parents=True, exist_ok=True)
    if not BACKUP.exists():
        shutil.copy2(SOURCE, BACKUP)
    shutil.copy2(BACKUP, OUTPUT)
    colors = dict(dk1=palette["body"], dk2=palette["outline"],
                  lt1="FFFFFF", lt2=palette["neutral"],
                  accent1=palette["accent1"], accent2=palette["accent2"],
                  accent3=palette["accent3"], accent4=palette["surface"],
                  accent5=palette["muted"], accent6=palette["neutral"],
                  hlink=palette["accent2"], folHlink=palette["title"])
    props = {f"theme.color.{key}": val for key, val in colors.items()}
    props.update({"theme.font.major.latin": "Arial", "theme.font.minor.latin": "Arial"})
    commands = [{"command": "set", "path": "/", "props": props}]
    # Explicit fonts and red title defaults live in the template layouts.
    # Raw-set changes only those attributes, preserving rich runs and fields.
    with ZipFile(BACKUP) as archive:
        for part in archive.namelist():
            if not part.endswith(".xml") or not part.startswith(
                    ("ppt/slides/", "ppt/slideLayouts/", "ppt/slideMasters/", "ppt/theme/")):
                continue
            tree = ET.fromstring(archive.read(part))
            if tree.findall(".//a:latin", NS):
                commands.append({"command": "raw-set", "part": "/" + part,
                                 "xpath": "//a:latin", "action": "setattr",
                                 "xml": "typeface=Arial"})
            # The proposal/legacy template contains explicit RGB runs, not just
            # theme slots. Convert the known originals while keeping logos intact.
            original_colors = {
                "C00000": palette["title"],
                "183B56": palette["title"],
                "008C95": palette["rule"],
                "DF973E": palette["accent3"],
                "20354A": palette["body"],
                "607184": palette["muted"],
            }
            original_colors.update({
                old: target for old, target in RED_MAP.items()
                if old not in original_colors and args.theme == "academic-red"
            })
            # The first command already replaces the theme's color slots.
            # Do not search those parts for old RGB values later in this batch.
            present = (set() if part.startswith("ppt/theme/") else
                       {e.get("val") for e in tree.findall(".//a:srgbClr", NS)})
            for old_color, new_color in original_colors.items():
                if old_color in present and old_color != new_color:
                    commands.append({
                        "command": "raw-set", "part": "/" + part,
                        "xpath": f"//a:srgbClr[@val='{old_color}']",
                        "action": "setattr", "xml": f"val={new_color}"})
    # The old connectors contain inherited color transforms; explicit teal
    # ensures identical rendering on the cover and contents layouts.
    for layout in (1, 2):
        commands.append({"command": "raw-set",
                         "part": f"/ppt/slideLayouts/slideLayout{layout}.xml",
                         "xpath": "//p:cxnSp/p:spPr/a:ln", "action": "replace",
                         "xml": '<a:ln w="19050"><a:solidFill><a:srgbClr val="' + palette["rule"] + '"/></a:solidFill></a:ln>'})
    commands.append({"command": "set", "path": "/slide[1]/shape[@id=10]",
                     "props": {"color": palette["title"], "text": "硕士研究生中期答辩"}})
    for page, ident in ((1, 5), (3, 4)):
        commands.append({"command": "set", "path": f"/slide[{page}]/shape[@id={ident}]",
                         "props": {"color": palette["muted"]}})
    # Raw XML loading drops standalone whitespace runs unless xml:space is
    # explicit. Restore their original values after the color/font edits.
    with ZipFile(BACKUP) as archive:
        for page in (1, 2, 3):
            part = f"ppt/slides/slide{page}.xml"
            tree = ET.fromstring(archive.read(part))
            for index, node in enumerate(tree.findall(".//a:t", NS), 1):
                if node.text and not node.text.strip():
                    commands.append({"command": "raw-set", "part": "/" + part,
                                     "xpath": f"(//a:t)[{index}]", "action": "replace",
                                     "xml": '<a:t xml:space="preserve">' + node.text + '</a:t>'})
    batch = WORK / "recolor-commands.json"
    batch.write_text(json.dumps(commands, ensure_ascii=False, indent=2) + "\n")
    result = subprocess.run([args.officecli, "batch", str(OUTPUT), "--input", str(batch), "--json"],
                            capture_output=True, text=True, check=True)
    (WORK / "recolor-results.json").write_text(result.stdout)
    print(result.stdout)
    subprocess.run([args.officecli, "close", str(OUTPUT)], check=True)
    subprocess.run([args.officecli, "validate", str(OUTPUT)], check=True)
    subprocess.run([args.officecli, "view", str(OUTPUT), "issues"], check=True)
    for page in (1, 2, 3):
        subprocess.run([args.officecli, "view", str(OUTPUT), "screenshot", "--page", str(page),
                        "-o", str(WORK / f"after-{page}.png")], check=True)


if __name__ == "__main__":
    main()
