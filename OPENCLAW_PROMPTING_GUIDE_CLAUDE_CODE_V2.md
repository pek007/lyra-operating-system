# OpenClaw Prompting Guide for Claude Code (v2)

Date: 2026-02-28
Owner: Peter/Lyra
Status: Active

## Core shift
Prompt for **outcomes + constraints + verification**, not micro-choreography.

## Default schema
Every implementation prompt should include:
1. **Mode** (`direct_implement`, `plan_then_implement`, `spec_first`, `review_only`, `continuation`)
2. **Goal** (user-visible end state)
3. **Context** (relevant files, source-of-truth docs, analogous patterns)
4. **Constraints** (must/must-not, compatibility, non-goals, safety boundaries)
5. **Verification** (commands/checks/acceptance criteria)
6. **Deliverable** (what artifacts/results must be returned)

## Mode selection rules
- `direct_implement`: small, obvious, local changes
- `plan_then_implement`: multi-file/uncertain work
- `spec_first`: ambiguous or high-stakes product-level changes
- `review_only`: audit/critique, no edits
- `continuation`: multi-session work with progress artifacts

## Non-negotiables
- No implementation prompt without verification block.
- Be explicit whether Claude should **act** or **analyze only**.
- Restart with fresh context after two failed correction cycles on the same issue.
- For larger work, maintain persistent state artifacts (`SPEC.md`, task list, progress log).

## Environment design split
- Stable repo conventions: `CLAUDE.md`
- Deterministic must-run rules: hooks
- Reusable specialist workflows: skills
- Heavy independent investigation/review: sub-agents
- Current task framing: prompt

## Evaluation policy
Grade prompt quality primarily on:
- correctness of outcome
- constraint compliance
- verification quality
- handoff quality
- avoid brittle grading based on exact internal tool-call sequence

## Version
- v2.0
- Date: 2026-02-28
