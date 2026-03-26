# Lyra OS Portfolio and Capability Model v1

Status: Draft  
Owner: Lyra OS  
Version: v0.1

## Purpose

This artifact defines the portfolio and capability ontology of Lyra OS.

Its purpose is to make explicit:
- what kinds of operating objects exist in Lyra OS
- what role each kind of object plays
- how those objects relate to one another
- when something should become a product, a shared capability, a workspace package element, a process artifact, or a local adaptation
- how the overall portfolio is meant to fit together

This artifact is the portfolio and capability layer of the Lyra OS Model.

## Scope

This model governs:
- product ontology
- shared capability ontology
- workspace enablement ontology
- downstream operating-package logic at the conceptual level
- portfolio structure and boundaries
- criteria for classifying new capabilities

It does not replace:
- product-local models
- workspace-local operating packages
- detailed delivery-mode decisions
- detailed process or implementation artifacts

## Core principle

**Lyra OS should have an explicit ontology for how capabilities are represented, owned, delivered, and consumed.**

Not every recurring need should become a product.  
Not every local adaptation should become a shared capability.  
Not every useful artifact should become portfolio-level structure.

This model exists to make those distinctions clearer.

## Top-level operating object types

Lyra OS currently or potentially contains the following primary object types.

## 1. Model
The Model is the canonical design authority for the system.

It defines:
- strategic design
- governance and authority design
- portfolio and capability design
- delivery and consumption design
- runtime and operating design
- learning and evolution design

The Model governs the system, but does not replace the operating objects below.

## 2. Product
A Product is the canonical unit of capability definition and capability operation.

A Product should exist when a capability needs:
- explicit ownership
- explicit strategy and operating model
- explicit interfaces
- explicit execution and review surfaces
- repeated evolution over time
- reusable delivery into one or more downstream scopes

Products are producer-side capability units.

## 3. Shared capability
A Shared Capability is a reusable capability that supports multiple products, loops, or downstream environments, but may not yet justify becoming a full standalone product.

A shared capability may be:
- embedded in a product
- jointly consumed across multiple products
- delivered through a pack, assembly, schema, policy, tool, or operating pattern

A shared capability should be promoted into fuller product form if:
- ownership complexity increases
- interfaces become important
- adoption expands
- dedicated strategy/governance is needed

## 4. Workspace operating package
A Workspace Operating Package is the canonical unit of downstream local operation.

It exists to make a workspace operationally usable as a consumer of Lyra OS capabilities.

A workspace operating package should define:
- purpose
- authority boundary
- source-of-truth map
- process discovery front door
- local operating routes
- local adaptations needed for consumption

Workspaces are consumer-side operating environments.

## 5. Workspace enablement capability
A Workspace Enablement Capability is a capability whose purpose is to help a workspace consume Lyra OS outputs correctly and reliably.

These capabilities may include:
- source-of-truth structure
- process discovery
- local runbooks
- local schema packs
- local ops packs
- consumer interfaces
- adoption helpers

Some workspace enablement is:
- default core
- capability-specific
- workspace-local

This distinction should remain explicit.

## 6. Process artifact
A Process Artifact defines how recurring operational work should be performed in a particular scope.

Process artifacts are not automatically products.

A process artifact should exist when:
- recurring work needs explicit routing or control
- consistency matters
- governance or risk matters
- handoff or inspectability matters

A process artifact may be:
- root/shared
- product-owned
- workspace-local

The most specific approved owning artifact should take precedence.

## 7. Runtime operating mechanism
A Runtime Operating Mechanism is a live execution structure that helps the system run.

Examples include:
- review loops
- nightly cycles
- cron-driven operating passes
- execution loops
- synthesis steps
- handoff loops

These are operating mechanisms, not necessarily products.

They should be linked back to canonical artifacts rather than operating as free-floating behavior.

## 8. Job / role / authority object
Jobs and roles are operating authority structures.

They define:
- accountable ownership
- authority boundaries
- decision rights
- obligations
- escalation paths

These are not products and not workspace packages.  
They are authority-bearing operating objects.

## 9. Knowledge / evidence / improvement object
These are objects that support system learning.

Examples include:
- knowledge reports
- evidence artifacts
- error reports
- corrective-action artifacts
- improvement records
- review outputs

These are not merely documentation.  
They are part of how Lyra OS learns and evolves.

## 10. Local adaptation
A Local Adaptation is a workspace-local or context-local solution that exists to make something work in practice without yet becoming shared system structure.

Local adaptations are legitimate, but should remain visible.

A local adaptation should not silently become a portfolio standard without explicit promotion.

---

## Portfolio structure principle

The Lyra OS portfolio should remain structured around **clear capability purpose**, not artifact proliferation.

That means:
- products should exist where capability ownership and evolution justify them
- shared capabilities should remain shared unless full productization is warranted
- workspace packages should remain local operating environments, not hidden copies of upstream product logic
- runtime mechanisms should remain connected to canonical artifacts
- local adaptations should be visible and promotable, not hidden system drift

## Product test

Something should likely become a Product when most of the following are true:

- it has a distinct enduring purpose
- it serves multiple consumers or a meaningful recurring need
- it requires explicit ownership
- it benefits from explicit interfaces
- it needs strategy and review over time
- it is likely to evolve independently enough to justify its own operating model

If these are not true, the capability may belong elsewhere.

## Shared capability test

Something should likely remain a Shared Capability when:

- it supports multiple products or workspaces
- it is clearly reusable
- it does not yet require full standalone product governance
- it is better understood as an enabling component than a portfolio unit

## Workspace enablement test

Something should likely be treated as Workspace Enablement when:

- its main purpose is to make downstream consumption operationally usable
- it must exist locally in a workspace to reduce ambiguity or fragility
- it is driven by consumer-side operating needs rather than producer-side capability identity

## Process test

Something should likely remain primarily a Process Artifact when:

- its main purpose is to govern recurring work
- it does not define a capability portfolio unit
- it is about routing, control, standardization, or execution discipline
- it does not require product-style strategy and delivery logic

## Local adaptation test

Something should likely remain a Local Adaptation when:

- it solves a local or temporary need
- it is not yet proven reusable
- portfolio-wide promotion would be premature
- the operational burden of standardizing it exceeds current value

But local adaptations should be reviewed for promotion when they recur or spread.

---

## Relationship between products and workspaces

A core rule of Lyra OS is:

- **Products are producer-side capability units**
- **Workspaces are consumer-side operating units**

Products define:
- capability identity
- capability boundaries
- interfaces
- delivery expectations
- capability evolution

Workspaces define:
- local operating context
- local authority
- local source-of-truth structure
- local process-discovery front door
- local adaptations needed for real use

This distinction should remain explicit.

## Relationship between products and runtime mechanisms

Runtime mechanisms should not become orphan operating behavior.

Where possible, runtime mechanisms should:
- be linked to an owning product or system-layer model
- operate against canonical artifacts
- update inspectable operating surfaces
- preserve traceability between decisions, work, and outcomes

## Relationship between portfolio logic and downstream delivery

A capability’s classification should affect how it is delivered.

Examples:
- a Product may require full product-local model artifacts and downstream interface rules
- a Workspace Enablement Capability may require local front-door artifacts and source-of-truth mapping
- a Process Artifact may require routing guidance but not full product packaging
- a Local Adaptation may remain visible but intentionally non-canonical

This is why ontology matters: it shapes delivery design.

## Promotion and evolution rule

Objects may evolve across types over time.

Examples:
- a local adaptation may become a shared capability
- a shared capability may become a product
- a product-local recurring pattern may become a portfolio standard
- a runtime loop may become a formally governed operating mechanism

Such promotions should happen deliberately, based on:
- recurring need
- evidence of reuse
- ownership clarity
- strategic importance
- governance need

Not by silent drift.

## Current portfolio posture

At v0.1, Lyra OS should bias toward:

- clear product boundaries
- explicit shared-capability logic
- strong workspace enablement discipline
- visible local adaptations
- deliberate promotion rules

It should avoid:
- turning every useful thing into a product
- copying upstream capability logic into downstream workspaces without need
- treating runtime loops as self-justifying without clear linkage to canonical design
- allowing local workarounds to quietly redefine the system

## Strategic implication

A strong portfolio and capability model improves:

- capability design quality
- delivery clarity
- workspace operability
- architecture consistency
- governance discipline
- system evolution

Without it, Lyra OS risks becoming a set of locally sensible but globally inconsistent structures.

## Short doctrine statement

**Lyra OS should use an explicit ontology for products, shared capabilities, workspace packages, enablement capabilities, process artifacts, runtime mechanisms, authority objects, and local adaptations.  
These objects should be owned, delivered, consumed, and promoted deliberately rather than emerging through hidden drift.**
