#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


def _read_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def _decision(snapshot: dict[str, Any]) -> str:
    integrity = snapshot.get("integrity", {})
    return "GO" if integrity.get("status") == "ok" else "ESCALATE"


def _escalation_reasons(snapshot: dict[str, Any]) -> list[str]:
    integrity = snapshot.get("integrity", {}) if isinstance(snapshot.get("integrity"), dict) else {}
    reasons: list[str] = []

    missing = integrity.get("missingArtifacts") or []
    stale = integrity.get("staleArtifacts") or []
    guardrail = integrity.get("guardrailSignals") or []

    if missing:
        reasons.append(f"Missing artifacts: {', '.join(missing)}")
    if stale:
        reasons.append(f"Stale artifacts: {', '.join(stale)}")
    if guardrail:
        reasons.append(f"Guardrail signals: {', '.join(guardrail)}")
    if not reasons:
        reasons.append("No escalation needed; all integrity and guardrail checks are OK.")

    return reasons


def build_packet(
    snapshot: dict[str, Any],
    snapshot_path: Path,
    s4_status: dict[str, Any],
    s7_cycle: dict[str, Any],
) -> dict[str, Any]:
    now = datetime.now(timezone.utc).isoformat()
    decision = _decision(snapshot)
    escalation_reasons = _escalation_reasons(snapshot)

    s4_guardrail = s4_status.get("guardrail", {}) if isinstance(s4_status.get("guardrail"), dict) else {}
    s7_guardrail = (
        s7_cycle.get("guardrailEvaluation", {}) if isinstance(s7_cycle.get("guardrailEvaluation"), dict) else {}
    )

    return {
        "generatedAt": now,
        "packetType": "owner_gate_packet",
        "decision": decision,
        "sourceSnapshot": str(snapshot_path),
        "integrity": snapshot.get("integrity", {}),
        "statusSnapshot": snapshot.get("statusSnapshot", {}),
        "guardrailOutputs": {
            "s4": {
                "status": s4_guardrail.get("status"),
                "violations": s4_guardrail.get("violations", []),
                "requiresApproval": s4_guardrail.get("requiresApproval", True),
            },
            "s7": {
                "status": s7_guardrail.get("status"),
                "signals": s7_guardrail.get("signals", []),
            },
        },
        "escalation": {
            "required": decision != "GO",
            "reasons": escalation_reasons,
            "ownerAction": (
                "Escalate to JOB-OWN-001 + JOB-ARC-001 for disposition; hold rollout actions fail-closed until resolved."
                if decision != "GO"
                else "No escalation action required."
            ),
        },
    }


def _to_markdown(packet: dict[str, Any]) -> str:
    integrity = packet.get("integrity", {})
    s7 = packet.get("statusSnapshot", {}).get("s7", {})
    lines = [
        "# TDE Owner Gate Packet",
        "",
        f"- Generated at: `{packet.get('generatedAt')}`",
        f"- Decision: **{packet.get('decision')}**",
        f"- Source snapshot: `{packet.get('sourceSnapshot')}`",
        f"- Integrity status: `{integrity.get('status')}`",
        "",
        "## Operational Snapshot",
        f"- S7 decision candidate: `{s7.get('decision')}`",
        f"- S7 stalled ratio: `{s7.get('stalledRatio')}`",
        f"- S7 guardrail status: `{s7.get('guardrailStatus')}`",
        "",
        "## Escalation",
        f"- Required: `{packet.get('escalation', {}).get('required')}`",
    ]

    for reason in packet.get("escalation", {}).get("reasons", []):
        lines.append(f"- Reason: {reason}")

    lines.extend(
        [
            f"- Owner action: {packet.get('escalation', {}).get('ownerAction')}",
            "",
            "## Guardrail Outputs",
            "```json",
            json.dumps(packet.get("guardrailOutputs", {}), indent=2),
            "```",
            "",
        ]
    )
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate owner-facing TDE gate packet from latest milestone snapshot")
    parser.add_argument("--snapshot-path", default="knowledge/evidence/2026-03/tde-milestone-s4-s7-snapshot.json")
    parser.add_argument("--s4-status-path", default="knowledge/evidence/2026-03/tde-canary-status-latest.json")
    parser.add_argument("--s7-cycle-path", default="knowledge/evidence/2026-03/tde-broader-scope-simulated-cycle.json")
    parser.add_argument("--output-json", default="knowledge/evidence/2026-03/tde-owner-gate-packet.json")
    parser.add_argument("--output-md", default="knowledge/evidence/2026-03/tde-owner-gate-packet.md")
    args = parser.parse_args()

    snapshot_path = Path(args.snapshot_path)
    snapshot = _read_json(snapshot_path)
    s4_status = _read_json(Path(args.s4_status_path))
    s7_cycle = _read_json(Path(args.s7_cycle_path))

    packet = build_packet(snapshot, snapshot_path, s4_status=s4_status, s7_cycle=s7_cycle)

    json_path = Path(args.output_json)
    md_path = Path(args.output_md)
    json_path.parent.mkdir(parents=True, exist_ok=True)
    json_path.write_text(json.dumps(packet, indent=2) + "\n", encoding="utf-8")
    md_path.write_text(_to_markdown(packet), encoding="utf-8")

    print(
        json.dumps(
            {
                "packetPath": str(json_path),
                "packetMarkdownPath": str(md_path),
                "decision": packet["decision"],
                "escalationRequired": packet["escalation"]["required"],
            }
        )
    )


if __name__ == "__main__":
    main()
