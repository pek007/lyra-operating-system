#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any

from tde_state_store import connect, init_schema

DEFAULT_DB_PATH = "os/runtime/tde_state.sqlite"


def _parse_ts(value: str | None) -> datetime | None:
    if not value:
        return None
    try:
        return datetime.fromisoformat(value.replace("Z", "+00:00"))
    except Exception:
        return None


def _ensure_schema(conn: Any) -> None:
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

        CREATE TABLE IF NOT EXISTS intake_packets (
          intake_id TEXT PRIMARY KEY,
          intake_class TEXT NOT NULL,
          source_system TEXT NOT NULL,
          source_reference TEXT NOT NULL,
          packet_hash TEXT NOT NULL,
          packet_json TEXT NOT NULL,
          triage_outcome TEXT NOT NULL,
          outcome_json TEXT NOT NULL,
          created_at TEXT NOT NULL,
          updated_at TEXT NOT NULL
        );
        """
    )
    conn.commit()


def _load_json(raw: str | None) -> dict[str, Any]:
    if not raw:
        return {}
    try:
        value = json.loads(raw)
    except Exception:
        return {}
    return value if isinstance(value, dict) else {}


def check_assignment_limbo(*, db_path: Path, stale_minutes: int = 15) -> dict[str, Any]:
    conn = connect(db_path)
    init_schema(conn)
    _ensure_schema(conn)
    conn.row_factory = None

    now = datetime.now(timezone.utc)
    stale_before = now - timedelta(minutes=stale_minutes)

    assignment_rows = conn.execute(
        "SELECT assignment_id, packet_json, acceptance_state, result_json, created_at, updated_at FROM assignment_packets ORDER BY created_at DESC"
    ).fetchall()

    findings: list[dict[str, Any]] = []

    for assignment_id, packet_json, acceptance_state, result_json, created_at, updated_at in assignment_rows:
        packet = _load_json(packet_json)
        result = _load_json(result_json)
        task_id = result.get("task_id")
        created_dt = _parse_ts(created_at) or _parse_ts(updated_at)

        if acceptance_state in {"duplicate", "rejected_invalid_assignment"}:
            continue
        if acceptance_state in {"accepted_no_runner", "accepted_pending_binding"}:
            continue
        if created_dt and created_dt > stale_before:
            continue

        task_row = None
        if task_id:
            task_row = conn.execute(
                "SELECT status, updated_at, metadata_json FROM tasks WHERE task_id=?",
                (task_id,),
            ).fetchone()

        intake_matches = []
        if assignment_id:
            intake_matches = conn.execute(
                "SELECT intake_id, intake_class, triage_outcome, created_at FROM intake_packets WHERE packet_json LIKE ? OR source_reference LIKE ? ORDER BY created_at DESC",
                (f'%{assignment_id}%', f'%{assignment_id}%'),
            ).fetchall()

        event_matches = []
        if assignment_id or task_id:
            clauses = []
            params = []
            if assignment_id:
                clauses.append("payload_json LIKE ?")
                params.append(f'%{assignment_id}%')
            if task_id:
                clauses.append("payload_json LIKE ?")
                params.append(f'%{task_id}%')
            query = f"SELECT event_id, at, type FROM events WHERE {' OR '.join(clauses)} ORDER BY at DESC"
            event_matches = conn.execute(query, tuple(params)).fetchall()

        has_assignment_event = any(ev_type == "assignment_accepted" for _, _, ev_type in event_matches)
        has_non_assignment_event = any(ev_type != "assignment_accepted" for _, _, ev_type in event_matches)
        has_intake_trace = len(intake_matches) > 0
        has_task = task_row is not None

        if has_task and (has_intake_trace or has_non_assignment_event):
            continue

        metadata = _load_json(task_row[2]) if task_row else {}
        findings.append(
            {
                "assignment_id": assignment_id,
                "acceptance_state": acceptance_state,
                "task_id": task_id,
                "assignment_created_at": created_at,
                "task_present": has_task,
                "task_status": task_row[0] if task_row else None,
                "task_updated_at": task_row[1] if task_row else None,
                "intake_trace_present": has_intake_trace,
                "intake_matches": [
                    {
                        "intake_id": intake_id,
                        "intake_class": intake_class,
                        "triage_outcome": triage_outcome,
                        "created_at": intake_created_at,
                    }
                    for intake_id, intake_class, triage_outcome, intake_created_at in intake_matches
                ],
                "non_assignment_event_present": has_non_assignment_event,
                "event_types": [ev_type for _, _, ev_type in event_matches],
                "task_metadata": metadata,
                "limbo_reason": "accepted_assignment_without_intake_or_follow_on_trace",
                "recommended_action": "Investigate producer path, intake linkage, and runner pickup for this assignment.",
            }
        )

    return {
        "checked_at": now.replace(microsecond=0).isoformat().replace("+00:00", "Z"),
        "db_path": str(db_path),
        "stale_minutes": stale_minutes,
        "assignment_count": len(assignment_rows),
        "limbo_count": len(findings),
        "findings": findings,
    }


def main() -> None:
    ap = argparse.ArgumentParser(description="Detect TDE assignment silent-limbo cases")
    ap.add_argument("--db-path", default=DEFAULT_DB_PATH)
    ap.add_argument("--stale-minutes", type=int, default=15)
    ap.add_argument("--out", default=None)
    args = ap.parse_args()

    result = check_assignment_limbo(db_path=Path(args.db_path), stale_minutes=args.stale_minutes)
    if args.out:
        out = Path(args.out)
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
