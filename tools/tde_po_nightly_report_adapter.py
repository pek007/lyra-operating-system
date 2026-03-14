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


def _priority_hint(report: dict[str, Any]) -> str:
    cp_priority = report.get("control_panel_priority")
    if cp_priority:
        return str(cp_priority)
    health = report.get("overall_health")
    if health == "red":
        return "high"
    if health == "yellow":
        return "medium"
    return "unspecified"


def _signal_types(report: dict[str, Any]) -> list[str]:
    signal_types = ["status"]
    if report.get("blockers"):
        signal_types.append("blocker")
    if report.get("risks"):
        signal_types.append("risk")
    if report.get("proposed_tde_actions") or report.get("control_panel_priority"):
        signal_types.append("priority_proposal")
    return signal_types


def adapt_po_nightly_report(*, report: dict[str, Any], workspace_scope: str) -> dict[str, Any]:
    _validate_against_schema(payload=report, artifact_type="tde_po_nightly_report", schema_version=str(report["schemaVersion"]))

    related_entities: list[dict[str, Any]] = [
        {
            "entity_type": "product",
            "entity_ref": str(report["product_id"]),
            "relationship": "reported_product",
        }
    ]
    for blocker in report.get("blockers", []):
        linked_tde_id = blocker.get("linked_tde_id")
        if linked_tde_id:
            related_entities.append(
                {
                    "entity_type": "tde_item",
                    "entity_ref": str(linked_tde_id),
                    "relationship": "linked_blocker",
                }
            )

    intake_packet = {
        "artifactType": "tde_intake_packet",
        "schemaVersion": "1.0.0",
        "intake_id": f"intake:{report['product_id']}:{report['report_date']}:{report['report_id']}",
        "intake_class": "signal",
        "source_system": "tde_po_nightly_report_adapter",
        "source_type": "report",
        "source_reference": report["source_reference"],
        "submitted_at": _iso_now(),
        "submitted_by": report["product_owner"],
        "title": f"Nightly PO report: {report['product_name']} ({report['report_date']})",
        "summary": report["summary"],
        "body": {
            "report_id": report["report_id"],
            "report_date": report["report_date"],
            "product_id": report["product_id"],
            "product_name": report["product_name"],
            "product_owner": report["product_owner"],
            "overall_health": report["overall_health"],
            "top_priorities": report["top_priorities"],
            "blockers": report["blockers"],
            "risks": report["risks"],
            "proposed_tde_actions": report["proposed_tde_actions"],
            "control_panel_priority": report.get("control_panel_priority"),
            "adapted_at": _iso_now(),
        },
        "priority_hint": _priority_hint(report),
        "workspace_scope": workspace_scope,
        "product_scope": report["product_id"],
        "related_entities": related_entities,
        "evidence_links": report["evidence_links"],
        "proposed_action": "triage_nightly_po_signal",
        "signal_types": _signal_types(report),
    }

    _validate_against_schema(payload=intake_packet, artifact_type="tde_intake_packet", schema_version="1.0.0")
    return intake_packet


def main() -> None:
    ap = argparse.ArgumentParser(description="Adapt a PO nightly report into a canonical TDE intake packet")
    ap.add_argument("--report-path", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--workspace-scope", required=True)
    args = ap.parse_args()

    report = json.loads(Path(args.report_path).read_text(encoding="utf-8"))
    intake_packet = adapt_po_nightly_report(report=report, workspace_scope=args.workspace_scope)

    out_path = Path(args.out)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(intake_packet, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"out": str(out_path), "intake_id": intake_packet["intake_id"]}, indent=2))


if __name__ == "__main__":
    main()
