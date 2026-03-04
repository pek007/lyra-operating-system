# Verification — WO-2026-TDE-KERNEL-S30

Date: 2026-03-04
Owner: JOB-PROD-001

## Scope verified
- Lead-time snapshot now includes commit->activation proxy.
- Slice table includes `Lead C->A(h)` column.

## Commands executed
1. `python3 tools/tde_dora_rollup.py`
2. `sed -n '1,90p' knowledge/evidence/metrics/TDE_DORA_WEEKLY.md`

## Result
- PASS
- Output now reports avg commit->activation lead time and per-slice values where data exists.
