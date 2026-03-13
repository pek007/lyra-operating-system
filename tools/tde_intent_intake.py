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


def form_basic_gui_request(*, request_text: str, source_ref: str) -> dict[str, Any]:
    now = datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace('+00:00', 'Z')
    formation_id = f"FORM-{_slug(source_ref)}"
    return {
        "artifactType": "tde_intent_formation_record",
        "schemaVersion": "1.0.0",
        "formation_id": formation_id,
        "source_type": "chat_request",
        "source_ref": source_ref,
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
        "known_unknowns": [
            "Which operator actions should be allowed in v1."
        ],
        "proposed_objective": {
            "objective_title": "Create first basic TDE GUI",
            "objective_summary": "Create a bounded first GUI attempt for TDE using DB-canonical state and staging-first validation.",
            "objective_id": None
        },
        "proposed_success_criteria": [
            "A first bounded GUI workflow exists and is testable in staging."
        ],
        "proposed_workflow_family": "implementation_verification_readiness",
        "proposed_first_stage_set": ["implementation", "verification", "readiness-review"],
        "proposed_first_task_set": [
            {
                "task_id": None,
                "task_title": "Define first bounded TDE GUI scope",
                "task_summary": "Define the minimum read-heavy operator GUI scope for the first attempt.",
                "stage_id": "implementation"
            },
            {
                "task_id": None,
                "task_title": "Verify first TDE GUI scope and constraints",
                "task_summary": "Verify that the proposed first GUI scope is coherent, safe, and aligned with DB-canonical state.",
                "stage_id": "verification"
            }
        ],
        "required_clarifications": [],
        "recommended_next_action": "proceed_with_assumptions",
        "formation_rationale": f"A useful first GUI work system can be formed from the request under explicit assumptions. Original request: {request_text}",
        "formed_at": now,
        "formed_by_role": "Product Owner"
    }


def detect_request_class(request_text: str) -> str | None:
    text = request_text.lower()
    if 'gui' in text and 'tde' in text:
        return 'basic_tde_gui'
    return None


def main() -> None:
    ap = argparse.ArgumentParser(description="Thin TDE intent intake for first real request classes")
    ap.add_argument("--request-text", required=True)
    ap.add_argument("--source-ref", required=True)
    ap.add_argument("--formation-out", required=True)
    ap.add_argument("--create-canonical", action="store_true")
    ap.add_argument("--db-path", default="os/runtime/staging/tde_state.sqlite")
    ap.add_argument("--objectives-path", default="os/runtime/staging/tde_objectives.json")
    ap.add_argument("--tasks-projection-path", default="os/runtime/staging/TASKS_from_db.md")
    args = ap.parse_args()

    request_class = detect_request_class(args.request_text)
    if request_class != 'basic_tde_gui':
        raise SystemExit('unsupported_request_class')

    formation = form_basic_gui_request(request_text=args.request_text, source_ref=args.source_ref)
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
