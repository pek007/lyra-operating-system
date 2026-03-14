#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from typing import Any

SECTION_RE = re.compile(r"^##\s+(.*)\s*$")
BULLET_RE = re.compile(r"^-\s+([^:]+):\s*(.*)$")
QUESTION_BULLET_RE = re.compile(r"^-\s+([^?]+\?)\s*(.*)$")
CHECKBOX_RE = re.compile(r"^-\s+\[ \]\s+(.*)$")


def _clean(value: str) -> str:
    return value.strip()


def _split_list(value: str) -> list[str]:
    if not value:
        return []
    return [item.strip() for item in value.split(",") if item.strip()]


def _parse_bullets(lines: list[str]) -> dict[str, str]:
    parsed: dict[str, str] = {}
    for line in lines:
        stripped = line.strip()
        m = BULLET_RE.match(stripped)
        if m:
            parsed[m.group(1).strip().lower()] = _clean(m.group(2))
            continue
        q = QUESTION_BULLET_RE.match(stripped)
        if q:
            parsed[q.group(1).strip().lower()] = _clean(q.group(2))
    return parsed


def parse_error_report_markdown(text: str, *, source_reference: str, priority_hint: str | None = None) -> dict[str, Any]:
    sections: dict[str, list[str]] = {}
    current: str | None = None
    for raw in text.splitlines():
        m = SECTION_RE.match(raw)
        if m:
            current = m.group(1).strip().lower()
            sections[current] = []
            continue
        if current is not None:
            sections[current].append(raw)

    header_map = _parse_bullets(sections.get("header", []))
    impact_map = _parse_bullets(sections.get("impact", []))
    detection_map = _parse_bullets(sections.get("detection", []))
    root_cause_map = _parse_bullets(sections.get("root cause", []))
    linked_map = _parse_bullets(sections.get("linked artifacts", []))
    summary_map = _parse_bullets(sections.get("summary", []))
    mitigation_map = _parse_bullets(sections.get("immediate mitigation", []))
    preventive_map = _parse_bullets(sections.get("preventive changes", []))

    summary = summary_map.get("what happened?", "")
    immediate_mitigation = mitigation_map.get("what was done immediately?", "")
    preventive_changes = preventive_map.get("what should change to reduce recurrence?", "")

    corrective_actions: list[str] = []
    for line in sections.get("corrective actions", []):
        m = CHECKBOX_RE.match(line.strip())
        if m:
            action = _clean(m.group(1))
            if action:
                corrective_actions.append(action)

    contributing_factors: list[str] = []
    rc = root_cause_map.get("contributing factors")
    if rc and rc != "TBD":
        contributing_factors = _split_list(rc)

    return {
        "artifactType": "tde_error_report",
        "schemaVersion": "1.0.0",
        "error_id": header_map.get("error id", ""),
        "date": header_map.get("date", ""),
        "title": header_map.get("title", ""),
        "type": header_map.get("type", ""),
        "scope": header_map.get("scope", ""),
        "owning_product_or_owner": header_map.get("owning product or owner", ""),
        "affected_products_contexts": _split_list(header_map.get("affected products/contexts", "")),
        "summary": summary,
        "impact": {
            "actual_impact": impact_map.get("actual impact", ""),
            "potential_impact": impact_map.get("potential impact", ""),
        },
        "detection_method": detection_map.get("how was it detected?", ""),
        "root_cause": root_cause_map.get("primary root cause", ""),
        "contributing_factors": contributing_factors,
        "immediate_mitigation": immediate_mitigation or None,
        "corrective_actions": corrective_actions,
        "preventive_changes": preventive_changes,
        "linked_artifacts": {
            "related_tasks": _split_list(linked_map.get("related tasks", "")),
            "related_decisions": _split_list(linked_map.get("related decisions", "")),
            "related_evidence": _split_list(linked_map.get("related evidence", "")),
            "related_product_shared_artifacts": _split_list(linked_map.get("related product/shared artifacts", "")),
        },
        "status": header_map.get("status", ""),
        "review_closure_date": header_map.get("review / closure date", "") or None,
        "source_reference": source_reference,
        "priority_hint": priority_hint or "unspecified",
    }


def main() -> None:
    ap = argparse.ArgumentParser(description="Parse markdown error report into structured tde_error_report JSON")
    ap.add_argument("--md-path", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--source-reference", default=None)
    ap.add_argument("--priority-hint", default=None)
    args = ap.parse_args()

    md_path = Path(args.md_path)
    report = parse_error_report_markdown(
        md_path.read_text(encoding="utf-8"),
        source_reference=args.source_reference or str(md_path),
        priority_hint=args.priority_hint,
    )
    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"out": str(out), "error_id": report["error_id"]}, indent=2))


if __name__ == "__main__":
    main()
