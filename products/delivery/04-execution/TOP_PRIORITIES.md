# TOP_PRIORITIES

Product: Delivery
Last updated: 2026-03-14
Owner: Product Owner / Control Tower

## Priority 1
**Title:** Run one real Delivery v0.1 pilot end to end and publish the evidence pack
**Why this matters now:** Delivery is well-defined conceptually, but still needs a concrete proof path showing that a real change can move through activation, gating, evidence capture, and credible rollback in a consuming environment.
**Current status:** Core delivery scaffolding exists, but the activation and verification path is still thinner than the management/model layer.
**Next concrete step:** Select one representative Delivery v0.1 pilot in PXS, run the full VERIFY path, and produce one canonical evidence pack covering distribution mechanism, gate application, evidence captured, rollback credibility, and pass/fail outcome.
**Links:** `products/delivery/04-execution/PLAN.md`, `assemblies/devsecops-delivery/v0.1/ACTIVATION.md`, `assemblies/devsecops-delivery/v0.1/VERIFY.md`, `products/delivery/04-execution/TDE_UI_PILOT_DELIVERY_CONTRACT_V1.md`

## Priority 2
**Title:** Upgrade the Delivery gate from checklist to contract
**Why this matters now:** Delivery reliability depends on gates being explicit, risk-aware, and evidence-backed rather than interpreted ad hoc per change.
**Current status:** Gate intent exists, but current checklist/verification language is still too thin to function as a compiled delivery contract.
**Next concrete step:** Expand the Delivery gate into a risk-classed contract with required checks, explicit evidence outputs, pass/fail logic, and at least one machine-checkable validation hook in the existing governance/validation pipeline.
**Links:** `products/delivery/04-execution/PLAN.md`, `products/delivery/04-execution/RISKS.md`, `products/delivery/05-performance/METRICS.md`, `assemblies/devsecops-delivery/v0.1/VERIFY.md`

## Priority 3
**Title:** Make Delivery measurement and review operational, not aspirational
**Why this matters now:** Delivery will not compound as a product if scorecards and reviews remain mostly conceptual instead of producing regular low-noise evidence and improvement decisions.
**Current status:** Metric intent is clear, but systematic baselines and real weekly review cadence are still light.
**Next concrete step:** Define a minimal low-noise weekly Delivery scorecard snapshot, run the first real weekly review against it, and record one concrete follow-through improvement from the result.
**Links:** `products/delivery/04-execution/PLAN.md`, `products/delivery/05-performance/METRICS.md`, `products/delivery/04-execution/RISKS.md`
