#!/usr/bin/env python3
from __future__ import annotations

import argparse
import glob
import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


def _read_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def _resolve_latest_envelope(explicit_path: str | None, pattern: str) -> Path:
    if explicit_path:
        candidate = Path(explicit_path)
        if not candidate.exists():
            raise FileNotFoundError(f"Envelope not found: {candidate}")
        return candidate

    matches = [Path(p) for p in glob.glob(pattern)]
    matches = [p for p in matches if p.is_file()]
    if not matches:
        raise FileNotFoundError(f"No release envelope matched: {pattern}")
    return max(matches, key=lambda p: p.stat().st_mtime)


def _deterministic_receipt_id(receipt_core: dict[str, Any]) -> str:
    canonical = json.dumps(receipt_core, sort_keys=True, separators=(",", ":"))
    digest = hashlib.sha256(canonical.encode("utf-8")).hexdigest()[:16]
    return f"actrcpt-{digest}"


def build_receipt(envelope: dict[str, Any], envelope_path: Path) -> dict[str, Any]:
    envelope_id = envelope.get("envelopeId") or "env-unknown"
    release_decision = envelope.get("releaseDecision")
    guard = envelope.get("activationGuard", {}) if isinstance(envelope.get("activationGuard"), dict) else {}

    guard_state = {
        "status": guard.get("status"),
        "handoffAllowed": bool(guard.get("handoffAllowed")),
        "escalationDetected": bool(guard.get("escalationDetected")),
        "escalationReasons": guard.get("escalationReasons", []),
        "blockOnEscalation": bool(guard.get("blockOnEscalation")),
        "failClosed": bool((guard.get("policy") or {}).get("failClosed")),
    }

    decision_trace = {
        "decision": "GO" if release_decision == "READY_FOR_HANDOFF" else "BLOCKED",
        "decisionSource": release_decision,
        "rationale": (
            "Activation handoff executed under deterministic pass guard."
            if guard_state["handoffAllowed"]
            else "Activation blocked by deterministic fail-closed guard due to escalation."
        ),
        "guardState": guard_state,
    }

    execution = {
        "executed": guard_state["handoffAllowed"],
        "route": (
            "handoff_to_JOB-PROD-001_and_JOB-ARC-001"
            if guard_state["handoffAllowed"]
            else "hold_fail_closed"
        ),
        "nextAction": (
            "Proceed with pre-authorized rollout handoff package."
            if guard_state["handoffAllowed"]
            else "Escalate evidence packet; activation remains blocked until escalation is cleared."
        ),
    }

    receipt_core = {
        "artifactType": "tde_activation_execution_receipt",
        "releaseEnvelopeRef": {
            "envelopeId": envelope_id,
            "path": str(envelope_path),
        },
        "decisionTrace": decision_trace,
        "execution": execution,
        "policy": {
            "preAuthorizationModel": "owner pre-authorization for escalation only; no approval bypass",
            "failClosed": True,
        },
    }

    return {
        "generatedAt": datetime.now(timezone.utc).isoformat(),
        "receiptId": _deterministic_receipt_id(receipt_core),
        **receipt_core,
    }


def _to_markdown(receipt: dict[str, Any]) -> str:
    trace = receipt.get("decisionTrace", {})
    guard = trace.get("guardState", {})
    execution = receipt.get("execution", {})
    return "\n".join(
        [
            "# TDE Activation Execution Receipt",
            "",
            f"- Generated at: `{receipt.get('generatedAt')}`",
            f"- Receipt ID: `{receipt.get('receiptId')}`",
            f"- Linked envelope ID: `{receipt.get('releaseEnvelopeRef', {}).get('envelopeId')}`",
            f"- Linked envelope path: `{receipt.get('releaseEnvelopeRef', {}).get('path')}`",
            "",
            "## Decision Trace",
            f"- Decision: **{trace.get('decision')}**",
            f"- Decision source: `{trace.get('decisionSource')}`",
            f"- Rationale: {trace.get('rationale')}",
            "",
            "## Guard State",
            f"- status: `{guard.get('status')}`",
            f"- handoffAllowed: `{guard.get('handoffAllowed')}`",
            f"- escalationDetected: `{guard.get('escalationDetected')}`",
            f"- blockOnEscalation: `{guard.get('blockOnEscalation')}`",
            f"- failClosed: `{guard.get('failClosed')}`",
            *[f"- escalationReason: {reason}" for reason in guard.get("escalationReasons", [])],
            "",
            "## Execution Result",
            f"- executed: `{execution.get('executed')}`",
            f"- route: `{execution.get('route')}`",
            f"- nextAction: {execution.get('nextAction')}",
            "",
        ]
    )


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate deterministic activation execution receipt from latest release envelope")
    parser.add_argument("--envelope-path", default=None, help="Explicit envelope JSON path; if omitted, latest matching file is used")
    parser.add_argument("--envelope-glob", default="knowledge/evidence/2026-03/tde-release-envelope-*.json")
    parser.add_argument("--output-json", default="knowledge/evidence/2026-03/tde-activation-execution-receipt.json")
    parser.add_argument("--output-md", default="knowledge/evidence/2026-03/tde-activation-execution-receipt.md")
    args = parser.parse_args()

    envelope_path = _resolve_latest_envelope(args.envelope_path, args.envelope_glob)
    envelope = _read_json(envelope_path)
    receipt = build_receipt(envelope, envelope_path)

    out_json = Path(args.output_json)
    out_md = Path(args.output_md)
    out_json.parent.mkdir(parents=True, exist_ok=True)
    out_json.write_text(json.dumps(receipt, indent=2) + "\n", encoding="utf-8")
    out_md.write_text(_to_markdown(receipt), encoding="utf-8")

    print(
        json.dumps(
            {
                "activationReceiptPath": str(out_json),
                "activationReceiptMarkdownPath": str(out_md),
                "receiptId": receipt["receiptId"],
                "envelopeId": receipt["releaseEnvelopeRef"]["envelopeId"],
                "decision": receipt["decisionTrace"]["decision"],
                "executed": receipt["execution"]["executed"],
            }
        )
    )


if __name__ == "__main__":
    main()
