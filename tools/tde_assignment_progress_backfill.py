#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from tde_state_store import connect, init_schema, record_event

DEFAULT_DB_PATH = "os/runtime/tde_state.sqlite"


def _load_json(raw: str | None) -> dict[str, Any]:
    if not raw:
        return {}
    try:
        value = json.loads(raw)
    except Exception:
        return {}
    return value if isinstance(value, dict) else {}


def backfill_assignment_progress(*, db_path: Path) -> dict[str, Any]:
    conn = connect(db_path)
    init_schema(conn)
    now = datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace('+00:00', 'Z')

    rows = conn.execute(
        "SELECT assignment_id, acceptance_state, result_json, created_at FROM assignment_packets ORDER BY created_at DESC"
    ).fetchall()
    created = []

    with conn:
        for assignment_id, acceptance_state, result_json, created_at in rows:
            if acceptance_state != 'accepted':
                continue
            result = _load_json(result_json)
            task_id = result.get('task_id')
            if not task_id:
                continue
            existing = conn.execute(
                "SELECT 1 FROM events WHERE type != 'assignment_accepted' AND payload_json LIKE ? LIMIT 1",
                (f'%{task_id}%',),
            ).fetchone()
            if existing:
                continue
            task_row = conn.execute(
                "SELECT status, metadata_json, updated_at FROM tasks WHERE task_id=?",
                (task_id,),
            ).fetchone()
            if not task_row:
                continue
            status, metadata_json, updated_at = task_row
            metadata = _load_json(metadata_json)
            record = record_event(
                conn,
                event_id=f"evt:assignment-progress-backfill:{assignment_id}",
                at=updated_at or created_at or now,
                event_type="assignment_progressed",
                payload={
                    "assignment_id": assignment_id,
                    "task_id": task_id,
                    "task_status": status,
                    "reason": "backfill_existing_task_state",
                    "task_metadata": {
                        "activated_at": metadata.get('activated_at'),
                        "activated_by": metadata.get('activated_by'),
                        "last_tick_id": metadata.get('last_tick_id'),
                    },
                },
            )
            created.append(record)

    return {
        'db_path': str(db_path),
        'created_count': len(created),
        'created': created,
    }


def main() -> None:
    ap = argparse.ArgumentParser(description='Backfill assignment progression events for existing accepted assignments')
    ap.add_argument('--db-path', default=DEFAULT_DB_PATH)
    args = ap.parse_args()
    print(json.dumps(backfill_assignment_progress(db_path=Path(args.db_path)), indent=2))


if __name__ == '__main__':
    main()
