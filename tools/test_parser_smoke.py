#!/usr/bin/env python3
from __future__ import annotations

import sys
import unittest
from pathlib import Path

TOOLS_DIR = Path(__file__).resolve().parent
if str(TOOLS_DIR) not in sys.path:
    sys.path.insert(0, str(TOOLS_DIR))

from validate_process_metadata import parse_frontmatter


class ParserSmokeTests(unittest.TestCase):
    def test_parse_frontmatter_scalar(self) -> None:
        text = "---\nname: demo\nowner: lyra\n---\nbody"
        m = parse_frontmatter(text)
        self.assertEqual(m.get("name"), "demo")
        self.assertEqual(m.get("owner"), "lyra")

    def test_parse_frontmatter_missing_block(self) -> None:
        text = "no frontmatter"
        m = parse_frontmatter(text)
        self.assertIsNone(m)


if __name__ == "__main__":
    unittest.main()
