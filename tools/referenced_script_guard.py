#!/usr/bin/env python3
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

# Match script paths in command-like text (e.g., `python3 tools/foo.py`, `bash tools/bar.sh`, `tools/baz.py`)
SCRIPT_REF_RE = re.compile(r"(?<![\w./-])(tools/[\w./-]+\.(?:py|sh))")

DEFAULT_SCAN_PATHS = [
    "CRON_SPEC_AUTONOMOUS_GOVERNANCE_SWEEPS.md",
    "OPENCLAW_RELEASE_DELTA_SOP.md",
    "governance",
]


def iter_markdown_files(paths: list[str]) -> list[Path]:
    files: list[Path] = []
    for rel in paths:
        p = ROOT / rel
        if p.is_file() and p.suffix.lower() == ".md":
            files.append(p)
            continue
        if p.is_dir():
            files.extend(sorted(x for x in p.rglob("*.md") if x.is_file()))
    return files


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Fail-fast guard: ensure referenced local scripts in runbook markdown exist."
    )
    parser.add_argument(
        "--paths",
        nargs="*",
        default=DEFAULT_SCAN_PATHS,
        help="Relative files/directories to scan for tools/*.py|*.sh references.",
    )
    args = parser.parse_args()

    md_files = iter_markdown_files(args.paths)
    if not md_files:
        print("WARN: no markdown files found for referenced-script guard")
        return 0

    missing: list[str] = []
    refs_found = 0

    for md in md_files:
        text = md.read_text(encoding="utf-8", errors="replace")
        for m in SCRIPT_REF_RE.finditer(text):
            refs_found += 1
            rel_script = m.group(1)
            target = ROOT / rel_script
            if not target.exists() or not target.is_file():
                missing.append(f"{md.relative_to(ROOT)} -> missing {rel_script}")

    if missing:
        print("Referenced script guard failed:\n")
        for item in sorted(set(missing)):
            print(f"- {item}")
        return 1

    print(f"Referenced script guard passed ({refs_found} references checked)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
