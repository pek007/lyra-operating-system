# Prompt Injection Defense — Implementable Now Plan (v1)

Source report: `knowledge/reports/2026-03-03__deepresearch__prompt-injection-defenses-and-best-practices__v1.md`
Date: 2026-03-03
Owner lane: Security + Architecture

## What we can implement now (highest ROI)

1. **Tool boundary enforcement shim (phase 0)**
   - Add a single policy-check wrapper for all local high-risk scripts first (`trello_sync`, `evidence_ingest`, any subprocess surfaces).
   - Decision outcomes: `allow | deny | needs_approval`.
   - Require explicit approval token for any write/network mutation.

2. **Compile `skills-policy.yaml` into an executable allowlist artifact**
   - Generate a machine-readable runtime policy map from `skills-policy.yaml`.
   - Fail closed if a tool is used without a policy entry.
   - Add drift check in CI: declared policy must match effective exposed tool set.

3. **Capability-drop mode for untrusted content**
   - For web/docs/email inputs: enforce read-only profile; block outbound writes and privileged exec.
   - Require explicit operator approval to transition from analysis context to action context.

4. **Prompt-injection regression suite gate**
   - Add adversarial tests for direct + indirect injection in CI.
   - Block promotion of prompt/policy changes on any bypass.

5. **Detection + telemetry minimum baseline**
   - Log all policy decisions as structured events.
   - Add 3 canaries:
     - approval-bypass sentinel,
     - cross-domain leakage sentinel (`os` -> `px`),
     - honeytoken exfil sentinel.

## Concrete repo changes to queue

- New: `tools/policy_enforcement.py` (central decision engine)
- New: `tools/compile_skills_policy.py` (yaml -> runtime artifact)
- New: `tools/tests/test_prompt_injection_regression.py`
- Update: `.github/workflows/devsecops-baseline.yml` to run security regression checks
- Update: `PROMPT_DRIFT_REVIEW_SOP.md` to require regression pass evidence
- Update: `SECURITY_ADOPTION_PLAN.md` with P0/P1 milestones and owners

## 14-day execution slice

- **Days 1–3**: policy wrapper + structured logging + trello guard rails
- **Days 4–6**: policy compiler + drift check in CI
- **Days 7–10**: injection regression tests (PI-D-001, PI-I-001, OUT-001, DOM-001)
- **Days 11–14**: capability-drop mode + canaries + incident runbook additions

## Success criteria

- Zero high-risk tool executions without approval token.
- CI fails on policy drift and injection regression failures.
- Untrusted-content workflows cannot perform privileged tool actions.
- All tool decisions emitted to structured audit logs.
