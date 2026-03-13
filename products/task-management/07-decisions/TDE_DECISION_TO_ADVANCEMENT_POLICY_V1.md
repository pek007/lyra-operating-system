# TDE Decision-to-Advancement Policy v1

Status: Draft
Owner: Peter + Lyra
Product: Task Management (`A-007`)
Date: 2026-03-13
Related:
- `governance/TDE_AUTONOMOUS_CHAINING_DESIGN_NOTE_V1.md`
- `os/sops/TDE_CHAINING_CONTRACT_V1.md`
- `governance/TDE_PRODUCT_OWNER_OPERATING_INSTRUCTION_V1.md`
- `DECISION_SCHEMA_V1.md`

## Purpose
Define the missing bridge between:
- a bounded execution step finishing, and
- the next bounded task starting without requiring Peter to approve every micro-handoff.

This policy treats the **D** in TDE as a governed continuation layer, not just a human approval record.

## Core statement
TDE needs three distinct layers:
- **T (Task):** what work exists and what state it is in
- **D (Decision):** whether to continue, branch, pause, research further, escalate, or stop
- **E (Execution):** perform a bounded unit of work and produce evidence

Without D as an explicit runtime layer, execution remains conversational:
- Lyra completes one small step
- Lyra recommends a next step
- Peter says "yes, do that"
- Lyra continues

With D as an explicit runtime layer, execution becomes operational:
- a step completes
- decision policy evaluates the result
- an authorized next move is selected
- the system advances automatically unless an escalation condition is hit

## Design goal
Enable bounded autonomous continuity while preserving:
- clear decision rights
- explicit escalation paths
- evidence-backed progression
- fail-closed governance
- role-based accountability

## Role model
Decision authority is role-based, not agent-based.

### Product Owner
The Product Owner role is responsible for:
- evaluating completion evidence
- proposing the next move
- deciding within delegated policy bounds
- triggering deeper decision evaluation when evidence is insufficient
- escalating to the Ultimate Decision-maker when authority or confidence is insufficient

In practice, the Product Owner may be embodied by Lyra or another runtime, but the authority belongs to the role.

### Ultimate Decision-maker
The Ultimate Decision-maker role is Peter.

This role is responsible for:
- approving escalated choices
- resolving material ambiguity or trade-offs
- making decisions outside Product Owner policy limits
- changing delegation boundaries or workflow family policy

## Canonical decision outcomes
After each bounded execution step, D must resolve to exactly one primary outcome:

1. **Continue**
   - Start the authorized next task.

2. **Branch**
   - Select one of several valid next paths.

3. **Block**
   - Mark work as blocked because a hard dependency, missing input, or external gate prevents continuation.

4. **Escalate**
   - Route a proposal to the Ultimate Decision-maker.

5. **Complete / Stop**
   - No further action is needed for this chain or objective stage.

6. **Retry**
   - Re-run the same step or a bounded correction variant under defined rules.

7. **Defer**
   - Pause intentionally until time, event, capacity, or sequencing conditions change.

8. **Research further**
   - Run a deeper decision-evaluation loop before deciding whether to continue, branch, block, escalate, retry, defer, or stop.

## Why "Research further" is a first-class outcome
"Research further" is not ordinary forward execution. It is a decision-quality loop.

Use it when:
- evidence is real but insufficient
- confidence is below threshold
- the next step has material trade-offs
- multiple valid paths exist and the recommendation quality is too weak
- a blocker may be removable through analysis rather than escalation

Canonical behavior:
- create or activate a bounded research/evaluation step
- collect additional evidence
- return to the decision check
- do not silently treat research as implicit continuation

## Decision cycle
The canonical cycle is:

**Execute -> assess evidence -> evaluate authority -> choose outcome -> act / record / escalate**

### Step 1: Execution completes
Execution must produce a completion receipt or equivalent evidence artifact showing:
- what was attempted
- result status
- relevant outputs
- errors or anomalies
- confidence signal if available
- recommendation for what should happen next

### Step 2: Product Owner assesses the result
The Product Owner evaluates:
- was the step actually completed?
- is the evidence sufficient?
- is there a clear recommended next move?
- are alternative paths materially different?
- is more research needed before deciding?

### Step 3: Authority check
The Product Owner then checks whether the recommended next move is inside delegated authority.

### Step 4: Outcome selection
One of the canonical decision outcomes is selected.

### Step 5: Runtime action
Depending on the selected outcome, the runtime:
- activates the next task
- creates a bounded research/evaluation task
- marks the work blocked
- emits an escalation package
- marks the chain complete
- schedules retry or deferral

### Step 6: Decision logging
The decision and rationale are recorded so progression is explainable and auditable.

## Decision gates
A Product Owner may auto-advance only when all of the following are true:
- the execution result is successful enough for progression
- the next step belongs to an approved workflow family or approved branch set
- the required evidence exists and meets the threshold for that family
- the next step is within delegated risk, cost, and scope bounds
- no mandatory human approval rule is triggered
- no contradiction with product goal, policy, or objective linkage exists

If any of these checks fail, the default is fail-closed:
- research further,
- block, or
- escalate.

## Delegation policy shape
Delegation should be defined per workflow family, stage family, or task family.

A policy envelope should define at minimum:
- family ID
- allowed next-step types
- allowed branching patterns
- evidence required to continue
- confidence threshold
- risk threshold
- cost / resource threshold
- write-scope boundary
- max autonomous hop count before review
- retry limit
- research budget / depth cap
- mandatory escalation triggers

## Proposed authority semantics
### Product Owner may decide
The Product Owner may select **Continue**, **Branch**, **Retry**, **Defer**, **Block**, or **Research further** when the action remains inside the approved policy envelope.

### Product Owner must escalate
Escalation to Peter is required when any of the following is true:
- authority boundary would be crossed
- risk/cost/scope exceeds delegated limits
- a meaningful strategic trade-off appears
- goal conflict or policy conflict exists
- evidence remains insufficient after bounded research
- a new workflow family or new branching pattern would be introduced
- the next step has material external, reputational, financial, legal, or architectural impact

## Research-further loop
The research-further path should be explicit and bounded.

### Inputs
- current task or decision context
- unanswered questions
- evidence gaps
- time or token budget
- expected output shape

### Outputs
A research loop should return:
- refined recommendation
- updated confidence level
- additional evidence refs
- explicit remaining uncertainties
- recommended next decision outcome

### Loop rule
After research completes, D runs again.
Research does not itself authorize continuation unless the resulting reevaluation passes the same authority gates.

## Example progression pattern
### Example A — straightforward continuation
1. Execution step finishes successfully.
2. Product Owner sees valid evidence.
3. Approved next step is deterministic and low risk.
4. Outcome = Continue.
5. Successor task is activated and started under normal TDE chaining rules.

### Example B — insufficient basis, deeper evaluation first
1. Execution step finishes with mixed evidence.
2. Product Owner sees two plausible next branches.
3. Confidence is below policy threshold.
4. Outcome = Research further.
5. Bounded evaluation task runs.
6. D reevaluates with new evidence.
7. If within authority, Product Owner continues or branches.
8. If not, escalate to Peter.

### Example C — true escalation
1. Execution step finishes and reveals a strategic trade-off.
2. Product Owner can frame options and recommendation.
3. The choice exceeds delegated authority.
4. Outcome = Escalate.
5. Peter receives a decision package with options, recommendation, evidence, and implications.

## Decision package for escalation
When escalation is required, the Product Owner should produce a compact package containing:
- decision question
- current objective / workflow context
- options
- recommended option
- rationale
- evidence refs
- confidence level
- risks / trade-offs
- consequence of delay
- what the Product Owner would do if delegated

## Relationship to existing TDE chaining
This policy does not replace state-driven chaining.
It sits above it.

- `TDE_CHAINING_CONTRACT_V1` governs how authorized successor tasks become ready.
- This policy governs whether the Product Owner is allowed to authorize the successor path in the first place.

In short:
- chaining answers **how ready work progresses**
- decision-to-advancement policy answers **whether and why that progression is allowed**

## Minimal v1 implementation stance
For v1, the system does not need a full universal decision engine.
A bounded implementation is enough if it supports:
- role-based decision rights
- explicit outcome enums including `research_further`
- policy envelopes by workflow family
- decision logging with rationale and evidence refs
- escalation packaging to the Ultimate Decision-maker
- reevaluation after bounded research

## Suggested canonical fields
A minimal decision-to-advancement record could include:
- `decision_id`
- `task_id`
- `objective_id`
- `workflow_family`
- `stage_id`
- `proposing_role` = `Product Owner`
- `escalation_role` = `Ultimate Decision-maker`
- `recommended_outcome`
- `selected_outcome`
- `recommended_next_task_id`
- `recommended_branch_id`
- `research_required` (bool)
- `confidence_score`
- `evidence_refs`
- `authority_check_result`
- `escalation_reason`
- `decision_rationale`
- `decided_at`
- `decided_by_role`

## Non-negotiables
1. Decision rights must belong to roles, not just runtimes.
2. Product Owner autonomy must be policy-bounded.
3. `research_further` must be explicit and re-enter the decision loop.
4. Escalations must target the Ultimate Decision-maker role, not vague human intervention.
5. Completion of a micro-step must not depend on transcript memory alone to determine what happens next.
6. The system must fail closed when authority, evidence, or policy alignment is unclear.

## Recommended next follow-on work
1. Map Product Owner and Ultimate Decision-maker into the broader role model.
2. Identify the first workflow family to pilot with explicit `research_further` support.
3. Add validation examples and one reference policy envelope artifact.
4. Decide whether `risk_threshold` and `cost_threshold` should remain coarse enums or move to richer typed contracts.
5. Wire these schemas into the runtime decision/chaining path.

## Machine-readable contracts added
The first v1 schema set for this policy is now defined in:
- `schemas/tde_decision_advancement_record/v1.0.0.schema.json`
- `schemas/tde_decision_policy_envelope/v1.0.0.schema.json`
- `schemas/tde_decision_escalation_package/v1.0.0.schema.json`

These cover:
- the per-step decision record,
- the workflow-family delegation envelope,
- and the Product Owner -> Ultimate Decision-maker escalation package.

A first reference envelope is also added at:
- `products/task-management/07-decisions/REFERENCE_TDE_POLICY_ENVELOPE_IMPLEMENTATION_VERIFICATION_V1.json`

## Bottom line
The missing bridge is real.

TDE already has meaningful state and chaining foundations, but it still needs an explicit role-governed decision-to-advancement layer.

That layer should let the Product Owner:
- assess execution results,
- decide within bounded authority,
- trigger deeper research when needed,
- and escalate cleanly to Peter as Ultimate Decision-maker when the boundary is reached.

That is the practical operating meaning of the **D** in TDE.