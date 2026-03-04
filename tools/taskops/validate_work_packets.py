#!/usr/bin/env python3
from __future__ import annotations
import json
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]


def _load_yaml(path: Path) -> dict[str, Any]:
    try:
        import yaml  # type: ignore
    except Exception:
        return {}
    return yaml.safe_load(path.read_text(encoding="utf-8")) or {}


def _risk_rank(level: str) -> int:
    ranks = {"low": 1, "medium": 2, "high": 3, "critical": 4}
    return ranks.get(level, 999)


def validate_work_packets(registry: dict[str, Any]) -> tuple[list[str], list[str]]:
    errors: list[str] = []
    warnings: list[str] = []

    try:
        import jsonschema  # type: ignore
    except Exception:
        warnings.append("WARN: jsonschema not installed; taskops_work_packet schema checks skipped")
        return errors, warnings

    schema_rel = registry.get("taskops_work_packet", {}).get("1.0.0")
    if not schema_rel:
        errors.append("Missing schema registry entry for taskops_work_packet@1.0.0")
        return errors, warnings
    schema = json.loads((ROOT / schema_rel).read_text(encoding="utf-8"))

    sidefx_policy = _load_yaml(ROOT / "knowledge/policies/taskops_side_effect_contracts.v1.yaml")
    autonomy_policy = _load_yaml(ROOT / "knowledge/policies/taskops_autonomy_policy.v1.yaml")
    surfaces = (sidefx_policy.get("surfaces") or {}) if isinstance(sidefx_policy, dict) else {}
    autonomy_levels = (autonomy_policy.get("autonomy_levels") or {}) if isinstance(autonomy_policy, dict) else {}

    for p in sorted((ROOT / "knowledge/taskops/work_packets").rglob("*.json")):
        try:
            obj = json.loads(p.read_text(encoding="utf-8"))
        except Exception as e:
            errors.append(f"{p}: invalid JSON ({e})")
            continue
        if obj.get("artifactType") != "taskops_work_packet":
            continue

        try:
            jsonschema.validate(obj, schema)
        except Exception as e:
            errors.append(f"{p}: schema validation failed ({e})")
            continue

        # side effect contract validation
        for se in obj.get("side_effects", []):
            surface = se.get("surface")
            action = se.get("action")
            if surface not in surfaces:
                errors.append(f"{p}: unknown side effect surface '{surface}'")
                continue
            allowed = surfaces[surface].get("allowed_actions", [])
            if action not in allowed:
                errors.append(f"{p}: action '{action}' not allowed for surface '{surface}'")

        # autonomy vs risk bound
        autonomy = obj.get("autonomy_level")
        risk = obj.get("risk_level")
        rule = autonomy_levels.get(autonomy)
        if not rule:
            errors.append(f"{p}: unknown autonomy_level '{autonomy}'")
        else:
            max_risk = rule.get("max_risk", "low")
            if _risk_rank(risk) > _risk_rank(max_risk):
                errors.append(f"{p}: risk_level '{risk}' exceeds max_risk '{max_risk}' for autonomy '{autonomy}'")

    return errors, warnings
