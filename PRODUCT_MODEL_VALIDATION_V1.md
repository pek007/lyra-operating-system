# Product Model Validation v1

Status: Draft active standard
Owner: Peter / Lyra
Date: 2026-03-11

## Purpose
Define lightweight validation rules for Product-as-Code so PX Strategy can check whether a product model is structurally present, internally coherent, and mature enough for its current role.

This validation is intentionally lightweight.
It is meant to catch obvious gaps and drift, not to create a brittle bureaucracy.

## Validation layers
Validation should happen at three levels:
1. structure
2. coherence
3. maturity fit

## 1. Structure validation

### Required checks for any canonical product model
A valid canonical product model should have:
- `PRODUCT.md`
- `MODEL.yaml`

And `MODEL.yaml` should include at minimum:
- `id`
- `slug`
- `name`
- `owner`
- `status`
- `lifecycle`
- `domain`
- `purpose`
- `artifacts`
- `review`

### Required checks for Standard-level products
A product claiming Standard-level maturity should also have:
- `01-identity/VISION.md`
- `01-identity/CUSTOMER.md`
- `02-strategy/STRATEGY.md`
- `02-strategy/DISTRIBUTION_MODEL.md` or justified omission
- `03-operating-model/OPERATING_MODEL.md`
- `03-operating-model/GOVERNANCE.md`
- `04-execution/ROADMAP.md`
- `04-execution/PLAN.md`
- `04-execution/RISKS.md`
- `05-performance/METRICS.md`
- `06-architecture/INTERFACES.md`
- `07-decisions/DECISIONS.md`

## 2. Coherence validation

### Metadata-to-artifact coherence
Check that:
- every artifact listed in `MODEL.yaml` exists
- listed artifact paths match the actual canonical files
- `PRODUCT.md` reflects the real artifact set, not an outdated list

### Identity coherence
Check that these agree across `PRODUCT.md` and `MODEL.yaml`:
- product ID
- product name
- owner
- status
- overall purpose

### Strategic coherence
Check that:
- `STRATEGY.md` does not contradict `PRODUCT.md` purpose
- `PLAN.md` plausibly advances the strategy
- `RISKS.md` reflects real strategic or operational concerns rather than generic filler

### Operating coherence
Check that:
- `OPERATING_MODEL.md` and `GOVERNANCE.md` describe compatible ways of working
- escalation logic is not contradicted elsewhere
- interfaces described in `INTERFACES.md` fit the stated product boundary and dependency model

### Decision coherence
Check that:
- `DECISIONS.md` includes at least one product-shaping decision
- the decision log aligns with the current operating posture

## 3. Maturity-fit validation
Validation should ask not only "is it complete?" but also "is it at the right level?"

### Level 1 fit
Passes if:
- model exists
- placeholder status is explicit
- undefined areas are not disguised as certainty

### Level 2 fit
Passes if:
- product identity is clear
- there is enough structure for orientation and light steering
- plan and decisions exist
- missing artifacts do not prevent normal lightweight use

### Level 3 fit
Passes if:
- the standard artifact set exists or justified exceptions are documented
- artifacts are populated with real product-specific content
- the model is usable for planning, review, and cross-product coordination

### Level 4 fit
Passes if:
- Level 3 fit is strong
- the model is actively used as an operational control system
- optional depth exists because it adds real value, not because completeness was gamed

## Validation outcomes
Use simple outcomes:
- **Pass** — good enough for stated maturity
- **Pass with gaps** — usable, but with visible issues to clean up
- **Fail** — not adequate for stated maturity

## Typical gap categories
- missing canonical artifact
- stale front door
- `MODEL.yaml` drift
- placeholder content in an active product
- unclear owner or boundary
- strategy-plan disconnect
- weak interface clarity
- risks too generic or absent
- decision memory too thin

## Lightweight operating rule
Validation should normally be done:
- when creating a new product model
- when claiming a higher maturity level
- during periodic portfolio reviews
- when a product feels hard to understand or steer

## Initial manual validation heuristic
A human or agent should be able to answer these quickly from the product model:
- What is this product for?
- Who does it serve?
- What is the strategy?
- What is happening now?
- What are the main risks?
- How is it governed?
- What interfaces matter?
- What decisions already shape it?

If these cannot be answered quickly, the product model is probably below the maturity it claims.
