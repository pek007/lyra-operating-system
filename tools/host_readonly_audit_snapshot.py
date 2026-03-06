#!/usr/bin/env python3
from __future__ import annotations

import shutil
import subprocess
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT_DIR = ROOT / "knowledge" / "evidence"


def run_cmd(cmd: list[str]) -> tuple[int, str]:
    try:
        p = subprocess.run(cmd, cwd=ROOT, capture_output=True, text=True, check=False)
        out = ((p.stdout or "") + ("\n" + p.stderr if p.stderr else "")).strip()
        return p.returncode, out or "(no output)"
    except Exception as e:
        return 127, f"command failed: {e}"


def section(title: str, cmd: list[str]) -> str:
    exe = cmd[0]
    if shutil.which(exe) is None and not exe.startswith("/"):
        return f"## `{title}`\n```\nSKIPPED: command not found: {exe}\n```\n"

    code, out = run_cmd(cmd)
    note = ""
    if code != 0:
        note = f"\nNOTE: non-zero exit ({code}). Treat as signal, not hard-fail; investigate if persistent."
    return f"## `{title}`\n```\n{out}\n```{note}\n"


def main() -> int:
    now = datetime.now(timezone.utc)
    day = now.date().isoformat()
    out_path = OUT_DIR / day[:7] / f"{now.strftime('%Y%m%d-%H%M%S')}__host-readonly-audit.md"
    out_path.parent.mkdir(parents=True, exist_ok=True)

    blocks = [
        "# Host read-only audit snapshot",
        "",
        f"Generated at: {now.isoformat()}",
        "",
        section("lsof -nP -iTCP -sTCP:LISTEN", ["lsof", "-nP", "-iTCP", "-sTCP:LISTEN"]),
        section("socketfilterfw --getglobalstate", ["/usr/libexec/ApplicationFirewall/socketfilterfw", "--getglobalstate"]),
        section("pfctl -s info", ["pfctl", "-s", "info"]),
        "Manual escalation: if PF status remains unavailable, run `sudo pfctl -s info` directly on host and attach output.",
        "",
    ]

    out_path.write_text("\n".join(blocks), encoding="utf-8")
    print(f"wrote {out_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
