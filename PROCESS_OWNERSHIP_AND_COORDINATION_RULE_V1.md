# Process Ownership and Coordination Rule v1

Status: Draft active rule
Owner: Peter / Lyra
Date: 2026-03-11

## Purpose
Prevent process-model drift as Product-as-Code matures.

This rule exists to keep the architecture clean:
- products own their own recurring operating processes
- central/shared artifacts define only genuine cross-product coordination mechanisms
- no parallel "process layer" should emerge that duplicates product-owned operational logic

## Core rule
**A recurring process should be owned by a product unless it is genuinely a cross-product coordination mechanism.**

This means:
- product-internal processes belong inside the product model
- central artifacts should not duplicate or compete with product-owned process definitions
- shared artifacts may define only the minimum coordination logic needed across products

## Product-owned processes
A process is product-owned when it primarily answers:
- how this product runs
- how this product reviews itself
- how this product changes
- how this product handles readiness, delivery, risk, or improvement inside its own boundary

These processes should normally live in the product’s canonical model, especially in:
- `03-operating-model/OPERATING_MODEL.md`
- `03-operating-model/GOVERNANCE.md`
- `04-execution/*`
- optional product-local artifacts where justified

Examples:
- Security posture review inside the Security product
- Delivery operating flow inside the Delivery product
- Task/decision operating flow inside Task Management
- Improvement cadence inside Improvement

## Cross-product coordination mechanisms
A mechanism is cross-product coordination only when it primarily answers:
- how products interact
- how shared decisions are made across boundaries
- how a portfolio-level review or handoff works
- how common rules constrain multiple products

These may live in central/shared artifacts because they coordinate between product-owned systems rather than replacing them.

Examples:
- portfolio review coordination
- interface / handoff change coordination
- portfolio-level readiness escalation
- shared delivery-mode decision rule
- portfolio boundary rules

## Anti-duplication rule
Do not create a central process artifact if it merely restates how one product already runs.

If a process appears in both:
- a product model, and
- a central/shared artifact,

then the central artifact must be limited to one of these:
1. coordination between products
2. shared constraints or inputs
3. escalation rules crossing product boundaries

Otherwise the product model should remain the canonical source.

## Canonical-source rule
When process ownership is product-local:
- the product model is the source of truth

When process ownership is cross-product:
- the shared coordination artifact is the source of truth
- but it should point back to the affected product models rather than replacing them

## Practical test
Before creating a new shared process artifact, ask:
1. Is this process mainly about how one product operates?
2. Does an owning product already exist?
3. Would a central document duplicate product-local logic?
4. Is the actual need coordination across product boundaries?

If the answer to 1 or 2 is yes, the process probably belongs inside the product.
If the answer to 4 is yes, a small shared coordination artifact may be justified.

## Current implication for PX Strategy
Given the current architecture:
- Product Review protocol is acceptable centrally because it is a shared review coordination mechanism across products.
- Delivery Modes Decision framework is acceptable centrally because it coordinates packaging/delivery choice across products.
- Security, Delivery, Task Management, and Improvement should continue to own their internal operating processes inside their own product models.
- Future central artifacts should be kept narrow and should avoid becoming a parallel operating manual.

## Design intent
The objective is not to minimize documentation for its own sake.
The objective is to preserve:
- clean ownership
- low ambiguity
- low duplication
- stronger product autonomy
- clearer coordination where coordination is actually needed

## Short rule
**Products own processes. Shared artifacts own coordination. Do not invent a parallel process layer.**
