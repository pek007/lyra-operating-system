# Decisions

## Decision log purpose
Capture the major product decisions that shape Task Management so the product does not depend on transcript memory alone.

## Recorded decisions
### D-001 — Task Management is a product
- Decision: Task and decision capability is treated as an explicit product rather than only a loose collection of docs, tools, and processes.
- Why it matters: This creates ownership, boundaries, interfaces, and a basis for deliberate improvement.

### D-002 — TDE is the primary capability focus
- Decision: TDE is the core capability focus for the product in the current phase.
- Why it matters: It gives the product a concrete center of gravity and keeps strategy tied to operational reality.

### D-003 — `pxs` is the first downstream consuming workspace
- Decision: The product must make Task Management capability consumable by `pxs`.
- Why it matters: It turns the product from an internal concept into an enabling capability with a real consumer.

### D-004 — Product-as-Code pilot starts with Task Management
- Decision: Task Management is the first product to receive a fuller Product-as-Code model.
- Why it matters: This product is close to the operating-system bottleneck and is a good proving ground for a reusable standard.

### D-005 — First formal downstream interface to `pxs` is an operating-contract artifact
- Decision: The first formal Task Management → `pxs` interface is defined as a documented operating contract in `06-architecture/PXS_CONSUMPTION_INTERFACE.md`, rather than a service or packaged capability boundary.
- Why it matters: This is the lightest interface shape that removes ambiguity now without forcing premature packaging.

### D-006 — Task Management delivery into `pxs` remains artifact-and-ops-pack based for now
- Decision: Task Management capability delivery into `pxs` should currently remain centered on workspace artifacts and ops-pack style operating assets, with schema-backed strengthening only where it adds clarity. It should not yet become a plugin or service.
- Why it matters: This preserves the lightest viable delivery mode while the interface is still stabilizing and avoids premature runtime packaging.

## Related decision artifact
- `07-decisions/DELIVERY_MODE_DECISION_PXS_V1.md`

## Next decisions likely needed
- what evidence threshold should define operational readiness for broader use
- when the `pxs` interface should evolve from operating-contract form into a stronger packaged or schema-backed interface
