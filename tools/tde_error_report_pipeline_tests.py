#!/usr/bin/env python3
from __future__ import annotations

import tempfile
from pathlib import Path

from tde_error_report_adapter_tests import _sample_report
from tde_error_report_pipeline import run_markdown_pipeline, run_pipeline

SAMPLE_MD = """# Error Report

## Header
- Error ID: ERR-PIPE-001
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
    with tempfile.TemporaryDirectory() as td:
        root = Path(td)
        report_path = root / "ERR-TEST.json"
        packet_path = root / "INTAKE.json"
        db_path = root / "tde.sqlite"
        result = run_pipeline(
            report=_sample_report(),
            report_out=report_path,
            packet_out=packet_path,
            workspace_scope="lyra-os-root",
            db_path=db_path,
        )
        assert report_path.exists()
        assert packet_path.exists()
        assert result["ingest"]["status"] == "ingested"
        assert result["intake_class"] == "work"

        md_path = root / "ERR-PIPE-001.md"
        md_path.write_text(SAMPLE_MD, encoding="utf-8")
        structured_path = root / "ERR-PIPE-001.json"
        md_packet_path = root / "ERR-PIPE-001.intake.json"
        md_result = run_markdown_pipeline(
            md_path=md_path,
            report_out=structured_path,
            packet_out=md_packet_path,
            workspace_scope="lyra-os-root",
            db_path=db_path,
            priority_hint="medium",
        )
        assert structured_path.exists()
        assert md_packet_path.exists()
        assert md_result["ingest"]["status"] == "ingested"
        assert md_result["intake_class"] == "work"
    print("[PASS] TDE error report pipeline tests passed")


if __name__ == "__main__":
    run_tests()
