from __future__ import annotations

import unittest
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
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


if __name__ == "__main__":
    unittest.main()
