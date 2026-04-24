# Git Topology and Sync Error Report — 2026-03-11

## Header
- Error ID: `ERR-SYS-2026-03-11-GIT-TOPOLOGY-01`
- Date: `2026-03-11`
- Title: `Wrong clone treated as authoritative for Git sync decision`
- Type: `decision_failure`
- Scope: `system_level`
- Owning product or owner: `Lyra / shared system coordination`
- Affected products/contexts: `Lyra OS`, `Task Management / TDE`, `Control Panel coordination context`, `workspace-root governance/model work`
- Status: `mitigated`
- Review / closure date: `2026-03-18`

## Summary
- A Git sync check in the workspace initially reported that `main` was ahead by 55 and behind by 24. This triggered an attempted sync/rebase path under the assumption that the workspace-root clone represented the relevant TDE / Lyra OS repo state. That assumption was wrong: the Task Management channel later verified that the more relevant nested TDE clone at `repos/lyra-operating-system` was actually ahead by 12 and behind by 0.

## Impact
- Actual impact:
  - a push attempt from the workspace-root clone failed
  - a rebase was started in the wrong clone and then aborted
  - time was lost investigating the wrong Git state for the TDE lineage question
- Potential impact:
  - unnecessary or incorrect reconciliation of TDE runtime code
  - mistaken Git decisions based on the wrong local authority
  - increased risk of damaging authoritative TDE continuity

## Detection
- How was it detected?
  - the attempted workspace-root push failed
  - the subsequent rebase hit overlapping TDE runtime conflicts
  - Task Management then checked the nested `repos/lyra-operating-system` clone directly and found a materially different Git state
- Detection gap, if any:
  - the canonical clone for TDE / Lyra OS had not been confirmed before sync action was taken
  - multiple local clones of the same remote were present without an explicit authority rule

## Root cause
- Primary root cause:
  - the wrong local clone was treated as the relevant authority for a TDE-related Git sync decision
- Contributing factors:
  - the workspace root is itself a Git clone of `lyra-operating-system`
  - a second nested clone exists at `repos/lyra-operating-system`
  - both point to the same remote but had different local states
  - there was no explicit canonical-clone rule in active use before the sync action

## Immediate mitigation
- The rebase was aborted once it became clear the workspace-root divergence was not the correct basis for the TDE lineage question.
- The relevant nested clone was inspected directly.
- A corrective Git topology rule was documented.

## Corrective actions
- [x] Define and publish a canonical repo map for active code-bearing products.
- [x] Use `repos/lyra-operating-system` as the canonical locus for TDE / Lyra OS code reconciliation unless explicitly changed.
- [x] Add an explicit repo-root confirmation step before future sync / rebase / push actions.
- [ ] Implement the canonical repo authority rule in ongoing operations and verify it through future sync decisions.
- [x] Adopt a lightweight Git sync cadence rule for active code-bearing products. (`GIT_AND_GITHUB_WAYS_OF_WORKING_V1.md`, 2026-04-24)
- [x] Assign these remaining corrective actions into the canonical action system instead of the legacy `TASKS.md` reference board.

## Preventive changes
- Before any Git sync decision:
  1. identify the intended product/repo explicitly
  2. confirm the active Git root explicitly
  3. check whether multiple local clones of the same remote exist
  4. operate only in the canonical clone for that product/repo
- Increase GitHub sync cadence so large local divergence stacks do not build up unnoticed.
- Prefer smaller, more frequent pushes for high-signal work.

## Linked artifacts
- Related tasks:
  - shared/system corrective actions remain anchored in this error report per `SHARED_CORRECTIVE_ACTION_SYSTEM_V1.md`; previous temporary placement in legacy `TASKS.md` was removed
- Related decisions:
  - none yet; should be added if canonical repo authority becomes a standing architectural decision
- Related evidence:
  - Git status/fetch output gathered during the failed push / aborted rebase investigation
  - Task Management channel assessment of `repos/lyra-operating-system` divergence state
- Related product/shared artifacts:
  - `PROCESS_OWNERSHIP_AND_COORDINATION_RULE_V1.md`
  - `ERROR_REPORTING_STANDARD_V1.md`
  - `GIT_TOPOLOGY_AND_SYNC_ERROR_REPORT_2026-03-11.md` (this artifact)

## Closure criteria
- canonical repo authority for active code-bearing products is documented
- future sync operations include explicit repo-root confirmation
- lightweight Git sync cadence rule is defined
- remaining corrective actions remain clearly anchored in the canonical shared/system corrective-action system
- no further Git sync decisions are made against the wrong clone for the same remote

## Closure note
- Initial incident mitigated by aborting the rebase and documenting the corrective rule.
- 2026-04-24 update: `CANONICAL_REPO_MAP_V1.md` was refreshed to reflect the active authoritative repo set and `GIT_AND_GITHUB_WAYS_OF_WORKING_V1.md` now defines the missing Git sync cadence rule.
- Full closure still depends on consistent use of the canonical authority rule in practice, including reconciling or retiring the divergent nested `repos/lyra-operating-system` clone so it cannot be mistaken for the active authority surface.
