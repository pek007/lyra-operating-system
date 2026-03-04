#!/usr/bin/env python3
from __future__ import annotations

import json
import subprocess
from datetime import datetime, timezone
from pathlib import Path


def run(cmd: list[str]) -> str:
    return subprocess.check_output(cmd, text=True).strip()


def main() -> None:
    ts = datetime.now(timezone.utc).isoformat()

    payload = {
        "timestamp": ts,
        "checks": {
            "security_audit": run(["openclaw", "security", "audit"]),
            "sandbox_mode": run(["openclaw", "config", "get", "agents.defaults.sandbox.mode"]),
            "workspace_only": run(["openclaw", "config", "get", "tools.fs.workspaceOnly"]),
            "gateway_bind": run(["openclaw", "config", "get", "gateway.bind"]),
            "trusted_proxies": run(["openclaw", "config", "get", "gateway.trustedProxies"]),
            "telegram_group_policy": run(["openclaw", "config", "get", "channels.telegram.groupPolicy"]),
            "telegram_group_allow_from": run(["openclaw", "config", "get", "channels.telegram.groupAllowFrom"]),
            "telegram_groups": run(["openclaw", "config", "get", "channels.telegram.groups"]),
        },
    }

    out = Path("knowledge/evidence/2026-03-04__ops-2026-060-trust-boundary-validation-bundle.json")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(f"[PASS] wrote {out}")


if __name__ == "__main__":
    main()
