# Task Management / TDE operator checklist

Use this checklist for one bounded Task Management operating cycle.

## 1. Frame the target
- Is this a task, job, product execution issue, readiness check, or continuity update?
- What is the smallest bounded action or decision?
- What result shape is expected: `result`, `status`, `blocked`, or `decision-needed`?

## 2. Confirm the canonical surfaces
Typical Task Management surfaces:
- `os/runtime/tde_state.sqlite`
- `os/runtime/TASKS_from_db.md`
- Task Management product execution artifacts
- job `STATE.md` / `HANDOVER.md`
- relevant evidence notes or decision artifacts

Do not treat chat history as the canonical state layer.

## 3. Read only what is necessary
Read the referenced task/job/product artifacts needed to act safely.
Avoid broad rediscovery unless the request explicitly asks for a larger review.

## 4. Operate the bounded cycle
Typical cycle:
1. identify the exact bounded target
2. inspect current state/evidence
3. determine the next smallest viable action or decision
4. update durable state if required in the same cycle
5. return concise outcome and next action

## 5. Continuity rules
Use the right continuity target:
- `jobs/<JOB-ID>/STATE.md` for active job state
- `jobs/<JOB-ID>/HANDOVER.md` when ownership changes or cross-session transfer matters
- product `PLAN.md` / `RISKS.md` / `DECISIONS.md` when product operating surfaces must change
- evidence note when the cycle materially affects readiness, verification, or product understanding

## 6. Escalation tests
Escalate when:
- a TDE kernel contract may need to change
- deployment/cutover judgment is required
- a cross-product interface conflict appears
- no adequate canonical state/evidence path exists
- the request is too broad for a bounded cycle

## 7. Return format
Use a concise structure:
- `target:`
- `outcome:`
- `state/evidence:`
- `note:`
- `next action:`

## Typical next actions
- update job state
- update product plan/risk/readiness artifact
- create or refresh evidence note
- escalate a substrate/interface decision
- hand off via Control Panel with explicit continuity target
