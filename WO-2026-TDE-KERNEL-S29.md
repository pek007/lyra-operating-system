# Work Order (WO) — TDE Kernel Slice S29

## Metadata
- WO-ID: WO-2026-TDE-KERNEL-S29
- Title: DORA rework-rate automation via commit-to-slice linkage
- Owner: JOB-PROD-001
- Date opened: 2026-03-04
- Lane: Build
- Work type: Metrics automation
- Risk class: Medium

## Closure
- Outcome summary: Enhanced DORA rollup to map git commits to slice IDs from commit messages and compute deployment rework-rate proxy automatically, plus per-slice commit/rework counts in weekly output.
- Accepted by: JOB-PROD-001
- Date closed: 2026-03-04
- Linked Change Artifact(s): `tools/tde_dora_rollup.py`; `knowledge/evidence/metrics/TDE_DORA_WEEKLY.md`
