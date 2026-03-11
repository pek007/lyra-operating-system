# Product Model Maturity v1

Status: Draft active standard
Owner: Peter / Lyra
Date: 2026-03-11

## Purpose
Define a simple maturity model for Product-as-Code so PX Strategy can describe each product’s model quality consistently.

The intent is not prestige labeling. The intent is to answer:
- how complete is this product model?
- how operationally useful is it?
- what is the next reasonable maturity step?

## Design principle
Maturity should reflect decision usefulness, not document count.

A product with fewer artifacts but clear operating value may be more mature than a product with many stale files.

## Maturity levels

### Level 0 — Unmodeled
Definition:
The product may exist in practice, but there is no canonical Product-as-Code model for it.

Characteristics:
- no canonical `PRODUCT.md`
- no canonical `MODEL.yaml`
- product identity or boundary is implicit
- operational state depends heavily on chat, memory, or scattered docs

Typical next move:
Create a thin canonical product folder and define basic identity.

---

### Level 1 — Placeholder
Definition:
A canonical folder exists, but the product is still mostly undefined.

Minimum characteristics:
- `PRODUCT.md` exists
- `MODEL.yaml` exists
- at least one identity artifact exists
- current state is explicitly marked as discovery or placeholder

Typical use case:
- reserved portfolio slot
- product not yet sufficiently defined
- transition placeholder during portfolio restructuring

Typical next move:
Define owner, purpose, and boundary.

---

### Level 2 — Thin
Definition:
The product has a usable front door and enough structure to orient a human or agent, but it is not yet a full operating model.

Minimum characteristics:
- clear product identity and purpose
- machine-readable metadata
- basic strategy or operating stance
- current plan exists
- a decision log exists

Typical artifact shape:
- `PRODUCT.md`
- `MODEL.yaml`
- `VISION.md`
- `STRATEGY.md` and/or `OPERATING_MODEL.md`
- `PLAN.md`
- `DECISIONS.md`

What Level 2 enables:
- portfolio visibility
- ownership clarity
- lightweight steering

Typical next move:
Add customer, governance, risks, roadmap, and interface clarity.

---

### Level 3 — Standard
Definition:
The product meets the canonical Product Model Standard and can be run with reasonable clarity from its product model.

Minimum characteristics:
- mandatory artifact set exists
- artifacts are coherent and non-placeholder
- customer, strategy, operating model, governance, plan, risks, metrics, interfaces, and decisions are all explicit
- `MODEL.yaml` accurately points to current artifacts
- model supports real planning, review, and cross-product coordination

What Level 3 enables:
- operational product management
- agent-readable decision context
- portfolio comparability
- structured review and governance

Typical next move:
Improve freshness, instrumentation, and tighter linkage between model and runtime evidence.

---

### Level 4 — Deep
Definition:
The product model is not only complete, but actively used as a high-quality control system with strong decision memory, evidence links, and evolving operational instrumentation.

Minimum characteristics:
- Level 3 requirements met well
- optional artifacts are present where they add real value
- model is actively maintained and materially used in reviews/decisions
- stronger metrics, evidence links, and/or ADR structure exist
- product model reduces dependence on transcript reconstruction

What Level 4 enables:
- high-confidence continuity across sessions/operators
- stronger automation and validation potential
- clearer readiness for externalization or scaling

Typical caution:
Do not force Level 4 on every product. Deep modeling should follow real complexity and value.

## Maturity assessment rules

### Rule 1: freshness matters
A stale "complete" model should not be scored above a regularly used thinner one without justification.

### Rule 2: placeholders are valid
A product can honestly remain Level 1 if the underlying product is still undefined.
That is better than fake completeness.

### Rule 3: thin is respectable
Level 2 is an acceptable steady state for lower-complexity products until stronger structure is warranted.

### Rule 4: standard is the default target
For active, important products, Level 3 should usually be the expected operating target.

### Rule 5: deep is selective
Only products with enough strategic, operational, or boundary complexity should be pushed toward Level 4.

## Initial portfolio interpretation
Based on the current portfolio state:
- `A-001` to `A-003`: Level 1 (Placeholder)
- `CP-001` Control Panel: Level 2 (Thin)
- `A-004` Security: between Level 2 and Level 3, trending toward Standard
- `A-005` Improvement: Level 2 (Thin)
- `A-006` Delivery: between Level 2 and Level 3, trending toward Standard
- `A-007` Task Management: Level 3, with some Level 4 characteristics

## Recommended default targets
- Discovery placeholders: Level 1
- Lower-complexity active products: Level 2
- Core active products: Level 3
- Mission-critical or externally facing products: Level 3 or Level 4 depending on complexity
