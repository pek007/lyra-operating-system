from __future__ import annotations

import unittest
import sys
import subprocess
from pathlib import Path
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parent))
import markdown_link_check as mlc
from markdown_link_check import extract_links


class MarkdownLinkCheckTests(unittest.TestCase):
    def test_ignores_links_in_code_fences(self) -> None:
        text = """
Normal [ok](./README.md)
```python
# [bad](./missing.md)
```
"""
        links = extract_links(text)
        self.assertEqual(links, ["./README.md"])

    def test_parses_optional_title(self) -> None:
        text = 'See [doc](./README.md "Read me")'
        links = extract_links(text)
        self.assertEqual(links, ["./README.md"])

    @patch("markdown_link_check.subprocess.check_output", side_effect=subprocess.CalledProcessError(1, ["git"]))
    @patch("markdown_link_check.all_markdown_paths", return_value=[Path("/tmp/fallback.md")])
    def test_changed_only_falls_back_to_full_scan_when_git_unavailable(self, all_paths_mock, _check_output_mock) -> None:
        paths = mlc.changed_markdown_paths()
        self.assertEqual(paths, [Path("/tmp/fallback.md")])
        all_paths_mock.assert_called_once()

    @patch("markdown_link_check.subprocess.check_output", side_effect=FileNotFoundError())
    @patch("markdown_link_check.all_markdown_paths", return_value=[Path("/tmp/fallback.md")])
    def test_changed_only_falls_back_when_git_binary_missing(self, all_paths_mock, _check_output_mock) -> None:
        paths = mlc.changed_markdown_paths()
        self.assertEqual(paths, [Path("/tmp/fallback.md")])
        all_paths_mock.assert_called_once()

    @patch("markdown_link_check.subprocess.check_output", side_effect=["repos/a.md\nTASKS.md\n", "TASKS.md\nrepos/b.md\n"])
    def test_changed_only_skips_repos_and_deduplicates_paths(self, _check_output_mock) -> None:
        expected = [mlc.ROOT / "TASKS.md"]
        paths = mlc.changed_markdown_paths()
        self.assertEqual(paths, expected)


if __name__ == "__main__":
    unittest.main()
