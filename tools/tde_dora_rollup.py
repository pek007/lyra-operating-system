#!/usr/bin/env python3
from __future__ import annotations

import re
from datetime import datetime, timezone
from pathlib import Path

WO_RE = re.compile(r"WO-2026-TDE-KERNEL-S(\d+)\.md$")
DATE_CLOSED_RE = re.compile(r"^- Date closed: (.+)$", re.MULTILINE)


def _parse_closed_date(text: str) -> str | None:
    m = DATE_CLOSED_RE.search(text)
    if not m:
        return None
    raw = m.group(1).strip()
    if raw.startswith("_Pending"):
        return None
    return raw


def main() -> None:
    root = Path(".")
    wos = sorted(root.glob("WO-2026-TDE-KERNEL-S*.md"))

    closed = []
    for wo in wos:
        m = WO_RE.search(wo.name)
        if not m:
            continue
        text = wo.read_text(encoding="utf-8")
        dc = _parse_closed_date(text)
        if dc:
            closed.append((int(m.group(1)), dc, wo.name))

    now = datetime.now(timezone.utc).isoformat()
    out = Path("knowledge/evidence/metrics/TDE_DORA_WEEKLY.md")
    out.parent.mkdir(parents=True, exist_ok=True)

    lines = [
        "# TDE DORA Weekly (Proxy)",
        "",
        f"Generated: {now}",
        "Boundary: merge-on-main + activation evidence (proxy v1)",
        "",
        "## Snapshot",
        f"- Closed kernel slices counted: {len(closed)}",
        f"- Deployment Frequency (proxy): {len(closed)} closed slices total (weekly trend automation pending)",
        "- Lead Time: pending per-slice timestamp extraction automation",
        "- Change Failure Rate: pending aggregation",
        "- Failed Deployment Recovery Time: pending aggregation",
        "- Deployment Rework Rate: pending aggregation",
        "",
        "## Closed slices observed",
    ]
    for sid, dc, name in closed[-12:]:
        lines.append(f"- S{sid}: {name} (closed: {dc})")

    out.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"[PASS] wrote {out}")


if __name__ == "__main__":
    main()
