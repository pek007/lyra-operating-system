#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path
from typing import Any


def write_escalation_package(*, artifact_dir: Path, tick_id: str, task_id: str, objective_id: str | None, metadata: dict[str, Any], workflow_family: str | None) -> str:
    artifact_dir.mkdir(parents=True, exist_ok=True)
    path = artifact_dir / f"tde-decision-escalation-{task_id.lower()}-{tick_id}.json"
    payload: dict[str, Any] = {
        "artifactType": "tde_decision_escalation_package",
        "schemaVersion": "1.0.0",
        "decision_id": f"DEC-{tick_id}-{task_id}",
        "task_id": task_id,
        "objective_id": objective_id,
        "workflow_family": workflow_family or metadata.get("workflow_family") or "unknown",
        "from_role": "Product Owner",
        "to_role": "Ultimate Decision-maker",
        "decision_question": metadata.get("decision_question") or f"How should task {task_id} proceed?",
        "context_summary": metadata.get("decision_context_summary"),
        "options": metadata.get("decision_options") or [
            {
                "option_id": "opt_review",
                "label": "Review and decide",
                "impact_summary": "Requires Peter decision before continuation."
            }
        ],
        "recommended_option_id": metadata.get("decision_recommended_option_id") or "opt_review",
        "rationale": metadata.get("decision_rationale") or "Escalation requested because delegated authority was not sufficient for autonomous continuation.",
        "evidence_refs": metadata.get("decision_evidence_refs") or [],
        "confidence_score": metadata.get("decision_confidence_score", 0.5),
        "risks_tradeoffs": metadata.get("decision_risks_tradeoffs") or "Trade-offs require Ultimate Decision-maker review.",
        "consequence_of_delay": metadata.get("decision_consequence_of_delay") or "Chain remains paused pending decision.",
        "would_do_if_delegated": metadata.get("decision_would_do_if_delegated") or "Pause and escalate for decision.",
        "escalation_reason": metadata.get("decision_escalation_reason") or "delegated_authority_exceeded",
        "escalated_at": metadata.get("decision_escalated_at") or __import__('datetime').datetime.utcnow().replace(microsecond=0).isoformat() + 'Z',
    }
    path.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    return str(path)
