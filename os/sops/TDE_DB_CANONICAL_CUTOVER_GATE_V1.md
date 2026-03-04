# TDE DB Canonical Cutover Gate v1

Status: Active
Owner: JOB-PROD-001
Date: 2026-03-04

## Purpose
Define hard GO/NO-GO criteria before switching canonical TDE task state from markdown SoR to DB SoR.

## Observation window
- Minimum: 3 consecutive days of scheduled dual-run shadow operation.

## Must-pass criteria
1. Shadow parity drift
   - Consecutive mismatches/errors must stay below threshold (default: < 3).
   - No unresolved drift incidents in observation window.
2. Ledger continuity
   - Shadow `actions` and `events` entries present for scheduled ticks.
   - No broken hash-chain write failures reported.
3. Runtime safety parity
   - Existing fail-closed authority/objective checks remain passing.
4. Regression suite
   - S15/S16/S17/S18/S32/S33/S35 tests passing.
5. Security posture
   - `openclaw security audit` has no critical findings.

## GO decision requires
- Explicit owner approval
- Linked evidence artifact from readiness report
- Rollback confirmation checklist ready

## Rollback trigger
Any parity drift burst, ledger failure, or regression failure during cutover window.
