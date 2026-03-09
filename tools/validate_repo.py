#!/usr/bin/env python3
from __future__ import annotations
import argparse
import json
import subprocess
import sys
from datetime import date
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
SCHEMA_REGISTRY = ROOT / "schemas/_registry.json"


def run(cmd: list[str]) -> None:
    subprocess.run(cmd, cwd=ROOT, check=True)


def parse_frontmatter(path: Path) -> dict:
    text = path.read_text(encoding="utf-8", errors="replace")
    if not text.startswith("---\n"):
        return {}
    end = text.find("\n---\n", 4)
    if end == -1:
        return {}
    block = text[4:end].splitlines()
    out = {}
    for line in block:
        if ":" not in line:
            continue
        k, v = line.split(":", 1)
        out[k.strip()] = v.strip().strip('"')
    return out


def check_drift(paths: list[Path]) -> list[str]:
    errs = []
    try:
        out = subprocess.check_output(["git", "status", "--porcelain", "--"] + [str(p) for p in paths], cwd=ROOT)
    except Exception as e:
        return [f"Unable to check drift with git: {e}"]
    if out.decode().strip():
        errs.append("Generated files are out of date. Run generators and commit changes.")
    return errs


def validate_schema_files() -> list[str]:
    errs = []
    for p in sorted((ROOT / "schemas").rglob("*.schema.json")):
        try:
            obj = json.loads(p.read_text())
        except Exception as e:
            errs.append(f"Invalid JSON schema file {p}: {e}")
            continue
        if "$schema" not in obj or "$id" not in obj:
            errs.append(f"Schema missing $schema/$id: {p}")
    return errs


def validate_decision_frontmatter() -> list[str]:
    errs = []
    required = [
        "decision_id",
        "title",
        "date",
        "status",
        "owner",
        "review_date",
        "context",
        "options_considered",
        "decision",
        "rationale",
    ]
    for p in sorted((ROOT / "knowledge/decisions").rglob("*.md")):
        meta = parse_frontmatter(p)
        miss = [k for k in required if not meta.get(k)]
        if miss:
            errs.append(f"{p}: missing frontmatter keys {miss}")
        for k in ("date", "review_date"):
            if meta.get(k):
                try:
                    date.fromisoformat(meta[k])
                except Exception:
                    errs.append(f"{p}: {k} must be YYYY-MM-DD")
    return errs


def validate_tde_artifacts() -> tuple[list[str], list[str]]:
    errs: list[str] = []
    warnings: list[str] = []
    try:
        import jsonschema  # type: ignore
    except Exception:
        errs.append(
            "jsonschema not installed; artifact schema checks are mandatory. Install dependency (e.g., `python3 -m pip install --user jsonschema`)"
        )
        return errs, warnings

    reg = json.loads(SCHEMA_REGISTRY.read_text())
    for p in sorted((ROOT / "knowledge/evidence").rglob("*.json")):
        try:
            obj = json.loads(p.read_text())
        except Exception as e:
            errs.append(f"{p}: invalid JSON ({e})")
            continue
        at = obj.get("artifactType")
        sv = obj.get("schemaVersion")
        if not at:
            continue
        if at not in reg:
            warnings.append(f"WARN: {p}: unknown artifactType {at}")
            continue
        if not sv:
            errs.append(f"{p}: artifactType={at} missing schemaVersion")
            continue
        schema_rel = reg.get(at, {}).get(sv)
        if not schema_rel:
            errs.append(f"{p}: no registered schema for {at}@{sv}")
            continue
        schema = json.loads((ROOT / schema_rel).read_text())
        try:
            jsonschema.validate(obj, schema)
        except Exception as e:
            errs.append(f"{p}: schema validation failed ({e})")
    return errs, warnings


def validate_report_decision_mapping() -> list[str]:
    errs = []
    report_index = ROOT / "knowledge/indexes/report_decision_index.json"
    decisions_index = ROOT / "knowledge/indexes/decisions_index.json"
    if not report_index.exists() or not decisions_index.exists():
        return errs

    try:
        reports = json.loads(report_index.read_text()).get("items", [])
        decisions = json.loads(decisions_index.read_text()).get("items", [])
    except Exception as e:
        return [f"Unable to parse report/decision indexes: {e}"]

    valid_decision_ids = {d.get("decision_id") for d in decisions if d.get("decision_id")}

    for r in reports:
        if not r.get("decision_impact"):
            continue
        has_decision = bool(r.get("decision_id")) and (r.get("decision_id") in valid_decision_ids)
        has_marker = bool(r.get("no_decision_marker"))
        if not has_decision and not has_marker:
            errs.append(
                f"{r.get('path')}: decision_impact=true requires valid decision_id or no_decision_marker"
            )
    return errs


def _load_observations_by_id() -> dict[str, dict[str, Any]]:
    out: dict[str, dict[str, Any]] = {}
    for p in sorted((ROOT / "knowledge/observations").rglob("*.json")):
        try:
            obj = json.loads(p.read_text(encoding="utf-8"))
        except Exception:
            continue
        if obj.get("artifactType") != "observation":
            continue
        oid = obj.get("observation_id")
        if oid:
            out[oid] = obj
    return out


def validate_evidence_observation_links() -> list[str]:
    errs: list[str] = []
    obs = _load_observations_by_id()
    for p in sorted((ROOT / "knowledge/evidence").rglob("*.json")):
        try:
            obj = json.loads(p.read_text(encoding="utf-8"))
        except Exception:
            continue
        links = (obj.get("evidence") or {}).get("observations") or []
        if not isinstance(links, list):
            errs.append(f"{p}: evidence.observations must be a list")
            continue
        for link in links:
            oid = link.get("observation_id") if isinstance(link, dict) else None
            rh = link.get("recordHash") if isinstance(link, dict) else None
            if not oid or not rh:
                errs.append(f"{p}: invalid observation link entry")
                continue
            target = obs.get(oid)
            if not target:
                errs.append(f"{p}: observation not found: {oid}")
                continue
            if target.get("integrity", {}).get("recordHash") != rh:
                errs.append(f"{p}: recordHash mismatch for observation {oid}")
    return errs


def main() -> int:
    parser = argparse.ArgumentParser(
        description=(
            "Validate governance artifacts and generated indexes. "
            "Note: the current default path regenerates deterministic derivatives before drift checks."
        )
    )
    parser.add_argument(
        "--fix",
        action="store_true",
        help="Regenerate deterministic derivatives and skip the post-generation git drift failure check.",
    )
    args = parser.parse_args()

    run([sys.executable, "tools/gen_inventory.py"])
    run([sys.executable, "tools/gen_knowledge_indexes.py"])
    run([sys.executable, "tools/gen_reports_index.py"])
    run([sys.executable, "tools/standard_change_policy_check.py", "--strict"])
    run([sys.executable, "tools/task_hygiene_check.py", "--file", "TASKS.md"])
    run([sys.executable, "tools/markdown_link_check.py", "--changed-only"])
    run([sys.executable, "tools/referenced_script_guard.py"])

    errors: list[str] = []
    messages: list[str] = []

    artifact_errors, artifact_warnings = validate_tde_artifacts()
    errors.extend(artifact_errors)
    messages.extend(artifact_warnings)
    errors.extend(validate_schema_files())
    errors.extend(validate_decision_frontmatter())
    errors.extend(validate_report_decision_mapping())
    errors.extend(validate_evidence_observation_links())

    try:
        from observe.validate_observations import validate_observations  # type: ignore

        obs_errors, obs_warnings = validate_observations(json.loads(SCHEMA_REGISTRY.read_text()))
        errors.extend(obs_errors)
        messages.extend(obs_warnings)
    except Exception as e:
        messages.append(f"WARN: observation validator unavailable ({e})")

    try:
        from taskops.validate_work_packets import validate_work_packets  # type: ignore

        wp_errors, wp_warnings = validate_work_packets(json.loads(SCHEMA_REGISTRY.read_text()))
        errors.extend(wp_errors)
        messages.extend(wp_warnings)
    except Exception as e:
        messages.append(f"WARN: taskops validator unavailable ({e})")

    if not args.fix:
        errors.extend(
            check_drift(
                [
                    ROOT / "inventory/generated/repo_inventory.json",
                    ROOT / "knowledge/indexes/inbox_index.json",
                    ROOT / "knowledge/indexes/decisions_index.json",
                    ROOT / "knowledge/indexes/report_decision_index.json",
                    ROOT / "knowledge/indexes/observations_index.json",
                    ROOT / "knowledge/indexes/indexes_manifest.json",
                    ROOT / "knowledge/reports/INDEX.md",
                ]
            )
        )

    for m in messages:
        print(m)
    if errors:
        print("\nValidation failed:")
        for e in errors:
            print(f"- {e}")
        return 1

    print("Validation passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
