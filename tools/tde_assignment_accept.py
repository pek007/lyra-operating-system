#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from tde_state_store import connect, init_schema, update_task_metadata

ROOT = Path(__file__).resolve().parents[1]
SCHEMA_REGISTRY = ROOT / "schemas/_registry.json"


class ValidationError(RuntimeError):
    pass


def _iso_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace('+00:00', 'Z')


def _load_schema(*, artifact_type: str, schema_version: str) -> dict[str, Any]:
    registry = json.loads(SCHEMA_REGISTRY.read_text(encoding="utf-8"))
    schema_rel = registry.get(artifact_type, {}).get(schema_version)
    if not schema_rel:
        raise ValidationError(f"missing_registered_schema:{artifact_type}@{schema_version}")
    return json.loads((ROOT / schema_rel).read_text(encoding="utf-8"))


def _validate_against_schema(*, payload: dict[str, Any], artifact_type: str, schema_version: str) -> None:
    try:
        import jsonschema  # type: ignore
    except Exception as exc:
        raise ValidationError("jsonschema_not_installed") from exc
    schema = _load_schema(artifact_type=artifact_type, schema_version=schema_version)
    try:
        jsonschema.validate(payload, schema)
    except Exception as exc:
        raise ValidationError(f"schema_validation_failed:{artifact_type}@{schema_version}: {exc}") from exc


def _ensure_assignment_schema(conn: Any) -> None:
    conn.executescript(
        """
        CREATE TABLE IF NOT EXISTS assignment_packets (
          assignment_id TEXT PRIMARY KEY,
          packet_hash TEXT NOT NULL,
          packet_json TEXT NOT NULL,
          acceptance_state TEXT NOT NULL,
          result_json TEXT NOT NULL,
          created_at TEXT NOT NULL,
          updated_at TEXT NOT NULL
        );
        """
    )
    conn.commit()


def _packet_hash(packet: dict[str, Any]) -> str:
    return hashlib.sha256(json.dumps(packet, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def _derive_task_id(packet: dict[str, Any]) -> str:
    assignment_id = str(packet["assignment_id"])
    if assignment_id.startswith("TASK-"):
        return assignment_id
    return f"TASK-{assignment_id}"


def _acceptance_state(packet: dict[str, Any]) -> tuple[str, str | None]:
    if packet.get("runner_binding_required") and not packet.get("decision_policy_ref"):
        return "accepted_pending_binding", "missing_decision_policy_ref"
    if not packet.get("objective_id"):
        return "accepted_no_runner", "missing_objective_id"
    return "accepted", None


def accept_assignment(*, packet: dict[str, Any], db_path: Path) -> dict[str, Any]:
    _validate_against_schema(payload=packet, artifact_type="tde_assignment_packet", schema_version=str(packet["schemaVersion"]))

    conn = connect(db_path)
    init_schema(conn)
    _ensure_assignment_schema(conn)

    packet_hash = _packet_hash(packet)
    existing = conn.execute(
        "SELECT packet_hash, result_json FROM assignment_packets WHERE assignment_id=?",
        (packet["assignment_id"],),
    ).fetchone()
    if existing:
        existing_hash, result_json = existing
        if existing_hash != packet_hash:
            raise ValidationError(f"idempotency_conflict:{packet['assignment_id']}")
        return {"assignment_id": packet["assignment_id"], "status": "duplicate", **json.loads(result_json)}

    task_id = _derive_task_id(packet)
    state, reason = _acceptance_state(packet)
    now = _iso_now()
    metadata = {
        "assignment_id": packet["assignment_id"],
        "assignment_source_system": packet["source_system"],
        "assignment_source_reference": packet["source_reference"],
        "assignment_owner_role": packet["assignment_owner_role"],
        "assignment_acceptance_state": state,
        "assignment_acceptance_reason": reason,
        "objective_id": packet.get("objective_id"),
        "decision_policy_ref": packet.get("decision_policy_ref"),
        "workflow_family": packet.get("workflow_family"),
        **(packet.get("metadata") or {}),
    }

    row = conn.execute("SELECT task_id FROM tasks WHERE task_id=?", (task_id,)).fetchone()
    with conn:
        if row:
            update_task_metadata(conn, task_id, metadata)
        else:
            conn.execute(
                "INSERT INTO tasks(task_id,title,status,checked,version,source,updated_at,metadata_json) VALUES(?,?,?,?,?,?,?,?)",
                (
                    task_id,
                    packet["title"],
                    "Active" if state == "accepted" else "Waiting",
                    0,
                    0,
                    packet["source_system"],
                    now,
                    json.dumps(metadata, separators=(",", ":")),
                ),
            )
        result = {
            "acceptance_state": state,
            "reason": reason,
            "task_id": task_id,
            "accepted_at": now,
        }
        conn.execute(
            "INSERT INTO assignment_packets(assignment_id,packet_hash,packet_json,acceptance_state,result_json,created_at,updated_at) VALUES(?,?,?,?,?,?,?)",
            (
                packet["assignment_id"],
                packet_hash,
                json.dumps(packet, separators=(",", ":")),
                state,
                json.dumps(result, separators=(",", ":")),
                now,
                now,
            ),
        )
        event_payload = {
            "assignment_id": packet["assignment_id"],
            "task_id": task_id,
            "acceptance_state": state,
            "reason": reason,
            "source_system": packet["source_system"],
        }
        conn.execute(
            "INSERT INTO events(event_id,at,type,payload_json,prev_hash,hash) VALUES(?,?,?,?,?,?)",
            (
                f"evt:assignment:{packet['assignment_id']}",
                now,
                "assignment_accepted",
                json.dumps(event_payload, separators=(",", ":")),
                None,
                hashlib.sha256(json.dumps(event_payload, sort_keys=True, separators=(",", ":")).encode()).hexdigest(),
            ),
        )
    return {"assignment_id": packet["assignment_id"], "status": "accepted", **result}


def main() -> None:
    ap = argparse.ArgumentParser(description="Accept a canonical TDE assignment packet")
    ap.add_argument("--packet-path", required=True)
    ap.add_argument("--db-path", default="os/runtime/tde_state.sqlite")
    args = ap.parse_args()
    packet = json.loads(Path(args.packet_path).read_text(encoding="utf-8"))
    print(json.dumps(accept_assignment(packet=packet, db_path=Path(args.db_path)), indent=2))


if __name__ == "__main__":
    main()
