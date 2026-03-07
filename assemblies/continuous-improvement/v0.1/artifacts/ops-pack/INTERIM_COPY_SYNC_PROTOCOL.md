# Interim Copy-Sync Protocol — Continuous Improvement (Temporary)

Use only until pinned assembly distribution is active.

## Rules
1. Each copied file must include provenance header (source path/commit/copy date/sunset date).
2. Copies are read-only in PXS.
3. Copied files must be listed in `pxs/PXS_ASSEMBLY_LOCK.md`.
4. Remove interim copies once pinned lane is active.

## Temporary Sync Procedure
1. Copy selected source files into `pxs/docs/assemblies/interim/continuous-improvement-v0.1/`.
2. Add metadata header with `REMOVE_WHEN_PINNED=true`.
3. Update lockfile and next review date.
4. Run verification checklist (`VERIFY.md`).
