#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from tde_decision_escalation import write_escalation_package
from tde_state_store import connect, init_schema, read_tasks, update_task_metadata, activate_task_db
from tde_chaining import evaluate_ready_promotions

ROOT = Path(__file__).resolve().parents[1]
SCHEMA_REGISTRY = ROOT / "schemas/_registry.json"

TASK_STATUS_MAP = {
    "Done": "Done",
    "Blocked": "Waiting",
    "Deferred": "Waiting",
    "Escalated": "Waiting",
}
DEFAULT_DB_PATH = "os/runtime/tde_state.sqlite"


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
        raise ValidationError(
            "jsonschema_not_installed: install dependency (e.g. `python3 -m pip install --user jsonschema`)"
        ) from exc
    schema = _load_schema(artifact_type=artifact_type, schema_version=schema_version)
    try:
        jsonschema.validate(payload, schema)
    except Exception as exc:
        raise ValidationError(f"schema_validation_failed:{artifact_type}@{schema_version}: {exc}") from exc


def _ensure_closure_schema(conn: Any) -> None:
    conn.executescript(
        """
        CREATE TABLE IF NOT EXISTS task_closures (
          closure_id TEXT PRIMARY KEY,
          task_id TEXT NOT NULL,
          closure_state TEXT NOT NULL,
          feedback_outcome TEXT NOT NULL,
          closure_json TEXT NOT NULL,
          created_at TEXT NOT NULL
        );
        CREATE UNIQUE INDEX IF NOT EXISTS idx_task_closures_task_id_closure_id
        ON task_closures(task_id, closure_id);
        """
    )
    conn.commit()


def build_closure_record(
    *,
    task_id: str,
    closure_state: str,
    result_summary: str,
    evidence_refs: list[str],
    outcome_vs_expected: str,
    next_recommendation: str,
    feedback_outcome: str,
    friction_flags: list[str],
    objective_id: str | None = None,
    followup_refs: list[str] | None = None,
) -> dict[str, Any]:
    return {
        "artifactType": "tde_task_closure_record",
        "schemaVersion": "1.0.0",
        "closure_id": f"CLOSE-{task_id}-{datetime.now(timezone.utc).strftime('%Y%m%d-%H%M%S-%f')}",
        "task_id": task_id,
        "objective_id": objective_id,
        "closure_state": closure_state,
        "result_summary": result_summary,
        "evidence_refs": evidence_refs,
        "outcome_vs_expected": outcome_vs_expected,
        "next_recommendation": next_recommendation,
        "feedback_outcome": feedback_outcome,
        "friction_flags": friction_flags,
        "followup_refs": followup_refs or [],
        "evaluated_at": _iso_now(),
        "evaluated_by_role": "Product Owner",
    }


def _slug(text: str) -> str:
    out = ''.join(c.lower() if c.isalnum() else '-' for c in text)
    while '--' in out:
        out = out.replace('--', '-')
    return out.strip('-')[:80] or 'item'


def _write_improvement_note(*, artifact_dir: Path, closure_record: dict[str, Any]) -> str:
    artifact_dir.mkdir(parents=True, exist_ok=True)
    path = artifact_dir / f"tde-improvement-{_slug(closure_record['task_id'])}-{_slug(closure_record['closure_id'])}.md"
    body = f"""# TDE Improvement Follow-up

- Source task: {closure_record['task_id']}
- Closure ID: {closure_record['closure_id']}
- Objective ID: {closure_record.get('objective_id')}
- Feedback outcome: {closure_record['feedback_outcome']}
- Evaluated at: {closure_record['evaluated_at']}

## Summary
{closure_record['result_summary']}

## Outcome vs expected
{closure_record['outcome_vs_expected']}

## Recommended next action
{closure_record['next_recommendation']}

## Friction flags
"""
    flags = closure_record.get("friction_flags", []) or []
    if flags:
        body += ''.join(f"- {flag}\n" for flag in flags)
    else:
        body += "- none recorded\n"
    body += "\n## Evidence refs\n"
    body += ''.join(f"- {ref}\n" for ref in closure_record.get("evidence_refs", []))
    body += "\n## Follow-up refs\n"
    followups = closure_record.get("followup_refs", []) or []
    if followups:
        body += ''.join(f"- {ref}\n" for ref in followups)
    else:
        body += "- none\n"
    path.write_text(body, encoding="utf-8")
    return str(path)


def _write_error_report(*, artifact_dir: Path, closure_record: dict[str, Any]) -> str:
    artifact_dir.mkdir(parents=True, exist_ok=True)
    error_id = f"ERR-{closure_record['task_id']}-{datetime.now(timezone.utc).strftime('%Y%m%d-%H%M%S')}"
    path = artifact_dir / f"{error_id}.md"
    evidence = closure_record.get("evidence_refs", []) or []
    followups = closure_record.get("followup_refs", []) or []
    body = f"""# Error Report

## Header
- Error ID: {error_id}
- Date: {closure_record['evaluated_at'][:10]}
- Title: TDE task closure error follow-up for {closure_record['task_id']}
- Type: process_failure
- Scope: product_local
- Owning product or owner: A-007 / Task Management
- Affected products/contexts: Task Management / TDE runtime
- Status: open
- Review / closure date: TBD

## Summary
- What happened?
  - {closure_record['result_summary']}

## Impact
- Actual impact:
  - Task ended with closure outcome `{closure_record['feedback_outcome']}` and requires error-path handling.
- Potential impact:
  - Recurrence could degrade TDE execution reliability and follow-through.

## Detection
- How was it detected?
  - Structured task closure evaluation in TDE.
- Detection gap, if any:
  - TBD

## Root cause
- Primary root cause:
  - TBD
- Contributing factors:
"""
    flags = closure_record.get("friction_flags", []) or []
    if flags:
        body += ''.join(f"  - {flag}\n" for flag in flags)
    else:
        body += "  - TBD\n"
    body += f"""

## Immediate mitigation
- What was done immediately?
  - Task closure was recorded and routed into the formal error path.

## Corrective actions
"""
    if followups:
        body += ''.join(f"- [ ] {ref}\n" for ref in followups)
    else:
        body += "- [ ] Define corrective action\n"
    body += f"""

## Preventive changes
- What should change to reduce recurrence?
  - {closure_record['next_recommendation']}

## Linked artifacts
- Related tasks: {', '.join(followups) if followups else 'none'}
- Related decisions: none
- Related evidence: {', '.join(evidence) if evidence else 'none'}
- Related product/shared artifacts: {closure_record['closure_id']}

## Closure criteria
- What must be true before this is considered closed?
  - Corrective action assigned
  - Relevant control/model updated
  - Verification path defined

## Closure note
- Final outcome / verification:
  - TBD
"""
    path.write_text(body, encoding="utf-8")
    return str(path)


def _close_followup_actions(*, conn: Any, closure_record: dict[str, Any], task_metadata: dict[str, Any], artifact_dir: Path | None) -> dict[str, Any]:
    feedback_outcome = closure_record["feedback_outcome"]
    followup_refs = closure_record.get("followup_refs", []) or []
    actions: dict[str, Any] = {
        "followup_refs": followup_refs,
        "activated_followups": [],
        "ready_promotions": [],
        "escalation_package_path": None,
        "improvement_refs": [],
        "improvement_artifact_path": None,
        "error_report_path": None,
    }

    if feedback_outcome == "close_and_chain":
        for ref in followup_refs:
            activation = activate_task_db(
                conn,
                ref,
                activated_by=f"closure:{closure_record['closure_id']}:followup",
                activated_at=_iso_now(),
            )
            actions["activated_followups"].append(activation)

        tasks = read_tasks(conn)
        chaining_eval = evaluate_ready_promotions(tasks, tick_id=closure_record["closure_id"])
        for promo in chaining_eval.get("promoted", []):
            activation = activate_task_db(
                conn,
                promo["task_id"],
                activated_by=promo["activated_by"],
                activated_at=promo["activated_at"],
            )
            actions["ready_promotions"].append(activation)

    elif feedback_outcome == "close_and_escalate":
        if artifact_dir is None:
            raise ValidationError("artifact_dir_required_for_escalation")
        actions["escalation_package_path"] = write_escalation_package(
            artifact_dir=artifact_dir,
            tick_id=closure_record["closure_id"],
            task_id=closure_record["task_id"],
            objective_id=closure_record.get("objective_id"),
            metadata={
                **task_metadata,
                "decision_rationale": closure_record["next_recommendation"],
                "decision_evidence_refs": closure_record["evidence_refs"],
                "decision_context_summary": closure_record["result_summary"],
            },
            workflow_family=task_metadata.get("workflow_family"),
        )

    elif feedback_outcome == "close_and_improve":
        if artifact_dir is None:
            raise ValidationError("artifact_dir_required_for_improvement")
        actions["improvement_refs"] = followup_refs
        actions["improvement_artifact_path"] = _write_improvement_note(
            artifact_dir=artifact_dir,
            closure_record=closure_record,
        )

    elif feedback_outcome == "close_as_error":
        if artifact_dir is None:
            raise ValidationError("artifact_dir_required_for_error")
        actions["improvement_refs"] = followup_refs
        actions["error_report_path"] = _write_error_report(
            artifact_dir=artifact_dir,
            closure_record=closure_record,
        )

    return actions


def close_task(*, closure_record: dict[str, Any], db_path: Path, artifact_dir: Path | None = None) -> dict[str, Any]:
    _validate_against_schema(
        payload=closure_record,
        artifact_type="tde_task_closure_record",
        schema_version=str(closure_record["schemaVersion"]),
    )

    conn = connect(db_path)
    init_schema(conn)
    _ensure_closure_schema(conn)

    task_row = conn.execute(
        "SELECT task_id, status, metadata_json FROM tasks WHERE task_id=?",
        (closure_record["task_id"],),
    ).fetchone()
    if not task_row:
        raise ValidationError(f"task_not_found:{closure_record['task_id']}")
    _, _, metadata_json = task_row
    try:
        task_metadata = json.loads(metadata_json or "{}")
    except Exception:
        task_metadata = {}
    if not isinstance(task_metadata, dict):
        task_metadata = {}

    status_target = TASK_STATUS_MAP[closure_record["closure_state"]]
    metadata_patch = {
        "closure_id": closure_record["closure_id"],
        "closure_state": closure_record["closure_state"],
        "feedback_outcome": closure_record["feedback_outcome"],
        "result_summary": closure_record["result_summary"],
        "outcome_vs_expected": closure_record["outcome_vs_expected"],
        "next_recommendation": closure_record["next_recommendation"],
        "friction_flags": closure_record["friction_flags"],
        "followup_refs": closure_record.get("followup_refs", []),
        "closure_evidence_refs": closure_record["evidence_refs"],
        "closure_evaluated_at": closure_record["evaluated_at"],
    }

    update_task_metadata(conn, closure_record["task_id"], metadata_patch)
    now = _iso_now()
    followup_actions: dict[str, Any]
    with conn:
        conn.execute(
            "UPDATE tasks SET status=?, checked=?, updated_at=? WHERE task_id=?",
            (
                status_target,
                1 if closure_record["closure_state"] == "Done" else 0,
                now,
                closure_record["task_id"],
            ),
        )
        conn.execute(
            "INSERT INTO task_closures(closure_id, task_id, closure_state, feedback_outcome, closure_json, created_at) VALUES(?,?,?,?,?,?)",
            (
                closure_record["closure_id"],
                closure_record["task_id"],
                closure_record["closure_state"],
                closure_record["feedback_outcome"],
                json.dumps(closure_record, separators=(",", ":")),
                now,
            ),
        )
        followup_actions = _close_followup_actions(
            conn=conn,
            closure_record=closure_record,
            task_metadata=task_metadata,
            artifact_dir=artifact_dir,
        )
        event_payload = {
            "task_id": closure_record["task_id"],
            "closure_id": closure_record["closure_id"],
            "closure_state": closure_record["closure_state"],
            "feedback_outcome": closure_record["feedback_outcome"],
            "followup_actions": followup_actions,
        }
        conn.execute(
            "INSERT INTO events(event_id,at,type,payload_json,prev_hash,hash) VALUES(?,?,?,?,?,?)",
            (
                f"evt:close:{closure_record['closure_id']}",
                now,
                "task_closed",
                json.dumps(event_payload, separators=(",", ":")),
                None,
                json.dumps(event_payload, sort_keys=True, separators=(",", ":")),
            ),
        )

    return {
        "task_id": closure_record["task_id"],
        "closure_id": closure_record["closure_id"],
        "closure_state": closure_record["closure_state"],
        "feedback_outcome": closure_record["feedback_outcome"],
        "db_status": status_target,
        "followup_actions": followup_actions,
    }


def main() -> None:
    ap = argparse.ArgumentParser(description="Close a TDE task with a structured closure record")
    ap.add_argument("--task-id", required=True)
    ap.add_argument("--closure-state", required=True, choices=["Done", "Blocked", "Deferred", "Escalated"])
    ap.add_argument("--result-summary", required=True)
    ap.add_argument("--evidence-ref", action="append", default=[])
    ap.add_argument("--outcome-vs-expected", required=True)
    ap.add_argument("--next-recommendation", required=True)
    ap.add_argument("--feedback-outcome", required=True, choices=["close_clean", "close_and_chain", "close_and_improve", "close_and_escalate", "close_as_error"])
    ap.add_argument("--friction-flag", action="append", default=[])
    ap.add_argument("--followup-ref", action="append", default=[])
    ap.add_argument("--objective-id", default=None)
    ap.add_argument("--db-path", default=DEFAULT_DB_PATH)
    ap.add_argument("--artifact-dir", default=None)
    ap.add_argument("--out", default=None)
    args = ap.parse_args()

    closure_record = build_closure_record(
        task_id=args.task_id,
        closure_state=args.closure_state,
        result_summary=args.result_summary,
        evidence_refs=args.evidence_ref,
        outcome_vs_expected=args.outcome_vs_expected,
        next_recommendation=args.next_recommendation,
        feedback_outcome=args.feedback_outcome,
        friction_flags=args.friction_flag,
        objective_id=args.objective_id,
        followup_refs=args.followup_ref,
    )
    result = close_task(
        closure_record=closure_record,
        db_path=Path(args.db_path),
        artifact_dir=Path(args.artifact_dir) if args.artifact_dir else None,
    )
    if args.out:
        out = Path(args.out)
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(json.dumps(closure_record, indent=2) + "\n", encoding="utf-8")
        result["closure_record_path"] = str(out)
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
