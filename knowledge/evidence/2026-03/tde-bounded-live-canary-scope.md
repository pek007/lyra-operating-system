# TDE Bounded Live Canary Scope

Date: 2026-03-10
Status: Draft scope declaration
Owner: Lyra
Linked WO: `WO-2026-TDE-KERNEL-S26`

## Selected canary domain

**Canary domain:** TDE-internal kernel work execution for `JOB-PROD-001` inside `repos/lyra-operating-system/TASKS.md`.

This is the narrowest credible live slice because:
- the runtime already proved real-task ingestion from canonical task state
- the runtime already proved one idempotent audited writeback on real workload
- the domain is internal, bounded, and reversible
- it avoids premature expansion into broader task-management or external system cutover

## Authority posture

During the bounded live window:
- `repos/lyra-operating-system/TASKS.md` is the **canonical source of truth** for the canary slice
- TDE runtime may read from and perform its already-proven low-risk writeback path within that bounded slice only
- Trello and any other legacy systems are **out of scope as operational authorities** for this slice
- no uncontrolled dual-write is permitted

## In-scope objects

The initial bounded slice includes only:
1. `JOB-PROD-001`-executed TDE kernel work items
2. task records in `TASKS.md` whose IDs begin with `TDE-2026-`
3. state transitions limited to already-proven low-risk task-lane movement and audit-linked mutation behavior
4. evidence artifacts produced under `knowledge/evidence/2026-03/` for each cycle

## Explicitly excluded

Out of scope for the canary window:
- non-TDE work items (`OPS-*`, `SEC-*`, `IMP-*`, etc.)
- multi-domain task-management cutover
- external system cutover or Trello retirement execution
- approval-boundary relaxation
- any new mutation type beyond the currently evidenced low-risk path

## Object inventory rule

Before GO, the canary inventory must list every open `TDE-2026-*` task in the active operating file and classify each as one of:
- in-scope canary object
- explicitly excluded
- blocked pending prerequisite

## Success condition

The canary window succeeds only if:
- TDE can operate the bounded `TDE-2026-*` slice across multiple cadence cycles
- no out-of-scope task is mutated
- no uncontrolled authority ambiguity appears
- the operator can explain state from TDE/TASKS/evidence artifacts alone

## Rollback posture

If any rollback trigger fires, the system reverts immediately to non-live-cutover posture for this slice, preserves all evidence, and resumes manual/operator-mediated task handling until the gap is fixed.
