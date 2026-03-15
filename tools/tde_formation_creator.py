#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from tde_state_store import connect, export_tasks, init_schema, update_task_metadata

POLICY_REF = "products/task-management/07-decisions/REFERENCE_TDE_POLICY_ENVELOPE_IMPLEMENTATION_VERIFICATION_V1.json"
ALLOWED_ACTIONS = {"proceed_directly", "proceed_with_assumptions"}
ALLOWED_FAMILY = "implementation_verification_readiness"
DEFAULT_DB_PATH = "os/runtime/tde_state.sqlite"
DEFAULT_OBJECTIVES_PATH = "os/runtime/tde_objectives.json"
DEFAULT_TASKS_PROJECTION_PATH = "os/runtime/TASKS_from_db.md"


def _load_json(path: Path) -> dict[str, Any]:
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise ValueError("formation_not_object")
    return data


def _validate_minimum_formation(payload: dict[str, Any]) -> None:
    if payload.get("artifactType") != "tde_intent_formation_record":
        raise ValueError("invalid_artifact_type")
    if payload.get("schemaVersion") != "1.0.0":
        raise ValueError("invalid_schema_version")
    if payload.get("recommended_next_action") not in ALLOWED_ACTIONS:
        raise ValueError("formation_not_execution_ready")
    if payload.get("proposed_workflow_family") != ALLOWED_FAMILY:
        raise ValueError("unsupported_workflow_family")
    if not payload.get("proposed_first_stage_set"):
        raise ValueError("missing_first_stage_set")
    if not payload.get("proposed_first_task_set"):
        raise ValueError("missing_first_task_set")


def _load_objectives(path: Path) -> dict[str, Any]:
    if not path.exists():
        return {"objectives": []}
    data = _load_json(path)
    if "objectives" not in data or not isinstance(data["objectives"], list):
        raise ValueError("invalid_objectives_registry")
    return data


def _write_objectives(path: Path, data: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")


def _objective_id(payload: dict[str, Any]) -> str:
    existing = ((payload.get("proposed_objective") or {}).get("objective_id"))
    if isinstance(existing, str) and existing.strip():
        return existing
    return f"OBJ-FORM-{payload['formation_id']}"


def create_from_formation(*, formation_path: Path, db_path: Path, objectives_path: Path, tasks_projection_path: Path) -> dict[str, Any]:
    payload = _load_json(formation_path)
    _validate_minimum_formation(payload)
    objective_id = _objective_id(payload)
    now = datetime.now(timezone.utc).isoformat()

    objectives = _load_objectives(objectives_path)
    if not any(obj.get("objective_id") == objective_id for obj in objectives["objectives"]):
        objectives["objectives"].append(
            {
                "objective_id": objective_id,
                "owner": "A-007",
                "title": payload["proposed_objective"]["objective_title"],
                "summary": payload["proposed_objective"]["objective_summary"],
                "workflow_family": payload["proposed_workflow_family"],
                "success_criteria": payload["proposed_success_criteria"],
                "formation_id": payload["formation_id"],
                "created_with_assumptions": payload["recommended_next_action"] == "proceed_with_assumptions",
                "creation_mapping_version": "v1",
                "created_at": now,
            }
        )
        _write_objectives(objectives_path, objectives)

    conn = connect(db_path)
    init_schema(conn)
    created_tasks: list[str] = []
    with conn:
        for index, task in enumerate(payload["proposed_first_task_set"]):
            task_id = task.get("task_id") or f"TDE-FORM-{payload['formation_id']}-{index+1:03d}"
            title = task["task_title"]
            summary = task["task_summary"]
            stage_id = task.get("stage_id") or (payload["proposed_first_stage_set"][0] if payload["proposed_first_stage_set"] else None)
            conn.execute(
                "INSERT OR REPLACE INTO tasks(task_id,title,status,checked,version,source,updated_at,metadata_json) VALUES(?,?,?,?,?,?,?,?)",
                (
                    task_id,
                    title,
                    "Waiting" if index else "Active",
                    0,
                    0,
                    str(formation_path),
                    now,
                    json.dumps({}, separators=(",", ":")),
                ),
            )
            metadata = {
                "formation_id": payload["formation_id"],
                "source_ref": payload["source_ref"],
                "workflow_family": payload["proposed_workflow_family"],
                "decision_policy_ref": POLICY_REF,
                "stage_id": stage_id,
                "objective_id": objective_id,
                "created_with_assumptions": payload["recommended_next_action"] == "proceed_with_assumptions",
                "creation_mapping_version": "v1",
                "task_summary": summary,
            }
            update_task_metadata(conn, task_id, metadata, replace=True)
            created_tasks.append(task_id)

    export_tasks(conn, tasks_projection_path)
    return {
        "formation_id": payload["formation_id"],
        "objective_id": objective_id,
        "created_tasks": created_tasks,
        "workflow_family": payload["proposed_workflow_family"],
        "tasks_projection_path": str(tasks_projection_path),
        "objectives_path": str(objectives_path),
    }


def main() -> None:
    ap = argparse.ArgumentParser(description="Create canonical TDE objective/tasks from a formation record")
    ap.add_argument("--formation-path", required=True)
    ap.add_argument("--db-path", default=DEFAULT_DB_PATH)
    ap.add_argument("--objectives-path", default=DEFAULT_OBJECTIVES_PATH)
    ap.add_argument("--tasks-projection-path", default=DEFAULT_TASKS_PROJECTION_PATH)
    args = ap.parse_args()
    result = create_from_formation(
        formation_path=Path(args.formation_path),
        db_path=Path(args.db_path),
        objectives_path=Path(args.objectives_path),
        tasks_projection_path=Path(args.tasks_projection_path),
    )
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
