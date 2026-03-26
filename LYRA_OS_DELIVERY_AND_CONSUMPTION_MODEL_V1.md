# Lyra OS Delivery and Consumption Model v1

Status: Draft  
Owner: Lyra OS  
Version: v0.1

## Purpose

This artifact defines how Lyra OS capabilities are delivered and consumed.

Its purpose is to make explicit:
- how capabilities move from producer-side definition into downstream operational use
- how delivery modes should be understood
- what downstream consumption requires in practice
- what must remain upstream versus what must exist locally
- how operability should be judged from the consumer side

This artifact is the delivery and consumption layer of the Lyra OS Model.

## Scope

This model governs:
- delivery logic
- downstream consumption logic
- delivery mode principles
- workspace enablement logic
- consumer/provider relationship design
- local instantiation boundaries
- downstream operability expectations

It does not replace:
- product-local interface artifacts
- detailed delivery-mode decisions
- workspace-local operating packages
- local implementation details
- detailed runbooks or onboarding instructions

## Core principle

**A capability is not truly delivered when it is merely defined upstream.  
It is delivered when it can be consumed operationally and coherently in the downstream environment.**

This means Lyra OS must think about delivery and consumption together, not as separate concerns.

## Producer-side and consumer-side distinction

Lyra OS should preserve a clear distinction between:

### Producer-side capability definition
This includes:
- product identity
- product boundaries
- interfaces
- delivery expectations
- capability evolution
- governance and strategy of the capability itself

### Consumer-side operational consumption
This includes:
- local authority
- local source-of-truth structure
- local process discovery
- local operating routes
- local adaptations
- local execution and review usability

The producer-side capability is necessary, but not sufficient.  
The consumer-side operating package is what makes it usable.

## Delivery principle

Delivery should be understood as the controlled movement of capability into use.

A delivered capability should be:
- understandable
- inspectable
- governable
- consumable without hidden upstream assumptions
- sufficiently supported by local operating structures where required

A delivered capability that still depends mainly on thread memory or hidden operator knowledge is not fully delivered.

## Consumption principle

Consumption should be treated as an explicit design problem, not an afterthought.

A downstream environment should be able to answer:
- what capability is being consumed
- what is authoritative locally
- what remains authoritative upstream
- what interfaces govern the consumption
- what local operating artifacts are required
- how the capability is actually used in recurring work

If these are unclear, consumption is still immature.

## Delivery modes

Lyra OS may deliver capabilities through different modes.

Examples may include:
- product-local artifact delivery
- schema packs
- policy packs
- ops packs
- skills
- assemblies
- services
- runtime loops
- workspace operating package components
- hybrid delivery patterns

The delivery mode should be chosen based on:
- the nature of the capability
- the consumer’s operating needs
- governance posture
- adoption and maintenance implications
- the need for local versus shared authority

Delivery mode should not be treated as a stylistic preference.

## Delivery-mode rule

The right delivery mode is the one that best preserves:

- capability clarity
- operability
- governance fit
- maintenance viability
- inspectability
- downstream usability

A more elaborate delivery mode is not automatically better.  
A more minimal delivery mode is not automatically better.

The correct question is:
**what delivery mode makes this capability operationally usable with the least harmful ambiguity?**

## Workspace enablement principle

Many capabilities require explicit workspace enablement in order to become operational downstream.

Workspace enablement may include:
- workspace profile
- source-of-truth map
- process discovery index
- local runbooks
- local adopted standards
- local interface or routing artifacts
- capability-specific operating notes

A capability should not be treated as “fully consumed” if the workspace lacks the enablement needed to use it correctly.

## Upstream vs local boundary rule

A key delivery and consumption question is:

**what should remain upstream, and what must be instantiated locally?**

As a general rule:

### Keep upstream when:
- the logic is shared and canonical
- centralized ownership is important
- downstream duplication would create drift
- local variation is undesirable
- the capability is better consumed by reference than by local copy

### Instantiate locally when:
- the consumer needs local authority or local clarity
- the workspace must operate without hidden upstream context
- local process discovery is necessary
- local execution routes must be explicit
- the capability cannot be used safely or coherently without local operating artifacts

This boundary should be deliberate.

## Consumer/provider relationship model

Capability delivery should preserve a clear relationship between provider and consumer.

The provider should make explicit:
- what is being delivered
- what the downstream consumer can rely on
- what interfaces apply
- what assumptions are required
- what local enablement is needed

The consumer should make explicit:
- how the capability is adopted locally
- what local artifacts become authoritative
- what local routes and responsibilities apply
- what remains external/shared

This should reduce ambiguous adoption.

## Operability test

A capability should count as operationally usable downstream only if the consuming environment can:

- identify what was delivered
- identify how to use it
- identify what is authoritative locally
- discover the relevant official processes
- route recurring work without depending mainly on transcript memory
- understand when to escalate back upstream
- maintain continuity under ordinary context transfer

If those conditions are not met, the capability may be present but not truly operational.

## Local adaptation rule

Local adaptation is allowed and often necessary.

However:
- local adaptations should remain visible
- local adaptations should not silently redefine the delivered capability
- repeated local adaptations should be reviewed for possible promotion into shared capability or workspace enablement standards

Delivery should not assume zero local variation, but it should not ignore the cost of unmanaged local variation either.

## Adoption maturity rule

Downstream consumption should be understood in maturity levels.

A simple maturity progression might be:

### Level 0 — Present but not usable
The capability technically exists, but depends mostly on hidden context or manual interpretation.

### Level 1 — Minimally usable
The capability can be used, but local clarity and support are thin.

### Level 2 — Operable
The capability has enough local operating structure to be used reliably in recurring work.

### Level 3 — Reliable
The capability is well integrated into local operation, review, and continuity.

Not every consumed capability needs to reach the same maturity at once, but maturity should be visible.

## Delivery failure principle

Delivery should fail visibly when core consumption assumptions are not met.

It is better to say:
- capability not yet operational
- workspace enablement missing
- authority still ambiguous
- interface not ready
- delivery mode not yet sufficient

than to pretend delivery is complete while downstream use remains fragile.

## Relationship to products

Products remain the main producer-side capability units.

The delivery and consumption model governs:
- how products are delivered downstream
- how consumption should be understood
- what workspace enablement may be required
- how consumer/provider obligations should be interpreted

Products define the capability.  
This model defines how that capability becomes operational in use.

## Relationship to workspaces

Workspaces remain the main consumer-side operating units.

A workspace operating package is the local structure that helps a workspace consume capabilities coherently.

This model governs:
- why workspace packages matter
- what kinds of local enablement are needed
- how to distinguish shared upstream logic from local operating reality

## Relationship to runtime

Some delivered capabilities may include runtime operating mechanisms such as:
- review loops
- nightly loops
- cron jobs
- execution passes

These should still follow delivery and consumption logic.

A runtime loop is not truly delivered if:
- its purpose is unclear
- its local authority is unclear
- its artifact relationship is unclear
- its outputs cannot be consumed coherently

## Relationship to portfolio design

Delivery and consumption logic should reinforce the portfolio model.

That means:
- products should be delivered as products
- workspace enablement should be recognized as enablement, not hidden glue
- process artifacts should not be mistaken for products
- local adaptations should not be mistaken for canonical standards
- hybrid capability forms should be explicit when deliberately chosen

## Strategic intent of this model

The delivery and consumption model should make Lyra OS:

- easier to deliver coherently
- easier to adopt safely
- easier to operate downstream
- less dependent on hidden context
- more disciplined about local versus shared authority
- more scalable without becoming more confusing

## Short doctrine statement

**In Lyra OS, delivery is complete only when downstream consumption becomes operationally usable.  
Capabilities must be delivered with clear interfaces, clear authority boundaries, and sufficient local enablement for real operation.**
