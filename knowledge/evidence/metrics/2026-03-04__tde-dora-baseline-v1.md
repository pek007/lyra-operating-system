# TDE DORA Baseline v1 (Proxy)

Date: 2026-03-04
Boundary spec: `os/sops/TDE_DELIVERY_BOUNDARY_AND_DORA_BASELINE_V1.md`

## Baseline observation window
- 2026-03-02 to 2026-03-04

## Initial values (proxy)
- Deployment Frequency: **Unspecified baseline** (manual collection started; requires routine weekly rollup)
- Lead Time for Changes: **Unspecified baseline** (slice-level commit->activation timestamps not yet auto-indexed)
- Change Failure Rate: **Unspecified baseline** (activation fail/pass events present but not yet aggregated)
- Failed Deployment Recovery Time: **Unspecified baseline**
- Deployment Rework Rate: **Unspecified baseline**

## Immediate next automation
1. Add script to parse WO + evidence timestamps into weekly metrics row.
2. Publish weekly `metrics/TDE_DORA_WEEKLY.md` update on cron.
3. Backfill S15-S18 slice rows for trendline seed.
