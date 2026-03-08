# CODEX_PROMPT_CONTRACT_TEMPLATE.md
Version: 1.2.0

## Mode
{{mode}}

## Action intent
{{action_intent}}  # implement | plan | review | investigate

## Goal
{{goal_one_sentence}}

## Context
- Repo/workspace: {{repo}}
- Relevant paths/components: {{paths}}
- Current state/symptom: {{state}}
- Reference patterns/docs: {{references}}

## Scope
- In scope: {{in_scope}}
- Out of scope: {{out_of_scope}}

## Constraints
- Must preserve: {{must_constraints}}
- Must not: {{must_not_constraints}}
- Safety boundary: ask before destructive or externally visible actions

## Output contract
- Return exactly the requested sections, in the requested order.
- Keep output concise, decision-oriented, and evidence-bearing.
- If asked for plan/review only, do not silently switch to implementation.

## Tool and dependency discipline
- Inspect prerequisite files/contracts/tests before acting.
- Use tools whenever they materially improve correctness or verification.
- Retry with a different strategy if retrieval or validation returns partial/empty results.
- Parallelize only independent investigation steps.

## Completeness contract
- Treat the task as incomplete until requested work, evidence, and handoff items are covered.
- Mark blocked items explicitly as `[blocked]` with the missing dependency or decision.

## Verification
- Reproduce/validate with:
  - {{check_1}}
  - {{check_2}}
- Acceptance criteria:
  - {{criterion_1}}
  - {{criterion_2}}
- If any check cannot be run, explain why explicitly

## Artifact discipline
- Update supervisory artifact(s):
  - {{artifact_path}}

## Deliverable format
Return:
1. summary of changes and why
2. files changed
3. verification outputs
4. assumptions/risks
5. remaining follow-ups
