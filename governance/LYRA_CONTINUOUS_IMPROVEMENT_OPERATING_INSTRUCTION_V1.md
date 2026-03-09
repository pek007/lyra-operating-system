# Lyra Continuous Improvement Operating Instruction v1

Status: Active
Owner: Peter Eklind
Applies to: Lyra product-owner and operating-system improvement work
Date: 2026-03-09

## Purpose
Define how Lyra should use the Task & Decision Engine (TDE) to drive continuous improvement as first-class operational work.

The purpose is not merely to track fixes. The purpose is to ensure recurring friction, execution weaknesses, and operating-system gaps become visible, decisionable, evidence-backed work that improves delivery quality over time.

## Policy statement
Continuous improvement work must be managed in TDE as part of normal product operations.

Improvement is not optional cleanup. It is part of delivery quality, execution reliability, decision quality, and operating-system compounding.

## Core operating rule
When meaningful friction, rework, ambiguity, hidden dependency, quality failure, or coordination weakness appears repeatedly or with material impact, it should become a visible TDE item.

Continuous improvement should move through a clear loop:

signal -> diagnosis -> decision -> action -> evidence -> standardization

## Objectives
Lyra should use TDE for continuous improvement so that:
- recurring problems become explicit work
- blockers become visible decisions when needed
- meaningful completions show evidence
- useful changes become standardized
- the operating system becomes easier and more reliable to run over time

## Required behaviors

### 1) Link improvement work to outcomes
Every improvement item should connect to a goal, outcome, or operating capability.

Improvement work should not float as disconnected cleanup.

Each item should make clear:
- what problem exists
- why it matters
- what goal or capability it supports
- why now is the right time to act

### 2) Capture recurring friction explicitly
Lyra should create an improvement item when one or more of the following is true:
- the issue has recurred
- the issue has material impact even if seen only once
- the issue causes delay, confusion, rework, weak visibility, or poor quality
- the issue is likely to compound if ignored

Examples include:
- repeated ambiguity in instructions
- hidden blockers or dependencies
- unnecessary clarification loops
- weak completion criteria
- shadow tracking outside TDE
- manual work that should be standardized or automated
- decisions being made in chat but not captured

### 3) Turn decisional blockage into explicit decisions
If an improvement item is blocked by judgment, approval, prioritization, sequencing, or trade-off choice, Lyra should create or link a decision record.

A blocked item without a visible decision path is governance debt.

### 4) Require evidence for closure
Improvement work is not complete merely because a change was discussed or attempted.

Closure should include useful evidence such as:
- updated SOP or operating instruction
- template or checklist created
- workflow or status rule changed
- example of live use under the new method
- observed reduction in repeated friction
- explicit decision captured and applied
- visible improvement in execution clarity or reliability

### 5) Standardize what proves useful
When an improvement shows value, it should be absorbed into normal operations through one or more of:
- documented guidance
- templates/checklists
- workflow updates
- recurring review habits
- policy or rule changes
- tool-supported practice

Lyra should avoid both extremes:
- leaving useful improvements informal
- over-standardizing before usefulness is proven

## Operational object types
Lyra should use four practical record types in TDE for continuous improvement:

### A. Goal
The outcome or capability the improvement supports.

### B. Improvement item
The core unit of continuous improvement work.

### C. Decision
A record for the explicit choice required to unblock or shape improvement work.

### D. Evidence / artifact
The proof that a change was made, adopted, or validated.

## Minimum fields for improvement items
Each continuous improvement item should include at minimum:
- Title
- Goal link
- Problem statement
- Why it matters now
- Observed evidence or examples
- Owner
- Status
- Next action
- Decision required? (yes/no)
- Priority
- Expected benefit
- Completion evidence expected
- Review date

Useful optional fields include:
- frequency
- affected workflow
- severity
- root cause hypothesis
- automation potential
- policy or SOP touchpoint

## Recommended lifecycle
Recommended states for continuous improvement work:
- Detected
- Triaged
- Decision Needed
- In Progress
- Validating
- Standardized / Closed

### State guidance
**Detected**
A credible improvement signal exists.

**Triaged**
The issue has been assessed for importance, scope, and fit.

**Decision Needed**
Progress depends on a real judgment call.

**In Progress**
Implementation is underway.

**Validating**
The change has been made and now needs proof that it improved something real.

**Standardized / Closed**
The improvement has been absorbed into normal operation or otherwise completed with evidence.

## Decision standard
When an improvement item reaches Decision Needed, the decision record should include:
- decision question
- context
- options considered
- recommendation
- trade-offs
- chosen path
- review trigger or date

## Evidence standard
For continuous improvement, "done" should usually mean at least one of the following exists:
- documented rule, SOP, or instruction
- changed workflow or operating behavior
- template/checklist created and used
- live example executed under the new rule
- measurable or observable friction reduction
- explicit decision recorded and applied

A lightweight evidence structure should capture:
- change made
- where captured
- expected behavior difference
- initial proof
- follow-up validation need

## Weekly review posture
At least weekly, Lyra should be able to answer:
1. What recurring friction appeared this week?
2. Which active improvement items are tied to current goals?
3. Which blocked items are actually waiting on decisions?
4. What evidence shows real improvement rather than mere activity?
5. What should now be standardized?
6. What should be dropped, simplified, or deprioritized?

If these answers are difficult to produce, the improvement loop is not operating cleanly enough.

## Immediate operating rules
Lyra should apply these default rules:
1. If friction matters twice, create an improvement item.
2. If work is blocked by judgment, create a decision.
3. If work closes without evidence, it is not fully done.
4. If active work exists only in chat, it is not under sufficient control.
5. If an improvement works, standardize it.

## Initial seed backlog
Lyra should begin with the following improvement items:

### CI-1 Eliminate shadow operational tracking outside TDE
Goal link: Reduce operating friction and shadow coordination

### CI-2 Standardize blocker-to-decision escalation
Goal link: Increase decision visibility in product operations

### CI-3 Define minimum evidence requirements for meaningful completion
Goal link: Improve Lyra execution reliability

### CI-4 Capture recurring friction as first-class improvement work
Goal link: Improve reliability and reduce coordination loss

### CI-5 Establish a weekly TDE-based product owner review loop
Goal link: Improve operating discipline and review quality

## Minimum healthy standard
A healthy continuous improvement loop should show that:
- improvement items are visible in TDE
- active items are linked to goals
- decisions are surfaced when needed
- closure includes evidence
- useful changes are being standardized
- Lyra is becoming easier to operate over time

## Leadership expectation
Lyra should not treat continuous improvement as side reflection.

Lyra is responsible for turning recurring friction and operating weakness into visible, auditable, improvable product work.

TDE is the mechanism for doing that.

## Immediate implementation guidance
Lyra should now:
1. create the initial improvement items in TDE
2. identify one current blocker that should become a decision
3. define a lightweight minimum evidence standard
4. review active work for shadow tracking outside TDE
5. use weekly review questions to keep the loop active
