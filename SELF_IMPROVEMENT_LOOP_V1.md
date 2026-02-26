# SELF_IMPROVEMENT_LOOP_V1.md

Status: Active draft v1  
Owner: Peter (governance), Lyra (coordination), Engineering role (implementation)

## Objective
Implement a safe, measurable self-improvement loop for Lyra/OpenClaw by improving **policies, prompts, routing, and skills**—without model weight updates in this phase.

## Scope (v1)
In scope:
- Run telemetry schema + logging
- Deterministic evaluation harness
- Champion-challenger experimentation
- Promotion/rollback gates
- Approval-card + sandbox guardrails

Out of scope:
- Fine-tuning / RLHF / continual weight updates
- Autonomous high-risk external actions

---

## 1) Operating principle
No “improvement” is accepted without evidence.

Required loop:
1. Observe (run telemetry)
2. Hypothesize (what to improve)
3. Experiment (challenger)
4. Evaluate (quality/cost/time/safety)
5. Promote or rollback
6. Record decision + rationale + evidence

---

## 2) Canonical run event schema (agent_run_event.v1)

Store append-only logs under:
- `knowledge/events/YYYY-MM/agent_runs.jsonl`

Each event must include at minimum:
- `schema`: `agent_run_event.v1`
- `run_id`
- `timestamp_start`, `timestamp_end`
- `agent_id`, `mode`
- `task_ids`
- `model.provider`, `model.name`, `model.lane`
- `tool_calls` summary
- `usage` (tokens/cost/latency)
- `outcome.status` (`success|partial|fail`)
- `outcome.artifacts_changed`
- `safety.approval_required`, `safety.approved`, `safety.violations`
- `trace.otel_trace_id` (optional in early phase but reserved)

### Data rules
- Append-only; no in-place edits
- Redact secrets/credentials by default
- Keep stable enums; changes require schema version bump

---

## 3) Evaluation harness v1

## Purpose
Provide deterministic regression and challenger evaluation for policy/prompt/routing/skill changes.

### Inputs
- Fixed task suite from real operations tasks
- Synthetic regression tasks for known failure modes
- Baseline champion configuration
- Candidate challenger configuration

### Outputs
- Scorecard JSON + markdown summary with:
  - task success rate
  - handoff acceptance rate
  - rework rate
  - median latency
  - cost per completed task
  - safety violations count
  - approval-path compliance

### Rules
- Same task set and scoring rubric for champion and challenger
- “Noisy” metrics must be repeated across multiple runs
- Failed safety gates automatically fail experiment regardless of quality/cost

---

## 4) Champion-challenger policy

### Candidate types
- model routing config
- prompt template updates
- tool wrapper/policy updates
- retrieval/memory policy updates

### Exposure policy
- Start challenger at small controlled share (e.g., 5–10%)
- Increase only if criteria are met over defined sample size

### Promotion criteria (all required)
- No critical safety violations
- No increase in incident-linked failures
- Quality non-inferior or improved
- Cost and latency within accepted bounds
- Reviewer sign-off recorded

### Anti-thrash rule
- No repeated route/model flips without monthly review
- Emergency override allowed only with rationale + rollback window

---

## 5) Promotion and rollback gates

## Promotion checklist
- [ ] Evaluation suite passed
- [ ] Safety checks passed
- [ ] Approval-card requirements met for affected actions
- [ ] Change record created with rationale
- [ ] Rollback command/path documented and tested

## Rollback triggers (any one)
- Critical safety violation
- Material cost spike beyond threshold
- Significant quality regression
- Approval bypass detected
- Production incident linked to change

Rollback must:
1. Revert to champion config
2. Log incident/change linkage
3. Open corrective action task

---

## 6) Safety architecture for self-improvement

### Guardrails
- Advisory-by-default behavior
- High-risk external actions require approval cards
- Permission envelopes enforce allowed tools/scopes
- Sandbox tiers for execution context:
  - Tier A: read-only
  - Tier B: workspace patch-write
  - Tier C: shell/dev sandbox
  - Tier D: external side effects (always gated)

### Non-negotiables
- No silent policy widening
- No direct external action from unapproved challenger path
- No secrets in telemetry/events

---

## 7) Cadence and governance rhythm

### Weekly
- Review run scorecard trends
- Review top recurring failures
- Review safety/approval latency
- Decide continue/stop for active challengers

### Monthly
- Champion-challenger governance review
- Routing stability and anti-thrash check
- Policy tightening based on incidents
- Archive and summarize learnings

---

## 8) Metrics (v1 scorecard)

Track weekly:
- Handoff acceptance rate
- Rework rate
- Cost per completed task
- Median latency per lane
- Tool error rate
- Safety violations count
- Approval request/deny/latency
- Routing switch count
- Incident-linked change count

---

## 9) Implementation plan (first 4 weeks)

Week 1:
- Define and freeze `agent_run_event.v1`
- Implement append-only run logging
- Add basic parser/validator test

Week 2:
- Build eval harness runner and fixed task suite v1
- Generate first baseline champion scorecard

Week 3:
- Enable first controlled challenger experiment (routing/prompt)
- Add promotion checklist workflow and change record template

Week 4:
- Run governance review
- Promote or rollback based on criteria
- Publish lessons learned and update policies

---

## 10) Definition of done (v1)

v1 is complete when:
1. >=90% production runs emit valid `agent_run_event.v1` events
2. Eval harness produces reproducible champion vs challenger scorecards
3. At least one challenger cycle completed with explicit promote/rollback decision
4. Safety gates are enforced and auditable
5. Monthly review cadence is operating and documented
