#!/usr/bin/env python3
from __future__ import annotations

import json
import shutil
from pathlib import Path


def main() -> None:
    config = Path.home() / ".openclaw" / "openclaw.json"
    if not config.exists():
        raise SystemExit("[FAIL] missing ~/.openclaw/openclaw.json")

    payload = json.loads(config.read_text(encoding="utf-8"))
    mode = (
        payload.get("agents", {})
        .get("defaults", {})
        .get("sandbox", {})
        .get("mode", "off")
    )

    if mode != "off" and shutil.which("docker") is None:
        raise SystemExit(
            f"[FAIL] sandbox mode is '{mode}' but docker is unavailable in PATH; keep mode=off or install docker before change"
        )

    print(f"[PASS] sandbox preflight OK (mode={mode})")


if __name__ == "__main__":
    main()
