# TOP_PRIORITIES

Product: Delivery
Last updated: 2026-04-15
Owner: Product Owner / Control Tower

## Priority 1
**Title:** Add repo-integrity fail-fast gates for merge markers and other delivery hygiene failures
**Why this matters now:** Delivery cannot credibly increase automation or claim trustworthy verification while repositories can still pass through obvious integrity failures. This is the strongest current bottleneck because it weakens every downstream delivery signal.
**Current status:** Core Delivery-as-Code scaffolding exists, but repo-integrity enforcement is still called out in the canonical execution order as unfinished enabling control work, and the newer Delivery improvement-interface direction now makes clear that repeated control misses must become explicit TDE-linked improvement signals rather than remain prose-only observations.
**Next concrete step:** Define and wire one enforceable repo-integrity gate that fails closed on merge markers and similarly obvious hygiene defects in the current governance/validation pathway, capture evidence from one real run, and make any repeated misses routeable into the new TDE-linked improvement path.
**Links:** `products/delivery/04-execution/PLAN.md`, `products/delivery/04-execution/RISKS.md`, `products/delivery/03-operating-model/GOVERNANCE.md`

## Priority 2
**Title:** Replace placeholder PXS quality gates with real enforceable checks
**Why this matters now:** Even with cleaner repos, Delivery remains weak if quality gates are still nominal. Real, machine-enforced checks are required before pilot evidence can be trusted.
**Current status:** The plan explicitly flags placeholder quality gates as unresolved, current metrics/governance expectations require stronger policy-backed verification than the present state implies, and the updated operating model/interfaces now make repeated weak-gate findings a Delivery-to-Improvement routing concern rather than a prose-only concern.
**Next concrete step:** Convert at least one placeholder PXS quality gate into a real enforceable validation hook with explicit pass/fail output and evidence capture aligned to Delivery guardrails, then ensure repeated weak-gate findings can be surfaced through the new TDE-linked improvement path.
**Links:** `products/delivery/04-execution/PLAN.md`, `products/delivery/05-performance/METRICS.md`, `products/delivery/04-execution/RISKS.md`, `products/delivery/03-operating-model/GOVERNANCE.md`

## Priority 3
**Title:** Define the minimum viable professional delivery baseline for backend-first internal operating systems
**Why this matters now:** PxS has now made explicit that Delivery needs to translate its direction into a compact operating model that small, AI-assisted, backend-first systems can actually run now. Without that baseline, Delivery risks improving controls without giving consuming systems sufficiently concrete guidance.
**Current status:** Delivery has strong enabling-control work and Delivery-as-Code direction, but its PxS-facing minimum professional baseline is not yet packaged clearly enough as a near-term output.
**Next concrete step:** Define a compact Delivery baseline covering minimum repository controls, required quality gates, evidence expectations, release/handoff discipline, and minimum security/compliance expectations for a PxS-class internal system.
**Links:** `products/delivery/04-execution/PLAN.md`, `products/delivery/03-operating-model/OPERATING_MODEL.md`, `products/delivery/06-architecture/DELIVERY_AS_CODE_DESIGN_V1.md`, `products/delivery/04-execution/PXS_OS_DELIVERY_REQUIREMENTS_ALIGNMENT_2026-03-26.md`

## Priority 4
**Title:** Professionalize PXS Tools software delivery through Delivery-owned patterns
**Why this matters now:** PXS-side architecture work now makes the need explicit: software development in PXS Tools should become more secure, efficient, auditable, repeatable, and improvable through Delivery, rather than remaining dependent on recurring manual orchestration.
**Current status:** Delivery already has strong enabling-control work and compact baseline direction, and the previously vague integration initiative is now narrowed to a selected first thin-slice autonomous support path: a Delivery-governed evidence-completeness gate plus a TDE-tracked execution-support loop for a bounded internal PXS Tools slice. CRM Core Slice 1 remains the first intended proving case, but it should only be used when the actual implementation repo is present and analyzed. Repeated manual development orchestration, validation/generation/documentation flow, and delivery reliability gaps are still not yet sufficiently absorbed into reusable Delivery-owned patterns.
**Next concrete step:** Use the selected first autonomous-support path plus the new test-case selection rule to choose one real bounded internal PXS Tools slice whose implementation target is already present and inspectable, then run it through explicit kickoff/support state, verification capture, evidence-completeness checking, and completion/follow-up judgment. Treat missing implementation-target access as a real blocker rather than hand-waving past it.
**Links:** `products/delivery/04-execution/PLAN.md`, `products/delivery/04-execution/2026-04-03_PXS_TOOLS_SOFTWARE_DELIVERY_PROFESSIONALIZATION_INTEGRATION_NOTE.md`, `products/delivery/04-execution/PXS_OS_DELIVERY_REQUIREMENTS_ALIGNMENT_2026-03-26.md`, `2026-04-03_DELIVERY_TDE_PXS_TOOLS_INTEGRATION_DECISION_NOTE.md`, `MINIMUM_AUTONOMOUS_DELIVERY_LOOP_V0_1_2026-04-03.md`

## Priority 5
**Title:** Run one real Delivery v0.1 pilot end to end and publish the evidence pack
**Why this matters now:** Delivery still needs proof that a real change can move through activation, gating, evidence capture, and credible rollback. That proof becomes more valuable once it also demonstrates the compact baseline PxS actually needs.
**Current status:** Pilot intent is now materially more concrete than before: the first bounded proving case is selected, the Delivery contract is codified, the kickoff packet is prepared, the implementation lane is confirmed, the first cycle is explicitly narrowed to internal CRM Core Slice 1a account/contact foundation, and pilot activation intake exists. The plan still shows prerequisite gate trustworthiness work ahead of treating the pilot as credible proof.
**Next concrete step:** Keep the narrowed CRM Core Slice 1a cycle as the first proving case inside the broader CRM Core Slice 1 pilot, but do not treat it as evidentiary closure until repo-integrity and at least one real quality gate are live enough to support a trustworthy VERIFY path and publish a canonical evidence pack.
**Links:** `products/delivery/04-execution/PLAN.md`, `assemblies/devsecops-delivery/v0.1/ACTIVATION.md`, `assemblies/devsecops-delivery/v0.1/VERIFY.md`, `products/delivery/04-execution/TDE_UI_PILOT_DELIVERY_CONTRACT_V1.md`, `products/delivery/04-execution/PXS_OS_DELIVERY_REQUIREMENTS_ALIGNMENT_2026-03-26.md`
