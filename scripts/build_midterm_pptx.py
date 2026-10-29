#!/usr/bin/env python3
"""Build REMUS midterm slides using OfficeCLI, outside the agent sandbox.

Run with the system Python; no third-party Python packages are required.
The default output stays in thesis/build/pptx until it has been reviewed.
"""

import argparse
import json
import os
from pathlib import Path
import shutil
import subprocess
import struct
import sys

from midterm_pptx import slide_01, slide_02, slide_03, slide_04, slide_05, slide_06, slide_07, slide_08, slide_09, slide_10, slide_11
from midterm_pptx.common import BUILD, THESIS, inches, THEMES, DEFAULT_THEME, recolor_commands
from midterm_pptx import slide_contents

# Register new page modules here; each exposes TITLE and build_commands().
SLIDES = {0: slide_contents, 1: slide_01, 2: slide_02, 3: slide_03, 4: slide_04, 5: slide_05, 6: slide_06,
          7: slide_07, 8: slide_08, 9: slide_09, 10: slide_10, 11: slide_11}


def main():
    """Build, inspect, and render one slide through OfficeCLI outside the sandbox."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--slide", type=int, choices=tuple(SLIDES), default=1)
    parser.add_argument("--all", action="store_true",
                        help="Build the contents and all 11 numbered slides into build/pptx/")
    parser.add_argument("--theme", choices=tuple(THEMES), default=DEFAULT_THEME,
                        help="Palette (default: academic-red; alternative: navy-teal)")
    parser.add_argument("--output", type=Path)
    parser.add_argument("--preview", type=Path)
    parser.add_argument("--officecli", default=shutil.which("officecli") or "/home/hgh/.local/bin/officecli")
    args = parser.parse_args()
    if args.all:
        if args.output is not None or args.preview is not None:
            parser.error("--all cannot be used with --output or --preview")
        script = Path(__file__).resolve()
        for number in sorted(SLIDES):
            subprocess.run([sys.executable, str(script), "--slide", str(number),
                            "--theme", args.theme, "--officecli", args.officecli],
                           check=True)
        return
    page = SLIDES[args.slide]
    output_stem = getattr(page, "OUTPUT_STEM", f"REMUS_Background_Slide_{args.slide}")
    preview_stem = getattr(page, "PREVIEW_STEM", f"midterm-background-{args.slide:02}")
    args.output = (args.output or BUILD / f"{output_stem}.pptx").resolve()
    args.preview = (args.preview or BUILD / f"{preview_stem}.png").resolve()
    commands = page.build_commands()
    # A new full-size red pause diagram can be placed here without overwriting
    # the legacy blue reference. Fit without changing the new PNG's aspect ratio.
    if args.slide == 6 and args.theme == "academic-red":
        red_png = THESIS / "figure/presentation-reference/midterm-progress-06-academic-red.png"
        if red_png.is_file():
            with red_png.open('rb') as image_file:
                header = image_file.read(24)
            if header[:8] != bytes.fromhex("89504e470d0a1a0a"):
                raise ValueError(f"Invalid PNG: {red_png}")
            sw, sh = struct.unpack(">II", header[16:24])
            if not sw or not sh:
                raise ValueError("Invalid PNG dimensions")
            bw, bh = 8.48, 5.84
            w = min(bw, bh * sw / sh)
            h = w * sh / sw
            picture = next(cmd for cmd in commands
                           if cmd.get("props", {}).get("name") == "S06.Pause.Illustration")
            picture["props"].update(
                src=str(red_png), crop="0,0,0,0",
                x=inches(4.50 + (bw - w) / 2),
                y=inches(1.12 + (bh - h) / 2),
                width=inches(w), height=inches(h))
        else:
            print("NOTICE: Slide 6 still uses the blue raster illustration; "
                  "copy the new diagram to figure/presentation-reference/"
                  "midterm-progress-06-academic-red.png")
    commands = recolor_commands(commands, args.theme)
    log_prefix = f"slide-{args.slide:02}"
    BUILD.mkdir(parents=True, exist_ok=True)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.preview.parent.mkdir(parents=True, exist_ok=True)
    env = dict(os.environ, OFFICECLI_NO_AUTO_RESIDENT="1")

    def cli(*arguments):
        result = subprocess.run([args.officecli, *map(str, arguments)], env=env,
                                capture_output=True, text=True)
        if result.returncode:
            raise RuntimeError(result.stdout + result.stderr)
        if "UNSUPPORTED" in result.stdout + result.stderr:
            raise RuntimeError(result.stdout + result.stderr)
        return result.stdout

    # Only the chosen build output is replaced; source assets and old decks stay intact.
    if args.output.exists():
        args.output.unlink()
    cli("create", args.output)
    cli("set", args.output, "/", "--prop", "slideSize=widescreen")
    palette = THEMES[args.theme]
    cli("set", args.output, "/theme", "--prop", "headingFont=Arial", "--prop", "bodyFont=Arial",
        "--prop", f"accent1={palette['accent1']}", "--prop", f"accent2={palette['accent2']}",
        "--prop", f"accent3={palette['accent3']}")
    cli("add", args.output, "/", "--type", "slide", "--prop", "layout=blank",
        "--prop", "background=FFFFFF", "--prop", f"title={page.TITLE}")
    (BUILD / f"{log_prefix}-initial.txt").write_text(cli("get", args.output, "/slide[1]", "--depth", "1"))
    commands_path = BUILD / f"{log_prefix}.json"
    commands_path.write_text(json.dumps(commands, indent=2) + "\n")
    (BUILD / f"{log_prefix}-batch.json").write_text(cli("batch", args.output, "--input", commands_path, "--json"))
    cli("save", args.output)
    for mode in ("text", "issues", "outline"):
        report = cli("view", args.output, mode)
        (BUILD / f"{log_prefix}-{mode}.txt").write_text(report)
        print(report.strip())
    print(cli("validate", args.output).strip())
    if args.preview.exists():
        args.preview.unlink()
    print(cli("view", args.output, "screenshot", "--page", "1", "-o", args.preview).strip())
    cli("close", args.output)
    print(args.output)


if __name__ == "__main__":
    main()
