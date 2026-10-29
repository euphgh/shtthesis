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

from midterm_pptx import slide_01, slide_02, slide_03, slide_04, slide_05, slide_06, slide_07, slide_08, slide_09, slide_10, slide_11
from midterm_pptx.common import BUILD, NAVY, TEAL, AMBER
from midterm_pptx.manual_revision import apply_manual_adjustments
from midterm_pptx import slide_contents

# Register new page modules here; each exposes TITLE and build_commands().
SLIDES = {0: slide_contents, 1: slide_01, 2: slide_02, 3: slide_03, 4: slide_04, 5: slide_05, 6: slide_06,
          7: slide_07, 8: slide_08, 9: slide_09, 10: slide_10, 11: slide_11}


def main():
    """Build, inspect, and render one slide through OfficeCLI outside the sandbox."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--slide", type=int, choices=tuple(SLIDES), default=1)
    parser.add_argument("--output", type=Path)
    parser.add_argument("--preview", type=Path)
    parser.add_argument("--officecli", default=shutil.which("officecli") or "/home/hgh/.local/bin/officecli")
    args = parser.parse_args()
    page = SLIDES[args.slide]
    output_stem = getattr(page, "OUTPUT_STEM", f"REMUS_Background_Slide_{args.slide}")
    preview_stem = getattr(page, "PREVIEW_STEM", f"midterm-background-{args.slide:02}")
    args.output = (args.output or BUILD / f"{output_stem}.pptx").resolve()
    args.preview = (args.preview or BUILD / f"{preview_stem}.png").resolve()
    commands = apply_manual_adjustments(args.slide, page.build_commands())
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
    cli("set", args.output, "/theme", "--prop", "headingFont=Arial", "--prop", "bodyFont=Arial",
        "--prop", f"accent1={NAVY}", "--prop", f"accent2={TEAL}", "--prop", f"accent3={AMBER}")
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
