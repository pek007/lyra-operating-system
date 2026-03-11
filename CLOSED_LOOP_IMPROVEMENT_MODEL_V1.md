# Closed-Loop Improvement Model v1

Status: Draft active model
Owner: Peter / Lyra
Date: 2026-03-11

## Purpose
Make the self-reinforcement logic of Lyra OS explicit.

This model exists to answer:
- how the system should learn from execution
- how issues should become durable improvements
- how to avoid being good at describing problems without changing behavior

## Core idea
Lyra OS should function as a closed-loop improvement system:

1. something happens in execution
2. the system detects a signal
3. the signal is classified and owned
4. corrective action is assigned
5. the right model/process/control layer is updated
6. the change is verified
7. the learning is retained

If one of those steps is missing, the loop is incomplete.

## The loop

### 1. Execution
Sources of signal:
- active product work
- delivery/runtime behavior
- product reviews
- incidents / near misses
- user feedback
- coordination failures
- evidence / health checks

Question:
What happened that the system should pay attention to?

### 2. Detection
Detection mechanisms include:
- product review protocol
- operational observation in execution
- error/incident reporting
- readiness checks
- evidence generation and audits
- direct human observation

Question:
Did we notice the issue, miss, drift, or opportunity clearly enough?

### 3. Classification
The system should classify the signal by at least:
- issue type: incident / near miss / control failure / process failure / decision failure / improvement opportunity
- scope: product-local / cross-product / system-level
- ownership: which product or shared owner should respond
- nature: execution problem / product-model problem / interface problem / governance problem / delivery-mode problem

Question:
What kind of thing is this, and who owns it?

## Ownership rule
Follow the process ownership rule:
- product-local issues belong to the owning product
- only genuinely cross-product/system issues should be handled in shared artifacts

### 4. Assignment
A meaningful signal should produce at least one of:
- corrective task
- product review follow-up
- decision to be made
- explicit error report
- product-model update requirement

Assignment must also respect canonical action placement:
- product-local issues -> owning product action system
- shared/system issues -> owning shared/system error report unless ownership is explicitly transferred or a dedicated shared board is deliberately created

Question:
What changes now, who is responsible, and where is the canonical action anchor?

### 5. Structural update
The system should update the correct layer, not just describe the problem.

Possible update targets:
- `PLAN.md`
- `RISKS.md`
- `GOVERNANCE.md`
- `INTERFACES.md`
- `DECISIONS.md`
- delivery-mode decision artifacts
- shared coordination rules
- error reports
- verification/evidence artifacts

Question:
Which artifact or control layer must change so future behavior changes too?

### 6. Verification
A fix is not complete until the system checks whether it worked.

Verification may include:
- product review follow-up
- specific evidence artifact
- readiness check
- successful execution under the new rule/control
- explicit closure criteria in an error report

Question:
How do we know this improvement actually changed the system?

### 7. Retention
If the issue taught the system something durable, that learning should be retained in the right place.

Retention mechanisms may include:
- decision records
- product-model updates
- standards/rules updates
- error reports
- governance updates
- daily memory / curated memory where appropriate

Question:
Where should this learning live so the system does not forget it?

## Effective-loop rule
A loop is effective only if it changes future behavior.

That means a meaningful issue should not stop at:
- observation
- summary
- discussion
- documentation alone

It should end in:
- changed work
- changed model
- changed control
- changed decision logic
- or an explicit decision not to change, with rationale

## Weak-loop failure modes
Watch for these anti-patterns:

### 1. Reflection without correction
The system describes the issue well but nothing changes.

### 2. Correction without retention
A fix happens, but no durable artifact is updated.

### 3. Retention without verification
A rule or document changes, but no one checks whether behavior improved.

### 4. Wrong-layer updates
The issue belongs to product ownership, but is only documented centrally; or vice versa.

### 5. Over-reporting
Too many weak signals become heavy artifacts, creating noise instead of learning.

## Current state assessment
Lyra OS is now stronger in:
- product modeling
- review structure
- delivery-mode decision quality
- error capture and reporting discipline

Lyra OS is weaker in:
- guaranteed assignment from issue to task/action
- consistent verification of whether fixes worked
- clear recurrence measurement

So the system is no longer open-loop, but it is not yet fully closed-loop in consistent operation.

## Practical operating rule
For every meaningful issue, ask:
1. What happened?
2. Who owns it?
3. What changes now?
4. Which artifact/control layer changes?
5. How will we verify the change worked?
6. Where is the learning retained?

If these questions cannot be answered, the improvement loop is incomplete.

## Relationship to existing artifacts
This model does not replace existing standards.
It connects them.

Examples:
- Product Review Protocol = major detection/classification mechanism
- Error Reporting Standard = structured issue capture mechanism
- Product Model Standard = structural retention layer
- Process Ownership Rule = ownership decision rule
- Delivery Modes Decision Framework = one type of structural update mechanism

## Short rule
**Execution should produce learning, learning should produce change, and change should be verified and retained.**
