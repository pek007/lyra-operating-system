#!/usr/bin/env python3
from __future__ import annotations

from tde_error_report_markdown import parse_error_report_markdown


SAMPLE = """# Error Report

## Header
- Error ID: ERR-2026-001
- Date: 2026-03-14
- Title: TDE corrective path missing
- Type: process_failure
- Scope: product_local
- Owning product or owner: A-007
- Affected products/contexts: Task Management, TDE runtime
- Status: open
- Review / closure date:

## Summary
- What happened? A meaningful issue was reported without canonical TDE corrective action.

## Impact
- Actual impact: Fix risked staying in prose.
- Potential impact: Follow-through could become untraceable.

## Detection
- How was it detected? Architecture review
- Detection gap, if any: None

## Root cause
- Primary root cause: Missing bridge from markdown error reports to TDE intake.
- Contributing factors: Process update outran tooling

## Immediate mitigation
- What was done immediately? Define bridge and parser.

## Corrective actions
- [ ] Add markdown-to-JSON parser
- [ ] Route parsed report through TDE pipeline

## Preventive changes
- What should change to reduce recurrence? Keep prose-first reports auto-convertible into canonical schema.

## Linked artifacts
- Related tasks: TDE-123
- Related decisions:
- Related evidence: ERROR_REPORTING_STANDARD_V1.md
- Related product/shared artifacts: AGENTS.md

## Closure criteria
- What must be true before this is considered closed? Corrective path exists in TDE.

## Closure note
- Final outcome / verification:
"""


def run_tests() -> None:
    report = parse_error_report_markdown(SAMPLE, source_reference="errors/ERR-2026-001.md", priority_hint="medium")
    assert report["artifactType"] == "tde_error_report"
    assert report["error_id"] == "ERR-2026-001"
    assert report["type"] == "process_failure"
    assert report["affected_products_contexts"] == ["Task Management", "TDE runtime"]
    assert len(report["corrective_actions"]) == 2
    assert report["linked_artifacts"]["related_tasks"] == ["TDE-123"]
    print("[PASS] TDE error report markdown tests passed")


if __name__ == "__main__":
    run_tests()
