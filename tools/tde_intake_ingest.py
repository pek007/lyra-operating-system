#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from tde_state_store import connect, init_schema

ROOT = Path(__file__).resolve().parents[1]
SCHEMA_REGISTRY = ROOT / "schemas/_registry.json"
DEFAULT_INTAKE_SCHEMA_KEY = "tde_intake_packet"
DEFAULT_INTAKE_SCHEMA_VERSION = "1.0.0"


class ValidationError(RuntimeError):
    pass


def _iso_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace('+00:00', 'Z')


def _load_schema(*, artifact_type: str, schema_version: str) -> dict[str, Any]:
    registry = json.loads(SCHEMA_REGISTRY.read_text(encoding="utf-8"))
    schema_rel = registry.get(artifact_type, {}).get(schema_version)
    if not schema_rel:
        raise ValidationError(f"missing_registered_schema:{artifact_type}@{schema_version}")
    schema_path = ROOT / schema_rel
    return json.loads(schema_path.read_text(encoding="utf-8"))


def _validate_against_schema(*, payload: dict[str, Any], artifact_type: str, schema_version: str) -> None:
    try:
        import jsonschema  # type: ignore
    except Exception as exc:
        raise ValidationError(
            "jsonschema_not_installed: install dependency (e.g. `python3 -m pip install --user jsonschema`)"
        ) from exc

    schema = _load_schema(artifact_type=artifact_type, schema_version=schema_version)
    try:
        jsonschema.validate(payload, schema)
    except Exception as exc:
        raise ValidationError(f"schema_validation_failed:{artifact_type}@{schema_version}: {exc}") from exc


def _ensure_ingest_schema(conn: Any) -> None:
    conn.executescript(
        """
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

        CREATE TABLE IF NOT EXISTS intake_links (
          link_id INTEGER PRIMARY KEY AUTOINCREMENT,
          intake_id TEXT NOT NULL,
          link_type TEXT NOT NULL,
          link_ref TEXT NOT NULL,
          created_at TEXT NOT NULL,
          UNIQUE(intake_id, link_type, link_ref)
        );
        """
    )
    conn.commit()


def _packet_hash(packet: dict[str, Any]) -> str:
    return hashlib.sha256(json.dumps(packet, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def _signal_triage(packet: dict[str, Any]) -> dict[str, Any]:
    body = packet.get("body") if isinstance(packet.get("body"), dict) else {}
    blockers = body.get("blockers") if isinstance(body.get("blockers"), list) else []
    risks = body.get("risks") if isinstance(body.get("risks"), list) else []
    proposed_actions = body.get("proposed_tde_actions") if isinstance(body.get("proposed_tde_actions"), list) else []
    overall_health = body.get("overall_health")

    linked_refs = []
    decision_blockers = 0
    for blocker in blockers:
        if not isinstance(blocker, dict):
            continue
        linked_id = blocker.get("linked_tde_id")
        if isinstance(linked_id, str) and linked_id.strip():
            linked_refs.append(linked_id)
        if blocker.get("blocker_type") == "decision":
            decision_blockers += 1

    if linked_refs:
        return {
            "triage_outcome": "update_existing",
            "reason": "linked_tde_items_present",
            "linked_refs": sorted(set(linked_refs)),
            "decision_blocker_count": decision_blockers,
            "counts": {
                "blockers": len(blockers),
                "risks": len(risks),
                "proposed_actions": len(proposed_actions),
            },
        }

    if decision_blockers > 0:
        return {
            "triage_outcome": "create_decision",
            "reason": "decision_blocker_present",
            "linked_refs": [],
            "decision_blocker_count": decision_blockers,
            "counts": {
                "blockers": len(blockers),
                "risks": len(risks),
                "proposed_actions": len(proposed_actions),
            },
        }

    if proposed_actions and overall_health in {"yellow", "red"}:
        return {
            "triage_outcome": "create_work",
            "reason": "actionable_followup_proposed_under_health_signal",
            "linked_refs": [],
            "decision_blocker_count": 0,
            "counts": {
                "blockers": len(blockers),
                "risks": len(risks),
                "proposed_actions": len(proposed_actions),
            },
        }

    return {
        "triage_outcome": "record_only",
        "reason": "no_promotion_threshold_met",
        "linked_refs": [],
        "decision_blocker_count": 0,
        "counts": {
            "blockers": len(blockers),
            "risks": len(risks),
            "proposed_actions": len(proposed_actions),
        },
    }


def _triage(packet: dict[str, Any]) -> dict[str, Any]:
    intake_class = packet.get("intake_class")
    if intake_class == "signal":
        return _signal_triage(packet)
    raise ValidationError(f"unsupported_intake_class:{intake_class}")


def ingest_packet(*, packet: dict[str, Any], db_path: Path) -> dict[str, Any]:
    _validate_against_schema(
        payload=packet,
        artifact_type=DEFAULT_INTAKE_SCHEMA_KEY,
        schema_version=str(packet["schemaVersion"]),
    )

    packet_hash = _packet_hash(packet)
    conn = connect(db_path)
    init_schema(conn)
    _ensure_ingest_schema(conn)

    existing = conn.execute(
        "SELECT packet_hash, outcome_json FROM intake_packets WHERE intake_id=?",
        (packet["intake_id"],),
    ).fetchone()
    if existing:
        existing_hash, existing_outcome_json = existing
        if existing_hash != packet_hash:
            raise ValidationError(f"idempotency_conflict:{packet['intake_id']}")
        existing_outcome = json.loads(existing_outcome_json)
        return {
            "intake_id": packet["intake_id"],
            "status": "duplicate",
            "triage_outcome": existing_outcome["triage_outcome"],
            "outcome": existing_outcome,
        }

    outcome = {
        **_triage(packet),
        "processed_at": _iso_now(),
        "intake_id": packet["intake_id"],
        "workspace_scope": packet["workspace_scope"],
        "product_scope": packet.get("product_scope"),
    }
    now = _iso_now()

    with conn:
        conn.execute(
            """
            INSERT INTO intake_packets(
              intake_id,intake_class,source_system,source_reference,packet_hash,packet_json,
              triage_outcome,outcome_json,created_at,updated_at
            ) VALUES(?,?,?,?,?,?,?,?,?,?)
            """,
            (
                packet["intake_id"],
                packet["intake_class"],
                packet["source_system"],
                packet["source_reference"],
                packet_hash,
                json.dumps(packet, separators=(",", ":")),
                outcome["triage_outcome"],
                json.dumps(outcome, separators=(",", ":")),
                now,
                now,
            ),
        )

        related_entities = packet.get("related_entities") if isinstance(packet.get("related_entities"), list) else []
        for entity in related_entities:
            if not isinstance(entity, dict):
                continue
            link_type = entity.get("entity_type")
            link_ref = entity.get("entity_ref")
            if isinstance(link_type, str) and link_type and isinstance(link_ref, str) and link_ref:
                conn.execute(
                    "INSERT OR IGNORE INTO intake_links(intake_id, link_type, link_ref, created_at) VALUES(?,?,?,?)",
                    (packet["intake_id"], link_type, link_ref, now),
                )

        event_payload = {
            "intake_id": packet["intake_id"],
            "intake_class": packet["intake_class"],
            "triage_outcome": outcome["triage_outcome"],
            "reason": outcome["reason"],
            "source_system": packet["source_system"],
        }
        request_hash = packet_hash
        conn.execute(
            """
            INSERT OR REPLACE INTO actions(action_id,idempotency_key,request_hash,state,response_json,created_at,updated_at)
            VALUES(?,?,?,?,?,?,?)
            """,
            (
                f"intake:{packet['intake_id']}",
                f"intake:{packet['intake_id']}",
                request_hash,
                outcome["triage_outcome"],
                json.dumps(outcome, separators=(",", ":")),
                now,
                now,
            ),
        )
        conn.execute(
            "INSERT INTO events(event_id,at,type,payload_json,prev_hash,hash) VALUES(?,?,?,?,?,?)",
            (
                f"evt:intake:{packet['intake_id']}",
                now,
                "intake_ingested",
                json.dumps(event_payload, separators=(",", ":")),
                None,
                hashlib.sha256(json.dumps(event_payload, sort_keys=True, separators=(",", ":")).encode()).hexdigest(),
            ),
        )

    return {
        "intake_id": packet["intake_id"],
        "status": "ingested",
        "triage_outcome": outcome["triage_outcome"],
        "outcome": outcome,
    }


def main() -> None:
    ap = argparse.ArgumentParser(description="Ingest a canonical TDE intake packet")
    ap.add_argument("--packet-path", required=True)
    ap.add_argument("--db-path", default="os/runtime/staging/tde_state.sqlite")
    args = ap.parse_args()

    packet = json.loads(Path(args.packet_path).read_text(encoding="utf-8"))
    result = ingest_packet(packet=packet, db_path=Path(args.db_path))
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
