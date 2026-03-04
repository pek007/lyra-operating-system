#!/usr/bin/env python3
from __future__ import annotations

import argparse
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TARGET_GLOBS = ["WO-*.md", "CA-*.md", "knowledge/changes/**/*.md"]


def extract_field(text: str, key: str) -> str | None:
    m = re.search(rf"(?im)^\s*-\s*{re.escape(key)}\s*:\s*(.+?)\s*$", text)
    return m.group(1).strip() if m else None


def normalize_yes_no(value: str | None) -> str | None:
    if value is None:
        return None
    v = value.strip().lower()
    if v in {"yes", "y", "true", "1"}:
        return "yes"
    if v in {"no", "n", "false", "0"}:
        return "no"
    return None


def iter_targets() -> list[Path]:
    out: list[Path] = []
    for g in TARGET_GLOBS:
        out.extend(ROOT.glob(g))
    # de-duplicate and keep deterministic order
    return sorted({p.resolve() for p in out if p.is_file()})


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate standard-change auto-promotion policy fields")
    parser.add_argument("--strict", action="store_true", help="Fail when required policy fields are missing on new-format artifacts")
    args = parser.parse_args()

    errors: list[str] = []
    warnings: list[str] = []

    for p in iter_targets():
        rel = p.relative_to(ROOT).as_posix()
        text = p.read_text(encoding="utf-8", errors="replace")

        # only validate artifacts using new routing fields
        change_class = extract_field(text, "Change class")
        if not change_class:
            continue

        standard_class = extract_field(text, "Standard class (if Standard)")
        auto_req_raw = extract_field(text, "Auto-promotion requested")
        exclusion_raw = extract_field(text, "Exclusion trigger present")

        auto_req = normalize_yes_no(auto_req_raw)
        exclusion = normalize_yes_no(exclusion_raw)

        if args.strict:
            if auto_req is None:
                errors.append(f"{rel}: missing/invalid 'Auto-promotion requested' (Yes/No)")
            if exclusion is None:
                errors.append(f"{rel}: missing/invalid 'Exclusion trigger present' (Yes/No)")

        cls = change_class.lower()
        is_standard = cls.startswith("standard")

        # Guardrail: standard class must be present when standard is selected.
        if is_standard and (not standard_class or standard_class.lower() == "n/a"):
            errors.append(f"{rel}: Change class=Standard requires a concrete Standard class (SC-xx)")

        # Guardrail: auto-promotion can only be requested for Standard changes.
        if auto_req == "yes" and not is_standard:
            errors.append(f"{rel}: Auto-promotion requested=Yes allowed only when Change class=Standard")

        # Guardrail: exclusion trigger always blocks auto-promotion.
        if auto_req == "yes" and exclusion == "yes":
            errors.append(f"{rel}: exclusion trigger present => auto-promotion must be No")

        # Hygiene warning: standard change but exclusion unknown.
        if is_standard and exclusion is None:
            warnings.append(f"WARN: {rel}: add 'Exclusion trigger present: Yes/No' for deterministic routing")

    for w in warnings:
        print(w)

    if errors:
        print("\nStandard-change policy check failed:")
        for e in errors:
            print(f"- {e}")
        return 1

    print("Standard-change policy check passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
