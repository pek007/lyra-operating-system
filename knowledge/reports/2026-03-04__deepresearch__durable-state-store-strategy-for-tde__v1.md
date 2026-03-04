# Durable State Store Strategy for TDE

Source: deep research report shared by Peter (2026-03-04)

## Executive recommendation (captured)
Adopt a single-node embedded durable state layer using **SQLite** with:
- append-only event log
- durable action/idempotency ledger
- materialized current-state tables

Treat `TASKS.md` as a **generated projection** during migration, not canonical write source.

## Why this is recommended
- Preserves current fail-closed safety invariants and authority checks.
- Improves concurrent writer safety via SQLite transactional boundary (WAL).
- Enables deterministic replay/recovery from durable events.
- Keeps migration practical within 2–4 sprints via dual-run cutover.
- Low operational overhead vs distributed data-layer alternatives.

## Option summary
1. **Recommended:** SQLite event log + projections (best balance)
2. Append-only NDJSON journal + snapshots (possible, more bespoke risk)
3. DB-backed current-state + audit table (good, less replay-first)

## Suggested phased rollout from report
- **Sprint 1:** State Layer v1 shadow mode (importer, dual-write verification)
- **Sprint 2:** Switch canonical writes to DB, export `TASKS.md` as projection
- **Sprint 3:** Add outbox for side effects + migrate small runtime state
- **Optional Sprint 4:** Expand first-class decision/approval tables

## Key acceptance criteria from report
- Fail-closed authority parity retained
- Durable idempotency ledger behavior retained
- Concurrent writer stress checks pass
- Rebuild-from-events deterministic match
- Crash consistency verified
- Backup/restore drill updated

## Notes
This report is aligned with current TDE hardening direction (S15–S30) and should drive the next implementation slice for production readiness.
