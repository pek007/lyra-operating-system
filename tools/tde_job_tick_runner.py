#!/usr/bin/env python3
from __future__ import annotations

import argparse
import fcntl
import json
import os
import re
import tempfile
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from tde_kernel import ActionRequest, TDEKernel
from tde_decision_policy import validate_task_policy_binding
from tde_state_store import connect as state_connect
from tde_state_store import init_schema as state_init_schema
from tde_state_store import import_tasks as state_import_tasks
from tde_state_store import parity_check as state_parity_check
from tde_state_store import record_shadow_tick as state_record_shadow_tick
from tde_state_store import read_tasks as state_read_tasks
from tde_state_store import export_tasks as state_export_tasks
from tde_state_store import apply_low_risk_writeback_db as state_apply_low_risk_writeback_db
from tde_state_store import apply_ready_promotions as state_apply_ready_promotions
from tde_chaining import evaluate_ready_promotions

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


def _validate_objective_linkage(objective_linkage: dict[str, Any]) -> tuple[bool, str | None]:
    required = ["objective_id", "objective_checkpoint", "rationale_trace"]
    for key in required:
        value = objective_linkage.get(key)
        if value is None:
            return False, f"missing_objective_linkage_field:{key}"
        if isinstance(value, str) and not value.strip():
            return False, f"missing_objective_linkage_field:{key}"
    return True, None


def _load_objective_registry(path: Path | None) -> dict[str, Any] | None:
    if path is None or not path.exists():
        return None
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
        if isinstance(payload, dict):
            return payload
    except Exception:
        return None
    return None


def _validate_objective_against_registry(
    objective_linkage: dict[str, Any], registry: dict[str, Any] | None
) -> tuple[bool, str | None, dict[str, Any] | None]:
    if registry is None:
        return False, "objective_registry_unavailable", None

    objectives = registry.get("objectives", [])
    if not isinstance(objectives, list):
        return False, "objective_registry_invalid", None

    objective_id = objective_linkage.get("objective_id")
    checkpoint = objective_linkage.get("objective_checkpoint")

    for obj in objectives:
        if not isinstance(obj, dict):
            continue
        if obj.get("objective_id") != objective_id:
            continue
        allowed = obj.get("allowed_checkpoints", [])
        if isinstance(allowed, list) and allowed and checkpoint not in allowed:
            return False, "objective_checkpoint_not_allowed", obj
        return True, None, obj

    return False, "objective_not_found", None


def _load_active_binding(
    *,
    binding_registry_path: Path | None,
    job_id: str,
    actor_id: str,
    session_key: str,
    fallback_binding_id: str,
) -> tuple[dict[str, Any], str]:
    """Return active binding object and provenance.

    Enforces lifecycle semantics:
    - status must be `active`
    - revoked/expired records are not valid authority
    """
    fallback = {
        "binding_id": fallback_binding_id,
        "job_id": job_id,
        "actor_id": actor_id,
        "session_key": session_key,
        "status": "active",
        "binding_epoch": 0,
    }

    if binding_registry_path is None or not binding_registry_path.exists():
        return fallback, "fallback_from_cli"

    try:
        payload = json.loads(binding_registry_path.read_text(encoding="utf-8"))
    except Exception:
        return fallback, "fallback_invalid_registry"

    bindings = payload.get("bindings", [])
    if not isinstance(bindings, list):
        return fallback, "fallback_invalid_registry"

    now = datetime.now(timezone.utc)

    def lifecycle_status(b: dict[str, Any]) -> str:
        status = str(b.get("status", "active"))
        if status == "revoked":
            return "revoked"
        expires_at = b.get("expires_at")
        if isinstance(expires_at, str) and expires_at.strip():
            try:
                exp = datetime.fromisoformat(expires_at.replace("Z", "+00:00"))
                if exp <= now:
                    return "expired"
            except Exception:
                return "invalid_expiry"
        return status

    # strict resolution for exact runtime context first
    for b in bindings:
        if not isinstance(b, dict):
            continue
        if b.get("job_id") != job_id or b.get("actor_id") != actor_id or b.get("session_key") != session_key:
            continue
        life = lifecycle_status(b)
        if life == "active":
            return b, "registry_exact"
        return b, f"registry_exact_{life}"

    # then by job + actor if session rotated
    for b in bindings:
        if not isinstance(b, dict):
            continue
        if b.get("job_id") != job_id or b.get("actor_id") != actor_id:
            continue
        life = lifecycle_status(b)
        if life == "active":
            return b, "registry_job_actor"
        return b, f"registry_job_actor_{life}"

    return fallback, "fallback_not_found"


def _validate_binding_integrity(
    *,
    active_binding: dict[str, Any],
    envelope: dict[str, Any],
    actor_id: str,
    session_key: str,
) -> tuple[bool, str | None, bool]:
    """Validate envelope against active binding object.

    Returns: (ok, reason, reauth_required)
    """
    expected_binding_id = str(active_binding.get("binding_id", "")).strip()
    expected_job_id = str(active_binding.get("job_id", "")).strip()
    expected_actor_id = str(active_binding.get("actor_id", "")).strip()
    expected_session_key = str(active_binding.get("session_key", "")).strip()

    if not expected_binding_id or not expected_job_id or not expected_actor_id:
        return False, "binding_registry_invalid_active_record", False

    if envelope.get("job_id") != expected_job_id:
        return False, "binding_job_mismatch", True

    if envelope.get("binding_id") != expected_binding_id:
        return False, "REAUTH_REQUIRED_ON_BINDING_CHANGE", True

    if actor_id != expected_actor_id:
        return False, "binding_actor_mismatch", True

    if expected_session_key and session_key != expected_session_key:
        return False, "REAUTH_REQUIRED_ON_BINDING_CHANGE", True

    return True, None, False


def _atomic_write_text(path: Path, content: str) -> None:
    with tempfile.NamedTemporaryFile("w", encoding="utf-8", dir=str(path.parent), delete=False) as tmp:
        tmp.write(content)
        tmp.flush()
        os.fsync(tmp.fileno())
        temp_name = tmp.name
    os.replace(temp_name, path)


def _apply_low_risk_writeback(tasks_path: Path, claimed_ids: list[str], tick_id: str) -> dict[str, Any]:
    """Low-risk canonical write-back: move claimed tasks from Active -> Waiting with audit suffix.

    Idempotency rule: if a claimed task no longer exists in Active, do not duplicate in Waiting.
    """
    if not tasks_path.exists() or not claimed_ids:
        return {"applied": False, "reason": "no_tasks_or_no_claims", "moved": []}

    lock_path = tasks_path.with_suffix(tasks_path.suffix + ".lock")
    lock_path.parent.mkdir(parents=True, exist_ok=True)
    with lock_path.open("a+", encoding="utf-8") as lock_file:
        acquired = False
        deadline = time.time() + 5.0
        while time.time() < deadline:
            try:
                fcntl.flock(lock_file.fileno(), fcntl.LOCK_EX | fcntl.LOCK_NB)
                acquired = True
                break
            except BlockingIOError:
                time.sleep(0.05)

        if not acquired:
            return {"applied": False, "reason": "write_lock_timeout", "moved": []}

        try:
            lines = tasks_path.read_text(encoding="utf-8").splitlines()
            sec = None
            active_idx: dict[str, int] = {}

            for i, raw in enumerate(lines):
                if raw.startswith('## '):
                    sec = raw.strip()
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

            waiting_lines = []
            for _, original in moved:
                line = original
                if f"[tick:{tick_id}]" not in line:
                    line = f"{line} [tick:{tick_id}]"
                waiting_lines.append(line)

            compact = [ln for ln in lines if ln is not None]

            insert_at = None
            for i, raw in enumerate(compact):
                if raw.strip() == '## Waiting':
                    insert_at = i + 1
                    break

            if insert_at is None:
                compact.extend(['', '## Waiting'])
                insert_at = len(compact)

            compact[insert_at:insert_at] = waiting_lines
            _atomic_write_text(tasks_path, "\n".join(compact) + "\n")
        finally:
            fcntl.flock(lock_file.fileno(), fcntl.LOCK_UN)

    return {
        "applied": True,
        "reason": None,
        "moved": [m[0] for m in moved],
        "targetSection": "Waiting",
    }


def _shadow_state_sync(tasks_path: Path, db_path: Path, tick_id: str, artifact: dict[str, Any]) -> dict[str, Any]:
    conn = state_connect(db_path)
    state_init_schema(conn)
    imported = state_import_tasks(conn, tasks_path)
    parity = state_parity_check(conn, tasks_path)
    ledger = state_record_shadow_tick(conn, tick_id, artifact)
    return {
        "enabled": True,
        "db_path": str(db_path),
        "imported": imported,
        "parity": parity,
        "ledger": ledger,
        "status": "ok" if parity.get("match") else "mismatch",
    }


def _shadow_state_evaluate_threshold(status: str, alert_path: Path | None, threshold: int) -> dict[str, Any]:
    if alert_path is None:
        return {"threshold_exceeded": False, "consecutive_failures": 0}

    alert_path.parent.mkdir(parents=True, exist_ok=True)
    existing: list[dict[str, Any]] = []
    if alert_path.exists():
        for line in alert_path.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if not line:
                continue
            try:
                existing.append(json.loads(line))
            except Exception:
                continue

    existing.append({"timestamp": _iso_now(), "status": status})
    alert_path.write_text("\n".join(json.dumps(x) for x in existing) + "\n", encoding="utf-8")

    consecutive = 0
    for row in reversed(existing):
        if row.get("status") in {"mismatch", "error"}:
            consecutive += 1
        else:
            break

    return {
        "threshold_exceeded": consecutive >= max(1, threshold),
        "consecutive_failures": consecutive,
        "alert_path": str(alert_path),
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
    objective_id: str,
    objective_checkpoint: str,
    rationale_trace: str,
    tasks_path: Path,
    artifact_path: Path,
    writeback_tasks_path: Path | None = None,
    binding_registry_path: Path | None = None,
    objective_registry_path: Path | None = None,
    canonical_store: str = "markdown",
    canonical_db_path: Path | None = None,
    shadow_state_enabled: bool = False,
    shadow_state_db_path: Path | None = None,
    shadow_state_alert_path: Path | None = None,
    shadow_state_mismatch_threshold: int = 3,
) -> dict[str, Any]:
    kernel = TDEKernel()
    canonical_conn = None
    chaining = {"enabled": canonical_store == "db", "promoted": [], "skipped": [], "applied": {"applied": 0, "task_ids": []}}
    if canonical_store == "db":
        canonical_db = canonical_db_path or Path("os/runtime/tde_state.sqlite")
        canonical_conn = state_connect(canonical_db)
        state_init_schema(canonical_conn)
        all_tasks = state_read_tasks(canonical_conn)
        chaining_eval = evaluate_ready_promotions(all_tasks, tick_id=tick_id)
        chaining["promoted"] = chaining_eval.get("promoted", [])
        chaining["skipped"] = chaining_eval.get("skipped", [])
        chaining["applied"] = state_apply_ready_promotions(canonical_conn, chaining["promoted"])
        all_tasks = state_read_tasks(canonical_conn)
        tasks = [
            {
                "id": row["task_id"],
                "title": row["title"],
                "state": "ready" if row["status"] == "Active" else row["status"].lower(),
                "metadata": row.get("metadata") or {},
            }
            for row in all_tasks if row["status"] == "Active"
        ]
    else:
        tasks = _read_tasks(tasks_path, section="Active")
    objective_linkage = {
        "objective_id": objective_id,
        "objective_checkpoint": objective_checkpoint,
        "rationale_trace": rationale_trace,
    }

    outcomes = {
        "progressed": 0,
        "blocked_pending_approval": 0,
        "failed_validation": 0,
        "no_work": 0,
        "reauth_required": 0,
    }

    active_binding, binding_source = _load_active_binding(
        binding_registry_path=binding_registry_path,
        job_id=job_id,
        actor_id=actor_id,
        session_key=session_key,
        fallback_binding_id=binding_id,
    )
    objective_registry = _load_objective_registry(objective_registry_path)

    if not job_id.strip() or not actor_id.strip() or not session_key.strip() or not tick_id.strip():
        outcomes["failed_validation"] += 1
        artifact = {
            "artifactType": "tde_job_tick",
            "schemaVersion": "1.0.0",
            "tick_id": tick_id,
            "trigger_source": trigger_source,
            "timestamp": _iso_now(),
            "job_id": job_id,
            "binding_id": binding_id,
            "actor_id": actor_id,
            "session_key": session_key,
            "objective_linkage": objective_linkage,
            "binding_context": {
                "active_binding": active_binding,
                "binding_source": binding_source,
                "binding_status": "invalid_identity",
            },
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
            "artifactType": "tde_job_tick",
            "schemaVersion": "1.0.0",
            "tick_id": tick_id,
            "trigger_source": trigger_source,
            "timestamp": _iso_now(),
            "job_id": job_id,
            "binding_id": binding_id,
            "actor_id": actor_id,
            "session_key": session_key,
            "objective_linkage": objective_linkage,
            "binding_context": {
                "active_binding": active_binding,
                "binding_source": binding_source,
                "binding_status": "binding_missing",
            },
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
        objective_ok, objective_error = _validate_objective_linkage(objective_linkage)
        objective_registry_ok = False
        objective_registry_error: str | None = None
        matched_objective: dict[str, Any] | None = None
        if objective_ok:
            objective_registry_ok, objective_registry_error, matched_objective = _validate_objective_against_registry(
                objective_linkage, objective_registry
            )

        if not objective_ok or not objective_registry_ok:
            outcomes["failed_validation"] += 1
            artifact = {
                "artifactType": "tde_job_tick",
                "schemaVersion": "1.0.0",
                "tick_id": tick_id,
                "trigger_source": trigger_source,
                "timestamp": _iso_now(),
                "job_id": job_id,
                "binding_id": binding_id,
                "actor_id": actor_id,
                "session_key": session_key,
                "objective_linkage": objective_linkage,
                "objective_registry_context": {
                    "registry_path": str(objective_registry_path) if objective_registry_path else None,
                    "registry_loaded": objective_registry is not None,
                    "matched_objective": matched_objective,
                },
                "binding_context": {
                    "active_binding": active_binding,
                    "binding_source": binding_source,
                    "binding_status": "active",
                },
                "claim_limit": max_claim,
                "claimed": [],
                "mutations": [],
                "decisions": [],
                "evidence_outputs": [],
                "outcomes": outcomes,
                "status": "failed_validation",
                "fail_closed": True,
                "fail_closed_reason": objective_error or objective_registry_error,
            }
            artifact_path.parent.mkdir(parents=True, exist_ok=True)
            artifact_path.write_text(json.dumps(artifact, indent=2) + "\n", encoding="utf-8")
            return artifact

        ready = [t for t in tasks if t.get("state") == "ready"]
        claimed = ready[: max(0, max_claim)]

        binding_proven = binding_source in {"registry_exact", "registry_job_actor"}
        if claimed and not binding_proven:
            outcomes["failed_validation"] += len(claimed)
            artifact = {
                "artifactType": "tde_job_tick",
                "schemaVersion": "1.0.0",
                "tick_id": tick_id,
                "trigger_source": trigger_source,
                "timestamp": _iso_now(),
                "job_id": job_id,
                "binding_id": binding_id,
                "actor_id": actor_id,
                "session_key": session_key,
                "objective_linkage": objective_linkage,
                "binding_context": {
                    "active_binding": active_binding,
                    "binding_source": binding_source,
                    "binding_status": "unproven",
                },
                "claim_limit": max_claim,
                "claimed": [c["id"] for c in claimed],
                "mutations": [
                    {
                        "task_id": c["id"],
                        "status": "failed_validation",
                        "fail_closed": True,
                        "fail_closed_reason": "binding_unresolved_fail_closed",
                        "required_on_retry": {
                            "binding_registry_resolution": True,
                            "fresh_policy_decision_id": True,
                            "fresh_idempotency_key": True,
                        },
                    }
                    for c in claimed
                ],
                "idempotency_references": [],
                "writeback": {"applied": False, "reason": "binding_unresolved_fail_closed", "moved": []},
                "decisions": [
                    {
                        "type": "decision_required",
                        "reason": "binding_unresolved_fail_closed",
                    }
                ],
                "evidence_outputs": [str(artifact_path)],
                "outcomes": outcomes,
                "status": "failed_validation",
                "fail_closed": True,
                "fail_closed_reason": "binding_unresolved_fail_closed",
            }
            artifact_path.parent.mkdir(parents=True, exist_ok=True)
            artifact_path.write_text(json.dumps(artifact, indent=2) + "\n", encoding="utf-8")
            return artifact

        mutations: list[dict[str, Any]] = []
        idempotency_refs: list[str] = []
        workspace_root = Path.cwd()

        for index, item in enumerate(claimed):
            idempotency_key = f"{tick_id}:{item['id']}"
            idempotency_refs.append(idempotency_key)

            policy_binding = validate_task_policy_binding(
                item.get("metadata") or {},
                workspace_root=workspace_root,
                expected_outcome="continue",
            ) if canonical_store == "db" and (item.get("metadata") or {}).get("workflow_family") else {"ok": True}
            if not policy_binding.get("ok", False):
                outcomes["failed_validation"] += 1
                mutations.append(
                    {
                        "task_id": item["id"],
                        "request_id": f"{tick_id}-{index}",
                        "idempotency_key": idempotency_key,
                        "status": "failed_validation",
                        "fail_closed": True,
                        "fail_closed_reason": policy_binding.get("reason"),
                        "decision_policy": {
                            "policy_ref": policy_binding.get("policy_ref"),
                            "resolved_path": policy_binding.get("resolved_path"),
                            "workflow_family": policy_binding.get("workflow_family"),
                            "expected_outcome": "continue",
                        },
                    }
                )
                continue

            mutation_envelope = {
                "job_id": job_id,
                "binding_id": binding_id,
                "policy_decision_id": f"pending:{tick_id}:{item['id']}",
                "idempotency_key": idempotency_key,
                "expected_version": 0,
                "objective_linkage": objective_linkage,
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

            binding_ok, binding_error, reauth_required = _validate_binding_integrity(
                active_binding=active_binding,
                envelope=mutation_envelope,
                actor_id=actor_id,
                session_key=session_key,
            )
            if not binding_ok:
                if reauth_required:
                    outcomes["reauth_required"] += 1
                    status = "reauth_required"
                else:
                    outcomes["failed_validation"] += 1
                    status = "failed_validation"
                mutations.append(
                    {
                        "task_id": item["id"],
                        "request_id": f"{tick_id}-{index}",
                        "idempotency_key": idempotency_key,
                        "status": status,
                        "fail_closed": True,
                        "fail_closed_reason": binding_error,
                        "binding_status": "mismatch",
                        "required_on_retry": {
                            "fresh_policy_decision_id": True,
                            "fresh_idempotency_key": True,
                        },
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
                    "binding_status": "active",
                    "decision_policy": {
                        "policy_ref": policy_binding.get("policy_ref"),
                        "resolved_path": policy_binding.get("resolved_path"),
                        "workflow_family": policy_binding.get("workflow_family"),
                        "expected_outcome": "continue",
                    },
                    "mutation_envelope": {
                        **mutation_envelope,
                        "policy_decision_id": result.get("policy_decision_id"),
                    },
                }
            )

        executable_claims = [m["task_id"] for m in mutations if m.get("status") in {"executed", "replay"}]
        if canonical_store == "db":
            writeback = state_apply_low_risk_writeback_db(canonical_conn, executable_claims, tick_id)
            state_export_tasks(canonical_conn, writeback_tasks_path or tasks_path)
        else:
            writeback = _apply_low_risk_writeback(writeback_tasks_path or tasks_path, executable_claims, tick_id)

        if not claimed:
            outcomes["no_work"] += 1

        binding_status = "active" if all(m.get("binding_status") != "mismatch" for m in mutations) else "mismatch"
        artifact = {
            "artifactType": "tde_job_tick",
            "schemaVersion": "1.0.0",
            "tick_id": tick_id,
            "trigger_source": trigger_source,
            "timestamp": _iso_now(),
            "job_id": job_id,
            "binding_id": binding_id,
            "actor_id": actor_id,
            "session_key": session_key,
            "objective_linkage": objective_linkage,
            "objective_registry_context": {
                "registry_path": str(objective_registry_path) if objective_registry_path else None,
                "registry_loaded": objective_registry is not None,
            },
            "binding_context": {
                "active_binding": active_binding,
                "binding_source": binding_source,
                "binding_status": binding_status,
            },
            "claim_limit": max_claim,
            "claimed": [c["id"] for c in claimed],
            "mutations": mutations,
            "idempotency_references": idempotency_refs,
            "writeback": writeback,
            "decisions": [],
            "evidence_outputs": [str(artifact_path)],
            "outcomes": outcomes,
            "status": "ok",
            "chaining": chaining,
            "fail_closed": any(m.get("fail_closed") for m in mutations),
            "fail_closed_reason": next((m.get("fail_closed_reason") for m in mutations if m.get("fail_closed_reason")), None),
        }

    if shadow_state_enabled:
        try:
            shadow_db = shadow_state_db_path or Path("os/runtime/tde_state.sqlite")
            shadow_source = writeback_tasks_path or tasks_path
            shadow = _shadow_state_sync(shadow_source, shadow_db, tick_id, artifact)
            threshold_meta = _shadow_state_evaluate_threshold(
                shadow.get("status", "error"),
                shadow_state_alert_path,
                shadow_state_mismatch_threshold,
            )
            shadow.update(threshold_meta)
            artifact["shadow_state"] = shadow
        except Exception as exc:
            threshold_meta = _shadow_state_evaluate_threshold("error", shadow_state_alert_path, shadow_state_mismatch_threshold)
            artifact["shadow_state"] = {
                "enabled": True,
                "status": "error",
                "error": str(exc),
                **threshold_meta,
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
    parser.add_argument("--objective-id", default="OBJ-TDE-FOUNDATION")
    parser.add_argument("--objective-checkpoint", default="S16")
    parser.add_argument("--rationale-trace", default="TDE-2026-027-objective-linkage")
    parser.add_argument("--tasks-path", default="TASKS.md")
    parser.add_argument(
        "--artifact-path",
        default="knowledge/evidence/2026-03/tde-job-tick-latest.json",
    )
    parser.add_argument("--writeback-tasks-path", default="TASKS.md")
    parser.add_argument("--binding-registry-path", default="os/runtime/tde_active_bindings.json")
    parser.add_argument("--objective-registry-path", default="os/runtime/tde_objectives.json")
    parser.add_argument("--canonical-store", choices=["markdown", "db"], default="markdown")
    parser.add_argument("--canonical-db-path", default="os/runtime/tde_state.sqlite")
    parser.add_argument("--shadow-state-enabled", action="store_true")
    parser.add_argument("--shadow-state-db-path", default="os/runtime/tde_state.sqlite")
    parser.add_argument("--shadow-state-alert-path", default="knowledge/evidence/metrics/tde-shadow-state-alerts.jsonl")
    parser.add_argument("--shadow-state-mismatch-threshold", type=int, default=3)

    args = parser.parse_args()
    artifact = run_job_tick(
        job_id=args.job_id,
        binding_id=args.binding_id,
        actor_id=args.actor_id,
        session_key=args.session_key,
        trigger_source=args.trigger_source,
        tick_id=args.tick_id,
        max_claim=args.max_claim,
        objective_id=args.objective_id,
        objective_checkpoint=args.objective_checkpoint,
        rationale_trace=args.rationale_trace,
        tasks_path=Path(args.tasks_path),
        artifact_path=Path(args.artifact_path),
        writeback_tasks_path=Path(args.writeback_tasks_path) if args.writeback_tasks_path else None,
        binding_registry_path=Path(args.binding_registry_path) if args.binding_registry_path else None,
        objective_registry_path=Path(args.objective_registry_path) if args.objective_registry_path else None,
        canonical_store=args.canonical_store,
        canonical_db_path=Path(args.canonical_db_path) if args.canonical_db_path else None,
        shadow_state_enabled=args.shadow_state_enabled,
        shadow_state_db_path=Path(args.shadow_state_db_path) if args.shadow_state_db_path else None,
        shadow_state_alert_path=Path(args.shadow_state_alert_path) if args.shadow_state_alert_path else None,
        shadow_state_mismatch_threshold=args.shadow_state_mismatch_threshold,
    )
    print(json.dumps(artifact))


if __name__ == "__main__":
    main()
