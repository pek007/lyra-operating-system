# Assembly Install / Promote / Rollback SOP v1

## Purpose
Operationalize safe transfer of Lyra OS Product Assemblies into PXS.

## 1) Install (candidate)
1. Select assembly version.
2. Register in `PXS_ASSEMBLY_LOCK.md`.
3. Install via pinned lane (or interim copy lane if not ready).
4. Run assembly `VERIFY.md` checks.
5. Record evidence and owner sign-off.

## 2) Promote (candidate -> stable)
Promotion conditions:
- Verification checks all pass
- No unresolved high-risk findings
- Usage evidence from at least one real PXS workflow

Promotion steps:
1. Update lock entry status to `stable`.
2. Tag promoted version in changelog.
3. Announce promoted version in PXS decision log.

## 3) Rollback
Rollback triggers:
- regression in enforced controls
- workflow breakage
- policy conflict with PXS operations

Rollback steps:
1. Revert lockfile to previous stable version.
2. Remove/disable new assembly artifacts.
3. Re-run previous stable verification.
4. Document incident and fix-forward plan.

## 4) Interim Copy Lane Controls (temporary)
- Must include provenance headers and sunset date.
- Must include `REMOVE_WHEN_PINNED=true` marker.
- Must be fully removed once pinned lane is active.
