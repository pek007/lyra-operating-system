# Verification — WO-2026-TDE-KERNEL-S15

Date: 2026-03-04
Owner: JOB-PROD-001
WO: `WO-2026-TDE-KERNEL-S15.md`

## Scope verified
- Runtime binding integrity check against active binding object (`actor_id`, `job_id`, `session_key`, `binding_id`)
- Deterministic fail-closed + re-authorization-required behavior on binding mismatch/change
- Fresh retry obligations surfaced in artifact (`fresh_policy_decision_id`, `fresh_idempotency_key`)
- Regression-safe execution path for valid binding context

## Commands executed
1. `python3 tools/test_s15_binding_integrity.py`
2. `python3 tools/tde_job_tick_runner.py ... --artifact-path knowledge/evidence/2026-03/tde-job-tick-s15-pass.json`
3. `python3 tools/tde_job_tick_runner.py ... --binding-id BIND-STALE-OLD --artifact-path knowledge/evidence/2026-03/tde-job-tick-s15-reauth-required.json`
4. `python3 tools/tde_job_tick_runner.py ... --actor-id not-lyra --artifact-path knowledge/evidence/2026-03/tde-job-tick-s15-failclosed-binding-mismatch.json`

## Results
- Unit/integration test script: **PASS** (`tools/test_s15_binding_integrity.py`)
- Pass path artifact: `knowledge/evidence/2026-03/tde-job-tick-s15-pass.json`
  - progressed: 1
  - reauth_required: 0
  - binding_status: active
- Reauth-required path artifact: `knowledge/evidence/2026-03/tde-job-tick-s15-reauth-required.json`
  - reauth_required: 1
  - fail_closed_reason: `REAUTH_REQUIRED_ON_BINDING_CHANGE`
  - writeback applied: false
- Fail-closed mismatch artifact: `knowledge/evidence/2026-03/tde-job-tick-s15-failclosed-binding-mismatch.json`
  - reauth_required: 1
  - fail_closed: true
  - mutation blocked due to binding mismatch in active context validation

## Acceptance criteria check (S15)
1. Reject mismatch vs active binding context: **PASS**
2. Binding-change/mismatch deterministic reauth-required behavior: **PASS**
3. Fresh retry obligations explicit: **PASS**
4. Artifact contains binding-context/audit fields: **PASS**
5. Existing envelope/fail-closed behavior retained: **PASS**

## Notes
- Verification used fixture task files under `knowledge/evidence/2026-03/tmp/` to avoid mutating canonical live board state while validating runtime behavior.
