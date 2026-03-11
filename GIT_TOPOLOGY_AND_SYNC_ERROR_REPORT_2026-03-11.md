# Git Topology and Sync Error Report — 2026-03-11

Status: Active error report
Owner: Lyra
Date: 2026-03-11

## Purpose
Record the Git sync confusion encountered on 2026-03-11, explain the root cause, and define the operational rule needed to avoid recurrence.

## Summary
A Git sync check in the workspace initially reported that `main` was:
- ahead by 55
- behind by 24

This triggered an attempted sync/rebase path under the assumption that this represented the active TDE / Lyra OS repo state.

That assumption was wrong.

The actual TDE-focused repo inspected in the Task Management channel (`repos/lyra-operating-system`) showed a materially different state:
- ahead by 12
- behind by 0

The discrepancy existed because there were multiple local Git clones of the same remote repository active inside the broader workspace.

## What happened
### Observed workspace-root state
Repo path:
- `/Users/lyra/.openclaw/workspace`

Remote:
- `https://github.com/pek007/lyra-operating-system.git`

Observed divergence:
- ahead 55
- behind 24

### Observed nested Lyra OS repo state
Repo path:
- `/Users/lyra/.openclaw/workspace/repos/lyra-operating-system`

Remote:
- `https://github.com/pek007/lyra-operating-system.git`

Observed divergence:
- ahead 12
- behind 0

### Additional nested repo
Repo path:
- `/Users/lyra/.openclaw/workspace/repos/control-panel`

Remote:
- `https://github.com/pek007/control-panel.git`

Observed divergence:
- ahead 2
- behind 0

## Root cause
The workspace contained more than one local clone of the same GitHub repository (`lyra-operating-system`):
1. the workspace root itself
2. `repos/lyra-operating-system`

Both pointed to the same remote, but they were in different local states.

The initial sync assessment was performed in the workspace-root clone, while the relevant TDE continuity/context work was actually being reasoned about in the nested `repos/lyra-operating-system` clone.

This created a false operational picture:
- the Git alarm was real for one clone
- but not the right clone for the TDE decision path being discussed

## Why this was risky
This topology creates several failure modes:
- checking the wrong repo and drawing the wrong sync conclusion
- attempting rebase/push operations in the wrong clone
- mixing product/model/governance work with code-lineage reconciliation unintentionally
- making TDE decisions based on an irrelevant Git state
- increased chance of conflict churn and mistaken recovery actions

## Incident details
An attempted selective push from the workspace-root clone failed because remote `main` had moved.
A subsequent rebase was started and then aborted after it became clear that:
- the rebase conflicts were in overlapping TDE runtime files
- the broader workspace-root divergence was not the correct basis for the TDE lineage question

The rebase was correctly aborted to avoid unnecessary risk to TDE.

## Corrective finding
For TDE-specific reconciliation, the more relevant active clone was:
- `repos/lyra-operating-system`

That clone showed a coherent local continuation branch on top of published `origin/main`, not the larger 55/24 split seen at the workspace root.

## Operational rule going forward
### Canonical clone rule
Before any Git sync, rebase, or push decision:
1. identify the intended product/repo explicitly
2. confirm the active Git root explicitly
3. verify whether multiple local clones of the same remote exist
4. operate only in the canonical clone for that product/repo

### Immediate practical rule
- TDE / Lyra OS code reconciliation should be handled in `repos/lyra-operating-system` unless explicitly decided otherwise.
- `repos/control-panel` should be treated as the canonical repo for Control Panel code work.
- The workspace root should not be assumed to be the authoritative code clone for a product merely because it is the agent workspace.

## Process lesson
This was not only a Git hygiene issue.
It was an architectural clarity issue about repo authority.

The lesson is:
- workspace context is not the same thing as canonical Git authority
- product/repo identity must be explicit before sync operations

## Preventive actions
1. Define canonical repo locations for each active code-bearing product.
2. Record those locations in the relevant product or portfolio artifact.
3. Before sync/push/rebase, run an explicit repo-root check.
4. Increase GitHub sync cadence so large divergence stacks do not build up unnoticed.
5. Prefer smaller, more frequent pushes for high-signal work.

## Follow-up recommendation
Create a small canonical-repo map / operating note that states, for each active code-bearing product:
- canonical repo path
- remote URL
- whether the workspace root is authoritative or not
- expected push/update cadence

## Bottom line
The sync confusion happened because there were multiple local clones of the same remote in different states, and the wrong clone was treated as the relevant authority for the TDE discussion.

The corrective principle is simple:
**always confirm the canonical clone before making Git sync decisions.**
