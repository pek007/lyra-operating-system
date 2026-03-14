# Delivery Modes Decision Framework v1

Status: Draft active framework
Owner: Peter / Lyra
Date: 2026-03-11

## Purpose
Provide a consistent way to choose delivery modes for PX Strategy product capabilities.

This framework exists because a product capability can often be delivered in multiple ways:
- skill
- plugin
- policy-pack
- schema-pack
- ops-pack
- workspace artifact
- assembly
- service / daemon
- cron-driven artifact/evidence loop

The goal is to choose the delivery mode that best fits:
- the product
- the consumer
- the interface shape
- the governance needs
- the runtime boundary
- the maturity of the capability

## Core principle
A delivery mode is not the product.
It is a vehicle for distributing and activating a product capability.

A delivery choice is also not complete until the consumer-side operating shape is clear.
If a capability is delivered into a downstream workspace, the decision should account for what that workspace must receive or instantiate as part of its local operating package.

Always choose delivery mode **after** clarifying:
1. product purpose
2. consumer/interface
3. operating assumptions
4. governance/risk posture

## Decision stack
Use this order:
1. **Product** — what capability exists and why?
2. **Interface** — what does the consumer actually need?
3. **Distribution model** — how should the capability reach the consumer?
4. **Delivery mode** — what vehicle best implements that distribution?
5. **Workspace operating package** — what must exist in the consumer's local operating environment for this delivery to be usable and governable?
6. **Activation** — how is it turned on in runtime?

## Delivery mode options

### 1. Skill
Best when:
- the capability is mainly operator/agent guidance
- human/agent behavior is the main delivery path
- the interface is instructional or workflow-oriented
- fast iteration matters more than hard runtime enforcement

Strengths:
- easy to author and revise
- good for reusable operating guidance
- low activation overhead

Weaknesses:
- weaker enforcement
- can drift if not tied to product/interface artifacts
- poor fit when hard runtime behavior is required

Use for:
- operator guidance
- runbook-style capability packaging
- product operating support

---

### 2. Plugin
Best when:
- the capability must integrate directly into runtime behavior
- activation should happen through a clear extension point
- the interface is more behavioral than documentary
- the product benefits from being attachable/enabled rather than manually followed

Strengths:
- strong runtime integration
- clearer activation path
- better for repeatable behavior than pure docs/skills

Weaknesses:
- higher implementation and maintenance cost
- stronger coupling risk
- more governance required for boundary and safety

Use for:
- runtime extensions
- durable activation logic
- behavior that should not depend on manual adherence alone

---

### 3. Policy-pack
Best when:
- the capability is primarily a rule, constraint, or governance surface
- multiple products need the same policy logic
- consistency matters more than custom product-local expression

Strengths:
- good for shared governance
- clear for versioning and reuse
- supports cross-product consistency

Weaknesses:
- can become abstract if not tied to real operating use
- enforcement may still require companion tooling or review

Use for:
- guardrails
- security/control policy
- change-control rules

---

### 4. Schema-pack
Best when:
- the capability depends on structured data contracts
- machine-readability and validation matter
- multiple products/consumers need a shared contract surface

Strengths:
- strong consistency and validation
- good for automation and portability
- reduces ambiguity in interfaces

Weaknesses:
- can be overkill early
- requires schema discipline and migration care

Use for:
- contracts
- typed registries
- machine-checkable interfaces

---

### 5. Ops-pack
Best when:
- the capability is delivered mainly through operating procedures, checklists, evidence flows, or review artifacts
- the main value is repeatable operation rather than code behavior alone

Strengths:
- practical for internal operating capabilities
- easy to inspect and adapt
- pairs well with Product-as-Code

Weaknesses:
- relies on disciplined usage
- weaker hard enforcement than runtime-native mechanisms

Use for:
- process assets
- review cadences
- readiness and evidence patterns

---

### 6. Workspace artifact
Best when:
- the capability is still local, product-specific, or early-stage
- flexibility matters more than packaging
- the product has not yet stabilized its interface enough for broader reuse

Strengths:
- fastest to evolve
- low overhead
- good for proving concepts in place

Weaknesses:
- less portable
- more prone to hidden coupling
- easy to confuse local implementation with product interface

Use for:
- early product development
- local-first proof cases
- transient or highly contextual assets

---

### 7. Assembly
Best when:
- the capability needs to bundle multiple artifact types together
- the consumer needs a coherent promoted unit rather than loose files
- deployment/versioning should happen as a product bundle

Strengths:
- better transfer unit
- good for multi-artifact promotion and verification
- clearer release boundary

Weaknesses:
- more packaging discipline required
- overhead not justified for very small/local capabilities

Use for:
- product bundles
- promoted multi-artifact releases
- controlled deployment packages

---

### 8. Service / daemon
Best when:
- the capability deserves its own runtime boundary
- uptime, isolation, or externalized interaction matters
- multiple consumers need stable interaction semantics
- product complexity justifies operational overhead

Strengths:
- clear runtime boundary
- stronger isolation potential
- better for broader reuse or externalization

Weaknesses:
- highest operational overhead
- requires stronger observability, deployment, and lifecycle management
- easy to do too early

Use for:
- stable reusable services
- control surfaces
- broader multi-consumer capability boundaries

---

### 9. Cron-driven artifact/evidence loop
Best when:
- the capability is periodic by nature
- value comes from recurring checks, summaries, audits, or evidence generation
- human initiation is unnecessary or too inconsistent

Strengths:
- reliable periodic execution
- good for hygiene, monitoring, and evidence freshness
- low interaction burden once shaped correctly

Weaknesses:
- can generate noise if poorly bounded
- weaker fit for interactive or highly contextual capability delivery

Use for:
- audits
- health checks
- recurring evidence loops
- periodic summaries

## Selection criteria
When comparing delivery modes, score or judge these dimensions:

### A. Consumer interaction shape
- Does the consumer need guidance, artifacts, behavior, or a service?

### B. Enforcement need
- Is soft guidance enough, or must the capability be activated/enforced in runtime?

### C. Boundary strength
- Does this capability need a stronger runtime/deployment boundary?

### D. Portability/reuse
- Is this local-first, cross-product, or future externalizable?

### E. Governance/risk
- What happens if the capability is misused, stale, or activated incorrectly?

### F. Maturity
- Is the capability early/provisional, or stable enough to justify heavier packaging?

### G. Operational overhead
- Is the added operational cost worth the clarity or control gained?

## Default mode heuristics

### Start lighter when:
- interface is still forming
- consumer needs are not yet stable
- capability is still being proven
- governance can be satisfied without hard runtime packaging

Preferred early modes:
- workspace artifact
- ops-pack
- skill
- policy-pack

### Move heavier when:
- the interface is stable
- multiple consumers depend on the capability
- hidden coupling is becoming a problem
- runtime enforcement/isolation is needed
- packaging/versioning matters materially

Preferred later modes:
- schema-pack
- assembly
- plugin
- service / daemon

## Anti-patterns
Avoid:
- choosing a mode because it is familiar rather than fit-for-purpose
- treating the first implementation form as the permanent product architecture
- forcing service boundaries before interface stability exists
- hiding governance-heavy behavior inside lightweight delivery modes without visibility
- using local workspace artifacts as if they were a published interface

## Current portfolio read

### Task Management (`A-007`)
Current best-fit modes:
- workspace artifacts
- ops-pack
- schema-pack / policy-pack as supporting forms
- future capability-pack or service only after interface maturity justifies it

Why:
The consumer interface is now an operating contract, not yet a service boundary.

### Security (`A-004`)
Current best-fit modes:
- policy-pack
- ops-pack
- recurring evidence/audit loops
- future schema-pack or tooling support where machine-checkability adds value

Why:
Security is primarily distributed through controls, posture outputs, and review practices.

### Delivery (`A-006`)
Current best-fit modes:
- ops-pack
- workspace/repo process assets
- future tooling or service surfaces only if the management/control need becomes strong enough

Why:
Delivery value currently lives in process, readiness, and verification discipline more than an isolated runtime service.

### Control Panel (`CP-001`)
Current best-fit modes:
- service / daemon
- skill-pack and policy-pack as supporting modes

Why:
Control Panel is explicitly a control-surface candidate and already has a separate-boundary logic.

### Improvement (`A-005`)
Current best-fit modes:
- ops-pack
- skill-pack
- assembly for bundled improvement delivery into consuming environments

Why:
Improvement is portfolio-wide process leverage rather than a standalone service today.

## Decision output format
When choosing a delivery mode, capture:
- product
- capability being delivered
- target consumer(s)
- chosen delivery mode(s)
- workspace operating package implications for the consumer
- rejected alternatives
- why this mode fits now
- what would trigger a future mode change

## Short rule
**Choose the lightest delivery mode that preserves interface clarity, governance fitness, and consumer usability.**
