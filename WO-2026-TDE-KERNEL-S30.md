# Work Order (WO) — TDE Kernel Slice S30

## Metadata
- WO-ID: WO-2026-TDE-KERNEL-S30
- Title: Lead-time fidelity improvement (first commit -> first activation)
- Owner: JOB-PROD-001
- Date opened: 2026-03-04
- Lane: Build
- Work type: Metrics automation
- Risk class: Medium

## Closure
- Outcome summary: Enhanced DORA rollup to compute lead-time proxy from first slice commit timestamp to first activation evidence timestamp and exposed it in snapshot + per-slice table.
- Accepted by: JOB-PROD-001
- Date closed: 2026-03-04
- Linked Change Artifact(s): `tools/tde_dora_rollup.py`; `knowledge/evidence/metrics/TDE_DORA_WEEKLY.md`
