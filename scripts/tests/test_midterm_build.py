"""Source-package and failure-safety checks; OfficeCLI is not needed."""

from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import build_midterm_pptx as build
from merge_midterm_pptx import Source, resolve_target


class MidtermBuildTest(unittest.TestCase):
    def test_frontmatter_is_self_contained_and_editable(self):
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / 'frontmatter.pptx'
            build.pack_frontmatter(path)
            source = Source(path, 1)
            self.assertEqual(len(source.slides), 2)
            for part in source.parts:
                for relation in source.relationships(part):
                    if relation.get('TargetMode') != 'External':
                        self.assertIn(resolve_target(part, relation.get('Target')), source.parts)
            self.assertIn('硕士研究生中期答辩', source.parts[source.slides[0]].decode())
            self.assertIn(b'<p:sp>', source.parts[source.slides[0]])

    def test_failed_build_preserves_final_and_failure_log(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            output = root / 'final.pptx'
            output.write_bytes(b'previous reviewed final')
            with patch.object(build, 'BUILD', root / 'build'), patch.object(
                build.subprocess, 'run', return_value=subprocess.CompletedProcess([], 1)
            ):
                with self.assertRaisesRegex(RuntimeError, 'slide-00 failed'):
                    build.build_deck(output, 'officecli')
            self.assertEqual(output.read_bytes(), b'previous reviewed final')
            self.assertEqual(len(list((root / 'build').glob('midterm-run-*/logs/slide-00.log'))), 1)

    def test_page_assets_are_present_and_not_ignored(self):
        for page in build.SLIDES.values():
            for command in page.build_commands():
                source = command.get('props', {}).get('src')
                if not source:
                    continue
                path = Path(source)
                self.assertTrue(path.is_file(), source)
                result = subprocess.run(['git', '-C', str(build.THESIS), 'check-ignore',
                                         '--no-index', str(path)], capture_output=True)
                self.assertEqual(result.returncode, 1, result.stdout.decode())


if __name__ == '__main__':
    unittest.main()
