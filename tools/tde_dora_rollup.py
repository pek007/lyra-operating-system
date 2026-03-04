#!/usr/bin/env python3
from __future__ import annotations

import json
import re
import subprocess
from collections import defaultdict
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path

WO_RE = re.compile(r"WO-2026-TDE-KERNEL-S(\d+)\.md$")
DATE_OPENED_RE = re.compile(r"^- Date opened: (.+)$", re.MULTILINE)
DATE_CLOSED_RE = re.compile(r"^- Date closed: (.+)$", re.MULTILINE)
ARTIFACT_S_RE = re.compile(r"tde-job-tick-s(\d+)-.*\.json$")
S_IN_MSG_RE = re.compile(r"\bS(\d{1,3})\b")


@dataclass
class SliceRow:
    sid: int
    wo: str
    opened: datetime | None
    closed: datetime | None
    lead_days: float | None
    lead_commit_to_activation_hours: float | None
    activations: int
    fails: int
    passes: int
    recovery_hours: float | None
    commit_count: int
    rework_commits: int


def _parse_day(raw: str | None) -> datetime | None:
    if not raw:
        return None
    s = raw.strip()
    if not s or s.startswith("_Pending"):
        return None
    try:
        return datetime.fromisoformat(s + "T00:00:00+00:00")
    except Exception:
        return None


def _parse_wo_dates(text: str) -> tuple[datetime | None, datetime | None]:
    mo = DATE_OPENED_RE.search(text)
    mc = DATE_CLOSED_RE.search(text)
    opened = _parse_day(mo.group(1) if mo else None)
    closed = _parse_day(mc.group(1) if mc else None)
    return opened, closed


def _safe_ts(raw: str | None) -> datetime | None:
    if not raw:
        return None
    try:
        return datetime.fromisoformat(raw.replace("Z", "+00:00"))
    except Exception:
        return None


def _git_commits_by_slice() -> dict[int, list[tuple[str, datetime]]]:
    out = subprocess.check_output([
        "git",
        "log",
        "--pretty=format:%H\t%cI\t%s",
    ], text=True)

    by_slice: dict[int, list[tuple[str, datetime]]] = defaultdict(list)
    for line in out.splitlines():
        parts = line.split("\t", 2)
        if len(parts) != 3:
            continue
        h, iso_ts, msg = parts
        try:
            ts = datetime.fromisoformat(iso_ts.replace("Z", "+00:00"))
        except Exception:
            continue
        matches = S_IN_MSG_RE.findall(msg)
        for m in matches:
            sid = int(m)
            by_slice[sid].append((h, ts))
    return by_slice


def main() -> None:
    root = Path(".")
    wos = sorted(root.glob("WO-2026-TDE-KERNEL-S*.md"))

    wo_map: dict[int, tuple[str, datetime | None, datetime | None]] = {}
    for wo in wos:
        m = WO_RE.search(wo.name)
        if not m:
            continue
        sid = int(m.group(1))
        text = wo.read_text(encoding="utf-8")
        opened, closed = _parse_wo_dates(text)
        wo_map[sid] = (wo.name, opened, closed)

    events: dict[int, list[tuple[datetime | None, bool]]] = defaultdict(list)
    for p in root.glob("knowledge/evidence/**/*.json"):
        m = ARTIFACT_S_RE.search(p.name)
        if not m:
            continue
        sid = int(m.group(1))
        try:
            payload = json.loads(p.read_text(encoding="utf-8"))
        except Exception:
            continue
        ts = _safe_ts(payload.get("timestamp"))
        fail = bool(payload.get("fail_closed")) or payload.get("status") in {"failed_validation", "reauth_required"}
        events[sid].append((ts, fail))

    commits_by_slice = _git_commits_by_slice()

    rows: list[SliceRow] = []
    for sid, (woname, opened, closed) in sorted(wo_map.items()):
        ev = events.get(sid, [])
        activations = len(ev)
        fails = sum(1 for _, is_fail in ev if is_fail)
        passes = sum(1 for _, is_fail in ev if not is_fail)

        lead_days = None
        if opened and closed:
            lead_days = (closed - opened).total_seconds() / 86400.0

        recovery_hours = None
        fail_ts = [t for t, is_fail in ev if is_fail and t]
        pass_ts = [t for t, is_fail in ev if (not is_fail) and t]
        if fail_ts and pass_ts:
            first_fail = min(fail_ts)
            first_pass_after = min([t for t in pass_ts if t >= first_fail], default=None)
            if first_pass_after:
                recovery_hours = (first_pass_after - first_fail).total_seconds() / 3600.0

        commits = commits_by_slice.get(sid, [])
        commit_count = len(commits)
        rework_commits = max(0, commit_count - 1)

        lead_commit_to_activation_hours = None
        commit_ts = [ts for _, ts in commits]
        activation_ts = [t for t, _ in ev if t]
        if commit_ts and activation_ts:
            first_commit = min(commit_ts)
            first_activation = min(activation_ts)
            if first_activation >= first_commit:
                lead_commit_to_activation_hours = (first_activation - first_commit).total_seconds() / 3600.0

        rows.append(
            SliceRow(
                sid=sid,
                wo=woname,
                opened=opened,
                closed=closed,
                lead_days=lead_days,
                lead_commit_to_activation_hours=lead_commit_to_activation_hours,
                activations=activations,
                fails=fails,
                passes=passes,
                recovery_hours=recovery_hours,
                commit_count=commit_count,
                rework_commits=rework_commits,
            )
        )

    now = datetime.now(timezone.utc)
    out = Path("knowledge/evidence/metrics/TDE_DORA_WEEKLY.md")
    out.parent.mkdir(parents=True, exist_ok=True)

    closed_recent = [r for r in rows if r.closed and (now - r.closed).days <= 7]
    dep_freq_week = len(closed_recent)
    rows_with_activation = [r for r in rows if r.activations > 0]
    fail_rate = (sum(1 for r in rows_with_activation if r.fails > 0) / len(rows_with_activation) * 100.0) if rows_with_activation else 0.0

    lead_vals = [r.lead_days for r in rows if r.lead_days is not None]
    avg_lead = (sum(lead_vals) / len(lead_vals)) if lead_vals else None

    lead_ca_vals = [r.lead_commit_to_activation_hours for r in rows if r.lead_commit_to_activation_hours is not None]
    avg_lead_ca = (sum(lead_ca_vals) / len(lead_ca_vals)) if lead_ca_vals else None

    rec_vals = [r.recovery_hours for r in rows if r.recovery_hours is not None]
    avg_recovery = (sum(rec_vals) / len(rec_vals)) if rec_vals else None

    slices_with_commits = [r for r in rows if r.commit_count > 0]
    rework_rate = (
        sum(r.rework_commits for r in slices_with_commits) / sum(r.commit_count for r in slices_with_commits) * 100.0
        if slices_with_commits else 0.0
    )

    lines = [
        "# TDE DORA Weekly (Proxy)",
        "",
        f"Generated: {now.isoformat()}",
        "Boundary: merge-on-main + activation evidence (proxy v1)",
        "",
        "## Snapshot",
        f"- Deployment Frequency (last 7d, proxy): {dep_freq_week} closed slices",
        f"- Lead Time for Changes (avg, opened->closed proxy): {avg_lead:.2f} days" if avg_lead is not None else "- Lead Time for Changes: insufficient data",
        f"- Lead Time for Changes (avg, first-commit->first-activation proxy): {avg_lead_ca:.2f} hours" if avg_lead_ca is not None else "- Lead Time (commit->activation): insufficient data",
        f"- Change Failure Rate (slice-level proxy): {fail_rate:.1f}% ({sum(1 for r in rows_with_activation if r.fails > 0)}/{len(rows_with_activation)})",
        f"- Failed Deployment Recovery Time (avg proxy): {avg_recovery:.2f} hours" if avg_recovery is not None else "- Failed Deployment Recovery Time: insufficient fail->pass timestamp pairs",
        f"- Deployment Rework Rate (commit proxy): {rework_rate:.1f}%",
        "",
        "## Slice details (recent)",
        "| Slice | WO | Lead(d) | Lead C->A(h) | Activations | Fails | Passes | Recovery(h) | Commits | Rework commits |",
        "|---|---|---:|---:|---:|---:|---:|---:|---:|---:|",
    ]

    for r in sorted(rows, key=lambda x: x.sid)[-15:]:
        lead_str = f"{r.lead_days:.2f}" if r.lead_days is not None else "n/a"
        lead_ca_str = f"{r.lead_commit_to_activation_hours:.2f}" if r.lead_commit_to_activation_hours is not None else "n/a"
        rec_str = f"{r.recovery_hours:.2f}" if r.recovery_hours is not None else "n/a"
        lines.append(
            f"| S{r.sid} | {r.wo} | {lead_str} | {lead_ca_str} | {r.activations} | {r.fails} | {r.passes} | {rec_str} | {r.commit_count} | {r.rework_commits} |"
        )

    out.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"[PASS] wrote {out}")


if __name__ == "__main__":
    main()
