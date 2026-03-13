#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from tde_intent_intake import REQUEST_CLASS_TABLE, detect_request_class
from tde_formation_creator import create_from_formation


def _iso_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace('+00:00', 'Z')


def _write_result_artifact(*, path: Path, request_text: str, source_ref: str, result: dict[str, Any]) -> str:
    path.parent.mkdir(parents=True, exist_ok=True)
    payload = {
        "artifactType": "tde_request_entry_result",
        "schemaVersion": "1.0.0",
        "recorded_at": _iso_now(),
        "request_text": request_text,
        "source_ref": source_ref,
        **result,
    }
    path.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    return str(path)


def run_request_entry(*, request_text: str, source_ref: str, formation_out: Path, db_path: Path, objectives_path: Path, tasks_projection_path: Path, result_out: Path | None = None) -> dict[str, Any]:
    request_class = detect_request_class(request_text)
    if request_class is None:
        raise ValueError("unsupported_request_class")

    formation = REQUEST_CLASS_TABLE[request_class](request_text=request_text, source_ref=source_ref)
    formation_out.parent.mkdir(parents=True, exist_ok=True)
    formation_out.write_text(json.dumps(formation, indent=2) + "\n", encoding="utf-8")

    result: dict[str, Any] = {
        "request_class": request_class,
        "formation_id": formation["formation_id"],
        "formation_path": str(formation_out),
        "recommended_next_action": formation["recommended_next_action"],
        "required_clarifications": formation.get("required_clarifications", []),
    }

    if formation["recommended_next_action"] in {"proceed_directly", "proceed_with_assumptions"}:
        result["canonical_creation"] = create_from_formation(
            formation_path=formation_out,
            db_path=db_path,
            objectives_path=objectives_path,
            tasks_projection_path=tasks_projection_path,
        )

    if result_out is not None:
        result["result_artifact_path"] = _write_result_artifact(
            path=result_out,
            request_text=request_text,
            source_ref=source_ref,
            result=result,
        )
    return result


def main() -> None:
    ap = argparse.ArgumentParser(description="Single-entry TDE request intake and formation workflow")
    ap.add_argument("--request-text", required=True)
    ap.add_argument("--source-ref", required=True)
    ap.add_argument("--formation-out", required=True)
    ap.add_argument("--result-out", default=None)
    ap.add_argument("--db-path", default="os/runtime/staging/tde_state.sqlite")
    ap.add_argument("--objectives-path", default="os/runtime/staging/tde_objectives.json")
    ap.add_argument("--tasks-projection-path", default="os/runtime/staging/TASKS_from_db.md")
    args = ap.parse_args()

    result = run_request_entry(
        request_text=args.request_text,
        source_ref=args.source_ref,
        formation_out=Path(args.formation_out),
        db_path=Path(args.db_path),
        objectives_path=Path(args.objectives_path),
        tasks_projection_path=Path(args.tasks_projection_path),
        result_out=Path(args.result_out) if args.result_out else None,
    )
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
