# Interim Copy-Sync Protocol (Temporary) — DevSecOps Delivery v0.1

Use this only until version-pinned assembly distribution is fully active.

## Goal
Allow PXS to use Delivery value immediately via controlled interim copy while preventing silent drift and unclear authority.

## Rules
1. Every copied file must include a provenance header with:
   - source path in Lyra OS
   - source commit hash if available
   - copy date
   - sunset target date
2. Interim copies are read-only in the consumer scope (edit at source, then recopy).
3. Every copied file must be listed in `pxs/PXS_ASSEMBLY_LOCK.md` under the relevant interim-copy section.
4. Interim copies must be removed when pinned assembly integration goes live.

## Temporary sync procedure
1. Select the required source files under `assemblies/devsecops-delivery/v0.1/`.
2. Copy them into the consumer interim path.
3. Add provenance header and `REMOVE_WHEN_PINNED=true` marker.
4. Update `pxs/PXS_ASSEMBLY_LOCK.md` with version and file list.
5. Run the Delivery verification baseline (`VERIFY.md`).

## Removal procedure
1. Confirm pinned assembly lane is active in the consumer workspace.
2. Remove all Delivery interim-copy files from the consumer interim path.
3. Update lockfile and changelog/removal note with the removal event.
