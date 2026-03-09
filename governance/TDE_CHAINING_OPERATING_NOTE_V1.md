# TDE Chaining Operating Note v1

Status: Active
Owner: Lyra
Date: 2026-03-09
Related contracts:
- `os/sops/TDE_CHAINING_CONTRACT_V1.md`
- `governance/TDE_PRODUCT_OWNER_OPERATING_INSTRUCTION_V1.md`

## Purpose
Provide a practical operating note for using the current bounded TDE chaining capability safely.

This note is for product owners and operators who want TDE to continue work toward a high-level target through staged task handoffs.

## What the current capability does
In DB-canonical TDE mode, a successor task can now be promoted automatically when:
- it has explicit chaining metadata,
- pilot gating is enabled,
- all predecessor tasks are `Done`,
- normal runtime controls pass.

The successor can then be claimed by the same or subsequent scheduled tick, subject to WIP bounds.

## When to use chaining
Use chaining when all of the following are true:
- the work is naturally staged,
- predecessor/successor relationships are clear,
- the handoff rule is deterministic,
- the next step should normally happen without waiting for a human prompt,
- the workflow is bounded and auditable.

Good examples:
- implementation -> verification -> deployment-readiness review
- verification -> closeout -> improvement-capture

## When not to use chaining
Do not use chaining when:
- the next step depends on broad human judgment,
- the workflow is exploratory or ambiguous,
- the handoff should require explicit re-prioritization,
- the successor is outside approved pilot families,
- the task graph is vague or likely to expand unpredictably.

## Current enablement boundary
The currently implemented path is intentionally narrow:
- canonical store must be DB-backed
- successor task must carry chaining metadata
- `chain_policy.pilot_enabled` must be `true`
- supported activation rule is only `all_predecessors_done`

## Minimum modeling rule
A chained task should have:
- a clear task ID
- a bounded title
- explicit predecessor task IDs in `depends_on`
- `activation_rule=all_predecessors_done`
- `chain_policy.pilot_enabled=true`
- `chain_policy.family=<approved-family>`
- optional `objective_id` and `stage_id`

## Operational pattern
1. Define the staged chain in canonical TDE state.
2. Mark predecessor completion truthfully.
3. Let the next scheduled tick evaluate successor eligibility.
4. Inspect runtime artifact if promotion/execution behavior needs review.
5. Treat skipped promotion reasons as operational signals to fix, not as invisible drift.

## Evidence expectation
When chaining is used, there should be usable proof of:
- what predecessor completed,
- which successor was promoted,
- when promotion happened,
- whether execution continued,
- why any successor was skipped.

## Guardrails
- Chaining does not bypass approvals.
- Chaining does not authorize scope expansion.
- Chaining should not be used to hide decisions that should remain explicit.
- If promotion behavior becomes unclear, disable the pilot path and revert to ordinary scheduled progression.

## Current proven pilot family
The currently proven real pilot family is:
- implementation -> verification -> deployment-readiness review

Evidence:
- `knowledge/evidence/2026-03-09__tde-chaining-pilot-first-handoff.md`
- `knowledge/evidence/2026-03-09__tde-chaining-pilot-second-handoff.md`

## Bottom line
Use TDE chaining to remove unnecessary handoff friction in clear staged workflows.
Do not use it as a substitute for strategy, judgment, or governance.
