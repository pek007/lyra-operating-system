# Work Order (WO) — TDE Kernel Slice S16

## Metadata
- WO-ID: WO-2026-TDE-KERNEL-S16
- Title: Objective-to-work linkage contract and artifact wiring
- Owner: JOB-PROD-001
- Date opened: 2026-03-04
- Lane: Build
- Work type: Feature
- Risk class: Medium

## Intent
- Objective: Make each active TDE task/dependency traceable to objective context (`objective_id`, checkpoint, rationale trace) so execution state ties directly to strategic outcomes.
- Why now: S15 hardened mutation authority; next bottleneck is decision-quality traceability from execution to objective intent.
- Non-goals: Objective model redesign, portfolio planning redesign, UI overhaul.

## Scope
1. Define a minimal objective-linkage contract for task/dependency artifacts.
2. Add deterministic validation for required linkage fields on in-scope TDE runtime artifacts.
3. Wire linkage fields into relevant artifact emissions.
4. Produce verification evidence for pass + fail-closed/validation paths.

## Acceptance Criteria
1. Contract fields are explicit and documented (`objective_id`, `objective_checkpoint`, `rationale_trace`).
2. New artifact emissions include linkage fields where required.
3. Missing linkage in required path is surfaced deterministically (validation error/fail-closed for guarded paths).
4. Verification artifact demonstrates both compliant and non-compliant cases.

## Planned change artifacts
- `os/sops/TDE_JOB_TICK_CONTRACT_V1.md` (or new objective-linkage SOP if cleaner)
- `tools/tde_job_tick_runner.py` (if artifact schema update needed)
- `tools/tde_kernel_slice_tests.py` and/or focused S16 tests
- `knowledge/evidence/2026-03/2026-03-04__verification__wo-2026-tde-kernel-s16.md`

## Closure
- Outcome summary: _Pending_
- Accepted by: _Pending_
- Date closed: _Pending_
- Linked Change Artifact(s): _Pending_
