#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

DIRECTION_SOURCES = [
    "AGENTS.md",
    "AI_NATIVE_OPERATING_POLICY_V1.md",
    "TASK_SYSTEM_POLICY_V1.md",
    "MODEL_ROUTING_POLICY.md",
    "STANDARD_CHANGE_CATALOG_V1.md",
    "ARTIFACT_ACTIVATION_MODEL_V1.md",
    "SOP-001_INTAKE_TRIAGE.md",
    "DECISION_PRINCIPLES.md",
]


def file_hash(path: Path) -> str:
    data = path.read_bytes()
    return "sha256:" + hashlib.sha256(data).hexdigest()


def main() -> int:
    generated_at = datetime.now(timezone.utc).isoformat()
    entries = []
    for rel in DIRECTION_SOURCES:
        p = ROOT / rel
        if not p.exists():
            continue
        entries.append(
            {
                "path": rel,
                "hash": file_hash(p),
                "bytes": p.stat().st_size,
                "modified_at": datetime.fromtimestamp(p.stat().st_mtime, tz=timezone.utc).isoformat(),
            }
        )

    canonical = json.dumps(entries, sort_keys=True, separators=(",", ":")).encode("utf-8")
    root_hash = "sha256:" + hashlib.sha256(canonical).hexdigest()

    snapshot = {
        "artifactType": "effective_direction_snapshot",
        "schemaVersion": "1.0.0",
        "generated_at": generated_at,
        "sources": entries,
        "source_count": len(entries),
        "root_hash": root_hash,
        "notes": [
            "This is a machine-readable fingerprint of active direction/policy sources.",
            "It is a compiler output/projection and does not replace source governance documents.",
        ],
    }

    out = ROOT / "os/runtime/effective_direction_snapshot.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(snapshot, indent=2) + "\n", encoding="utf-8")

    print(json.dumps({"status": "ok", "path": str(out.relative_to(ROOT)), "source_count": len(entries), "root_hash": root_hash}))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
