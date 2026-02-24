# OPS-001: Backup & Restore Runbook

## Purpose
Ensure data and operational continuity with tested backup/restore procedures.

## Scope
Covers critical operating-system artifacts and OpenClaw workspace continuity.

## Recovery Targets
- **RTO (Recovery Time Objective):** 4 hours (initial target)
- **RPO (Recovery Point Objective):** 24 hours (initial target)

## Critical Assets
- Workspace docs (`/Users/lyra/.openclaw/workspace`)
- Git history for operating-system files
- OpenClaw config/state (as applicable)
- Key runbooks, policies, registries

## Backup Baseline
1. Ensure automated local backup is enabled (e.g., Time Machine)
2. Ensure workspace is versioned in Git and committed regularly
3. Keep at least one off-device/offsite copy path (to be finalized)

## Weekly Backup Check
- Confirm latest backup timestamp
- Confirm latest git commit recency
- Confirm critical docs exist and are readable

## Monthly Restore Test (required)
1. Select sample files:
   - `CONTROL_PANEL.md`
   - `MISSION.md`
   - `TASKS.md`
2. Restore to a test location (not overwrite production)
3. Verify file integrity and readability
4. Record results in `RESTORE_TEST_LOG.md`

## Failure Handling
If backup/restore check fails:
1. Open incident (SEV-2 if no viable backup exists)
2. Notify Peter
3. Fix backup configuration immediately
4. Re-run restore test and document evidence

## Evidence Files
- `RESTORE_TEST_LOG.md`
- `METRICS_WEEKLY.md` note (backup status)

## Version
- v1.0
- Date: 2026-02-24
