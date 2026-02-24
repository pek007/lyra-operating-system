# Control Panel MVP — Implementation Cuts (Distilled)

## Goal
Deliver a practical MVP without rebuilding the platform.

## MVP Scope (4 weeks)

### Cut 1 — Data contracts (week 1)
- Standardize YAML/frontmatter schema for registries:
  - agent contract
  - routing rule
  - evidence record
  - change record
- Ensure machine-readable ingest from existing markdown docs.

### Cut 2 — Event + evidence ingestion (week 2)
- Ingest OpenClaw status/security/doctor outputs on schedule.
- Normalize logs into evidence entries.
- Link evidence to task IDs and risk items.

### Cut 3 — Operator views (week 3)
- Control Tower home (Now/Next/Watch/Change feed)
- Evidence registry view
- Routing scorecard view

### Cut 4 — Governance gates (week 4)
- Type-1 change gate: rationale + rollback + review date required
- Monthly anti-thrash routing update process
- Exportable evidence pack for due diligence

## Non-goals (for MVP)
- Full custom app framework rebuild
- Complex real-time telemetry stack migration
- Perfect bi-directional sync across all systems

## Immediate Value
- Higher transparency
- Better risk/compliance posture
- Faster operator decision-making
- Reduced model-cost drift
