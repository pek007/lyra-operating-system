# Distribution Model

For Security, distribution means propagation of security requirements, controls, posture outputs, and review practices into the products and environments that depend on them.

## Primary distribution path
Security is distributed through:
- policy and control artifacts
- review and audit outputs
- deployment security requirements
- posture summaries and residual-risk decisions
- evidence loops and verification expectations

## Adoption model
1. Define practical controls and posture expectations in the Security product.
2. Push those expectations into active products and consuming environments through explicit requirements and review loops.
3. Keep residual-risk and exception handling visible.
4. Improve packaging and repeatability only after the operating model is stable.

## Distribution mechanisms
- workspace policy and operating artifacts
- recurring audit/evidence generation
- deployment baselines for consuming environments such as `pxs`
- product-facing guidance and escalation signals
- future reusable control packs or schema-backed security contracts if warranted

## Workspace consumption requirements
For a downstream workspace such as `pxs`, Security distribution should not stop at shipping control artifacts.
The consumer workspace should also have enough local operating-package structure to make the adopted security posture discoverable and actionable.

At minimum, consuming workspaces should make explicit:
- local source-of-truth and process-discovery front doors
- local error/incident handling path
- local decision/escalation path for exceptions or residual-risk implications
- any adopted security baseline or boundary artifacts relevant to that workspace

## Activation model
Security becomes active in a consuming context when:
- relevant requirements or controls are adopted
- posture reviews and evidence loops are in place
- residual-risk decisions are explicit
- changes with material downside trigger the expected escalation path

## Success signal
Consuming products and environments know what security posture applies, what exceptions exist, and what they must do to remain inside the accepted boundary.
