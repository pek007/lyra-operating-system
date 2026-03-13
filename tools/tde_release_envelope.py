#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


def _read_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def _derive_escalation(snapshot: dict[str, Any], owner_packet: dict[str, Any]) -> list[str]:
    integrity = snapshot.get("integrity", {}) if isinstance(snapshot.get("integrity"), dict) else {}
    reasons: list[str] = []

    missing = integrity.get("missingArtifacts") or []
    stale = integrity.get("staleArtifacts") or []
    guardrails = integrity.get("guardrailSignals") or []

    if missing:
        reasons.append(f"missing_artifacts:{','.join(missing)}")
    if stale:
        reasons.append(f"stale_artifacts:{','.join(stale)}")
    if guardrails:
        reasons.append(f"guardrail_signals:{','.join(guardrails)}")

    escalation = owner_packet.get("escalation", {}) if isinstance(owner_packet.get("escalation"), dict) else {}
    if escalation.get("required"):
        for reason in escalation.get("reasons", []):
            if isinstance(reason, str) and reason:
                reasons.append(f"owner_packet:{reason}")

    deduped: list[str] = []
    for item in reasons:
        if item not in deduped:
            deduped.append(item)
    return deduped


def _deterministic_envelope_id(payload: dict[str, Any]) -> str:
    canonical = json.dumps(payload, sort_keys=True, separators=(",", ":"))
    digest = hashlib.sha256(canonical.encode("utf-8")).hexdigest()[:16]
    return f"env-{digest}"


def build_release_envelope(
    snapshot: dict[str, Any],
    owner_packet: dict[str, Any],
    snapshot_path: Path,
    owner_packet_path: Path,
    forced_escalation_reason: str | None,
) -> dict[str, Any]:
    now = datetime.now(timezone.utc).isoformat()
    escalation_reasons = _derive_escalation(snapshot, owner_packet)
    if forced_escalation_reason:
        escalation_reasons.append(f"simulated:{forced_escalation_reason}")

    handoff_allowed = len(escalation_reasons) == 0
    activation_guard = {
        "status": "pass" if handoff_allowed else "blocked",
        "deterministic": True,
        "handoffAllowed": handoff_allowed,
        "blockOnEscalation": True,
        "escalationDetected": not handoff_allowed,
        "escalationReasons": escalation_reasons,
        "policy": {
            "preAuthorizationModel": "owner pre-authorization for escalation only; no approval bypass",
            "failClosed": True,
        },
    }

    envelope_core = {
        "artifactType": "tde_release_envelope",
        "schemaVersion": "1.0.0",
        "releaseDecision": "READY_FOR_HANDOFF" if handoff_allowed else "BLOCKED_ESCALATION",
        "sourceArtifacts": {
            "milestoneSnapshot": str(snapshot_path),
            "ownerGatePacket": str(owner_packet_path),
        },
        "statusSnapshot": snapshot.get("statusSnapshot", {}),
        "integrity": snapshot.get("integrity", {}),
        "ownerGatePacket": {
            "decision": owner_packet.get("decision"),
            "escalation": owner_packet.get("escalation", {}),
        },
        "activationGuard": activation_guard,
        "rolloutHandoff": {
            "eligible": handoff_allowed,
            "route": "handoff_to_JOB-PROD-001_and_JOB-ARC-001" if handoff_allowed else "hold_fail_closed",
            "nextAction": (
                "Proceed with pre-authorized rollout handoff package."
                if handoff_allowed
                else "Escalate evidence packet; no rollout handoff permitted until escalation is cleared."
            ),
        },
    }

    envelope = {
        "generatedAt": now,
        "envelopeId": _deterministic_envelope_id(envelope_core),
        **envelope_core,
    }
    return envelope


def _to_markdown(envelope: dict[str, Any]) -> str:
    guard = envelope.get("activationGuard", {})
    lines = [
        "# TDE Release Envelope",
        "",
        f"- Generated at: `{envelope.get('generatedAt')}`",
        f"- Envelope ID: `{envelope.get('envelopeId')}`",
        f"- Release decision: **{envelope.get('releaseDecision')}**",
        f"- Handoff eligible: `{envelope.get('rolloutHandoff', {}).get('eligible')}`",
        "",
        "## Deterministic Activation Guard",
        f"- Status: `{guard.get('status')}`",
        f"- blockOnEscalation: `{guard.get('blockOnEscalation')}`",
        f"- escalationDetected: `{guard.get('escalationDetected')}`",
    ]

    for reason in guard.get("escalationReasons", []):
        lines.append(f"- escalationReason: {reason}")

    lines.extend(
        [
            "",
            "## Rollout Handoff",
            f"- Route: `{envelope.get('rolloutHandoff', {}).get('route')}`",
            f"- Next action: {envelope.get('rolloutHandoff', {}).get('nextAction')}",
            "",
        ]
    )
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser(description="Build deterministic TDE release envelope with activation guard")
    parser.add_argument("--env", choices=["dev", "staging", "prod"], default=None)
    parser.add_argument("--snapshot-path", default=None)
    parser.add_argument("--owner-packet-path", default=None)
    parser.add_argument("--output-json", default=None)
    parser.add_argument("--output-md", default=None)
    parser.add_argument("--force-escalation-reason", default=None)
    args = parser.parse_args()

    if args.env:
        period = datetime.now(timezone.utc).strftime('%Y-%m')
        evidence_dir = Path(f"knowledge/evidence/{args.env}/{period}")
        snapshot_path = Path(args.snapshot_path) if args.snapshot_path else evidence_dir / "tde-milestone-s4-s7-snapshot.json"
        owner_packet_path = Path(args.owner_packet_path) if args.owner_packet_path else evidence_dir / "tde-owner-gate-packet.json"
        output_json = Path(args.output_json) if args.output_json else evidence_dir / "tde-release-envelope.json"
        output_md = Path(args.output_md) if args.output_md else evidence_dir / "tde-release-envelope.md"
    else:
        snapshot_path = Path(args.snapshot_path or "knowledge/evidence/2026-03/tde-milestone-s4-s7-snapshot.json")
        owner_packet_path = Path(args.owner_packet_path or "knowledge/evidence/2026-03/tde-owner-gate-packet.json")
        output_json = Path(args.output_json or "knowledge/evidence/2026-03/tde-release-envelope.json")
        output_md = Path(args.output_md or "knowledge/evidence/2026-03/tde-release-envelope.md")
    snapshot = _read_json(snapshot_path)
    owner_packet = _read_json(owner_packet_path)

    envelope = build_release_envelope(
        snapshot=snapshot,
        owner_packet=owner_packet,
        snapshot_path=snapshot_path,
        owner_packet_path=owner_packet_path,
        forced_escalation_reason=args.force_escalation_reason,
    )

    out_json = output_json
    out_md = output_md
    out_json.parent.mkdir(parents=True, exist_ok=True)
    out_json.write_text(json.dumps(envelope, indent=2) + "\n", encoding="utf-8")
    out_md.write_text(_to_markdown(envelope), encoding="utf-8")

    print(
        json.dumps(
            {
                "releaseEnvelopePath": str(out_json),
                "releaseEnvelopeMarkdownPath": str(out_md),
                "envelopeId": envelope["envelopeId"],
                "releaseDecision": envelope["releaseDecision"],
                "handoffEligible": envelope["rolloutHandoff"]["eligible"],
            }
        )
    )


if __name__ == "__main__":
    main()
