#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
SCHEMA_REGISTRY = ROOT / "schemas/_registry.json"


class ValidationError(RuntimeError):
    pass


def _iso_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace('+00:00', 'Z')


def _load_schema(*, artifact_type: str, schema_version: str) -> dict[str, Any]:
    registry = json.loads(SCHEMA_REGISTRY.read_text(encoding="utf-8"))
    schema_rel = registry.get(artifact_type, {}).get(schema_version)
    if not schema_rel:
        raise ValidationError(f"missing_registered_schema:{artifact_type}@{schema_version}")
    return json.loads((ROOT / schema_rel).read_text(encoding="utf-8"))


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


def _intake_class(report: dict[str, Any]) -> str:
    report_type = report.get("type")
    priority = report.get("priority_hint") or "unspecified"
    if priority == "critical" or report_type == "incident":
        return "incident"
    if report_type == "decision_failure":
        return "decision"
    return "work"


def adapt_error_report(*, report: dict[str, Any], workspace_scope: str) -> dict[str, Any]:
    _validate_against_schema(payload=report, artifact_type="tde_error_report", schema_version=str(report["schemaVersion"]))

    intake_class = _intake_class(report)
    linked = report.get("linked_artifacts") or {}
    related_entities = []
    owner = str(report["owning_product_or_owner"])
    related_entities.append({"entity_type": "owner_scope", "entity_ref": owner, "relationship": "owning_scope"})
    for ref in linked.get("related_tasks", []) or []:
        related_entities.append({"entity_type": "tde_item", "entity_ref": str(ref), "relationship": "related_task"})
    for ref in linked.get("related_decisions", []) or []:
        related_entities.append({"entity_type": "decision", "entity_ref": str(ref), "relationship": "related_decision"})

    evidence_links = [{"kind": "error_report", "ref": report["source_reference"], "note": report["error_id"]}]
    for ref in linked.get("related_evidence", []) or []:
        evidence_links.append({"kind": "evidence", "ref": str(ref), "note": None})

    body = {
        "error_id": report["error_id"],
        "error_type": report["type"],
        "scope": report["scope"],
        "summary": report["summary"],
        "impact": report["impact"],
        "detection_method": report["detection_method"],
        "root_cause": report["root_cause"],
        "contributing_factors": report.get("contributing_factors", []),
        "immediate_mitigation": report.get("immediate_mitigation"),
        "corrective_actions": report["corrective_actions"],
        "preventive_changes": report["preventive_changes"],
        "status": report["status"],
        "adapted_at": _iso_now(),
    }

    packet = {
        "artifactType": "tde_intake_packet",
        "schemaVersion": "1.0.0",
        "intake_id": f"intake:error:{report['error_id']}",
        "intake_class": intake_class,
        "source_system": "tde_error_report_adapter",
        "source_type": "document",
        "source_reference": report["source_reference"],
        "submitted_at": _iso_now(),
        "submitted_by": report["owning_product_or_owner"],
        "title": f"Corrective action from error report: {report['title']}",
        "summary": report["summary"],
        "body": body,
        "priority_hint": report.get("priority_hint") or "unspecified",
        "workspace_scope": workspace_scope,
        "product_scope": report["owning_product_or_owner"],
        "related_entities": related_entities,
        "evidence_links": evidence_links,
        "proposed_action": "route_error_corrective_action",
    }

    if intake_class == "work":
        packet["requested_action"] = "; ".join(report["corrective_actions"])
        packet["success_signal"] = report["preventive_changes"]
    elif intake_class == "decision":
        packet["decision_question"] = f"What is the correct corrective path for error {report['error_id']}?"
    elif intake_class == "incident":
        packet["incident_summary"] = report["summary"]
        packet["impact_summary"] = report["impact"]["actual_impact"]
        packet["severity_hint"] = "sev1" if (report.get("priority_hint") == "critical") else "unknown"

    _validate_against_schema(payload=packet, artifact_type="tde_intake_packet", schema_version="1.0.0")
    return packet


def main() -> None:
    ap = argparse.ArgumentParser(description="Adapt a structured error report into canonical TDE intake")
    ap.add_argument("--report-path", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--workspace-scope", required=True)
    args = ap.parse_args()
    report = json.loads(Path(args.report_path).read_text(encoding="utf-8"))
    packet = adapt_error_report(report=report, workspace_scope=args.workspace_scope)
    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(packet, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"out": str(out), "intake_id": packet["intake_id"], "intake_class": packet["intake_class"]}, indent=2))


if __name__ == "__main__":
    main()
