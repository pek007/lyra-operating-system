# TOP_PRIORITIES

Product: Delivery
Last updated: 2026-03-26
Owner: Product Owner / Control Tower

## Priority 1
**Title:** Add repo-integrity fail-fast gates for merge markers and other delivery hygiene failures
**Why this matters now:** Delivery cannot credibly increase automation or claim trustworthy verification while repositories can still pass through obvious integrity failures. This is the strongest current bottleneck because it weakens every downstream delivery signal.
**Current status:** Core Delivery-as-Code scaffolding exists, but repo-integrity enforcement is still called out in the canonical execution order as unfinished enabling control work.
**Next concrete step:** Define and wire one enforceable repo-integrity gate that fails closed on merge markers and similarly obvious hygiene defects in the current governance/validation pathway, then capture evidence from one real run.
**Links:** `products/delivery/04-execution/PLAN.md`, `products/delivery/04-execution/RISKS.md`, `products/delivery/03-operating-model/GOVERNANCE.md`

## Priority 2
**Title:** Replace placeholder PXS quality gates with real enforceable checks
**Why this matters now:** Even with cleaner repos, Delivery remains weak if quality gates are still nominal. Real, machine-enforced checks are required before pilot evidence can be trusted.
**Current status:** The plan explicitly flags placeholder quality gates as unresolved, and current metrics/governance expectations require stronger policy-backed verification than the present state implies.
**Next concrete step:** Convert at least one placeholder PXS quality gate into a real enforceable validation hook with explicit pass/fail output and evidence capture aligned to Delivery guardrails.
**Links:** `products/delivery/04-execution/PLAN.md`, `products/delivery/05-performance/METRICS.md`, `products/delivery/04-execution/RISKS.md`, `products/delivery/03-operating-model/GOVERNANCE.md`

## Priority 3
**Title:** Define the minimum viable professional delivery baseline for backend-first internal operating systems
**Why this matters now:** PxS has now made explicit that Delivery needs to translate its direction into a compact operating model that small, AI-assisted, backend-first systems can actually run now. Without that baseline, Delivery risks improving controls without giving consuming systems sufficiently concrete guidance.
**Current status:** Delivery has strong enabling-control work and Delivery-as-Code direction, but its PxS-facing minimum professional baseline is not yet packaged clearly enough as a near-term output.
**Next concrete step:** Define a compact Delivery baseline covering minimum repository controls, required quality gates, evidence expectations, release/handoff discipline, and minimum security/compliance expectations for a PxS-class internal system.
**Links:** `products/delivery/04-execution/PLAN.md`, `products/delivery/03-operating-model/OPERATING_MODEL.md`, `products/delivery/06-architecture/DELIVERY_AS_CODE_DESIGN_V1.md`, `products/delivery/04-execution/PXS_OS_DELIVERY_REQUIREMENTS_ALIGNMENT_2026-03-26.md`

## Priority 4
**Title:** Run one real Delivery v0.1 pilot end to end and publish the evidence pack
**Why this matters now:** Delivery still needs proof that a real change can move through activation, gating, evidence capture, and credible rollback. That proof becomes more valuable once it also demonstrates the compact baseline PxS actually needs.
**Current status:** Pilot intent and delivery contract exist, but the plan shows prerequisite gate trustworthiness work still ahead of the pilot in execution order.
**Next concrete step:** After repo-integrity and at least one real quality gate are live — and with the compact baseline framed clearly enough to test — select one representative Delivery v0.1 pilot in PXS, run the full VERIFY path, and publish the canonical evidence pack.
**Links:** `products/delivery/04-execution/PLAN.md`, `assemblies/devsecops-delivery/v0.1/ACTIVATION.md`, `assemblies/devsecops-delivery/v0.1/VERIFY.md`, `products/delivery/04-execution/TDE_UI_PILOT_DELIVERY_CONTRACT_V1.md`, `products/delivery/04-execution/PXS_OS_DELIVERY_REQUIREMENTS_ALIGNMENT_2026-03-26.md`
