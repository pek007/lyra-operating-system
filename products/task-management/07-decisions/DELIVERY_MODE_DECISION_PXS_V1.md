# Delivery Mode Decision — Task Management capability delivery into `pxs`

Status: Active
Date: 2026-03-11
Product: Task Management (`A-007`)
Capability: TDE / Task Management consumption by `pxs`
Decision owner: Lyra

## Context
Task Management is now the strongest Standard-level product in the portfolio. The product has:
- a formal `pxs` consumption interface (`06-architecture/PXS_CONSUMPTION_INTERFACE.md`)
- a readiness scorecard (`05-performance/READINESS_SCORECARD.md`)
- a distribution model that currently emphasizes explicit interfaces, operating patterns, readiness gates, and evidence-backed adoption

The decision question is what delivery mode should currently be used for Task Management capability delivery into `pxs`.

## Product and interface context
### Product purpose
Provide reliable task and decision management capability that makes work visible, traceable, governable, and easier to execute.

### Consumer need
`pxs` needs a practical task/decision operating capability with low-friction adoption, explicit state, and minimal dependence on chat-memory reconstruction.

### Current interface shape
The current interface is an **artifact-and-operating-model based contract**, not a dedicated service boundary.

### Governance/risk posture
Moderate governance intensity. Hidden coupling and premature packaging are both risks.

### Current maturity of the capability
The product model is strong, but readiness and downstream consumption are still **Yellow-Green / Yellow** rather than fully proven.

## Candidate delivery modes considered
- workspace artifact
- ops-pack
- schema-pack (supporting)
- plugin
- service / daemon
- assembly

## Assessment
### Consumer interaction shape
Mainly:
- operating guidance
- explicit artifacts
- reviewable task/decision discipline
- not yet a runtime API/service interaction need

### Enforcement need
- soft guidance alone is not enough
- but full runtime-native packaging is also not yet justified
- the best fit currently is structured artifact delivery plus explicit operating contract

### Boundary strength
- stronger than loose local notes
- not yet strong enough or stable enough to justify a service boundary
- current boundary should remain workspace/product scoped with explicit interface documentation

### Portability/reuse
- needs to become reusable across consumers
- but the interface is still stabilizing
- portability should improve through clearer artifacts and supporting contracts before heavier runtime packaging

### Governance/risk
Main risks if the wrong mode is chosen now:
- too light: `pxs` adoption remains vague and depends on tribal knowledge
- too heavy: product gets prematurely locked into a service/plugin architecture before the interface is stable

### Operational overhead
Current acceptable overhead is moderate. A service boundary would create more overhead than the product can currently justify.

## Decision
### Chosen mode(s)
**Primary current modes:**
- workspace artifacts
- ops-pack style operating assets

**Supporting mode:**
- schema-pack style contracts where machine-checkable task/decision interfaces become useful

### Rejected alternatives for now
#### Plugin
Rejected for now because:
- the interface is not yet mature enough
- runtime coupling would likely grow faster than clarity
- current consumer need is still mostly operating-contract based

#### Service / daemon
Rejected for now because:
- the capability does not yet require a stable multi-consumer runtime boundary
- operational overhead would outrun current readiness
- the product still needs more evidence of real downstream use first

#### Assembly
Deferred rather than rejected:
- may become useful once a clearer multi-artifact promoted unit is needed for downstream consumption
- not yet necessary for the first real `pxs` delivery shape

## Why this fits now
This is the lightest mode that still preserves:
- interface clarity
- reviewability
- consumer usability
- governance fitness

It also aligns with the existing explicit decision that the first formal `pxs` interface should be an operating-contract artifact rather than a premature packaged/runtime boundary.

## Workspace operating package implications
Current delivery into `pxs` requires a consumer-side local operating package, not just provider-side product artifacts.

At minimum, the consumer workspace should expose:
- workspace profile / authority boundary
- source-of-truth map
- process discovery front door
- task system of record
- decision/escalation path
- error/incident handling path

This keeps Task Management consumption from collapsing back into hidden thread-memory dependence.

## Activation path
Task Management capability is currently activated in `pxs` through:
- explicit operating rules
- product/task artifacts
- TDE-related contracts
- readiness and review discipline
- visible owner/review loop expectations
- a minimum local workspace operating package in the consumer scope

## Evidence of success expected
This decision is working if:
- `pxs` can adopt Task Management with minimal bespoke explanation
- another operator/agent can inspect state and understand what matters
- recurring friction becomes explicit improvement work
- the product no longer depends on transcript memory alone for operational continuity

## Trigger for future mode change
Revisit this decision when one or more of these become true:
1. multiple consumers need a more stable packaged interface
2. the interface becomes stable enough for schema-backed or packaged promotion
3. runtime enforcement/integration becomes materially more important than operating-contract flexibility
4. operational overhead of staying artifact-based becomes greater than the cost of packaging/service boundary creation

## Conclusion
For now, Task Management capability delivery into `pxs` should remain primarily an **artifact-and-ops-pack style delivery model**, with selective schema-backed strengthening where useful.

It should **not** yet become a plugin or service.
