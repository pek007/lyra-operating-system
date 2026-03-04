#!/usr/bin/env python3
from __future__ import annotations
import json
from pathlib import Path
from typing import Any

from .hash_util import compute_record_hash

ROOT = Path(__file__).resolve().parents[2]


def _load_yaml(path: Path) -> dict[str, Any]:
    try:
        import yaml  # type: ignore
    except Exception:
        return {}
    return yaml.safe_load(path.read_text(encoding="utf-8")) or {}


def validate_observations(registry: dict[str, Any]) -> tuple[list[str], list[str]]:
    errors: list[str] = []
    warnings: list[str] = []

    try:
        import jsonschema  # type: ignore
    except Exception:
        warnings.append("WARN: jsonschema not installed; observation schema checks skipped")
        return errors, warnings

    source_policy = _load_yaml(ROOT / "knowledge/policies/observation_sources.v1.yaml")
    source_map = ((source_policy.get("sources") or {}) if isinstance(source_policy, dict) else {})

    obs_by_id: dict[str, dict] = {}
    for p in sorted((ROOT / "knowledge/observations").rglob("*.json")):
        try:
            obj = json.loads(p.read_text(encoding="utf-8"))
        except Exception as e:
            errors.append(f"{p}: invalid JSON ({e})")
            continue

        at = obj.get("artifactType")
        if at != "observation":
            continue
        sv = obj.get("schemaVersion")
        schema_rel = registry.get("observation", {}).get(sv)
        if not schema_rel:
            errors.append(f"{p}: missing registered schema for observation@{sv}")
            continue
        schema = json.loads((ROOT / schema_rel).read_text(encoding="utf-8"))
        try:
            jsonschema.validate(obj, schema)
        except Exception as e:
            errors.append(f"{p}: schema validation failed ({e})")
            continue

        rid = obj.get("observation_id")
        if rid:
            obs_by_id[rid] = obj

        expected = compute_record_hash(obj)
        got = obj.get("integrity", {}).get("recordHash")
        if got != expected:
            errors.append(f"{p}: recordHash mismatch")

        system = obj.get("source", {}).get("system")
        kind = obj.get("source", {}).get("kind")
        if system not in source_map:
            errors.append(f"{p}: source.system '{system}' is not registered")
        else:
            allowed = source_map[system].get("allowed_kinds", [])
            if kind not in allowed:
                errors.append(f"{p}: source.kind '{kind}' not allowed for '{system}'")

        storage = obj.get("content", {}).get("storage", {}) if isinstance(obj.get("content"), dict) else {}
        if storage.get("mode") == "blob_ref":
            blob = storage.get("blobPath")
            if blob:
                blob_path = ROOT / blob
                if not blob_path.exists():
                    errors.append(f"{p}: blob missing at {blob}")

    # provenance parent checks
    for p in sorted((ROOT / "knowledge/observations").rglob("*.json")):
        try:
            obj = json.loads(p.read_text(encoding="utf-8"))
        except Exception:
            continue
        if obj.get("artifactType") != "observation":
            continue
        parents = obj.get("provenance", {}).get("parents", [])
        for parent in parents:
            pid = parent.get("observation_id")
            phash = parent.get("recordHash")
            pobj = obs_by_id.get(pid)
            if not pobj:
                errors.append(f"{p}: parent observation not found: {pid}")
                continue
            if pobj.get("integrity", {}).get("recordHash") != phash:
                errors.append(f"{p}: parent hash mismatch for {pid}")

    return errors, warnings
