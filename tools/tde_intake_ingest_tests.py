#!/usr/bin/env python3
from __future__ import annotations

import tempfile
from pathlib import Path

from tde_intake_ingest import ValidationError, ingest_packet
from tde_po_nightly_report_adapter_tests import _sample_report
from tde_po_nightly_report_adapter import adapt_po_nightly_report


def run_tests() -> None:
    with tempfile.TemporaryDirectory() as td:
        root = Path(td)
        db_path = root / "tde_state.sqlite"

        packet = adapt_po_nightly_report(report=_sample_report(), workspace_scope="lyra-os-root")
        result = ingest_packet(packet=packet, db_path=db_path)
        assert result["status"] == "ingested"
        assert result["triage_outcome"] == "update_existing"
        assert "TDE-123" in result["outcome"]["linked_refs"]

        duplicate = ingest_packet(packet=packet, db_path=db_path)
        assert duplicate["status"] == "duplicate"
        assert duplicate["triage_outcome"] == "update_existing"

        decision_report = _sample_report()
        decision_report["report_id"] = "po-nightly-task-mgmt-2026-03-15"
        decision_report["report_date"] = "2026-03-15"
        decision_report["source_reference"] = "control-panel:nightly-report:A-007:2026-03-15"
        decision_report["blockers"] = [
            {
                "title": "Need a scope trade-off decision",
                "blocker_type": "decision",
                "next_step": "Open decision item",
                "linked_tde_id": None,
            }
        ]
        decision_report["proposed_tde_actions"] = []
        decision_packet = adapt_po_nightly_report(report=decision_report, workspace_scope="lyra-os-root")
        decision_result = ingest_packet(packet=decision_packet, db_path=db_path)
        assert decision_result["triage_outcome"] == "create_decision"

        work_report = _sample_report()
        work_report["report_id"] = "po-nightly-task-mgmt-2026-03-16"
        work_report["report_date"] = "2026-03-16"
        work_report["source_reference"] = "control-panel:nightly-report:A-007:2026-03-16"
        work_report["blockers"] = []
        work_report["risks"] = []
        work_report["proposed_tde_actions"] = ["Create adapter backlog item"]
        work_report["control_panel_priority"] = None
        work_packet = adapt_po_nightly_report(report=work_report, workspace_scope="lyra-os-root")
        work_result = ingest_packet(packet=work_packet, db_path=db_path)
        assert work_result["triage_outcome"] == "create_work"

        conflict_packet = dict(packet)
        conflict_packet["summary"] = "Changed summary"
        try:
            ingest_packet(packet=conflict_packet, db_path=db_path)
            raise AssertionError("expected idempotency conflict")
        except ValidationError:
            pass

    print("[PASS] TDE intake ingest tests passed")


if __name__ == "__main__":
    run_tests()
