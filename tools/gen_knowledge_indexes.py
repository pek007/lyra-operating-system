#!/usr/bin/env python3
from __future__ import annotations
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
KNOW = ROOT / "knowledge"
IDX = KNOW / "indexes"


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


def index_dir(name: str) -> list[dict]:
    d = KNOW / name
    if not d.exists():
        return []
    rows = []
    for p in sorted(d.rglob("*.md")):
        rel = p.relative_to(ROOT).as_posix()
        meta = parse_frontmatter(p)
        rows.append({
            "path": rel,
            "title": meta.get("title") or p.stem,
            "decision_id": meta.get("decision_id"),
            "status": meta.get("status"),
        })
    return rows


def index_reports_for_decisions() -> list[dict]:
    d = KNOW / "reports"
    if not d.exists():
        return []
    rows = []
    for p in sorted(d.rglob("*.md")):
        rel = p.relative_to(ROOT).as_posix()
        meta = parse_frontmatter(p)
        impact_raw = str(meta.get("decision_impact", "")).lower()
        rows.append({
            "path": rel,
            "title": meta.get("title") or p.stem,
            "decision_impact": impact_raw in {"true", "yes", "1"},
            "decision_id": meta.get("decision_id"),
            "no_decision_marker": meta.get("no_decision_marker"),
        })
    return rows


def index_observations() -> dict:
    d = KNOW / "observations"
    entries: list[dict] = []
    if d.exists():
        for p in sorted(d.rglob("*.json")):
            rel = p.relative_to(ROOT).as_posix()
            try:
                obj = json.loads(p.read_text(encoding="utf-8"))
            except Exception:
                continue
            if obj.get("artifactType") != "observation":
                continue
            entries.append({
                "observation_id": obj.get("observation_id"),
                "observedAt": obj.get("observedAt"),
                "kind": obj.get("source", {}).get("kind"),
                "trust": obj.get("trust", {}).get("level"),
                "redaction": obj.get("redaction", {}).get("state"),
                "contentHash": obj.get("integrity", {}).get("contentHash"),
                "recordHash": obj.get("integrity", {}).get("recordHash"),
                "path": rel,
            })

    entries = sorted(entries, key=lambda x: ((x.get("observedAt") or ""), (x.get("observation_id") or "")))
    canonical = json.dumps(entries, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8")
    root_hash = "sha256:" + hashlib.sha256(canonical).hexdigest()
    return {
        "artifactType": "observations_index",
        "schemaVersion": "1.0.0",
        "entries": entries,
        "rootHash": root_hash,
    }


def main() -> int:
    IDX.mkdir(parents=True, exist_ok=True)
    inbox = index_dir("inbox")
    decisions = index_dir("decisions")
    report_decisions = index_reports_for_decisions()
    observations_index = index_observations()

    (IDX / "inbox_index.json").write_text(json.dumps({"items": inbox}, indent=2) + "\n")
    (IDX / "decisions_index.json").write_text(json.dumps({"items": decisions}, indent=2) + "\n")
    (IDX / "report_decision_index.json").write_text(json.dumps({"items": report_decisions}, indent=2) + "\n")
    (IDX / "observations_index.json").write_text(json.dumps(observations_index, indent=2) + "\n")
    (IDX / "indexes_manifest.json").write_text(
        json.dumps(
            {
                "generatedBy": "tools/gen_knowledge_indexes.py",
                "outputs": [
                    "knowledge/indexes/inbox_index.json",
                    "knowledge/indexes/decisions_index.json",
                    "knowledge/indexes/report_decision_index.json",
                    "knowledge/indexes/observations_index.json",
                ],
                "counts": {
                    "inbox": len(inbox),
                    "decisions": len(decisions),
                    "report_decisions": len(report_decisions),
                    "observations": len(observations_index.get("entries", [])),
                },
                "observationRootHash": observations_index.get("rootHash"),
            },
            indent=2,
        )
        + "\n"
    )
    print("knowledge indexes generated")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
