# PRODUCT_WAY_OF_WORKING_PROCESS_V1

Status: Active (v1)
Owner: Lyra (Control Panel Product Owner)

## Purpose
Define the common framework all Lyra OS products use to set:
1) Vision
2) Goals
3) Plan
4) Continuous improvement loop

This process defines **structure and governance**. Product Owners provide product-specific content.

## Design principles
- Outcome-first, artifact-light
- Trigger-based (not calendar-based)
- Evidence before escalation
- One source of truth per product
- Comparable structure across products

## Canonical storage model
Per product, store product management artifacts under:

`products/<product-id>/management/`

Required files:
- `VISION.md`
- `GOALS.md`
- `PLAN.md`
- `IMPROVEMENT_LOG.md`
- `SCORECARD.md`
- `DECISIONS.md`

Optional:
- `CUSTOMER_MAP.md`
- `RISKS.md`
- `INTERFACES.md`

## Artifact contracts (required sections)

### 1) VISION.md
- Product mission
- Primary customers
- Customer problems/jobs
- Value proposition
- Non-goals / out-of-scope
- Success definition (qualitative)

### 2) GOALS.md
For each goal:
- Goal ID
- Outcome statement
- Leading indicator(s)
- Lagging indicator(s)
- Guardrails / constraints
- Owner job role
- Exit criteria

### 3) PLAN.md
Use a rolling priority stack (no date horizon required):
- Now
- Next
- Later

Each initiative includes:
- Initiative ID
- Problem to solve
- Expected outcome
- Dependencies
- Acceptance criteria
- Evidence required

### 4) IMPROVEMENT_LOG.md
Log each improvement cycle entry:
- Trigger
- Observation
- Hypothesis
- Change made
- Result
- Decision (adopt/revert/continue-test)
- Follow-up action

### 5) SCORECARD.md
Minimum metrics:
- Customer value signal
- Reliability/quality signal
- Flow signal (lead/cycle/WIP)
- Risk/compliance signal
- Cost-efficiency signal

### 6) DECISIONS.md
For all meaningful decisions:
- Decision ID
- Context
- Decision
- Trade-offs
- Impacted artifacts/processes
- Reversal conditions

## Operating loop (trigger-based)

### Entry triggers
Start a product cycle when any trigger occurs:
- New customer need or demand shift
- KPI drift outside guardrail
- Material incident / repeated defects
- Architecture/process bottleneck
- New strategic directive

### Loop steps
1. **Sense**: capture signal and evidence
2. **Frame**: update problem statement and desired outcome
3. **Prioritize**: re-rank Now/Next/Later initiatives
4. **Execute**: run smallest viable change
5. **Verify**: measure effect vs acceptance criteria
6. **Decide**: adopt / adapt / revert
7. **Codify**: update docs + standards + scorecard

## Governance rules
- No initiative in PLAN without explicit acceptance criteria.
- No major change closed without evidence link.
- Goals must be outcome-based, not activity-based.
- Cross-product dependencies require interface declaration.
- Product Owners can tailor sections, but may not remove required artifacts.

## Process ownership and refinement
- Process owner: Control Panel Product Owner (Lyra)
- Product Owners propose improvements through `DECISIONS.md` and pull requests.
- Refinements are versioned here (v1, v1.1, ...), with change rationale.

## Minimum adoption checklist (for each product)
- [ ] Product folder created at `products/<product-id>/management/`
- [ ] Required artifacts present
- [ ] At least one active goal with indicators and guardrails
- [ ] Plan initiatives with acceptance criteria
- [ ] Improvement log contains first loop entry
