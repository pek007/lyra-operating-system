#!/usr/bin/env python3
from __future__ import annotations

import json
import sqlite3
from datetime import datetime, timezone
from pathlib import Path


def main() -> None:
    alert_path = Path("knowledge/evidence/metrics/tde-shadow-state-alerts.jsonl")
    latest_tick = Path("knowledge/evidence/2026-03/tde-job-tick-latest.json")
    db_path = Path("os/runtime/tde_state.sqlite")

    alerts = []
    if alert_path.exists():
        for line in alert_path.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if not line:
                continue
            try:
                alerts.append(json.loads(line))
            except Exception:
                pass

    consecutive_failures = 0
    for row in reversed(alerts):
        if row.get("status") in {"mismatch", "error"}:
            consecutive_failures += 1
        else:
            break

    threshold = 3
    parity_ok = consecutive_failures < threshold

    latest_shadow = {}
    if latest_tick.exists():
        try:
            latest_shadow = json.loads(latest_tick.read_text(encoding="utf-8")).get("shadow_state", {})
        except Exception:
            latest_shadow = {}

    actions = events = 0
    if db_path.exists():
        conn = sqlite3.connect(str(db_path))
        actions = conn.execute("SELECT COUNT(*) FROM actions").fetchone()[0]
        events = conn.execute("SELECT COUNT(*) FROM events").fetchone()[0]

    verdict = "GO_CANDIDATE" if (parity_ok and actions > 0 and events > 0) else "NO_GO"

    report = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "gate": "TDE_DB_CANONICAL_CUTOVER_GATE_V1",
        "verdict": verdict,
        "checks": {
            "parity_consecutive_failures": consecutive_failures,
            "parity_threshold": threshold,
            "parity_ok": parity_ok,
            "latest_shadow_status": latest_shadow.get("status"),
            "actions_count": actions,
            "events_count": events,
        },
        "note": "GO_CANDIDATE here is preliminary and still requires 3-day observation + explicit owner approval.",
    }

    out = Path("knowledge/evidence/metrics/2026-03-04__tde-db-cutover-readiness-report-v1.json")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(f"[PASS] wrote {out}")


if __name__ == "__main__":
    main()
