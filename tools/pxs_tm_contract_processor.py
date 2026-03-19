#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
SCHEMA_REGISTRY = ROOT / "schemas/_registry.json"


class ContractValidationError(RuntimeError):
    def __init__(self, code: str, message: str, field: str | None = None):
        super().__init__(message)
        self.code = code
        self.message = message
        self.field = field


def _iso_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace('+00:00', 'Z')


def _load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def _load_schema(artifact_type: str, schema_version: str) -> dict[str, Any]:
    registry = _load_json(SCHEMA_REGISTRY)
    schema_rel = registry.get(artifact_type, {}).get(schema_version)
    if not schema_rel:
        raise ContractValidationError(
            code="missing_registered_schema",
            message=f"No registered schema for {artifact_type}@{schema_version}.",
            field="schemaVersion",
        )
    return _load_json(ROOT / schema_rel)


def _validate_against_schema(payload: dict[str, Any], artifact_type: str, schema_version: str) -> None:
    try:
        import jsonschema  # type: ignore
    except Exception as exc:
        raise ContractValidationError(
            code="jsonschema_not_installed",
            message="jsonschema is required to validate contract payloads.",
        ) from exc
    schema = _load_schema(artifact_type, schema_version)
    validator = jsonschema.Draft202012Validator(schema)
    errors = sorted(validator.iter_errors(payload), key=lambda e: list(e.path))
    if errors:
        err = errors[0]
        field = "/".join(map(str, err.path)) if err.path else None
        raise ContractValidationError(
            code="schema_validation_failed",
            message=err.message,
            field=field,
        )


def _find_duplicate_response(request_id: str, search_root: Path) -> Path | None:
    for path in sorted(search_root.rglob("*.json")):
        try:
            data = _load_json(path)
        except Exception:
            continue
        if data.get("artifactType") != "pxs_tm_response_envelope":
            continue
        if data.get("request_id") == request_id:
            return path.relative_to(ROOT)
    return None


def _build_response(*, request: dict[str, Any], status: str, handled_at: str, note: str, target_refs: list[dict[str, Any]], validation_errors: list[dict[str, Any]] | None = None) -> dict[str, Any]:
    return {
        "artifactType": "pxs_tm_response_envelope",
        "schemaVersion": "1.0.0",
        "response_id": f"{request['request_id']}:response",
        "request_id": request["request_id"],
        "handled_by": "Lyra",
        "handled_at": handled_at,
        "status": status,
        "canonical_target_refs": target_refs,
        "validation_errors": validation_errors or [],
        "note": note,
    }


def process_request(*, request_path: Path, search_root: Path | None = None) -> dict[str, Any]:
    search_root = search_root or (ROOT / "products/task-management/07-decisions/examples")
    request = _load_json(request_path)
    now = _iso_now()

    try:
        _validate_against_schema(request, "pxs_tm_request_envelope", str(request.get("schemaVersion")))
    except ContractValidationError as exc:
        return _build_response(
            request=request,
            status="rejected_invalid_request",
            handled_at=now,
            note="Request rejected because the envelope failed validation.",
            target_refs=[],
            validation_errors=[{"code": exc.code, "message": exc.message, "field": exc.field}],
        )

    duplicate_ref = _find_duplicate_response(str(request["request_id"]), search_root)
    if duplicate_ref is not None:
        return _build_response(
            request=request,
            status="duplicate",
            handled_at=now,
            note="Duplicate request detected: an explicit response already exists for this request id.",
            target_refs=[
                {
                    "kind": "artifact",
                    "ref": str(duplicate_ref),
                    "note": "Existing response envelope for this request id.",
                }
            ],
        )

    payload = request.get("payload_inline")
    if payload is None:
        return _build_response(
            request=request,
            status="rejected_invalid_request",
            handled_at=now,
            note="Request rejected because payload_inline is required for the minimal processor.",
            target_refs=[],
            validation_errors=[
                {
                    "code": "payload_inline_required",
                    "message": "The minimal processor currently supports inline payloads only.",
                    "field": "payload_inline",
                }
            ],
        )

    artifact_type = str(payload.get("artifactType"))
    schema_version = str(payload.get("schemaVersion"))
    try:
        _validate_against_schema(payload, artifact_type, schema_version)
    except ContractValidationError as exc:
        return _build_response(
            request=request,
            status="rejected_invalid_request",
            handled_at=now,
            note="Request rejected because the nested payload failed validation.",
            target_refs=[],
            validation_errors=[{"code": exc.code, "message": exc.message, "field": exc.field}],
        )

    source_ref = str(request.get("source_reference") or payload.get("source_reference") or "")
    refs = []
    if source_ref:
        refs.append({"kind": "artifact", "ref": source_ref, "note": "Source reference for the accepted request."})
    if request.get("canonical_contract_ref"):
        refs.append({"kind": "artifact", "ref": request["canonical_contract_ref"], "note": "Canonical contract used for handling."})

    return _build_response(
        request=request,
        status="accepted",
        handled_at=now,
        note="Request accepted by the minimal processor after envelope and nested payload validation.",
        target_refs=refs,
    )


def main() -> None:
    parser = argparse.ArgumentParser(description="Process a PXS Task Management contract request envelope.")
    parser.add_argument("request", help="Path to the request envelope JSON file")
    parser.add_argument("--search-root", help="Directory to scan for duplicate response envelopes")
    parser.add_argument("--output", help="Optional path to write the response envelope JSON")
    args = parser.parse_args()

    request_path = Path(args.request).resolve()
    response = process_request(
        request_path=request_path,
        search_root=Path(args.search_root).resolve() if args.search_root else None,
    )

    text = json.dumps(response, indent=2, ensure_ascii=False) + "\n"
    if args.output:
        Path(args.output).write_text(text, encoding="utf-8")
    else:
        print(text, end="")


if __name__ == "__main__":
    main()
