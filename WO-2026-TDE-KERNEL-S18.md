# Work Order (WO) — TDE Kernel Slice S18

## Metadata
- WO-ID: WO-2026-TDE-KERNEL-S18
- Title: Atomic/locked TASKS writeback for job tick runner
- Owner: JOB-PROD-001
- Date opened: 2026-03-04
- Lane: Build
- Work type: Hardening
- Risk class: High

## Intent
Prevent concurrent write corruption/lost updates by introducing lock + atomic file replacement semantics in TASKS writeback path.

## Acceptance Criteria
1. Writeback acquires exclusive lock with timeout behavior.
2. File writes use atomic replace flow.
3. Concurrent write attempts do not corrupt TASKS structure.
4. Verification includes concurrency test and evidence artifact.

## Closure
- Outcome summary: Implemented lock-file based exclusive write access (`fcntl`) with timeout reason `write_lock_timeout` and atomic write via fsync + replace.
- Accepted by: JOB-PROD-001 (execution baseline); JOB-ARC-001 formal sign-off pending
- Date closed: 2026-03-04
- Linked Change Artifact(s): `tools/tde_job_tick_runner.py`; `tools/test_s18_atomic_writeback.py`
