# Trello Retirement Design v1 (State-Based)

Status: Draft for definition phase  
Date: 2026-03-01  
Owner: Peter (A), Lyra (R)

## Purpose
Define a low-risk, state-based path to retire Trello as an operational dependency while preserving traceability and continuity.

## Principles
1. Single source of truth per phase
2. No uncontrolled dual-write
3. State/criteria gates (not calendar milestones)
4. Rollback must be cheap and explicit

## Target end-state
- TDE is canonical for task + decision + evidence/action linkage.
- Trello is read-only archive or fully retired.
- No operational write path depends on Trello tokens.

## Phase model (state-based)

### Phase A — Mapping/Contracts Frozen
Entry:
- Decision memo v2 adopted
- Start packet approved

Exit criteria:
- board/list/card -> TDE mapping approved
- lifecycle alias map approved (list -> canonical state)
- audit import level selected (A/B/C)
- reconciliation spec approved

### Phase B — Backfill Complete
Exit criteria:
- snapshot import complete for in-scope domain(s)
- external refs linked (card IDs/URLs)
- orphan checks pass
- export archive stored (with integrity hash)

### Phase C — Shadow Stable (TDE can track live deltas)
Exit criteria:
- webhook/poll delta capture stable
- daily reconciliation converges
- no sustained rate-limit failures

### Phase D — Canary Domain Live in TDE
Exit criteria:
- one domain slice runs end-to-end in TDE
- no Trello writes for that slice across multiple cadence cycles
- decision/evidence/audit chain complete

### Phase E — Progressive Expansion
Exit criteria:
- each new slice meets canary criteria before expansion
- drift remains bounded and explainable

### Phase F — Trello Read-Only Archive
Exit criteria:
- all operational domains TDE-canonical
- Trello used only for historical lookup
- write tokens removed from active automation paths

### Phase G — Trello Retired
Exit criteria:
- retention/export requirements satisfied
- runbooks/policies updated to Trello-free operation
- operational continuity proven without Trello access

## Risk controls
- Outbox-driven projection if temporary TDE->Trello visibility is needed
- Idempotency keys on sync actions
- Deterministic conflict handling and replay
- Explicit rollback triggers and reconciliation runbook

## Decision gate for build phase
Build phase should not proceed unless Phase A design artifacts are complete and reviewable.