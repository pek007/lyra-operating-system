# TDE Bounded Live Canary Backup and Rollback Posture

Date: 2026-03-10
Status: Draft execution posture
Owner: Lyra
Linked WO: `WO-2026-TDE-KERNEL-S26`

## Scope
This posture applies only to the bounded canary slice:
- `JOB-PROD-001`
- open `TDE-2026-*` work in `repos/lyra-operating-system/TASKS.md`

## Backup approach before each live canary cycle
1. Create a point-in-time backup copy of `TASKS.md`.
2. Store it under `knowledge/evidence/2026-03/backups/` with timestamp in filename.
3. Record the backup path in the cycle execution evidence.

## Reconciliation source of truth
- Primary state file: `TASKS.md`
- Cycle evidence artifact: per-run `tde-job-tick-*.json`
- Supporting packet artifacts: canary scope, inventory/provenance check, readiness, runbook, owner packet

## Rollback procedure for this slice
If a rollback trigger fires:
1. Stop the canary sequence.
2. Restore `TASKS.md` from the most recent pre-cycle backup.
3. Preserve both the failed cycle artifact and the restored backup path.
4. Reconcile expected canary object set against restored `TASKS.md`.
5. Publish discrepancy note with root-cause classification.

## Rollback owner and route
- Operator: Lyra / JOB-PROD-001
- Decision visibility: Peter remains owner-visible decision point for expand/hold/rollback after bounded run evidence

## Current adequacy assessment
This rollback posture is sufficient for a one-object internal repo-local canary because:
- the mutation surface is narrow
- the state file is text and easily versioned/restored
- the object inventory is currently one open task
- evidence artifacts can be preserved independently of task-state restoration
