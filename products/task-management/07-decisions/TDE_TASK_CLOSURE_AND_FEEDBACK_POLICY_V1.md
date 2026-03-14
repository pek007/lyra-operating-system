# TDE Task Closure and Feedback Policy v1

Status: Draft active
Owner: Peter + Lyra
Product: Task Management (`A-007`)
Date: 2026-03-14
Related:
- `products/task-management/07-decisions/TDE_DECISION_TO_ADVANCEMENT_POLICY_V1.md`
- `CLOSED_LOOP_IMPROVEMENT_MODEL_V1.md`
- `products/task-management/03-operating-model/OPERATING_MODEL.md`

## Purpose
Define how a TDE task ends and how task completion or stoppage feeds a closed-loop improvement path instead of becoming a dead end.

This policy exists because task state alone is not enough.
A task reaching `Done` answers whether that work item completed.
It does not by itself answer whether:
- the objective is complete,
- the workflow should continue,
- the result produced useful evidence,
- friction exposed a system weakness,
- or follow-up work should be created.

## Core statement
A TDE task should end in two layers:
1. task-level closure state
2. post-close feedback evaluation

Both are required for a healthy operating loop.

## Task-level closure states
### Canonical completion state
- `Done` remains the canonical task-level completion state.

### Other meaningful non-active end states
A task may also end its current execution cycle as:
- `Blocked`
- `Deferred`
- `Escalated`

Interpretation:
- `Done` = this bounded work item completed
- `Blocked` = this bounded work item cannot currently proceed due to a hard blocker
- `Deferred` = this bounded work item is intentionally paused for later re-entry
- `Escalated` = continuation depends on a higher authority or broader decision path

These are task-cycle end states, not necessarily objective end states.

## Mandatory post-close evaluation
For non-trivial tasks, TDE should perform a post-close evaluation after the task leaves active execution.

This evaluation should answer at minimum:
1. What happened?
2. Did the task achieve the intended result?
3. What evidence exists?
4. Did execution expose friction, ambiguity, or failure?
5. What should happen next?

## Minimum closure record
A closure evaluation should produce a durable record containing at least:
- `task_id`
- `closure_state`
- `result_summary`
- `evidence_refs`
- `outcome_vs_expected`
- `next_recommendation`
- `friction_flags`
- `evaluated_at`
- `evaluated_by_role`

This does not require a universal heavy artifact for every trivial task.
But meaningful work should not rely only on transcript memory to explain why it ended and what followed.

## Canonical feedback outcomes
After closure evaluation, one primary feedback outcome should be selected.

### 1. `close_clean`
Use when:
- the task completed as intended,
- evidence is sufficient,
- and no meaningful structural follow-up is needed.

Expected effect:
- task stays `Done`
- workflow/objective evaluation may continue normally
- no additional improvement artifact required

### 2. `close_and_chain`
Use when:
- the task completed,
- and the next bounded task or workflow stage should proceed.

Expected effect:
- task stays `Done`
- successor path may activate under decision/chaining policy

### 3. `close_and_improve`
Use when:
- the task completed,
- but execution revealed recurring friction, weak interfaces, missing standards, or process debt.

Expected effect:
- task stays `Done`
- create or update an improvement item in the correct owning layer
- retain the learning structurally, not just conversationally

### 4. `close_and_escalate`
Use when:
- the task reached a point where continuation depends on a meaningful decision outside delegated authority,
- or the result exposed a material trade-off requiring Peter or another higher authority.

Expected effect:
- task ends as `Escalated` or `Done` with escalation linkage, depending on context
- create or update a decision/escalation artifact

### 5. `close_as_error`
Use when:
- the task exposed a meaningful error, control break, process failure, or incident-grade miss.

Expected effect:
- route into the error/incident handling path
- create or update the correct error/control artifact
- trigger corrective and preventive action where appropriate

## Relationship to decision-to-advancement
This policy complements the decision-to-advancement policy.

- decision-to-advancement answers: what happens next in the workflow?
- task-closure-and-feedback answers: what did this task ending mean, and what should the system learn from it?

In practice:
- `close_and_chain` often pairs with decision outcome `continue`
- `close_and_escalate` often pairs with decision outcome `escalate`
- `Blocked` / `Deferred` closures may pair with `block` / `defer`
- `close_as_error` may coexist with a block, escalation, or retry path depending on severity

## Closed-loop rule
Task closure should feed the broader closed-loop improvement model:
- execution happens
- result is detected and evaluated
- signal is classified
- ownership is assigned
- the right structural layer is updated
- verification is expected
- durable learning is retained

A task is not fully closed in system terms if the task ended but the meaningful learning or corrective follow-up was lost.

## Ownership rule
Feedback follow-up must respect ownership boundaries.

- product-local friction -> owning product artifacts and actions
- cross-product/system issues -> shared/system owning layer
- incidents/errors -> approved error/incident path

Task closure should not be used to dump product-local process detail into central shared artifacts.

## Lightweightness rule
Do not create heavy closure overhead for every trivial task.

Use proportionate control:
- trivial/low-risk tasks may use compact closure logging
- meaningful, risky, blocked, escalated, or learning-rich tasks should produce stronger closure records

The principle is not maximum paperwork.
The principle is that important task endings should change future behavior when warranted.

## Practical examples
### Example A — clean completion
- task completes successfully
- evidence exists
- no recurring friction observed
- closure outcome = `close_clean`

### Example B — completion with process debt revealed
- task completes
- execution required ad hoc workaround because the interface was unclear
- closure outcome = `close_and_improve`
- improvement item created in owning product

### Example C — completion reveals strategic trade-off
- task completes enough to surface a real choice
- Product Owner cannot decide within delegation
- closure outcome = `close_and_escalate`
- escalation package created

### Example D — task stops because of control failure
- task cannot continue due to integrity/risk/process failure
- closure outcome = `close_as_error`
- error path triggered and corrective action anchored

## Minimum implementation stance
For v1, TDE does not need a universal sophisticated closure engine.
A bounded implementation is enough if it ensures:
- `Done` remains the canonical completion state
- meaningful non-clean endings are explicit
- evidence/result summary is captured for meaningful tasks
- friction can become improvement work
- incidents/errors route into the proper loop
- chaining/continuation does not erase learning from the finished task

## Bottom line
A TDE task should not simply disappear into `Done`.

It should end with:
- an explicit task-level closure state,
- a proportionate feedback evaluation,
- and, when warranted, a structural follow-up that changes future behavior.

That is how TDE becomes an operating system rather than just a task tracker.
