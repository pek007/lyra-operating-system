#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from tde_formation_creator import create_from_formation


def _slug(text: str) -> str:
    chars = [c if c.isalnum() else '-' for c in text.upper()]
    out = ''.join(chars)
    while '--' in out:
        out = out.replace('--', '-')
    return out.strip('-')[:40] or 'REQUEST'


def _base_record(*, source_ref: str, request_text: str) -> dict[str, Any]:
    now = datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace('+00:00', 'Z')
    return {
        "artifactType": "tde_intent_formation_record",
        "schemaVersion": "1.0.0",
        "formation_id": f"FORM-{_slug(source_ref)}",
        "source_type": "chat_request",
        "source_ref": source_ref,
        "formed_at": now,
        "formed_by_role": "Product Owner",
        "formation_rationale": request_text,
    }


def form_basic_gui_request(*, request_text: str, source_ref: str) -> dict[str, Any]:
    base = _base_record(source_ref=source_ref, request_text=request_text)
    return {
        **base,
        "interpreted_intent": "Create a first basic internal TDE GUI with a bounded, read-heavy scope.",
        "request_type": "implementation_request",
        "specificity_level": "medium",
        "ambiguity_types": ["missing_scope", "missing_quality_bar"],
        "actionability_status": "executable_with_assumptions",
        "assumptions": [
            "The first version is an internal operator interface.",
            "The first version is read-heavy rather than fully editable.",
            "The GUI should read DB-canonical state and be validated in staging first."
        ],
        "known_unknowns": ["Which operator actions should be allowed in v1."],
        "proposed_objective": {
            "objective_title": "Create first basic TDE GUI",
            "objective_summary": "Create a bounded first GUI attempt for TDE using DB-canonical state and staging-first validation.",
            "objective_id": None
        },
        "proposed_success_criteria": ["A first bounded GUI workflow exists and is testable in staging."],
        "proposed_workflow_family": "implementation_verification_readiness",
        "proposed_first_stage_set": ["implementation", "verification", "readiness-review"],
        "proposed_first_task_set": [
            {"task_id": None, "task_title": "Define first bounded TDE GUI scope", "task_summary": "Define the minimum read-heavy operator GUI scope for the first attempt.", "stage_id": "implementation"},
            {"task_id": None, "task_title": "Verify first TDE GUI scope and constraints", "task_summary": "Verify that the proposed first GUI scope is coherent, safe, and aligned with DB-canonical state.", "stage_id": "verification"}
        ],
        "required_clarifications": [],
        "recommended_next_action": "proceed_with_assumptions",
        "formation_rationale": f"A useful first GUI work system can be formed from the request under explicit assumptions. Original request: {request_text}",
    }


def form_internal_tool_request(*, request_text: str, source_ref: str) -> dict[str, Any]:
    base = _base_record(source_ref=source_ref, request_text=request_text)
    return {
        **base,
        "interpreted_intent": "Create a bounded internal tool with a staging-first, implementation/verification flow.",
        "request_type": "implementation_request",
        "specificity_level": "medium",
        "ambiguity_types": ["missing_scope", "missing_success_criteria"],
        "actionability_status": "executable_with_assumptions",
        "assumptions": [
            "The first version is internal-only.",
            "The first version should be bounded and testable in staging."
        ],
        "known_unknowns": ["Precise feature scope for v1."],
        "proposed_objective": {
            "objective_title": "Create first bounded internal tool",
            "objective_summary": "Create a first bounded internal tool using a staging-first delivery path.",
            "objective_id": None
        },
        "proposed_success_criteria": ["A bounded internal tool workflow exists and is testable in staging."],
        "proposed_workflow_family": "implementation_verification_readiness",
        "proposed_first_stage_set": ["implementation", "verification", "readiness-review"],
        "proposed_first_task_set": [
            {"task_id": None, "task_title": "Define first bounded internal tool scope", "task_summary": "Define the minimum viable scope for the internal tool.", "stage_id": "implementation"},
            {"task_id": None, "task_title": "Verify first internal tool scope and constraints", "task_summary": "Verify that the proposed scope is coherent, safe, and staged correctly.", "stage_id": "verification"}
        ],
        "required_clarifications": [],
        "recommended_next_action": "proceed_with_assumptions",
        "formation_rationale": f"A useful first internal tool work system can be formed under explicit assumptions. Original request: {request_text}",
    }


def form_runtime_hardening_request(*, request_text: str, source_ref: str) -> dict[str, Any]:
    base = _base_record(source_ref=source_ref, request_text=request_text)
    return {
        **base,
        "interpreted_intent": "Harden TDE/OpenClaw runtime behavior with bounded implementation, verification, and readiness steps.",
        "request_type": "implementation_request",
        "specificity_level": "medium",
        "ambiguity_types": ["missing_scope"],
        "actionability_status": "executable_with_assumptions",
        "assumptions": [
            "Hardening work should remain internal and staging-first.",
            "Changes should preserve promotion/rollback discipline."
        ],
        "known_unknowns": ["Exact hardening boundary for this request."],
        "proposed_objective": {
            "objective_title": "Harden TDE runtime behavior",
            "objective_summary": "Implement a bounded hardening slice for TDE/OpenClaw runtime behavior.",
            "objective_id": None
        },
        "proposed_success_criteria": ["A bounded runtime hardening slice is implemented and validated in staging."],
        "proposed_workflow_family": "implementation_verification_readiness",
        "proposed_first_stage_set": ["implementation", "verification", "readiness-review"],
        "proposed_first_task_set": [
            {"task_id": None, "task_title": "Define bounded runtime hardening scope", "task_summary": "Define the exact hardening slice to implement.", "stage_id": "implementation"},
            {"task_id": None, "task_title": "Verify runtime hardening scope and safety", "task_summary": "Verify that the hardening slice is safe and professionally controlled.", "stage_id": "verification"}
        ],
        "required_clarifications": [],
        "recommended_next_action": "proceed_with_assumptions",
        "formation_rationale": f"A bounded runtime hardening work system can be formed under explicit assumptions. Original request: {request_text}",
    }


def form_research_request(*, request_text: str, source_ref: str) -> dict[str, Any]:
    base = _base_record(source_ref=source_ref, request_text=request_text)
    return {
        **base,
        "interpreted_intent": "Conduct bounded research and produce a professionally useful first result.",
        "request_type": "research_request",
        "specificity_level": "medium",
        "ambiguity_types": ["missing_success_criteria"],
        "actionability_status": "executable_with_assumptions",
        "assumptions": ["The first output should be a bounded research result rather than a full implementation."],
        "known_unknowns": ["Exact depth required for the research result."],
        "proposed_objective": {
            "objective_title": "Conduct bounded research task",
            "objective_summary": "Run a bounded research slice and capture a professionally useful first result.",
            "objective_id": None
        },
        "proposed_success_criteria": ["A bounded research result is produced and can be reviewed."],
        "proposed_workflow_family": "implementation_verification_readiness",
        "proposed_first_stage_set": ["implementation", "verification"],
        "proposed_first_task_set": [
            {"task_id": None, "task_title": "Define research scope and question", "task_summary": "Define the bounded question and success criteria for the research task.", "stage_id": "implementation"},
            {"task_id": None, "task_title": "Verify research framing and output expectations", "task_summary": "Verify that the research framing is coherent and reviewable.", "stage_id": "verification"}
        ],
        "required_clarifications": [],
        "recommended_next_action": "proceed_with_assumptions",
        "formation_rationale": f"A bounded research work system can be formed under explicit assumptions. Original request: {request_text}",
    }


def form_review_audit_request(*, request_text: str, source_ref: str) -> dict[str, Any]:
    base = _base_record(source_ref=source_ref, request_text=request_text)
    return {
        **base,
        "interpreted_intent": "Conduct a bounded review/audit and return findings in a professional structure.",
        "request_type": "review_audit_request",
        "specificity_level": "medium",
        "ambiguity_types": ["missing_scope"],
        "actionability_status": "executable_with_assumptions",
        "assumptions": ["The first review/audit pass should be bounded and evidence-oriented."],
        "known_unknowns": ["The exact review depth expected in v1."],
        "proposed_objective": {
            "objective_title": "Conduct bounded review or audit",
            "objective_summary": "Run a bounded review/audit slice and capture findings clearly.",
            "objective_id": None
        },
        "proposed_success_criteria": ["A bounded review/audit result is produced with useful findings."],
        "proposed_workflow_family": "implementation_verification_readiness",
        "proposed_first_stage_set": ["implementation", "verification"],
        "proposed_first_task_set": [
            {"task_id": None, "task_title": "Define review/audit scope", "task_summary": "Define the bounded scope for the review or audit task.", "stage_id": "implementation"},
            {"task_id": None, "task_title": "Verify review/audit framing", "task_summary": "Verify that the review or audit framing is coherent and useful.", "stage_id": "verification"}
        ],
        "required_clarifications": [],
        "recommended_next_action": "proceed_with_assumptions",
        "formation_rationale": f"A bounded review/audit work system can be formed under explicit assumptions. Original request: {request_text}",
    }


REQUEST_CLASS_TABLE = {
    'basic_tde_gui': form_basic_gui_request,
    'internal_tool': form_internal_tool_request,
    'runtime_hardening': form_runtime_hardening_request,
    'research_request': form_research_request,
    'review_audit_request': form_review_audit_request,
}


def detect_request_class(request_text: str) -> str | None:
    text = request_text.lower()
    if 'gui' in text and 'tde' in text:
        return 'basic_tde_gui'
    if 'internal tool' in text or ('tool' in text and 'internal' in text):
        return 'internal_tool'
    if 'hardening' in text or ('runtime' in text and ('harden' in text or 'improve' in text)):
        return 'runtime_hardening'
    if 'audit' in text or 'review' in text:
        return 'review_audit_request'
    if 'research' in text or 'investigate' in text:
        return 'research_request'
    return None


def main() -> None:
    ap = argparse.ArgumentParser(description='Thin TDE intent intake for first real request classes')
    ap.add_argument('--request-text', required=True)
    ap.add_argument('--source-ref', required=True)
    ap.add_argument('--formation-out', required=True)
    ap.add_argument('--create-canonical', action='store_true')
    ap.add_argument('--db-path', default='os/runtime/staging/tde_state.sqlite')
    ap.add_argument('--objectives-path', default='os/runtime/staging/tde_objectives.json')
    ap.add_argument('--tasks-projection-path', default='os/runtime/staging/TASKS_from_db.md')
    args = ap.parse_args()

    request_class = detect_request_class(args.request_text)
    if request_class is None:
        raise SystemExit('unsupported_request_class')

    formation = REQUEST_CLASS_TABLE[request_class](request_text=args.request_text, source_ref=args.source_ref)
    out_path = Path(args.formation_out)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(formation, indent=2) + '\n', encoding='utf-8')

    result: dict[str, Any] = {
        'request_class': request_class,
        'formation_path': str(out_path),
        'formation_id': formation['formation_id'],
    }
    if args.create_canonical:
        result['canonical_creation'] = create_from_formation(
            formation_path=out_path,
            db_path=Path(args.db_path),
            objectives_path=Path(args.objectives_path),
            tasks_projection_path=Path(args.tasks_projection_path),
        )
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
