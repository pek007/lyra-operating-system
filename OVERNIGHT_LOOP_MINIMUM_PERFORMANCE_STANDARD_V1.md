# OVERNIGHT_LOOP_MINIMUM_PERFORMANCE_STANDARD_V1.md

Status: Active
Owner: Lyra
Date: 2026-03-23

## Purpose
Keep overnight performance management simple, useful, and auditable.

This standard exists to answer only three questions:
1. Did the loop run according to plan?
2. Did it move us meaningfully closer to current priorities / vision?
3. Can we reconstruct what happened if we need to audit or debug it?

Do not expand this into a large KPI framework unless there is a clear unmet need.

## The minimum model

### 1. Execution
We need to know whether each planned overnight stage actually ran.

For each overnight stage, record:
- stage name
- scheduled run window/date
- status: `success` | `failed` | `partial` | `skipped`
- expected output artifact/object
- actual output artifact/object (if different)
- short blocker/failure note if relevant

### 2. Contribution
We need to know whether the overnight work helped, not just whether activity occurred.

Each stage should classify its contribution using one primary category:
- `advanced_priority`
- `reduced_blocker`
- `improved_understanding`
- `prepared_next_step`
- `no_meaningful_movement`

Use one category only unless there is a strong reason otherwise.

### 3. Auditability
We need to be able to reconstruct what happened.

Each stage should retain or link:
- key input surfaces used
- key output artifact/object
- material decisions or dispositions made
- changes executed, if any
- blocker/failure details, if any

This should be sufficient for after-the-fact review without re-reading full chat history.

## Stuckness rule
A stage/item should be treated as potentially stuck when either condition holds:
- the same priority is selected repeatedly without a clear new advancement, or
- the same blocker/failure persists across multiple cycles without disposition change

When a stuckness pattern is detected, the overnight system should explicitly mark it as one of:
- `escalate`
- `replan`
- `record_no_action`

Do not allow silent repetition by inertia.

## Minimum nightly ledger
Maintain one compact overnight ledger entry per night that covers the full loop:
- product learn-and-replan passes
- portfolio input consolidation
- portfolio decide-and-kickoff
- overnight execution loop
- morning executive brief

For each stage include only:
- stage
- status
- output reference
- contribution category
- blocker note (optional)

## Weekly review questions
Review the overnight loop weekly using only these questions:
1. Did the loop run reliably?
2. Did it produce meaningful movement often enough?
3. Where did we see repeat-stuck patterns?
4. Did the audit trail stay clear enough to inspect any questionable night?
5. Does the current loop still fit the portfolio bottleneck and Phase 1 priorities?

## Management intent
This is a control standard, not a reporting burden.

The goal is:
- enough structure to notice failure, drift, or empty activity
- enough traceability to inspect what happened
- not so much measurement that the measurement system becomes its own workload
