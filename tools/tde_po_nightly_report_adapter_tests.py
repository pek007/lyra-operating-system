#!/usr/bin/env python3
from __future__ import annotations

from tde_po_nightly_report_adapter import adapt_po_nightly_report, ValidationError


def _sample_report() -> dict:
    return {
        "artifactType": "tde_po_nightly_report",
        "schemaVersion": "1.0.0",
        "report_id": "po-nightly-task-mgmt-2026-03-14",
        "report_date": "2026-03-14",
        "product_id": "A-007",
        "product_name": "Task Management",
        "product_owner": "Lyra",
        "overall_health": "yellow",
        "summary": "Progress is steady, but two blockers need triage and one risk needs watching.",
        "top_priorities": [
            "Stabilize intake validation path",
            "Clarify producer adapter contract"
        ],
        "blockers": [
            {
                "title": "Producer adapter path not yet wired for nightly reports",
                "blocker_type": "operational",
                "next_step": "Implement first adapter",
                "linked_tde_id": "TDE-123"
            },
            {
                "title": "Need policy decision on triage thresholds",
                "blocker_type": "decision",
                "next_step": "Open decision item",
                "linked_tde_id": None
            }
        ],
        "risks": [
            {
                "title": "Signal-to-task promotion may create noise",
                "impact": "Low-quality work inflation",
                "mitigation": "Keep default triage as record/update-first"
            }
        ],
        "proposed_tde_actions": [
            "Create producer adapter for nightly PO report",
            "Define promotion thresholds"
        ],
        "evidence_links": [
            {
                "kind": "doc",
                "ref": "products/task-management/06-architecture/TDE_INTAKE_INTERFACE_CONTRACT_V1.md",
                "note": "Canonical intake contract"
            }
        ],
        "source_reference": "control-panel:nightly-report:A-007:2026-03-14",
        "control_panel_priority": "high"
    }


def run_tests() -> None:
    report = _sample_report()
    packet = adapt_po_nightly_report(report=report, workspace_scope="lyra-os-root")
    assert packet["artifactType"] == "tde_intake_packet"
    assert packet["intake_class"] == "signal"
    assert packet["priority_hint"] == "high"
    assert packet["product_scope"] == "A-007"
    assert packet["signal_types"] == ["status", "blocker", "risk", "priority_proposal"]
    assert any(entity["entity_ref"] == "A-007" for entity in packet["related_entities"])
    assert any(entity["entity_ref"] == "TDE-123" for entity in packet["related_entities"])

    bad = _sample_report()
    del bad["summary"]
    try:
        adapt_po_nightly_report(report=bad, workspace_scope="lyra-os-root")
        raise AssertionError("expected ValidationError for invalid source report")
    except ValidationError:
        pass

    print("[PASS] TDE PO nightly report adapter tests passed")


if __name__ == "__main__":
    run_tests()
