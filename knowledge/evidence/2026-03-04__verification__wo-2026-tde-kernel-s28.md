# Verification — WO-2026-TDE-KERNEL-S28

Date: 2026-03-04
Owner: JOB-PROD-001

## Scope verified
- DORA rollup now computes non-placeholder per-slice proxies.
- Weekly output includes summary metrics + slice-level table.

## Commands executed
1. `python3 tools/tde_dora_rollup.py`
2. `sed -n '1,80p' knowledge/evidence/metrics/TDE_DORA_WEEKLY.md`

## Result
- Rollup script PASS
- Output updated with:
  - deployment frequency (7d proxy)
  - lead-time (opened->closed proxy)
  - slice-level failure-rate proxy
  - recovery-time proxy (first fail->first pass where available)
