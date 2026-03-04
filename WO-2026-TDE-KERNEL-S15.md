# Work Order (WO) — TDE Kernel Slice S15

## Metadata
- WO-ID: WO-2026-TDE-KERNEL-S15
- Title: Runtime binding integrity and re-authorization on binding change
- Owner: JOB-PROD-001
- Date opened: 2026-03-04
- Lane: Build
- Work type: Feature
- Risk class: Medium-High

## One-page start packet

### Objective
Harden authority correctness by enforcing runtime job-binding integrity (`actor/job/session_key -> active binding`) and requiring explicit re-authorization when binding context changes.

### Why now
S12–S14 proved real-workload ingestion and guarded mutation execution. The next highest-risk gap is **context drift**: a mutation can still appear structurally valid while authority context has changed. S15 closes that gap.

### Scope (this slice only)
1. Add deterministic runtime binding resolver for mutation execution path.
2. Validate binding match across `actor_id`, `job_id`, and `session_key` against active binding record.
3. On binding change/mismatch, fail closed and require fresh policy decision (`policy_decision_id`) + new idempotency key.
4. Emit explicit audit reason codes for mismatch/rebind/re-authorize outcomes.
5. Add tests for pass + fail-closed + re-authorization-required paths.

### Non-goals
- Multi-job orchestration expansion
- Trello cutover expansion
- UI/control-panel changes
- Broad policy model redesign

### Acceptance criteria
1. Runtime mutation path rejects execution when active binding does not match envelope context.
2. Binding change path returns deterministic `REAUTH_REQUIRED_ON_BINDING_CHANGE` (or equivalent) and performs no side effects.
3. Re-authorized retry with fresh decision reference + idempotency key succeeds idempotently.
4. Evidence artifact contains: `job_id`, `actor_id`, `session_key`, `binding_id`, `binding_status`, `policy_decision_id`, `idempotency_key`, `result`, `reason`.
5. Existing S14 fail-closed guarantees remain intact.

### Planned change artifacts
- `tools/tde_job_tick_runner.py`
- `tools/tde_kernel_slice_tests.py`
- `os/sops/TDE_JOB_TICK_CONTRACT_V1.md` (update if contract fields/reason codes change)
- `knowledge/evidence/2026-03/2026-03-04__verification__wo-2026-tde-kernel-s15.md`
- `knowledge/evidence/2026-03/tde-job-tick-s15-pass.json`
- `knowledge/evidence/2026-03/tde-job-tick-s15-failclosed-binding-mismatch.json`
- `knowledge/evidence/2026-03/tde-job-tick-s15-reauth-required.json`

### Risks and controls
- **Risk:** false-positive binding mismatch blocks valid work.
  - **Control:** explicit reason codes + deterministic resolver + test fixtures.
- **Risk:** bypass via stale approval token reuse.
  - **Control:** enforce fresh `policy_decision_id` and fresh idempotency key on binding change.
- **Risk:** regression in existing S14 mutation envelope checks.
  - **Control:** run S14 regression tests in S15 verification bundle.

### Exit decision
GO to S16 only if all acceptance criteria pass with evidence artifacts and no side-effecting execution in mismatch paths.

## Closure
- Outcome summary: Implemented runtime binding-integrity checks against active binding object (`actor_id`/`job_id`/`session_key`/`binding_id`) in mutation path; binding mismatch now fails closed with explicit `REAUTH_REQUIRED_ON_BINDING_CHANGE` semantics and retry obligations (fresh `policy_decision_id` + fresh `idempotency_key`). Added deterministic evidence for pass + reauth-required + fail-closed mismatch paths.
- Accepted by: JOB-PROD-001 (execution baseline); JOB-ARC-001 formal sign-off pending
- Date closed: 2026-03-04
- Linked Change Artifact(s): `tools/tde_job_tick_runner.py`; `tools/test_s15_binding_integrity.py`; `os/runtime/tde_active_bindings.json`; `os/sops/TDE_JOB_TICK_CONTRACT_V1.md`; `knowledge/evidence/2026-03/tde-job-tick-s15-pass.json`; `knowledge/evidence/2026-03/tde-job-tick-s15-reauth-required.json`; `knowledge/evidence/2026-03/tde-job-tick-s15-failclosed-binding-mismatch.json`; `knowledge/evidence/2026-03/2026-03-04__verification__wo-2026-tde-kernel-s15.md`
