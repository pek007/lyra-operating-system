# TDE Release Recovery Playbook v1

Status: Active
Owner: JOB-PROD-001
Date: 2026-03-04

## Purpose
Provide a deterministic, low-drama recovery sequence when TDE release/deployment behavior degrades or fails.

## Trigger conditions
Start this playbook when any of the following occurs:
- release gating fails repeatedly
- canary indicates degraded/blocked progression
- mutation path fail-closed loops persist
- runtime context mismatch or missing repo/toolchain is detected

## Phase 0 — Stabilize (0–10 min)
1. Freeze release progression decisions (no broadening scope).
2. Pause non-critical automations that amplify noise.
3. Open incident entry in `INCIDENT_LOG.md`.
4. Assign owner + timestamp for this recovery run.

## Phase 1 — Environment integrity gate (10–20 min)
Run:
```bash
cd ~/.openclaw/workspace/repos/lyra-operating-system
./tools/openclaw-preflight.sh --repo lyra-operating-system
```

If this fails:
- classify as `ENVIRONMENT_MISMATCH`
- do not continue release work until fixed
- use sandbox env doctor output as evidence artifact

## Phase 2 — Contract integrity gate (20–35 min)
Run thin-slice deterministic tests:
```bash
cd ~/.openclaw/workspace/repos/lyra-operating-system
python3 tools/tde_kernel_slice_tests.py
```

If failures occur:
- block rollout progression
- identify failing contract family (binding/objective/writeback)
- open targeted remediation task before retry

## Phase 3 — Runtime state verification (35–50 min)
Check:
- `os/runtime/tde_active_bindings.json` integrity and intended active binding
- `os/runtime/tde_objectives.json` integrity and checkpoint allowlists
- latest canary status artifact freshness and stall counters

Decision:
- If binding/objective mismatch persists, treat as authority issue, not delivery issue.

## Phase 4 — Controlled recovery path (50–80 min)
Choose exactly one path:
1. **Fix-forward (preferred):** minimal scoped patch to failing contract/path.
2. **Rollback:** revert to last known-good release envelope/commit for affected slice.

Rules:
- no parallel speculative fixes
- one change at a time + re-test after each
- maintain rollback checkpoint before each mutation

## Phase 5 — Re-validate and resume (80–100 min)
Required before resume:
1. Preflight passes
2. Thin-slice tests pass
3. Canary healthy for at least 2 consecutive cycles
4. No critical security findings after changes

Then:
- resume release progression in canary-first mode
- keep heightened monitoring window active for next 2 cycles

## Failure classification quick map
- `ENVIRONMENT_MISMATCH` → runtime/mount/toolchain issue
- `AUTHORITY_DRIFT` → binding/session/actor mismatch
- `OBJECTIVE_CONTRACT_FAILURE` → linkage/checkpoint/rationale missing
- `WRITEBACK_INTEGRITY_FAILURE` → atomicity/version conflict
- `CANARY_DEGRADATION` → stale/degraded canary or guardrail violation

## Evidence checklist
Attach to incident/release record:
- preflight output
- tde kernel test output
- canary artifact snapshot
- exact commands executed
- fix-forward or rollback decision rationale
- resume timestamp and first clean cycle evidence
