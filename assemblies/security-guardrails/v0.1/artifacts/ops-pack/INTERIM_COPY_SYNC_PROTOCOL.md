# Interim Copy-Sync Protocol — Security Guardrails (Temporary)

Use only until pinned assembly distribution is active.

## Rules
1. Each copied file must include provenance header:
   - source path
   - source commit hash
   - copy date
   - sunset date
2. Copies are read-only in PXS.
3. Every copied file must be listed in `pxs/PXS_ASSEMBLY_LOCK.md`.
4. Remove all interim copies when pinned lane is live.

## Temporary Sync Procedure
1. Copy selected source files into `pxs/docs/assemblies/interim/security-guardrails-v0.1/`.
2. Add metadata header with `REMOVE_WHEN_PINNED=true`.
3. Update lockfile with file list and review date.
4. Run verification checks in `VERIFY.md`.
