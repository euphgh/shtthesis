#!/usr/bin/env python3
"""Build the complete Academic Red midterm deck, or debug one page with --slide.

Python standard library plus OfficeCLI. Run outside the agent sandbox.
"""

import argparse
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
from zipfile import ZIP_DEFLATED, ZipFile

from midterm_pptx import slide_01, slide_02, slide_03, slide_04, slide_05, slide_06
from midterm_pptx import slide_07, slide_08, slide_09, slide_10, slide_11, slide_contents
from midterm_pptx.common import BUILD, THESIS, THEMES, DEFAULT_THEME, recolor_commands

SLIDES = {0: slide_contents, 1: slide_01, 2: slide_02, 3: slide_03, 4: slide_04,
          5: slide_05, 6: slide_06, 7: slide_07, 8: slide_08, 9: slide_09,
          10: slide_10, 11: slide_11}
FINAL = THESIS / "pptx/midterm/REMUS_Midterm_Final.pptx"
FRONTMATTER = Path(__file__).resolve().parent / "midterm_pptx/frontmatter"


def pack_frontmatter(output):
    """Build two native template slides from tracked XML and logo assets.

    The template is source, not a previous build or the delivery PPTX. Keep
    package bytes unchanged so rich text, layouts and the institution logo survive.
    """
    files = sorted(p for p in FRONTMATTER.rglob('*')
                   if p.is_file() and p.name != 'README.md')
    if not (FRONTMATTER / '[Content_Types].xml').is_file():
        raise FileNotFoundError('Missing frontmatter source package')
    output.parent.mkdir(parents=True, exist_ok=True)
    with ZipFile(output, 'w', ZIP_DEFLATED) as archive:
        for source in files:
            archive.write(source, source.relative_to(FRONTMATTER).as_posix())


def build_slide(number, output, preview, reports, officecli):
    """Build and validate one page; keep all diagnostics in its build directory."""
    page = SLIDES[number]
    commands = recolor_commands(page.build_commands())
    for command in commands:
        source = command.get('props', {}).get('src')
        if source and not Path(source).is_file():
            raise FileNotFoundError(source)
    for directory in (output.parent, preview.parent, reports):
        directory.mkdir(parents=True, exist_ok=True)
    env = dict(os.environ, OFFICECLI_NO_AUTO_RESIDENT='1')

    def cli(*arguments):
        result = subprocess.run([officecli, *map(str, arguments)], env=env,
                                capture_output=True, text=True)
        if result.returncode or 'UNSUPPORTED' in result.stdout + result.stderr:
            raise RuntimeError(result.stdout + result.stderr)
        return result.stdout

    if output.exists():
        output.unlink()
    cli('create', output)
    try:
        cli('set', output, '/', '--prop', 'slideSize=widescreen')
        palette = THEMES[DEFAULT_THEME]
        cli('set', output, '/theme', '--prop', 'headingFont=Arial', '--prop', 'bodyFont=Arial',
            '--prop', f"accent1={palette['accent1']}", '--prop', f"accent2={palette['accent2']}",
            '--prop', f"accent3={palette['accent3']}")
        cli('add', output, '/', '--type', 'slide', '--prop', 'layout=blank',
            '--prop', 'background=FFFFFF', '--prop', f'title={page.TITLE}')
        batch = reports / 'commands.json'
        batch.write_text(json.dumps(commands, indent=2) + '\n')
        (reports / 'batch.json').write_text(cli('batch', output, '--input', batch, '--json'))
        cli('save', output)
        for mode in ('text', 'issues', 'outline'):
            (reports / f'{mode}.txt').write_text(cli('view', output, mode))
        validation = cli('validate', output)
        (reports / 'validate.txt').write_text(validation)
        if 'Validation passed' not in validation:
            raise RuntimeError(validation)
        if preview.exists():
            preview.unlink()
        cli('view', output, 'screenshot', '--page', '1', '-o', preview)
    finally:
        cli('close', output)
    print(f'Built slide {number}: {output}', flush=True)


def build_deck(output, officecli):
    """Build fresh sources, validate/render the merge, then publish atomically.

    Each run has an isolated directory, so no stale single-page files can enter
    the result. Failures retain that directory and leave the final deck untouched.
    """
    BUILD.mkdir(parents=True, exist_ok=True)
    work = Path(tempfile.mkdtemp(prefix='midterm-run-', dir=BUILD))
    singles, logs = work / 'single', work / 'logs'
    singles.mkdir()
    logs.mkdir()
    script = Path(__file__).resolve()

    def run(label, arguments):
        log = logs / f'{label}.log'
        print(label, flush=True)
        with log.open('w') as stream:
            result = subprocess.run(arguments, stdout=stream, stderr=subprocess.STDOUT,
                                    env=dict(os.environ, OFFICECLI_NO_AUTO_RESIDENT='1'))
        if result.returncode:
            raise RuntimeError(f'{label} failed; see {log}')

    try:
        pack_frontmatter(singles / 'REMUS-midterm.pptx')
        for number, page in SLIDES.items():
            stem = getattr(page, 'OUTPUT_STEM', f'REMUS_Background_Slide_{number}')
            run(f'slide-{number:02}', [sys.executable, str(script), '--slide', str(number),
                '--output', str(singles / f'{stem}.pptx'), '--preview',
                str(work / 'single-preview' / f'slide-{number:02}.png'), '--reports',
                str(logs / f'slide-{number:02}'), '--officecli', officecli])
        candidate = work / 'REMUS_Midterm_Final.pptx'
        run('merge', [sys.executable, str(script.with_name('merge_midterm_pptx.py')),
            '--input-dir', str(singles), '--output', str(candidate), '--preview-dir',
            str(work / 'preview'), '--officecli', officecli])
        # Rewrite temporary source paths before archiving the build diagnostics.
        archive = BUILD / 'midterm'
        manifest = candidate.with_suffix('.manifest.json')
        manifest.write_text(manifest.read_text().replace(str(work), str(archive)))
        output.parent.mkdir(parents=True, exist_ok=True)
        with tempfile.NamedTemporaryFile(dir=output.parent, suffix='.pptx', delete=False) as f:
            temporary = Path(f.name)
        try:
            shutil.copyfile(candidate, temporary)
            os.replace(temporary, output)
        finally:
            temporary.unlink(missing_ok=True)
        if archive.exists():
            shutil.rmtree(archive)
        work.rename(archive)
        print(f'Saved: {output}\nPreviews and reports: {archive}', flush=True)
    except Exception:
        print(f'Build diagnostics retained at: {work}', file=sys.stderr)
        raise


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--slide', type=int, choices=tuple(SLIDES),
                        help='Debug only Contents (0) or a body page (1–11)')
    parser.add_argument('--output', type=Path, help='Override final or single-page destination')
    parser.add_argument('--preview', type=Path, help='Single-page PNG destination')
    parser.add_argument('--reports', type=Path, help='Single-page diagnostic directory')
    parser.add_argument('--officecli', default=shutil.which('officecli') or
                        str(Path.home() / '.local/bin/officecli'))
    args = parser.parse_args()
    if not shutil.which(args.officecli):
        parser.error(f'OfficeCLI not found: {args.officecli}')
    if args.slide is None:
        if args.preview or args.reports:
            parser.error('--preview and --reports require --slide')
        build_deck((args.output or FINAL).resolve(), args.officecli)
    else:
        page = SLIDES[args.slide]
        stem = getattr(page, 'OUTPUT_STEM', f'REMUS_Background_Slide_{args.slide}')
        build_slide(args.slide, (args.output or BUILD / f'{stem}.pptx').resolve(),
                    (args.preview or BUILD / f'{stem}.png').resolve(),
                    (args.reports or BUILD / f'slide-{args.slide:02}').resolve(), args.officecli)


if __name__ == '__main__':
    main()
