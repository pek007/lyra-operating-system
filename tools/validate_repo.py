#!/usr/bin/env python3
from __future__ import annotations
import argparse
import json
import subprocess
import sys
from datetime import date
from pathlib import Path

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


def validate_tde_artifacts() -> list[str]:
    errs = []
    warnings = []
    try:
        import jsonschema  # type: ignore
    except Exception:
        return ["WARN: jsonschema not installed; skipping artifact schema checks."]

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
    return warnings + errs


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


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--fix", action="store_true")
    args = parser.parse_args()

    run([sys.executable, "tools/gen_inventory.py"])
    run([sys.executable, "tools/gen_knowledge_indexes.py"])

    errors: list[str] = []
    messages: list[str] = []

    messages.extend(validate_tde_artifacts())
    errors.extend(validate_schema_files())
    errors.extend(validate_decision_frontmatter())
    errors.extend(validate_report_decision_mapping())

    if not args.fix:
        errors.extend(
            check_drift(
                [
                    ROOT / "inventory/generated/repo_inventory.json",
                    ROOT / "knowledge/indexes/inbox_index.json",
                    ROOT / "knowledge/indexes/decisions_index.json",
                    ROOT / "knowledge/indexes/report_decision_index.json",
                    ROOT / "knowledge/indexes/indexes_manifest.json",
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
