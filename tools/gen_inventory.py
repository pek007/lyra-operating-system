#!/usr/bin/env python3
from __future__ import annotations
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "inventory/generated/repo_inventory.json"
EXCLUDE_DIRS = {".git", "node_modules", ".openclaw", ".control-panel", "metrics"}
EXCLUDE_PREFIXES = {
    "inventory/generated/",
    "knowledge/indexes/",
}


def should_skip(path: Path) -> bool:
    rel = path.as_posix()
    if any(rel.startswith(prefix) for prefix in EXCLUDE_PREFIXES):
        return True
    return any(part in EXCLUDE_DIRS for part in path.parts)


def main() -> int:
    rows = []
    for p in sorted(ROOT.rglob("*")):
        if should_skip(p.relative_to(ROOT)):
            continue
        if p.is_dir():
            continue
        rel = p.relative_to(ROOT).as_posix()
        st = p.stat()
        rows.append({
            "path": rel,
            "size": st.st_size,
            "mtime": int(st.st_mtime),
            "ext": p.suffix.lower(),
        })

    payload = {
        "schemaVersion": "1.0.0",
        "generatedBy": "tools/gen_inventory.py",
        "files": rows,
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(payload, indent=2) + "\n")
    print(f"wrote {OUT}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
