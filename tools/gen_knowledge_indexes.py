#!/usr/bin/env python3
from __future__ import annotations
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


def main() -> int:
    IDX.mkdir(parents=True, exist_ok=True)
    inbox = index_dir("inbox")
    decisions = index_dir("decisions")

    (IDX / "inbox_index.json").write_text(json.dumps({"items": inbox}, indent=2) + "\n")
    (IDX / "decisions_index.json").write_text(json.dumps({"items": decisions}, indent=2) + "\n")
    (IDX / "indexes_manifest.json").write_text(
        json.dumps(
            {
                "generatedBy": "tools/gen_knowledge_indexes.py",
                "outputs": [
                    "knowledge/indexes/inbox_index.json",
                    "knowledge/indexes/decisions_index.json",
                ],
                "counts": {"inbox": len(inbox), "decisions": len(decisions)},
            },
            indent=2,
        )
        + "\n"
    )
    print("knowledge indexes generated")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
