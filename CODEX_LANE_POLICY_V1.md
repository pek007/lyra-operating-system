# CODEX_LANE_POLICY_V1.md

Status: Active draft v1  
Owner: Peter (governance), Lyra (operations)

## Objective
Standardize GPT-5.3-Codex usage so delivery quality is high, risk is bounded, and outcomes are measurable.

## Principle
Treat Codex as a long-horizon execution controller, not a one-shot code generator.

---

## 1) Lane contract

Each Codex work order must define:
1. Goal (single sentence)
2. Scope and explicit non-goals
3. Hard constraints (must/must-not)
4. Verification commands/checks
5. Artifact update requirement
6. Deliverable schema

No contract => no execution.

---

## 2) Reasoning effort policy (routing-level)

Default settings:
- `medium` for routine coding and ops tasks
- `high` for architecture/security/significant cross-file changes
- `xhigh` only for high-ambiguity, high-consequence, long-horizon work

Rules:
- Set reasoning effort in lane/routing config, not ad-hoc prompt wording.
- Escalation to higher effort must include rationale in task notes.

---

## 3) Prompt discipline

### Required style
- concise, contract-driven, verification-focused
- specify boundaries and outcomes
- avoid over-prescriptive internal step micromanagement

### Prohibited style
- verbose “ritualized reasoning” instructions without measurable value
- broad repo-dump prompts when targeted retrieval is enough

---

## 4) AGENTS layering policy

- Global AGENTS: minimal universal norms
- Repo AGENTS: execution norms (tests, diff standards, done criteria)
- Directory overrides: only where workflows materially differ

Goal: reduce instruction collisions and truncation risk.

---

## 5) Safety controls

- Destructive commands require approval gate
- Network/web usage must be explicit and narrow
- Sensitive paths/files protected by deny rules where applicable
- High-risk actions require evidence + rollback notes

---

## 6) Verification and artifact discipline

Every non-trivial run must return:
1. files changed
2. verification/test outputs
3. assumptions and known risks
4. supervisory artifact update (task/plan/change note)

Missing any required item => result is incomplete.

---

## 7) Operational metrics

Track weekly:
- first-pass acceptance rate
- rework rate
- cost per successful task
- verification completeness rate
- artifact update compliance rate
- safety incident count

---

## 8) Promotion and drift policy

- Codex lane behavior reviewed monthly under champion/challenger process
- Template/routing changes require scorecard evidence
- Regressions trigger rollback to previous known-good lane policy

---

## 9) Done definition (v1)

v1 is active when:
1. Contract template is used for all Codex work orders.
2. Reasoning effort policy is reflected in routing docs.
3. Verification/artifact discipline is enforced in reviews.
4. Weekly scorecard is captured and reviewed.
