# Interfaces

## Upstream interfaces
- governance, shared platform capabilities, and relevant repos
- product intent, objectives, and work intake
- TDE state and work-order/control surfaces

## Downstream interfaces
- delivery outputs and readiness signals to products and consuming environments
- rendered packets: verification, release/handoff, approval, audit, and post-delivery review

## Control interfaces
Delivery-as-Code should expose or standardize interfaces for:
- Delivery Unit definitions
- state transitions
- evidence records
- decision records
- exception records
- rendered outputs

Reference:
- `DELIVERY_AS_CODE_DESIGN_V1.md`

## Key boundary rule
Delivery owns the shipping system, not the full strategy of every product it serves.
