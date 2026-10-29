"""Fast regression tests for the REMUS palette switch (no OfficeCLI needed)."""

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from midterm_pptx.theme import DEFAULT_THEME, THEMES, recolor_commands


class ThemeMappingTest(unittest.TestCase):
    def setUp(self):
        self.original = [
            {"command": "add", "props": {"name": "S01.Title", "color": "#183B56"}},
            {"command": "set",
             "path": "/slide[1]/shape[@name=S01.Title]/paragraph[1]",
             "props": {"color": "#183B56"}},
            {"command": "add",
             "props": {"name": "S01.TitleRule", "fill": "008C95"}},
            {"command": "add",
             "props": {"name": "S08.Resources.Chart", "series": [
                 {"fill": "183B56"}, {"fill": "008C95"}]}},
            {"command": "add", "type": "picture",
             "props": {"name": "S06.Pause.Illustration",
                       "src": "figure/presentation-reference/midterm-progress-06-v1.png"}},
        ]

    def test_default_and_both_palettes(self):
        self.assertEqual(DEFAULT_THEME, "academic-red")
        self.assertIn("navy-teal", THEMES)

    def test_red_theme_main_title_and_rule(self):
        result = recolor_commands(self.original, "academic-red")
        self.assertEqual(result[0]["props"]["color"], "#C00000")
        self.assertEqual(result[1]["props"]["color"], "#C00000")
        self.assertEqual(result[2]["props"]["fill"], "C55A11")

    def test_chart_and_raster_preservation(self):
        result = recolor_commands(self.original)
        self.assertEqual(result[3]["props"]["series"][0]["fill"], "333333")
        self.assertEqual(result[3]["props"]["series"][1]["fill"], "70AD47")
        self.assertEqual(result[4]["props"]["src"],
                         self.original[4]["props"]["src"])

    def test_title_rich_runs_inherit_owner_from_parent(self):
        commands = [{"command": "add", "type": "run",
                     "parent": "/slide[1]/shape[@name=S08.Title]/paragraph[1]",
                     "props": {"color": "#183B56", "text": "Progress3"}}]
        self.assertEqual(recolor_commands(commands)[0]["props"]["color"],
                         "#C00000")

    def test_legacy_and_source_not_mutated(self):
        result = recolor_commands(self.original, "navy-teal")
        self.assertEqual(result, self.original)
        self.assertIsNot(result, self.original)
        recolor_commands(self.original, "academic-red")
        self.assertEqual(self.original[0]["props"]["color"], "#183B56")


if __name__ == "__main__":
    unittest.main()
