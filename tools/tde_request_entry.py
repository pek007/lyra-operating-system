#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from tde_intent_intake import REQUEST_CLASS_TABLE, detect_request_class
from tde_formation_creator import create_from_formation

ROOT = Path(__file__).resolve().parents[1]
SCHEMA_REGISTRY = ROOT / "schemas/_registry.json"
DEFAULT_INTAKE_SCHEMA_KEY = "tde_intake_packet"
DEFAULT_INTAKE_SCHEMA_VERSION = "1.0.0"
DEFAULT_WORKSPACE_SCOPE = "lyra-os-root"
DEFAULT_PRODUCT_SCOPE = "A-007"
DEFAULT_DB_PATH = "os/runtime/tde_state.sqlite"
DEFAULT_OBJECTIVES_PATH = "os/runtime/tde_objectives.json"
DEFAULT_TASKS_PROJECTION_PATH = "os/runtime/TASKS_from_db.md"


class ValidationError(RuntimeError):
    pass


def _iso_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace('+00:00', 'Z')


def _load_schema(*, artifact_type: str, schema_version: str) -> dict[str, Any]:
    registry = json.loads(SCHEMA_REGISTRY.read_text(encoding="utf-8"))
    schema_rel = registry.get(artifact_type, {}).get(schema_version)
    if not schema_rel:
        raise ValidationError(f"missing_registered_schema:{artifact_type}@{schema_version}")
    schema_path = ROOT / schema_rel
    return json.loads(schema_path.read_text(encoding="utf-8"))


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


def _classify_intake_class(*, request_class: str) -> str:
    if request_class in {"basic_tde_gui", "internal_tool", "runtime_hardening", "research_request", "review_audit_request"}:
        return "work"
    raise ValidationError(f"unsupported_intake_mapping:{request_class}")


def _build_intake_packet(*, request_text: str, source_ref: str, request_class: str, workspace_scope: str, product_scope: str | None) -> dict[str, Any]:
    intake_class = _classify_intake_class(request_class=request_class)
    return {
        "artifactType": DEFAULT_INTAKE_SCHEMA_KEY,
        "schemaVersion": DEFAULT_INTAKE_SCHEMA_VERSION,
        "intake_id": f"INTAKE-{source_ref}",
        "intake_class": intake_class,
        "source_system": "tde_request_entry",
        "source_type": "manual_entry",
        "source_reference": source_ref,
        "submitted_at": _iso_now(),
        "submitted_by": "Lyra",
        "title": request_text[:120],
        "summary": request_text,
        "body": {
            "request_text": request_text,
            "request_class": request_class,
        },
        "priority_hint": "unspecified",
        "workspace_scope": workspace_scope,
        "product_scope": product_scope,
        "related_entities": [],
        "evidence_links": [],
        "proposed_action": "run_intent_formation",
        "requested_action": request_text,
        "success_signal": None,
    }


def _write_json(*, path: Path, payload: dict[str, Any]) -> str:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    return str(path)


def _write_result_artifact(*, path: Path, request_text: str, source_ref: str, result: dict[str, Any]) -> str:
    payload = {
        "artifactType": "tde_request_entry_result",
        "schemaVersion": "1.0.0",
        "recorded_at": _iso_now(),
        "request_text": request_text,
        "source_ref": source_ref,
        **result,
    }
    return _write_json(path=path, payload=payload)


def run_request_entry(
    *,
    request_text: str,
    source_ref: str,
    formation_out: Path,
    db_path: Path,
    objectives_path: Path,
    tasks_projection_path: Path,
    result_out: Path | None = None,
    intake_packet_out: Path | None = None,
    workspace_scope: str = DEFAULT_WORKSPACE_SCOPE,
    product_scope: str | None = DEFAULT_PRODUCT_SCOPE,
) -> dict[str, Any]:
    request_class = detect_request_class(request_text)
    if request_class is None:
        raise ValueError("unsupported_request_class")

    intake_packet = _build_intake_packet(
        request_text=request_text,
        source_ref=source_ref,
        request_class=request_class,
        workspace_scope=workspace_scope,
        product_scope=product_scope,
    )
    _validate_against_schema(
        payload=intake_packet,
        artifact_type=DEFAULT_INTAKE_SCHEMA_KEY,
        schema_version=DEFAULT_INTAKE_SCHEMA_VERSION,
    )

    formation = REQUEST_CLASS_TABLE[request_class](request_text=request_text, source_ref=source_ref)
    _validate_against_schema(
        payload=formation,
        artifact_type="tde_intent_formation_record",
        schema_version=str(formation["schemaVersion"]),
    )

    result: dict[str, Any] = {
        "request_class": request_class,
        "intake_class": intake_packet["intake_class"],
        "intake_validation": "passed",
        "formation_validation": "passed",
        "formation_id": formation["formation_id"],
        "recommended_next_action": formation["recommended_next_action"],
        "required_clarifications": formation.get("required_clarifications", []),
    }

    if intake_packet_out is not None:
        result["intake_packet_path"] = _write_json(path=intake_packet_out, payload=intake_packet)

    result["formation_path"] = _write_json(path=formation_out, payload=formation)

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
    ap.add_argument("--intake-packet-out", default=None)
    ap.add_argument("--result-out", default=None)
    ap.add_argument("--workspace-scope", default=DEFAULT_WORKSPACE_SCOPE)
    ap.add_argument("--product-scope", default=DEFAULT_PRODUCT_SCOPE)
    ap.add_argument("--db-path", default=DEFAULT_DB_PATH)
    ap.add_argument("--objectives-path", default=DEFAULT_OBJECTIVES_PATH)
    ap.add_argument("--tasks-projection-path", default=DEFAULT_TASKS_PROJECTION_PATH)
    args = ap.parse_args()

    result = run_request_entry(
        request_text=args.request_text,
        source_ref=args.source_ref,
        formation_out=Path(args.formation_out),
        intake_packet_out=Path(args.intake_packet_out) if args.intake_packet_out else None,
        db_path=Path(args.db_path),
        objectives_path=Path(args.objectives_path),
        tasks_projection_path=Path(args.tasks_projection_path),
        result_out=Path(args.result_out) if args.result_out else None,
        workspace_scope=args.workspace_scope,
        product_scope=args.product_scope,
    )
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
