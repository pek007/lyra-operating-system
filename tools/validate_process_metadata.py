#!/usr/bin/env python3
"""Minimal process metadata validator (v1).

Checks markdown files for YAML frontmatter and required fields.
Usage:
  python3 tools/validate_process_metadata.py
"""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = ["id", "type", "title", "status", "owner", "created", "nextReview"]
TARGET_DIRS = [ROOT / "processes", ROOT / "governance"]


def parse_frontmatter(text: str):
    if not text.startswith('---\n'):
        return None
    end = text.find('\n---\n', 4)
    if end == -1:
        return None
    block = text[4:end]
    data = {}
    for line in block.splitlines():
        if ':' in line:
            k, v = line.split(':', 1)
            data[k.strip()] = v.strip()
    return data


def iter_md_files():
    seen = set()
    for d in TARGET_DIRS:
        if not d.exists():
            continue
        for p in d.rglob('*.md'):
            if '.git/' in str(p):
                continue
            if p in seen:
                continue
            seen.add(p)
            yield p


def main():
    failures = []
    for p in iter_md_files():
        text = p.read_text(encoding='utf-8', errors='ignore')
        fm = parse_frontmatter(text)
        if not fm:
            continue
        missing = [k for k in REQUIRED if not fm.get(k)]
        if missing:
            failures.append((p, missing))
    if failures:
        print('Process metadata validation failures:')
        for p, missing in failures:
            print(f"- {p.relative_to(ROOT)}: missing {', '.join(missing)}")
        raise SystemExit(1)
    print('Process metadata validation passed.')


if __name__ == '__main__':
    main()
