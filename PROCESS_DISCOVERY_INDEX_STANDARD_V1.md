# Process Discovery Index Standard v1

Status: Draft standard
Owner: Lyra OS
Date: 2026-03-14

## Purpose
Define the role, shape, and guardrails for a Process Discovery Index within a workspace or operating scope.

The Process Discovery Index is the front door for locating official processes. It exists to improve retrieval and execution discipline without creating a parallel central process layer.

## Core definition
A Process Discovery Index is a concise routing artifact that tells an operator or agent:
- what counts as an official process artifact in this scope
- where to look first for specific process families
- how to resolve authority when multiple artifacts exist

It is a locator and authority map, not a process manual.

## When to use
Operators or agents should consult the Process Discovery Index when they are about to perform a non-trivial operational activity and need to determine whether an official process, SOP, runbook, or standard exists.

## What counts as an official process artifact
In a given scope, an official process artifact is an approved operating artifact located in an owning location, such as:
- SOPs
- runbooks
- operating standards
- approved process docs
- approved local operating instructions

Official status should be determined by local governance/authority rules, not by filename alone.

## What the index must do
A valid Process Discovery Index must:
1. define its scope
2. define what qualifies as official in that scope
3. route users to the main process families
4. state precedence rules
5. link to related authority artifacts such as the source-of-truth map

## What the index must not do
A valid Process Discovery Index must not:
- duplicate detailed process instructions from owning artifacts
- become a giant central registry of all processes everywhere
- centralize product-local recurring processes into a shared layer without need
- replace product/domain ownership

## Recommended artifact name
Recommended local artifact:
- `PROCESS_DISCOVERY_INDEX.md`

Alternative names are acceptable if they are explicit and stable, but this standard prefers one recognizable front-door name.

## Recommended structure
### 1. Purpose and scope
State:
- what scope this index applies to
- what it is for
- who should use it

### 2. Use rule
State a short retrieval rule, for example:
- before performing a non-trivial operational activity, check whether an official process applies here

### 3. Official artifact rule
State what qualifies as official in this scope.

### 4. Process family routing
List the main process families and where their authoritative artifacts live.

Common families may include:
- execution / task management
- decision / escalation
- error / incident handling
- change / release / deployment
- external communications
- security / access / recovery
- workspace-specific operating flows

### 5. Precedence rules
State how to decide between multiple candidate artifacts.

Recommended precedence logic:
1. most specific approved local artifact
2. approved shared standard explicitly adopted by this scope
3. broader internal/shared artifact only when no more specific approved artifact exists

### 6. Related authority artifacts
Link at minimum to:
- `SOURCE_OF_TRUTH.md` or equivalent
- local `AGENTS.md` or equivalent
- any local authority/governance map if present

## Relationship to ownership rules
The Process Discovery Index must respect the broader ownership rule:
- product-local recurring processes should remain with the owning product/domain
- shared artifacts should define only genuine cross-product coordination mechanisms

The index may point to product-owned processes when they apply in the local scope, but should not absorb or duplicate them.

## Relationship to workspace packages
The Process Discovery Index is one component of a Workspace Operating Package.
It should be present in any workspace that expects agents or operators to perform meaningful operational work.

## Minimal template
A minimal valid Process Discovery Index should contain:
- scope
- use rule
- official artifact rule
- process family routing
- precedence rule
- links to related authority artifacts

## Example skeleton
```md
# PROCESS_DISCOVERY_INDEX

## Scope
This index applies to <workspace/scope>.

## Use rule
Before performing a non-trivial operational activity, check whether an official process applies.

## Official artifacts
Official process artifacts in this scope are approved SOPs, runbooks, standards, and local operating docs located in their owning locations.

## Process families
- Execution / task management -> <path>
- Decision / escalation -> <path>
- Error / incident handling -> <path>
- Change / deployment -> <path>
- External communications -> <path>

## Precedence
1. Most specific approved local artifact
2. Approved shared artifact adopted by this scope
3. Broader fallback artifact when no more specific approved artifact exists

## Related authority artifacts
- `SOURCE_OF_TRUTH.md`
- `AGENTS.md`
```

## Validation rules
A valid Process Discovery Index should be:
- concise
- intelligible at a glance
- sufficient for routing
- aligned with local authority boundaries
- small enough to maintain

## Failure modes to avoid
- becoming a dumping ground for process content
- linking to unofficial or stale artifacts without authority clarity
- assuming users know which artifacts are internal-only versus locally applicable
- becoming so abstract that it no longer helps route real work

## Version
- v1.0
- Date: 2026-03-14
- Owner: Lyra OS
