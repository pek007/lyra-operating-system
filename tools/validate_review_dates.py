#!/usr/bin/env python3
"""Validate next review dates in PROCESS_REGISTRY.md.
Fails if any Active item has next review in the past (YYYY-MM-DD).
"""
from datetime import date
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
REG = ROOT / 'PROCESS_REGISTRY.md'


def main():
    if not REG.exists():
        print('PROCESS_REGISTRY.md not found; skipping')
        return
    today = date.today()
    failures = []
    for line in REG.read_text(encoding='utf-8', errors='ignore').splitlines():
        if not line.startswith('|') or '---' in line:
            continue
        cols = [c.strip() for c in line.strip('|').split('|')]
        if len(cols) < 6:
            continue
        doc, _type, _owner, status, _last, next_review = cols[:6]
        if status.lower() != 'active':
            continue
        if not re.match(r'^\d{4}-\d{2}-\d{2}$', next_review):
            continue
        y, m, d = map(int, next_review.split('-'))
        nr = date(y, m, d)
        if nr < today:
            failures.append((doc, next_review))
    if failures:
        print('Overdue process reviews detected:')
        for doc, nr in failures:
            print(f'- {doc}: next review {nr}')
        raise SystemExit(1)
    print('Review date validation passed.')


if __name__ == '__main__':
    main()
