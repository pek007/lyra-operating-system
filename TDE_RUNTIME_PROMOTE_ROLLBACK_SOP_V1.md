# TDE Runtime Promote / Rollback SOP v1

Status: Draft
Owner: Peter + Lyra
Date: 2026-03-13
Related:
- `TDE_RUNTIME_PROMOTION_CHECKLIST_V1.md`
- `TDE_ENVIRONMENT_AND_PROMOTION_MODEL_V1.md`
- `OPENCLAW_CONFIG_CHANGE_SOP_V1.md`
- `ASSEMBLY_INSTALL_PROMOTE_ROLLBACK_SOP_V1.md`

## Purpose
Operationalize safe promotion and rollback for TDE/OpenClaw runtime changes.

This SOP is specifically for runtime-path changes, not general product docs or non-operative examples.

## Scope
Use this SOP for changes to:
- TDE runtime scripts
- chaining/activation behavior
- decision-policy enforcement behavior
- environment/path routing for runtime artifacts
- cron/tick execution routing
- release/evidence scripts that participate in operational gating

## 1) Prepare candidate
1. Identify exact candidate commit/version.
2. Define scope and risk class.
3. Identify last known-good rollback target.
4. Link relevant specs/artifacts.

## 2) Validate in staging
1. Run the candidate in staging paths only.
2. Confirm environment isolation:
   - staging DB
   - staging bindings
   - staging objectives
   - staging evidence outputs
3. Run focused tests.
4. Run at least one staging execution path relevant to the change.
5. Capture evidence bundle.

## 3) Approval gate
For high-risk runtime changes:
1. Present candidate summary.
2. Provide staging evidence refs.
3. State expected production impact.
4. State rollback plan.
5. Receive explicit Peter approval before promotion.

## 4) Promote
1. Apply only the approved candidate.
2. Do not bundle unrelated changes.
3. Ensure production/proto-prod path targets are explicit.
4. Preserve backup/snapshot as appropriate.

## 5) Verify after promotion
Immediately verify:
1. runtime loads cleanly
2. intended paths are used
3. no fail-open behavior exists
4. no unexpected mutation occurs
5. evidence output is correct

## 6) Rollback
Rollback immediately if:
- wrong environment path is used
- runtime degrades
- fail-open enforcement appears
- scheduler behavior is wrong
- unexpected state mutation occurs
- evidence chain becomes unreliable

Rollback steps:
1. Revert to last known-good commit/version.
2. Restore any relevant live file/config backup if applicable.
3. Re-run verification on the rollback target.
4. Record incident + follow-up action.

## Minimum rollback record
- what was rolled back
- why rollback triggered
- rollback target
- verification result after rollback
- prevention/fix-forward note

## Bottom line
Promotion is not just "the code seems OK".
For TDE runtime changes, promotion means:
- tested in staging,
- approved explicitly,
- applied narrowly,
- verified immediately,
- rolled back fast if trust is threatened.
