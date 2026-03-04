# Work Order (WO) — TDE Kernel Slice S25

## Metadata
- WO-ID: WO-2026-TDE-KERNEL-S25
- Title: Binding lifecycle semantics (active/expired/revoked) and fail-closed rotation guard
- Owner: JOB-PROD-001
- Date opened: 2026-03-04
- Lane: Build
- Work type: Hardening
- Risk class: High

## Closure
- Outcome summary: Added binding lifecycle handling in active-binding resolution (`active` required; `revoked`/`expired`/invalid-expiry treated as unresolved) and preserved fail-closed mutation behavior. Added lifecycle regression tests and updated runtime registry baseline with explicit expiry metadata.
- Accepted by: JOB-PROD-001
- Date closed: 2026-03-04
- Linked Change Artifact(s): `tools/tde_job_tick_runner.py`; `tools/test_s25_binding_lifecycle.py`; `os/runtime/tde_active_bindings.json`; `os/sops/TDE_JOB_TICK_CONTRACT_V1.md`; `.github/workflows/devsecops-baseline.yml`
