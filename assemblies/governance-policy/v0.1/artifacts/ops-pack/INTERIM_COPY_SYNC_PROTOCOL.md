# Interim Copy-Sync Protocol (Temporary)

Use this only until version-pinned assembly distribution is fully implemented.

## Goal
Allow PXS to use Lyra OS governance value immediately via controlled copy/paste of markdown artifacts.

## Rules
1. Every copied file must include a provenance header with:
   - source path in Lyra OS
   - source commit hash
   - copy date
   - sunset target date
2. Copies are read-only in PXS (edit at source, then recopy).
3. Every copied file must be listed in `pxs/PXS_ASSEMBLY_LOCK.md` under `interim_copies`.
4. Interim copies must be removed when pinned assembly integration goes live.

## Temporary Sync Procedure
1. Select source files in Lyra OS.
2. Copy into `pxs/docs/assemblies/interim/governance-policy-v0.1/`.
3. Add provenance header and `REMOVE_WHEN_PINNED=true` marker.
4. Update `pxs/PXS_ASSEMBLY_LOCK.md` (version + file list).
5. Run verification checklist (`VERIFY.md`).

## Removal Procedure
1. Confirm pinned assembly lane active in PXS.
2. Remove all files under `pxs/docs/assemblies/interim/governance-policy-v0.1/`.
3. Update lockfile and changelog with removal event.
