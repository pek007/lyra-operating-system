# PROMPTING_OS_V1.md

Status: Active draft v1  
Owner: Peter (governance), Lyra (operations), Engineering role (automation)

## Objective
Standardize how Lyra uses external 3PP lanes (Claude Code, OpenAI Deep Research) so output quality is high, risk is bounded, and results are reusable.

## Core principle
Prompting is interface design, not conversation craft.

## Core shift (2026-02-28)
Default to outcome-oriented prompting: define destination, constraints, and verification; avoid unnecessary step-by-step choreography.

---

## 1) Lane model

### Lane A: Claude Code (implementation lane)
- Primary role: plan/implement/verify code changes
- Prompt type: implementation contract
- Required outputs: plan artifact, diffs, tests, verification checklist

### Lane B: Deep Research (research lane)
- Primary role: evidence-backed synthesis and decision support
- Prompt type: research specification
- Required outputs: structured report with citations and recommendation

### Lane C: Handoff artifacts (integration lane)
- DDA = Decision/Design Artifact (research -> decision)
- CA = Change Artifact (implementation -> verification)

---

## 2) Prompt stack (3 layers)

1. **Policy layer (stable)**
- security boundaries
- source/tool restrictions
- output/citation standards

2. **Work-order layer (semi-stable)**
- objective, scope, constraints, acceptance criteria
- expected output schema

3. **Task layer (volatile)**
- specific ask, references, deadlines, context specifics

Rule: task updates must not silently mutate policy.

---

## 3) Required mode model (explicit)

Select one mode before writing the prompt:
- `direct_implement`
- `plan_then_implement`
- `spec_first`
- `review_only`
- `continuation`

Mode rules:
- Small/obvious/local: `direct_implement`
- Multi-file or uncertain: `plan_then_implement`
- Ambiguous/high-stakes product decisions: `spec_first`
- Audit/critique only: `review_only`
- Multi-session work: `continuation`

### Required phase discipline
When a mode includes implementation, enforce:
1. Clarify (if needed)
2. Inspect current implementation
3. Plan (brief, only when complexity warrants)
4. Execute in bounded increments
5. Verify against explicit acceptance checks

---

## 4) Prompt quality checklist (mandatory)

A prompt is valid only if it has:
- [ ] explicit mode
- [ ] clear objective and non-goals
- [ ] targeted context anchors (relevant files/patterns/sources)
- [ ] explicit trust boundary (sources/tools)
- [ ] explicit acceptance criteria and verification commands/checks
- [ ] explicit output schema
- [ ] explicit risk constraints
- [ ] handoff format (DDA or CA)
- [ ] explicit action intent (implement vs analyze/review only)

---

## 5) Prompt semver and governance

## Versioning
- Prompt templates use semver:
  - MAJOR: output schema or policy contract change
  - MINOR: additive improvements
  - PATCH: wording/tightening with same behavior target

## Changelog
All template changes must update:
- `PROMPT_CHANGELOG.md`
- rationale
- expected impact
- rollback instruction

## Approval policy
- MAJOR changes require human approval
- MINOR/PATCH can be approved by Chief Architect + logged

---

## 6) Update process (model and best-practice drift)

Create a recurring **Prompt Drift Review** process.

### Cadence
- Weekly: lightweight scan (new model/runtime notes, failures observed)
- Monthly: formal review and template updates
- Quarterly: major refresh and deprecation decisions

### Inputs
- Vendor release notes (Claude/OpenAI)
- Internal failure cases and regressions
- Cost/latency/quality metrics
- Security advisories (prompt injection, exfiltration patterns)

### Process steps
1. Detect change signal
2. Assess impact by lane
3. Propose template updates (semver bump)
4. Run evaluation set (representative prompts/tasks)
5. Approve + deploy
6. Monitor outcomes for 1-2 weeks
7. Roll back if regressions exceed threshold

### Drift triggers (automatic review)
- model behavior regressions (quality drop)
- cost spikes > threshold
- latency degradation > threshold
- increased safety incidents
- vendor deprecation/feature changes

---

## 7) Evaluation and release gates

Before promoting prompt template changes:
- [ ] compare baseline vs candidate on representative tasks
- [ ] verify output schema compliance
- [ ] verify citation quality (research lane)
- [ ] verify test/diff quality (implementation lane)
- [ ] verify no safety-boundary regression

Release status:
- candidate -> pilot -> stable -> deprecated

---

## 8) Operational metrics

Track per lane:
- first-pass acceptance rate
- rework rate
- time-to-usable-output
- cost per completed work-order
- safety/constraint violation rate
- citation adequacy (research)
- test evidence completeness (implementation)
- prompt-mode selection quality (was chosen mode appropriate?)
- fresh-context recovery rate after correction loops

## 9) Session reset rule
If the same issue requires two corrective loops, stop patching the current context and restart with a clean prompt in a fresh session.

---

## 9) Required artifacts

- `prompts/claude-code/WO_plan.md`
- `prompts/claude-code/WO_execute.md`
- `prompts/deep-research/RO_public.md`
- `prompts/deep-research/RO_private.md`
- `prompts/handoff/DDA_report.md`
- `prompts/handoff/CA_change.md`
- `PROMPT_CHANGELOG.md`
- `PROMPT_DRIFT_REVIEW_SOP.md`

---

## 10) Done definition (v1)

v1 is complete when:
1. All six templates are live and versioned.
2. Prompt changelog and drift SOP are active.
3. Monthly drift review is scheduled and owned.
4. Prompt changes pass defined evaluation gates before stable promotion.
5. At least one pilot template update has completed full detect->deploy->monitor loop.
