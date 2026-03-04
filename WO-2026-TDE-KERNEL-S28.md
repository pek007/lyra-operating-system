# Work Order (WO) — TDE Kernel Slice S28

## Metadata
- WO-ID: WO-2026-TDE-KERNEL-S28
- Title: DORA rollup enhancement with per-slice lead/failure/recovery proxies
- Owner: JOB-PROD-001
- Date opened: 2026-03-04
- Lane: Build
- Work type: Metrics automation
- Risk class: Medium

## Closure
- Outcome summary: Enhanced `tools/tde_dora_rollup.py` to compute per-slice proxy metrics from WO metadata and activation evidence artifacts (lead-time proxy, failure-rate proxy, recovery-time proxy), and regenerated `knowledge/evidence/metrics/TDE_DORA_WEEKLY.md` with structured slice table.
- Accepted by: JOB-PROD-001
- Date closed: 2026-03-04
- Linked Change Artifact(s): `tools/tde_dora_rollup.py`; `knowledge/evidence/metrics/TDE_DORA_WEEKLY.md`
