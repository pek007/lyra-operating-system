#!/usr/bin/env python3
from __future__ import annotations

import glob
import json
import sqlite3
from datetime import datetime, timezone
from pathlib import Path


def _load_alerts(path: Path) -> list[dict]:
    rows: list[dict] = []
    if not path.exists():
        return rows
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line:
            continue
        try:
            rows.append(json.loads(line))
        except Exception:
            continue
    return rows


def _latest_report_path(exclude: Path | None = None) -> Path | None:
    files = sorted(glob.glob("knowledge/evidence/metrics/*__tde-db-cutover-readiness-report-v1.json"))
    if exclude is not None:
        files = [f for f in files if Path(f) != exclude]
    return Path(files[-1]) if files else None


def main() -> None:
    now = datetime.now(timezone.utc)
    date_tag = now.strftime("%Y-%m-%d")

    alert_path = Path("knowledge/evidence/metrics/tde-shadow-state-alerts.jsonl")
    latest_tick = Path("knowledge/evidence/2026-03/tde-job-tick-latest.json")
    db_path = Path("os/runtime/tde_state.sqlite")

    alerts = _load_alerts(alert_path)

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
        try:
            actions = conn.execute("SELECT COUNT(*) FROM actions").fetchone()[0]
            events = conn.execute("SELECT COUNT(*) FROM events").fetchone()[0]
        finally:
            conn.close()

    verdict = "GO_CANDIDATE" if (parity_ok and actions > 0 and events > 0) else "NO_GO"

    dated = Path(f"knowledge/evidence/metrics/{date_tag}__tde-db-cutover-readiness-report-v1.json")
    previous = _latest_report_path(exclude=dated)
    report = {
        "timestamp": now.isoformat(),
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
        "evidence": {
            "report_date": date_tag,
            "previous_report": str(previous) if previous else None,
        },
        "note": "GO_CANDIDATE is preliminary and requires observation-window completion + explicit owner approval.",
    }

    out_dir = Path("knowledge/evidence/metrics")
    out_dir.mkdir(parents=True, exist_ok=True)

    latest = out_dir / "tde-db-cutover-readiness-report-latest.json"

    payload = json.dumps(report, indent=2) + "\n"
    dated.write_text(payload, encoding="utf-8")
    latest.write_text(payload, encoding="utf-8")

    print(f"[PASS] wrote {dated}")
    print(f"[PASS] wrote {latest}")


if __name__ == "__main__":
    main()
