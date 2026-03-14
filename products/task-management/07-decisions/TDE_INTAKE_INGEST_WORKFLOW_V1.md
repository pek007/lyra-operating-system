# TDE Intake Ingest Workflow v1

Status: Draft active
Owner: Peter + Lyra
Product: Task Management (`A-007`)
Date: 2026-03-14
Related:
- `products/task-management/06-architecture/TDE_INTAKE_INTERFACE_CONTRACT_V1.md`
- `products/task-management/06-architecture/TDE_PO_NIGHTLY_REPORT_ADAPTER_CONTRACT_V1.md`
- `tools/tde_intake_ingest.py`

## Purpose
Define the first thin runtime ingest path for canonical TDE intake packets.

This workflow turns validated intake packets into persisted TDE intake records with idempotency and a first bounded triage outcome.

## Scope
This v1 workflow supports:
- canonical `tde_intake_packet` ingestion
- idempotency/deduplication by `intake_id`
- persistence of raw packet and triage outcome
- first bounded triage for `intake_class = signal`

This v1 workflow does not yet:
- create canonical tasks or decisions automatically from ingest
- support all intake classes
- apply deep policy families or enrichment chains

## Workflow shape
### Step 1 — Validate packet
Validate the incoming `tde_intake_packet` against the registered schema.

### Step 2 — Idempotency check
Check whether `intake_id` already exists.

Outcomes:
- same packet hash -> return duplicate result
- different packet hash -> fail closed with idempotency conflict

### Step 3 — Persist raw packet
Persist the packet in canonical intake storage so the original input remains replayable and auditable.

### Step 4 — Triage
Apply a first bounded triage policy.

For `signal` packets, current outcomes are:
- `record_only`
- `update_existing`
- `create_decision`
- `create_work`

### Step 5 — Persist outcome
Persist:
- triage outcome
- outcome detail JSON
- related entity links
- event/action records for auditability

## First signal triage policy
### `update_existing`
Use when the signal already links to existing TDE items.

### `create_decision`
Use when the signal contains unlinked decision blockers.

### `create_work`
Use when the signal proposes actionable follow-up under a yellow/red health signal and no linked existing item covers it.

### `record_only`
Use when no promotion threshold is met.

## Implementation note
The first implementation now exists at:
- `tools/tde_intake_ingest.py`

## Current architectural stance
This workflow is intentionally thin.

It creates:
- canonical intake persistence
- idempotency behavior
- first triage outcomes

It does not yet collapse ingest, decisioning, and creation into one opaque step.
That separation is deliberate so routing behavior remains inspectable.
