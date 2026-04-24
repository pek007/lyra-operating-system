# Git and GitHub Ways of Working v1

Status: Active
Owner: Peter / Lyra
Date: 2026-04-24

## Purpose
Define the minimum operating discipline that keeps active repos current, reduces local-divergence risk, and makes GitHub the reliable external source for committed work.

This is intentionally lightweight. The goal is not ceremony; it is to avoid stale local stacks, wrong-repo sync mistakes, and invisible unpushed progress.

## Scope
Applies to the active repos in `CANONICAL_REPO_MAP_V1.md`.

## Core rule
**Completed bounded work should reach GitHub quickly.**

Default stance:
- work in small batches
- commit when a bounded unit is coherent
- push the same session or same day once the minimal verification gate passes
- do not let committed local history sit for days without an explicit reason

## Repo authority rule
Before any fetch / rebase / pull / push action:
1. identify the intended repo
2. confirm the canonical local path in `CANONICAL_REPO_MAP_V1.md`
3. verify you are operating in that clone
4. if a second local clone exists for the same remote, treat it as non-authoritative unless the repo map explicitly says otherwise

## Start-of-work hygiene
At the start of a work cycle for a repo:
1. `git fetch --prune`
2. check `ahead/behind`
3. check `git status --short`
4. confirm whether uncommitted work already exists

If the repo is already dirty, decide explicitly whether the new work:
- belongs with that existing change set,
- needs a separate commit boundary, or
- should be delayed until the tree is clean enough to avoid accidental mixing.

## Commit and push discipline
### Default cadence
- Push completed bounded commits the same session or same day.
- Prefer multiple small pushes over large catch-up pushes.
- If a repo is ahead of origin by more than one bounded work packet, treat that as a hygiene drift signal.

### Before push
Minimum pre-push gate:
1. review changed files / diff
2. ensure no unintended files are staged or included
3. run the smallest meaningful verification step available
4. push only the intended committed history

### After push
Always verify:
1. `git fetch --prune`
2. confirm `ahead 0 / behind 0`
3. note any remaining uncommitted work separately from the pushed history

## Branching stance
This environment is effectively owner-operated.

Default:
- direct commits to `main` are acceptable for bounded, understood, reversible work
- use a branch / PR path when the change is high-risk, hard to review in one pass, externally consequential, or likely to benefit from explicit review separation

Even when working directly on `main`, keep commit boundaries tight enough that each push is understandable on its own.

## Dirty working tree rule
Uncommitted work is allowed, but it must remain legible.

Do not leave a repo in a long-lived state where it is:
- both heavily dirty and poorly understood
- ahead of origin by many commits
- mixed across unrelated workstreams

When dirt accumulates, resolve it by doing one of:
- commit and push a coherent subset
- stash intentionally
- split into smaller bounded packets
- discard only with explicit confirmation if destructive

## Weekly hygiene review
At least once per working week, review each active repo for:
- canonical path correctness
- ahead/behind status
- dirty working tree size
- presence of duplicate local clones for the same remote
- auth health for both `git` and `gh`

This review is successful only if it results in either:
- clean/synced repos, or
- explicit bounded follow-up actions for the remaining dirt/divergence

## Authentication rule
Treat `git` auth and `gh` auth as separate paths.

Check both when access changes or failures occur:
- `git` push/pull path
- `gh auth status`

Preferred local posture on this machine today:
- `git` over HTTPS
- credentials stored in macOS keychain
- `gh` authenticated separately for CLI/API operations

## Current best-practice translation for this setup
For this owner-operated multi-repo environment, “best practice” means:
- small frequent pushes
- fast sync verification
- no silent local divergence buildup
- explicit repo authority
- direct-to-main only when the work is bounded and understood
- visible cleanup of dirty trees before they become archaeology

## Immediate standing expectations
- `pxs-crm` should remain clean and synced by default
- `pxs` should have its remaining local dirt reviewed and either committed, stashed, or left intentionally bounded
- `lyra-operating-system` workspace root is the active authoritative mainline and should stay synced frequently
- the nested `repos/lyra-operating-system` clone should be reconciled or retired; it must not remain an ambiguous second authority surface

## Relationship to prior corrective action
This artifact closes the previously identified need for a lightweight Git sync cadence rule in `GIT_TOPOLOGY_AND_SYNC_ERROR_REPORT_2026-03-11.md`.
