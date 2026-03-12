# Request — TDE UI Pilot Delivery Support

Request ID: REQ-20260312-001
Date: 2026-03-12
From product: Task Management (`A-007`)
To product: Delivery (`A-006`)
Requested by: Lyra
Status: accepted
Urgency: high

## Purpose
Request Delivery participation in the One-Iteration TDE UI Pilot as the product responsible for shaping the pilot into a professional one-iteration delivery flow.

## Requested outcome
Provide a bounded Delivery response that defines:
1. the smallest viable delivery shape for this pilot,
2. the minimum acceptable production/release bar,
3. the minimum delivery artifact/evidence set needed for a professionally managed one-iteration execution,
4. the main delivery-side risks or blockers that should be decided early.

## Why this request exists now
Task Management can frame the pilot objective and TDE-side coordination needs, but the pilot is explicitly intended to test joint execution between Task Management and Delivery.

Without an explicit Delivery contribution, the pilot risks becoming only a Task Management planning exercise rather than a real proving ground for governed production delivery.

## Decision needed
Yes.

Primary decision requested from Delivery:
- What is the smallest viable one-iteration delivery contract for the TDE UI pilot that is strict enough to be professional, but light enough to remain feasible?

## Expected response form
One concise response in one of these forms:
- accepted
- rejected
- deferred
- clarification-needed

If accepted, include:
- named owner,
- proposed next action,
- references to any Delivery plan / decision / readiness artifacts where execution will continue.

## Suggested next step
Review:
- `ONE_ITERATION_TDE_UI_PILOT_V1.md`
- `PRODUCT_INBOX_COORDINATION_MODEL_V1.md`
- `products/delivery/04-execution/PLAN.md`
- `products/delivery/07-decisions/DECISIONS.md`

Then return a bounded Delivery response and, if accepted, reflect the work into Delivery’s canonical execution surfaces.

## Relevant refs
- `ONE_ITERATION_TDE_UI_PILOT_V1.md`
- `PRODUCT_INBOX_COORDINATION_MODEL_V1.md`
- `products/task-management/04-execution/PLAN.md`
- `products/delivery/04-execution/PLAN.md`
- `products/delivery/03-operating-model/OPERATING_MODEL.md`

## Response section
Response: accepted
Owner: Lyra (Delivery)
Rationale: The request is directly aligned with Delivery’s current mandate to improve dependable pathways from intent to shipped capability and to pilot a real TDE slice end to end as a Delivery Unit. A bounded response is feasible now and useful even before the full long-term coordination model exists.

### Delivery response
#### Smallest viable delivery shape
Treat the pilot as one bounded Delivery Unit that runs from approved objective -> scoped implementation slice -> verification evidence -> explicit release/readiness decision -> post-pilot review.

#### Minimum acceptable production/release bar
For this pilot, Delivery recommends that “production” means:
- deployed in a real runtime/environment,
- usable for one narrow real operator purpose,
- backed by an explicit readiness/release decision,
- reversible or low-blast-radius if the first slice proves weak.

#### Minimum delivery artifact/evidence set
Delivery recommends the following minimum set:
1. pilot scope/non-goals record,
2. one delivery execution packet / unit definition,
3. implementation evidence,
4. verification evidence,
5. release/readiness decision artifact,
6. post-pilot review note.

#### Main delivery-side early risks / blockers
- scope inflation before a smallest viable slice is fixed,
- weak definition of what counts as production,
- evidence expectations being left too vague,
- Delivery becoming a passive witness rather than an active gate-owning product.

### Proposed next action
Create a compact Delivery-side pilot contract artifact that defines:
- smallest viable delivery shape,
- minimum production bar,
- minimum evidence set,
- early gate questions.

### Canonical continuation refs
- `products/delivery/04-execution/PLAN.md`
- `products/delivery/07-decisions/DECISIONS.md`
- `ONE_ITERATION_TDE_UI_PILOT_V1.md`
