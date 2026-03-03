#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from tde_kernel_slice_tests import ActionRequest, TDEKernel

TASK_LINE_RE = re.compile(r"^- \[ \] (?P<id>[A-Z0-9-]+) \| (?P<title>.+)$")


def _iso_now() -> str:
    return datetime.now(timezone.utc).isoformat()


def _read_tasks(tasks_path: Path, section: str = "Active") -> list[dict[str, Any]]:
    if not tasks_path.exists():
        return []

    lines = tasks_path.read_text(encoding="utf-8").splitlines()
    in_section = False
    out: list[dict[str, Any]] = []

    for line in lines:
        if line.startswith("## "):
            in_section = line.strip() == f"## {section}"
            continue
        if not in_section:
            continue

        match = TASK_LINE_RE.match(line.strip())
        if match:
            out.append(
                {
                    "id": match.group("id"),
                    "title": match.group("title"),
                    "state": "ready",
                }
            )

    return out


def _validate_mutation_envelope(envelope: dict[str, Any]) -> tuple[bool, str | None]:
    required = ["job_id", "binding_id", "policy_decision_id", "idempotency_key", "expected_version"]
    for key in required:
        if key not in envelope:
            return False, f"missing_required_field:{key}"
        value = envelope[key]
        if value is None:
            return False, f"missing_required_field:{key}"
        if isinstance(value, str) and not value.strip():
            return False, f"missing_required_field:{key}"
    return True, None




def _apply_low_risk_writeback(tasks_path: Path, claimed_ids: list[str], tick_id: str) -> dict[str, Any]:
    """Low-risk canonical write-back: move claimed tasks from Active -> Waiting with audit suffix.

    Idempotency rule: if a claimed task no longer exists in Active, do not duplicate in Waiting.
    """
    if not tasks_path.exists() or not claimed_ids:
        return {"applied": False, "reason": "no_tasks_or_no_claims", "moved": []}

    lines = tasks_path.read_text(encoding="utf-8").splitlines()
    sec = None
    active_idx: dict[str, int] = {}
    waiting_start = None

    for i, raw in enumerate(lines):
        if raw.startswith('## '):
            sec = raw.strip()
            if sec == '## Waiting':
                waiting_start = i
            continue
        if sec == '## Active':
            m = TASK_LINE_RE.match(raw.strip())
            if m:
                active_idx[m.group('id')] = i

    moved = []
    for task_id in claimed_ids:
        idx = active_idx.get(task_id)
        if idx is None:
            continue
        original = lines[idx]
        lines[idx] = None
        moved.append((task_id, original))

    if not moved:
        return {"applied": False, "reason": "no_active_claims_to_move", "moved": []}

    # Build waiting lines with deterministic audit suffix
    waiting_lines = []
    for task_id, original in moved:
        line = original
        if f"[tick:{tick_id}]" not in line:
            line = f"{line} [tick:{tick_id}]"
        waiting_lines.append(line)

    compact = [ln for ln in lines if ln is not None]

    # Re-find waiting section insertion point in compacted content
    insert_at = None
    for i, raw in enumerate(compact):
        if raw.strip() == '## Waiting':
            insert_at = i + 1
            break

    if insert_at is None:
        compact.extend(['', '## Waiting'])
        insert_at = len(compact)

    # Insert at top of waiting block preserving order
    compact[insert_at:insert_at] = waiting_lines
    tasks_path.write_text("\n".join(compact) + "\n", encoding='utf-8')

    return {
        "applied": True,
        "reason": None,
        "moved": [m[0] for m in moved],
        "targetSection": "Waiting",
    }

def run_job_tick(
    *,
    job_id: str,
    binding_id: str,
    actor_id: str,
    session_key: str,
    trigger_source: str,
    tick_id: str,
    max_claim: int,
    tasks_path: Path,
    artifact_path: Path,
    writeback_tasks_path: Path | None = None,
) -> dict[str, Any]:
    kernel = TDEKernel()
    tasks = _read_tasks(tasks_path, section="Active")

    outcomes = {
        "progressed": 0,
        "blocked_pending_approval": 0,
        "failed_validation": 0,
        "no_work": 0,
    }

    if not job_id.strip() or not actor_id.strip() or not session_key.strip() or not tick_id.strip():
        outcomes["failed_validation"] += 1
        artifact = {
            "tick_id": tick_id,
            "trigger_source": trigger_source,
            "timestamp": _iso_now(),
            "job_id": job_id,
            "binding_id": binding_id,
            "actor_id": actor_id,
            "session_key": session_key,
            "claim_limit": max_claim,
            "claimed": [],
            "mutations": [],
            "decisions": [],
            "evidence_outputs": [],
            "outcomes": outcomes,
            "status": "failed_validation",
            "fail_closed": True,
            "fail_closed_reason": "missing_required_identity_fields",
        }
    elif not binding_id.strip():
        outcomes["failed_validation"] += 1
        artifact = {
            "tick_id": tick_id,
            "trigger_source": trigger_source,
            "timestamp": _iso_now(),
            "job_id": job_id,
            "binding_id": binding_id,
            "actor_id": actor_id,
            "session_key": session_key,
            "claim_limit": max_claim,
            "claimed": [],
            "mutations": [],
            "decisions": [
                {
                    "type": "decision_required",
                    "reason": "binding_missing_or_invalid",
                }
            ],
            "evidence_outputs": [],
            "outcomes": outcomes,
            "status": "failed_validation",
            "fail_closed": True,
            "fail_closed_reason": "binding_missing_or_invalid",
        }
    else:
        ready = [t for t in tasks if t.get("state") == "ready"]
        claimed = ready[: max(0, max_claim)]

        mutations: list[dict[str, Any]] = []
        idempotency_refs: list[str] = []

        for index, item in enumerate(claimed):
            idempotency_key = f"{tick_id}:{item['id']}"
            idempotency_refs.append(idempotency_key)

            mutation_envelope = {
                "job_id": job_id,
                "binding_id": binding_id,
                "policy_decision_id": f"pending:{tick_id}:{item['id']}",
                "idempotency_key": idempotency_key,
                "expected_version": 0,
            }
            envelope_ok, envelope_error = _validate_mutation_envelope(mutation_envelope)
            if not envelope_ok:
                outcomes["failed_validation"] += 1
                mutations.append(
                    {
                        "task_id": item["id"],
                        "request_id": f"{tick_id}-{index}",
                        "idempotency_key": idempotency_key,
                        "status": "failed_validation",
                        "fail_closed": True,
                        "fail_closed_reason": envelope_error,
                        "mutation_envelope": mutation_envelope,
                    }
                )
                continue

            req = ActionRequest(
                request_id=f"{tick_id}-{index}",
                idempotency_key=idempotency_key,
                intent_hash=f"job-tick-progress:{item['id']}",
                actor=actor_id,
                job=job_id,
                action="task.transition",
                target_id=item["id"],
                expected_version=mutation_envelope["expected_version"],
                risk="low",
            )
            result = kernel.execute(req)
            status = result["status"]
            if status in {"executed", "replay"}:
                outcomes["progressed"] += 1
            elif status == "blocked_pending_approval":
                outcomes["blocked_pending_approval"] += 1
            else:
                outcomes["failed_validation"] += 1
            mutations.append(
                {
                    "task_id": item["id"],
                    "request_id": req.request_id,
                    "idempotency_key": idempotency_key,
                    "policy_decision_id": result.get("policy_decision_id"),
                    "audit_link": result.get("audit_link"),
                    "status": status,
                    "mutation_envelope": {
                        **mutation_envelope,
                        "policy_decision_id": result.get("policy_decision_id"),
                    },
                }
            )

        writeback = _apply_low_risk_writeback(writeback_tasks_path or tasks_path, [c["id"] for c in claimed], tick_id)

        if not claimed:
            outcomes["no_work"] += 1

        artifact = {
            "tick_id": tick_id,
            "trigger_source": trigger_source,
            "timestamp": _iso_now(),
            "job_id": job_id,
            "binding_id": binding_id,
            "actor_id": actor_id,
            "session_key": session_key,
            "claim_limit": max_claim,
            "claimed": [c["id"] for c in claimed],
            "mutations": mutations,
            "idempotency_references": idempotency_refs,
            "writeback": writeback,
            "decisions": [],
            "evidence_outputs": [str(artifact_path)],
            "outcomes": outcomes,
            "status": "ok",
            "fail_closed": False,
            "fail_closed_reason": None,
        }

    artifact_path.parent.mkdir(parents=True, exist_ok=True)
    artifact_path.write_text(json.dumps(artifact, indent=2) + "\n", encoding="utf-8")
    return artifact


def main() -> None:
    parser = argparse.ArgumentParser(description="Run one deterministic TDE job tick")
    parser.add_argument("--job-id", default="JOB-PROD-001")
    parser.add_argument("--binding-id", default="BIND-JOB-PROD-001-ACTIVE")
    parser.add_argument("--actor-id", default="lyra")
    parser.add_argument("--session-key", default="cron:tde-job-runner-v1")
    parser.add_argument("--trigger-source", choices=["cron", "heartbeat"], default="cron")
    parser.add_argument("--tick-id", default=f"job-tick-{datetime.now(timezone.utc).strftime('%Y%m%d-%H%M%S')}")
    parser.add_argument("--max-claim", type=int, default=1)
    parser.add_argument("--tasks-path", default="TASKS.md")
    parser.add_argument(
        "--artifact-path",
        default="knowledge/evidence/2026-03/tde-job-tick-latest.json",
    )
    parser.add_argument("--writeback-tasks-path", default="TASKS.md")

    args = parser.parse_args()
    artifact = run_job_tick(
        job_id=args.job_id,
        binding_id=args.binding_id,
        actor_id=args.actor_id,
        session_key=args.session_key,
        trigger_source=args.trigger_source,
        tick_id=args.tick_id,
        max_claim=args.max_claim,
        tasks_path=Path(args.tasks_path),
        artifact_path=Path(args.artifact_path),
        writeback_tasks_path=Path(args.writeback_tasks_path) if args.writeback_tasks_path else None,
    )
    print(json.dumps(artifact))


if __name__ == "__main__":
    main()
