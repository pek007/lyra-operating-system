# CODEX_PROMPT_CONTRACT_TEMPLATE.md
Version: 1.1.0

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
