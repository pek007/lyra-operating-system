# Product Review Protocol v1

Status: Draft active protocol
Owner: Peter / Lyra
Date: 2026-03-11

## Purpose
Define how PX Strategy should review products now that Product-as-Code models exist.

The goal is to make product reviews:
- grounded in canonical product artifacts
- useful for decisions rather than ceremonial reporting
- linked to TDE and real execution state
- comparable across the portfolio without forcing identical depth for every product

## Core principle
A product review should answer:
- Is this product still pointed at the right outcome?
- Is it operating coherently?
- Is active work aligned with strategy?
- Are the main risks visible and managed?
- What decision or intervention is needed now?

If a review cannot answer those questions, the product model or execution system is probably too weak.

## Review inputs
Every product review should use the canonical product model as the primary input.

Minimum expected inputs:
- `PRODUCT.md`
- `MODEL.yaml`
- `04-execution/PLAN.md`
- `04-execution/RISKS.md` if present
- `05-performance/METRICS.md` if present
- `07-decisions/DECISIONS.md`
- current TDE state / active work / blockers / evidence

For Standard-level products, the full standard artifact set should be the review basis.

## Review cadences

### 1. Weekly product review
Purpose:
- inspect current operating health
- check active work, blockers, and evidence
- capture recurring friction and next actions

Best for:
- active products
- products with meaningful current execution load

### 2. Monthly product model review
Purpose:
- inspect whether the product model itself is still coherent and current
- check maturity, artifact freshness, and structural gaps

Best for:
- all active products
- especially products at Thin or Standard maturity

### 3. Milestone or gate review
Purpose:
- review major readiness, deployment, strategic shift, or boundary decisions

Best for:
- launches
- production activation
- major interface changes
- material governance or risk decisions

## Review layers

### Layer A — Direction
Review:
- purpose
- vision
- customer
- strategy

Questions:
- Is the product still solving the right problem?
- Is strategy still coherent with the current portfolio context?
- Has customer or consumption reality changed?

### Layer B — Operation
Review:
- operating model
- governance
- interfaces
- decision log

Questions:
- Is the product being run the way it says it should be run?
- Are ownership, escalation, and interface boundaries clear?
- Are important decisions being made explicitly?

### Layer C — Execution
Review:
- roadmap
- plan
- active TDE work
- blockers and decisions needed

Questions:
- Does active work clearly advance strategy?
- Is the product moving, blocked, or drifting?
- What should change now?

### Layer D — Health and risk
Review:
- metrics
- risks
- evidence of progress

Questions:
- What shows real progress?
- What is degrading?
- Which risk now matters most?

## Default review output
Each review should produce a compact output with:
- product reviewed
- review period/date
- overall health: green / yellow / red
- current maturity level
- top 1-3 goals
- top blockers or decision needs
- strongest evidence of progress
- main risk
- highest-leverage next action
- actions to create/update in TDE
- product-model updates required, if any

## Operating rules

### Rule 1: review from the product model, not from memory
Chat memory may help, but the review should be anchored in canonical artifacts.

### Rule 2: missing clarity should trigger artifact or TDE updates
Do not leave major gaps as vague observations.
If something is unclear, update the model or execution layer.

### Rule 3: separate product-model problems from execution problems
Examples:
- unclear purpose = product-model problem
- blocked task with clear purpose = execution problem
- hidden dependency = interface/governance problem

### Rule 4: reviews should end in decisions or actions
A review that only summarizes is incomplete.

### Rule 5: maturity should shape expectations
- Placeholder: review identity and definition needs
- Thin: review clarity and next strengthening step
- Standard: review operational coherence and active steering
- Deep: review control quality, evidence links, and system compounding

## Minimum review questions by maturity

### Placeholder products
- Is this still a valid product slot?
- What definition work is needed next?

### Thin products
- Is the product identity clear enough?
- Is the current plan coherent?
- What artifact would add the most leverage next?

### Standard products
- Is strategy aligned with current work?
- Are risks and interfaces explicit enough?
- Is the product model current enough to steer confidently?

### Deep products
- Is the model actively reducing ambiguity and improving decisions?
- Are optional artifacts still earning their keep?
- Where can stronger instrumentation or automation improve control?

## Relationship to TDE weekly review
The existing TDE weekly review template remains the execution review layer.
This Product Review Protocol sits one level above it:
- TDE weekly review checks execution cleanliness
- Product review checks whole-product coherence using the product model plus TDE state

This protocol is a shared coordination mechanism, not a replacement for product-owned internal operating processes.

## Recommended first use
Use this protocol first for:
- Task Management
- Security
- Delivery

These are currently the strongest Standard-level products and best candidates for proving the review pattern.
