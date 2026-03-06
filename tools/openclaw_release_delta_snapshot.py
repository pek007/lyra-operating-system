#!/usr/bin/env python3
from __future__ import annotations

import subprocess
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT_DIR = ROOT / "knowledge" / "evidence"


def run(cmd: list[str]) -> str:
    try:
        p = subprocess.run(cmd, cwd=ROOT, capture_output=True, text=True, check=False)
        body = (p.stdout or "") + ("\n" + p.stderr if p.stderr else "")
        return body.strip() or "(no output)"
    except Exception as e:
        return f"(command failed: {e})"


def main() -> int:
    now = datetime.now(timezone.utc)
    day = now.date().isoformat()
    out_path = OUT_DIR / f"{day}__openclaw-release-delta-snapshot.md"
    out_path.parent.mkdir(parents=True, exist_ok=True)

    sections = [
        ("openclaw --version", run(["openclaw", "--version"])),
        ("openclaw status", run(["openclaw", "status"])),
        ("openclaw update status", run(["openclaw", "update", "status"])),
    ]

    lines = [
        f"# OpenClaw release-delta snapshot ({day})",
        "",
        f"Generated at: {now.isoformat()}",
        "",
    ]
    for title, content in sections:
        lines.extend([f"## `{title}`", "```", content, "```", ""])

    out_path.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")
    print(f"wrote {out_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
