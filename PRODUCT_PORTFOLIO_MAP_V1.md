# Product Portfolio Map v1

Status: Active draft
Date: 2026-03-11
Owner: Peter / Lyra

## Purpose
Create an explicit mapping between:
- portfolio product IDs
- older `products/<ID>/management/` paths
- newer slug-based Product-as-Code folders under `products/<slug>/`

This prevents drift during the transition from management-pack placeholders to fuller product models.

## Mapping

| Product ID | Product Name | Legacy management path | Canonical Product-as-Code path | Notes |
|---|---|---|---|---|
| `CP-001` | Control Panel | `products/CP-001-control-panel/management/` | `products/control-panel/` | New slug-based model is canonical; legacy pack retained as historical/source material for now |
| `A-001` | TBD | `products/A-001/management/` | `products/A-001-thin/` | Discovery placeholder only |
| `A-002` | TBD | `products/A-002/management/` | `products/A-002-thin/` | Discovery placeholder only |
| `A-003` | TBD | `products/A-003/management/` | `products/A-003-thin/` | Discovery placeholder only |
| `A-004` | Security | `products/A-004/management/` | `products/security/` | New slug-based model is canonical; legacy pack retained as source material |
| `A-005` | Improvement | `products/A-005/management/` | `products/improvement/` | New slug-based model is canonical; legacy pack retained as source material |
| `A-006` | Delivery | `products/A-006/management/` | `products/delivery/` | New slug-based model is canonical; legacy pack retained as source material |
| `A-007` | Task Management | `products/A-007/management/` | `products/task-management/` | New slug-based model is canonical; legacy pack retained as source material |

## Canonical path rule
Until further notice, the canonical product model for each product is the slug-based folder listed above.

Legacy `management/` folders may still contain useful source material, but they should not be treated as the primary forward-looking product model once a canonical Product-as-Code folder exists.

## Transition rule
When a product has both:
- a legacy management pack, and
- a slug-based Product-as-Code folder,

the slug-based folder wins for:
- current product identity
- current operating model
- current execution model
- current interface model
- current decision model

Legacy packs may still be mined for:
- earlier decisions
- product-boundary thinking
- previous plans
- historical context worth migrating forward
