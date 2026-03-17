# TOP_PRIORITIES

Product: Security
Last updated: 2026-03-16
Owner: Product Owner / Control Tower

## Priority 1
**Title:** Enforce the OS↔PXS boundary as a real control — close the exec/sandbox gap
**Why this matters now:** The declared boundary is still not enforced as a deny-by-default runtime control. The `px-internal-dev` filesystem-tool surface was narrowed on 2026-03-15, but exec-based cross-domain access remains open (`sandbox.mode=off`, `tools.exec.security=full`, `tools.exec.ask=off`). E2 (acceptance sheet) stays FAIL. The boundary is tighter but not closed.
**Current status:** Partial progress — FS tools narrowed, exec/sandbox posture unresolved. Highest active security risk.
**Next concrete step:** Decide and document whether to (a) tighten `px-internal-dev` exec/sandbox posture to deny cross-domain exec access by default, or (b) narrow the E2 acceptance claim honestly to FS-tool surface only and formally accept exec-based access as a residual risk with logged decision. Whichever path is chosen, refresh the acceptance sheet (B1/C1/C2/E2) and re-run the relevant acceptance checks with committed evidence.
**Links:** `products/security/04-execution/PLAN.md`, `products/security/04-execution/RISKS.md`, `products/security/06-architecture/BOUNDARY.md`, `governance/VEGA_ACCEPTANCE_TEST_RUN_SHEET_V1.md`, `products/task-management/04-execution/VEGA_PXS_BOUNDARY_POST_CHANGE_VALIDATION_2026-03-15.md`

## Priority 2
**Title:** Harden the tool and evidence execution surfaces that function as policy-enforcement points
**Why this matters now:** Security posture is weakest where execution still depends on sharp procedural paths instead of deterministic hardened controls. The exec/sandbox configuration gap now directly blocks P1 closure, making this urgent and concrete rather than aspirational.
**Current status:** Adoption-plan direction exists; exec/sandbox posture on `px-internal-dev` is now the live highest-risk surface requiring explicit decision.
**Next concrete step:** Once the P1 exec/sandbox decision is made, apply the chosen config posture, verify runtime behavior, and record the decision in `07-decisions/DECISIONS.md` as a formal logged posture choice. Then assess whether remaining shell-based evidence ingestion paths should be hardened in the same change window.
**Links:** `products/security/04-execution/PLAN.md`, `products/security/04-execution/RISKS.md`, `SECURITY_ADOPTION_PLAN.md`, `products/security/07-decisions/DECISIONS.md`

## Priority 3
**Title:** Close the posture → evidence → enforcement loop for PXS consumption
**Why this matters now:** Security requirements for consuming environments only become trustworthy when they are backed by reproducible evidence and narrow promotion checks rather than prose alone.
**Current status:** Baseline and boundary artifacts exist; some references still depend on local/latest evidence; the full consumption loop is not yet tight enough. The capability-delivery gap inventory (what Vega workflows actually break under narrowed FS access) is still pending and needed before the acceptance sheet can be fully refreshed.
**Next concrete step:** Run the live Vega workflow check set to identify missing capability-delivery gaps under the current FS narrowing. Update the acceptance sheet (B1/C1/C2/E2). Then define the narrow set of checks that must pass before security-impacting versions are promoted into PXS.
**Links:** `products/security/05-performance/PXS_DEPLOYMENT_BASELINE.md`, `products/security/06-architecture/INTERFACES.md`, `products/security/04-execution/RISKS.md`, `products/task-management/04-execution/VEGA_PXS_BOUNDARY_POST_CHANGE_VALIDATION_2026-03-15.md`
