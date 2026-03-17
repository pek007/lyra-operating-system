# Capability Model Standard v1

Status: Draft active standard
Owner: Lyra OS
Date: 2026-03-17

## Purpose
Define the missing capabilities-as-code layer in Lyra OS.

This standard exists to make product capabilities explicit, governable, discoverable, testable, and distributable without collapsing them into either vague strategy language or premature service/plugin architecture.

It answers:
- what a capability is
- how a capability relates to a product
- how a capability is discovered and consumed
- how a capability connects to delivery modes, governance, evidence, and lifecycle management

## Why this exists
Lyra OS already has meaningful layers in code:
- Product-as-Code
- process discovery and workspace operating packages
- delivery-mode decisions
- governance/control artifacts
- evidence and readiness artifacts
- improvement/error loops

What has been missing is the explicit layer between product purpose and downstream delivery:
**the capability model**.

Without that layer, the system can describe products and implement fragments, but still struggle to answer:
- what it can actually provide now
- how consumers can use it
- what is real vs aspirational
- what should be improved, packaged, approved, or retired

## Core definition
A **capability** is a managed unit of useful system power that a product can provide to one or more consumers.

A capability should be concrete enough to answer:
- what it does
- who owns it
- who can use it
- how it is delivered
- what controls apply
- what evidence proves it works

A capability is **not** the same thing as:
- a product (broader)
- a process (one possible delivery/support mechanism)
- a service (one possible delivery mode)
- a tool/script (one implementation element)
- a document (one expression artifact)

## Relationship to Product-as-Code
Products remain the canonical unit of strategic ownership.

Products define:
- purpose
- strategic role
- boundaries
- product-local recurring processes
- interfaces
- delivery/distribution choices

Capabilities define:
- what useful power the product actually provides
- the unit that moves through readiness, delivery, support, and retirement

### Short rule
- **Product** = why and for whom
- **Capability** = what the product can actually provide
- **Delivery mode** = how the capability reaches a consumer
- **Workspace operating package** = what the consumer must have locally to use it correctly

## Relationship to discovery and workspace packages
This standard must connect directly to the discovery model.

### Process discovery answers:
- where the official process lives
- what artifact is authoritative in scope
- what front door to use first

### Capability model answers:
- what useful capability exists behind those routes
- what consumers can access it
- what delivery mode and controls apply

A capability record should therefore point to:
- product owner
- source-of-truth location
- discovery/front-door path where relevant
- consumer-side workspace implications

This prevents the capability layer from becoming a disconnected catalog.

## Relationship to delivery-mode decisions
A capability is not complete until its delivery shape is explicit.

Use `DELIVERY_MODES_DECISION_FRAMEWORK_V1.md` after clarifying:
1. product purpose
2. capability definition
3. consumer need/interface
4. operating assumptions
5. governance/risk posture

A capability may be distributed through one or more modes, such as:
- governance artifacts
- workspace artifacts
- ops-pack
- schema-pack
- skill
- plugin
- runtime tooling
- service / daemon
- cron loop
- assembly

## Relationship to lifecycle management
A capability is the unit that moves through lifecycle states.

This standard defines the object.
`CAPABILITY_LIFECYCLE_STANDARD_V1.md` defines how it is proposed, built, validated, distributed, supported, improved, and retired.

## Required capability fields
Every formal capability record should include at minimum:

- **Capability ID**
- **Capability name**
- **Owning product**
- **Purpose**
- **Scope / boundary**
- **Primary consumers**
- **Delivery mode(s)**
- **Entrypoint / interface**
- **Source-of-truth / canonical artifacts**
- **Dependencies**
- **Constraints / guardrails**
- **Readiness**
- **Lifecycle state**
- **Evidence / verification references**
- **Known gaps / risks**
- **Retirement or upgrade triggers**

## Recommended capability fields
Where useful, also include:
- non-goals
- support owner
- operational cadence / monitoring path
- security/compliance approval path
- compatibility/version expectations
- current consumers actually using it vs merely eligible consumers

## Capability ID rule
Capability IDs should be stable and product-scoped.

Recommended format:
- `<PRODUCT-ID>.C<n>`

Examples:
- `A-007.C1`
- `A-008.C3`
- `CP-001.C2`

Sub-capabilities may be added later if needed, but v1 should stay simple.

## Capability readiness states
Use one of these:

- **draft**
  - concept and/or artifacts exist, but practical use is not yet proven
- **usable**
  - can be used now in bounded form by at least one consumer
- **proven**
  - exercised with evidence and dependable enough for normal internal use
- **scaled**
  - reusable across multiple consumers with explicit interface and control discipline
- **retiring**
  - being phased out in favor of a replacement or removal path
- **retired**
  - no longer active as a current capability

## Capability lifecycle states
Lifecycle state and readiness are related but not identical.

Recommended lifecycle states:
- proposed
- approved
- building
- validating
- active
- improving
- constrained
- retiring
- retired

Example:
- a capability may be `active` but only `usable`
- a capability may be `improving` and already `proven`

## Capability boundaries
A valid capability record must make boundary assumptions explicit.

Questions to answer:
- where does this capability stop?
- what does it depend on but not own?
- what consumer assumptions are required?
- what boundary/security/compliance conditions apply?

A capability should not silently imply broader authority than its owning product actually has.

## Canonical storage pattern
### Cross-product inventory
Use a shared inventory to make the portfolio visible.

Suggested artifact:
- `governance/CAPABILITY_DISTRIBUTION_INVENTORY_V1.md`

### Product-local records
The canonical home for durable capability records should be product-local.

Suggested options:
- `products/<slug>/06-architecture/CAPABILITIES.md`
- `products/<slug>/CAPABILITIES.yaml`
- another explicit product-local capability artifact

Use whichever format best fits the product, but keep it stable and explicit.

## Relationship to evidence and readiness
A capability should not be considered fully formed without a verification path.

Capability records should link to:
- acceptance criteria
- test/evidence artifacts
- readiness scorecards/checks where relevant
- real consumer validation when the capability is downstream-facing

### Short rule
A capability without evidence may be strategic intent, but not yet operationally reliable capability.

## Relationship to governance, security, and compliance
Capabilities that affect trust, side effects, external interactions, or boundary behavior must specify:
- approval path
- change-control expectations
- security/compliance review path where relevant
- rollback/disable path

This prevents capability records from becoming purely descriptive while operational risk lives elsewhere.

## Relationship to improvement and retirement
Capability records must support:
- improvement from incidents, friction, reviews, and evidence
- retirement when a capability becomes obsolete, unsafe, superseded, or too costly

Retirement should be treated as a first-class lifecycle path, not an afterthought.

## Anti-patterns
Avoid:
- treating a tool/script as if it were the whole capability
- treating a product purpose statement as if it already defined a capability
- creating capabilities with no consumer or no evidence path
- inventing a capability catalog detached from discovery, governance, and delivery mode
- forcing every capability into service/plugin framing prematurely
- letting capabilities remain implicit in thread memory or tribal knowledge

## Minimal capability record template
```md
## <CAPABILITY-ID> — <Capability name>
- Owning product:
- Purpose:
- Scope / boundary:
- Primary consumers:
- Delivery mode(s):
- Entrypoint / interface:
- Canonical artifacts:
- Dependencies:
- Constraints / guardrails:
- Readiness:
- Lifecycle state:
- Evidence:
- Known gaps / risks:
- Upgrade / retirement trigger:
```

## Practical operating rule
Before claiming that a product “has” a capability, be able to answer:
1. what exactly does it do?
2. who can use it now?
3. how does it reach that consumer?
4. what proves it works?
5. what controls and boundaries apply?
6. what would improve or retire it?

If those questions cannot be answered, the capability is not yet modeled robustly.

## Version
- v1.0
- Date: 2026-03-17
- Owner: Lyra OS
