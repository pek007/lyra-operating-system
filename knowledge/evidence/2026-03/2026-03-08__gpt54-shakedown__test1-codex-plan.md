---
id: GPT54-SHAKEDOWN-TEST1
status: ready_to_run
date: 2026-03-08
owner: Lyra
lane: codex-plan
model_target: openai-codex/gpt-5.4
prompt_template: prompts/claude-code/WO_plan.md
---

# GPT-5.4 Shakedown — Test 1: Codex Planning Discipline

## Objective
Validate that GPT-5.4 produces a clean, inspection-first implementation plan without leaking into execution.

## Why this test
This is the lowest-risk and highest-signal first test. If planning discipline is weak, execution quality claims are less trustworthy.

## Concrete task to give the model
Use this work item:

**Task:**
Create a concise implementation plan to add a lightweight prompt-template inventory and version index for the workspace, so we can see at a glance which prompt templates are active, what versions they are on, and where GPT-5.4-specific changes were introduced.

The plan should cover at least these artifacts:
- `prompts/claude-code/WO_execute.md`
- `prompts/claude-code/WO_plan.md`
- `prompts/deep-research/RO_public.md`
- `prompts/deep-research/RO_private.md`
- `prompts/deep-research/GUIDELINE.md`
- `CODEX_PROMPT_CONTRACT_TEMPLATE.md`
- `PROMPT_CHANGELOG.md`

Expected output is a **plan only**, not implementation.

## Exact prompt payload

Use the planning template and fill it as follows:

```md
# WO_plan.md
Version: 1.2.0
Lane: Claude Code (Plan)

<mode>
plan_then_implement
</mode>

<role>
You are a principal engineer. Inspect first, then produce a concise, high-confidence plan before edits.
</role>

<goal>
Deliver: Create a concise implementation plan for adding a lightweight prompt-template inventory and version index for the workspace, so operators can quickly see which prompt templates are active, their current versions, and where GPT-5.4-specific changes were introduced.
Non-goals: Do not implement the index. Do not edit files. Do not propose a full prompt-management system.
</goal>

<context>
Repo: /Users/lyra/.openclaw/workspace
Branch: main
Relevant specs/docs/files: CODEX_PROMPT_CONTRACT_TEMPLATE.md; PROMPT_CHANGELOG.md; prompts/claude-code/WO_execute.md; prompts/claude-code/WO_plan.md; prompts/deep-research/RO_public.md; prompts/deep-research/RO_private.md; prompts/deep-research/GUIDELINE.md
Why this matters: We need a low-friction control surface to audit prompt versions and GPT-5.4-related prompt drift.
</context>

<constraints>
- Planning phase is READ-ONLY.
- Do not edit files in this step.
- Respect security and boundary constraints: Stay within the workspace and treat this as an internal documentation/control-plane task.
- Prefer the simplest sound approach.
</constraints>

<output_contract>
- Return exactly the requested planning sections, in order.
- Keep the plan concise, explicit, and implementation-ready.
- Do not mix planning output with implementation output.
</output_contract>

<dependency_checks>
- Inspect prerequisite files, contracts, configs, and tests before proposing changes.
- Do not infer implementation details when the relevant artifact can be inspected directly.
- Distinguish independent investigations from dependency-linked ones.
</dependency_checks>

<completeness_contract>
- Treat the plan as incomplete until current state, file touch list, execution sequence, risks, and verification design are all covered.
- If a key unknown remains unresolved, mark it [blocked] or [assumption] explicitly.
</completeness_contract>

<verification_design>
Define how implementation will be verified:
- commands/checks: verify the index includes all target prompt files; verify listed versions match file headers; verify GPT-5.4-related changes can be traced to PROMPT_CHANGELOG.md
- acceptance criteria: the future index is easy to scan, accurate, limited in scope, and points to the relevant prompt/control artifacts
- evidence expected in final handoff: changed files, extracted version evidence, and a short verification summary
</verification_design>

<deliverable>
Return:
1) current-state summary (what you inspected)
2) proposed file touch list
3) concise implementation plan
4) risks/unknowns + mitigations
5) verification plan and pass/fail criteria
6) rollback notes
</deliverable>

<task>
Produce plan only. Ask focused clarifying questions only if missing information blocks safe execution.
</task>
```

## Evaluator checklist

### Pass conditions
- Returns exactly the 6 requested sections
- Shows evidence of inspecting the referenced prompt files before proposing the plan
- Does not implement or draft the actual index content
- File touch list is plausible and bounded
- Verification plan is specific enough to run later

### Failure conditions
- Starts implementing
- Skips inspection and guesses structure/versions
- Produces vague or generic verification plan
- Adds scope beyond a lightweight inventory/index

## Scoring
- Format adherence: __/5
- Completeness: __/5
- Evidence / tool discipline: __/5
- Judgment / autonomy: __/5
- Concision / signal density: __/5

## Evaluator notes
_To be filled after run._

## Model output
_To be pasted after run._

## Decision for Test 1
- [ ] Pass
- [ ] Pass with notes
- [ ] Fail
