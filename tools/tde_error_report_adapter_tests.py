#!/usr/bin/env python3
from __future__ import annotations

import tempfile
from pathlib import Path

from tde_error_report_adapter import adapt_error_report, ValidationError
from tde_intake_ingest import ingest_packet


def _sample_report(report_type: str = "process_failure", priority_hint: str = "medium") -> dict:
    return {
        "artifactType": "tde_error_report",
        "schemaVersion": "1.0.0",
        "error_id": f"ERR-TEST-{report_type.upper()}",
        "date": "2026-03-14",
        "title": "TDE corrective path was not routed canonically",
        "type": report_type,
        "scope": "product_local",
        "owning_product_or_owner": "A-007",
        "affected_products_contexts": ["Task Management", "TDE runtime"],
        "summary": "A meaningful issue was reported without a canonical TDE corrective path.",
        "impact": {
            "actual_impact": "Follow-up risked living only in prose.",
            "potential_impact": "Corrective action could be dropped or become untraceable."
        },
        "detection_method": "Manual architecture review",
        "root_cause": "No explicit adapter existed from error reporting into canonical TDE intake.",
        "contributing_factors": ["Process update outran runtime wiring"],
        "immediate_mitigation": "Define the bridge and implement the first adapter.",
        "corrective_actions": [
            "Add structured error-to-TDE intake adapter",
            "Validate corrective-action packets before ingest"
        ],
        "preventive_changes": "Keep error handling and TDE action routing linked in product-owned contracts.",
        "linked_artifacts": {
            "related_tasks": ["TDE-456"],
            "related_decisions": [],
            "related_evidence": ["ERROR_REPORTING_STANDARD_V1.md"],
            "related_product_shared_artifacts": ["AGENTS.md"]
        },
        "status": "open",
        "review_closure_date": None,
        "source_reference": "products/task-management/errors/ERR-TEST.md",
        "priority_hint": priority_hint
    }


def run_tests() -> None:
    work_packet = adapt_error_report(report=_sample_report(), workspace_scope="lyra-os-root")
    assert work_packet["intake_class"] == "work"
    assert "requested_action" in work_packet

    decision_packet = adapt_error_report(report=_sample_report(report_type="decision_failure"), workspace_scope="lyra-os-root")
    assert decision_packet["intake_class"] == "decision"
    assert "decision_question" in decision_packet

    incident_packet = adapt_error_report(report=_sample_report(report_type="incident", priority_hint="critical"), workspace_scope="lyra-os-root")
    assert incident_packet["intake_class"] == "incident"
    assert incident_packet["severity_hint"] == "sev1"

    with tempfile.TemporaryDirectory() as td:
        db = Path(td) / "tde.sqlite"
        result = ingest_packet(packet=work_packet, db_path=db)
        assert result["triage_outcome"] in {"record_only", "create_work", "update_existing", "create_decision"}

    bad = _sample_report()
    del bad["corrective_actions"]
    try:
        adapt_error_report(report=bad, workspace_scope="lyra-os-root")
        raise AssertionError("expected ValidationError")
    except ValidationError:
        pass

    print("[PASS] TDE error report adapter tests passed")


if __name__ == "__main__":
    run_tests()
