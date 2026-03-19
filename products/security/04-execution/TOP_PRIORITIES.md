# TOP_PRIORITIES

Product: Security
Last updated: 2026-03-19
Owner: Product Owner / Control Tower

## Priority 1
**Title:** Build and operationalize the canonical Security estate picture
**Why this matters now:** Security scope has expanded beyond a narrow boundary-and-baseline view. We are responsible for Lyra OS, `pxs`, and now additional surfaces such as Google Workspace. If the estate picture is not explicit, Security strategy and controls will lag the real operating environment.
**Current status:** The first estate and capability artifacts now exist, but they have not yet been fully integrated into the rest of the Security product.
**Next concrete step:** Use `06-architecture/ESTATE_MAP.md`, `06-architecture/CAPABILITY_MAP.md`, and `04-execution/SURFACE_CHANGE_LOG.md` as canonical inputs and align the product’s baseline, risks, and planning artifacts to the explicit estate model.
**Links:** `products/security/06-architecture/ESTATE_MAP.md`, `products/security/06-architecture/CAPABILITY_MAP.md`, `products/security/04-execution/SURFACE_CHANGE_LOG.md`, `products/security/05-performance/PXS_DEPLOYMENT_BASELINE.md`, `products/security/04-execution/RISKS.md`

## Priority 2
**Title:** Assess Google Workspace as a new `pxs` security surface
**Why this matters now:** Google Workspace introduces new identity, communication, sharing, document, and integration attack surfaces inside `pxs`. This is a material security expansion, not just a tooling convenience.
**Current status:** The change is recognized and logged, but the minimum acceptable posture, capability implications, and resulting control priorities have not yet been defined.
**Next concrete step:** Run an explicit Security assessment of Google Workspace in `pxs`, define the minimum acceptable posture, and record the capability, baseline, and roadmap consequences.
**Links:** `products/security/04-execution/SURFACE_CHANGE_LOG.md`, `products/security/06-architecture/ESTATE_MAP.md`, `products/security/06-architecture/CAPABILITY_MAP.md`

## Priority 3
**Title:** Establish OpenClaw upstream release and security-impact monitoring as a standing loop
**Why this matters now:** OpenClaw is moving quickly, including fixes for known weaknesses. Security posture can change upstream even when the local environment appears unchanged, and version drift may carry explicit residual risk.
**Current status:** The need is now explicit and a monitoring model exists, but it is not yet a fully embedded operating cadence.
**Next concrete step:** Start using `08-research/UPSTREAM_MONITORING_MODEL.md` as the triage frame for release-impact review, and record the first deliberate update/defer/watch dispositions.
**Links:** `products/security/08-research/UPSTREAM_MONITORING_MODEL.md`, `products/security/04-execution/SURFACE_CHANGE_LOG.md`, `products/security/08-research/IMPLICATIONS.md`

## Priority 4
**Title:** Define the minimum traceability/logging standard for high-risk actions
**Why this matters now:** Security increasingly depends on being able to reconstruct what happened, what failed, what was attempted, and whether controls actually fired. Auditability is currently important in principle, but still underdefined as an explicit capability.
**Current status:** Logging and traceability have been recognized as high-value needs, but there is no compact canonical minimum standard for the highest-risk actions and surfaces.
**Next concrete step:** Identify the first set of high-risk actions, external-write paths, boundary-affecting changes, and automation surfaces that should carry stronger traceability expectations, then define a narrow first standard.
**Links:** `products/security/06-architecture/CAPABILITY_MAP.md`, `products/security/08-research/ECOSYSTEM_PATTERN_LOG.md`, `products/security/04-execution/PLAN.md`

## Priority 5
**Title:** Keep accepted Phase 1 posture honest while planning future hardening
**Why this matters now:** The product still needs to distinguish between accepted current-state posture and future hardening needs. Without that discipline, Security either overstates confidence or keeps treating accepted decisions as unresolved blockers.
**Current status:** The Phase 1 boundary decision exists, but some downstream artifacts still need tightening to reflect accepted posture vs future improvement work clearly.
**Next concrete step:** Update `RISKS.md`, `PXS_DEPLOYMENT_BASELINE.md`, and `DECISIONS.md` so they explicitly distinguish current accepted state from future hardening and tie that distinction back to the broader estate/capability model.
**Links:** `products/security/05-performance/PXS_DEPLOYMENT_BASELINE.md`, `products/security/04-execution/RISKS.md`, `products/security/07-decisions/DECISIONS.md`, `governance/VEGA_ACCEPTANCE_TEST_RUN_SHEET_V1.md`
