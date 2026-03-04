# CONTROL_TOWER_MVP_VIEWS_SPEC.md

## Purpose
Define the first Control Panel views for fast operational transparency.

## View 1 — Now
Shows live operational state:
- Active tasks (from TASKS/Trello sync)
- Running/failed cron jobs
- Latest security/doctor evidence status
- Open incidents

## View 2 — Next
Shows prioritized upcoming work:
- Top active items by priority and due risk
- Upcoming scheduled reviews (subscription, access, security)
- Blocked items requiring human decision

## View 3 — Watch
Risk and reliability watchlist:
- Security warnings trend
- Cost/usage anomalies (Brave/OpenRouter)
- Automation failures (sync/evidence jobs)
- Drift alerts (stale registries/reviews)

## View 4 — Change Feed
Audit-style recent changes:
- Policy/routing edits
- Runbook changes
- Task state transitions
- Evidence entries created
- Git commit summaries

## Data Sources
- `TASKS.md`
- `knowledge/evidence/*`
- `RISK_REGISTER.md`
- `SUBSCRIPTION_REGISTER.md`
- `PROCESS_REGISTRY.md`
- git log summaries

## MVP UX Rules
- High signal, low clutter
- One-click drill-down to source file
- Explicit status colors: pass/warn/fail
- Time-stamped freshness indicators

## Non-goals (MVP)
- Full custom app with auth/roles
- Rich real-time charts
- Bi-directional arbitrary editing across all docs

## Version
- v1.0
- Date: 2026-02-25
