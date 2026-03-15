#!/usr/bin/env python3
from __future__ import annotations

import tempfile
from pathlib import Path

from tde_assignment_accept import accept_assignment
from tde_assignment_limbo_check import check_assignment_limbo
from tde_intake_ingest import ingest_packet
from tde_state_store import connect, init_schema


def _assignment_packet(assignment_id: str) -> dict:
    return {
        "artifactType": "tde_assignment_packet",
        "schemaVersion": "1.0.0",
        "assignment_id": assignment_id,
        "source_system": "control-panel-api",
        "source_reference": f"cp:test:{assignment_id}",
        "submitted_at": "2026-03-15T16:55:00Z",
        "submitted_by": "Lyra",
        "title": f"Assignment {assignment_id}",
        "summary": "Used to validate limbo detection behavior.",
        "requested_action": "Validate limbo detection behavior.",
        "priority_hint": "medium",
        "workspace_scope": "lyra-os",
        "product_scope": "A-007",
        "related_entities": [],
        "evidence_links": [],
        "assignment_owner_role": "Task Management",
        "objective_id": "OBJ-TDE-FOUNDATION",
    }


def _intake_packet(intake_id: str, assignment_id: str) -> dict:
    return {
        "artifactType": "tde_intake_packet",
        "schemaVersion": "1.0.0",
        "intake_id": intake_id,
        "intake_class": "work",
        "source_system": "control-panel-api",
        "source_type": "api",
        "source_reference": f"assignment:{assignment_id}",
        "submitted_at": "2026-03-15T16:56:00Z",
        "submitted_by": "Lyra",
        "title": f"Intake for {assignment_id}",
        "summary": "Used to validate intake-linked assignment behavior.",
        "body": {"assignment_id": assignment_id},
        "requested_action": "Create or update canonical work for this assignment.",
        "priority_hint": "medium",
        "workspace_scope": "lyra-os",
        "product_scope": "A-007",
        "related_entities": [{"entity_type": "tde_item", "entity_ref": assignment_id, "relationship": "assignment"}],
        "evidence_links": [],
        "proposed_action": "create_work",
    }


def run_tests() -> None:
    with tempfile.TemporaryDirectory() as td:
        db = Path(td) / "tde.sqlite"

        # stale accepted assignment without intake trace should be flagged
        accept_assignment(packet=_assignment_packet("TASK-LIMBO-001"), db_path=db)
        conn = connect(db)
        init_schema(conn)
        with conn:
            conn.execute("UPDATE assignment_packets SET created_at='2026-03-15T15:00:00Z', updated_at='2026-03-15T15:00:00Z' WHERE assignment_id='TASK-LIMBO-001'")
            conn.execute("UPDATE tasks SET updated_at='2026-03-15T15:00:00Z' WHERE task_id='TASK-LIMBO-001'")

        result = check_assignment_limbo(db_path=db, stale_minutes=15)
        assert result["limbo_count"] == 1
        assert result["findings"][0]["assignment_id"] == "TASK-LIMBO-001"

        # stale accepted assignment with intake trace should not be flagged
        accept_assignment(packet=_assignment_packet("TASK-LIMBO-002"), db_path=db)
        ingest_packet(packet=_intake_packet("INTAKE-TASK-LIMBO-002", "TASK-LIMBO-002"), db_path=db)
        with conn:
            conn.execute("UPDATE assignment_packets SET created_at='2026-03-15T15:00:00Z', updated_at='2026-03-15T15:00:00Z' WHERE assignment_id='TASK-LIMBO-002'")
            conn.execute("UPDATE tasks SET updated_at='2026-03-15T15:00:00Z' WHERE task_id='TASK-LIMBO-002'")
            conn.execute("UPDATE intake_packets SET created_at='2026-03-15T15:01:00Z', updated_at='2026-03-15T15:01:00Z' WHERE intake_id='INTAKE-TASK-LIMBO-002'")

        result = check_assignment_limbo(db_path=db, stale_minutes=15)
        flagged = {f['assignment_id'] for f in result['findings']}
        assert 'TASK-LIMBO-001' in flagged
        assert 'TASK-LIMBO-002' not in flagged

    print('[PASS] TDE assignment limbo check tests passed')


if __name__ == '__main__':
    run_tests()
