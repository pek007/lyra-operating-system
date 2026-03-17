# Security Product — Nightly Report

```yaml
artifactType: po_nightly_synthesis
schemaVersion: "1.0"
synthesisId: security-nightly-2026-03-17
productId: A-004
productName: Security
productOwner: Lyra
synthesisDate: "2026-03-17T00:05:00Z"

overallHealth: needs_decision

summary: >
  Security posture is operationally GO under the current trusted-boundary model,
  but the exec/sandbox decision that determines whether the OS↔PXS boundary is
  a real control or a partially-enforced one remains unresolved. The FS-tool
  surface was narrowed on 2026-03-15. Exec-based cross-domain access (sandbox.mode=off,
  tools.exec.security=full, tools.exec.ask=off) remains open, holding E2 at FAIL.
  Priority stack is current and unchanged. No new risks or research deltas this cycle.

materialChanges:
  - "No material changes since 2026-03-16 TOP_PRIORITIES.md update."
  - "MODEL.yaml last_reviewed corrected from 2026-03-11 to 2026-03-17 (housekeeping)."

topPriorities:
  - rank: 1
    title: "Enforce the OS↔PXS boundary as a real control — close the exec/sandbox gap"
    status: execution_in_progress
    bottleneck: "Decision deferred: whether to tighten px-internal-dev exec/sandbox posture or narrow E2 acceptance claim and formally log exec-based access as accepted residual risk."
    nextConcreteStep: "Make and document the exec/sandbox posture decision. Refresh acceptance sheet (B1/C1/C2/E2). Re-run acceptance checks with committed evidence."

  - rank: 2
    title: "Harden tool and evidence execution surfaces that function as policy-enforcement points"
    status: blocked_on_p1
    bottleneck: "Depends on P1 exec/sandbox decision before config can be applied and verified."
    nextConcreteStep: "Once P1 decision is made: apply chosen posture, verify runtime behaviour, log formal decision in DECISIONS.md. Then assess shell-based evidence ingestion paths."

  - rank: 3
    title: "Close the posture → evidence → enforcement loop for PXS consumption"
    status: execution_in_progress
    bottleneck: "Capability-delivery gap inventory (what Vega workflows break under narrowed FS access) still pending — required before acceptance sheet can be fully refreshed."
    nextConcreteStep: "Run live Vega workflow check set against current FS narrowing. Update acceptance sheet. Define minimum promotion-gate check set."

constraints:
  - "Exec/sandbox posture decision is the current rate-limiting factor across all three priorities."
  - "E2 acceptance check holds FAIL; acceptance sheet cannot close until posture decision is committed."
  - "Capability-delivery gap inventory incomplete — blocks P3 acceptance sheet refresh."
  - "MODEL.yaml last_reviewed was stale (2026-03-11); corrected this cycle."

risksOrOpportunities:
  - id: R-001
    title: "OS↔PXS boundary not yet enforced as a real control"
    level: high_active
    trend: stable_unresolved
    note: "Cross-domain blast radius remains larger than declared architecture allows until P1 is closed."
  - id: R-002
    title: "High-risk execution surfaces remain procedural rather than hardened"
    level: medium_active
    trend: stable
    note: "exec/sandbox posture is the live surface; resolution tied to P1 decision."
  - id: R-003
    title: "Posture evidence not always reproducible from committed artifacts"
    level: medium
    trend: stable
    note: "Baseline references some local/latest artifacts; not blocking but requires attention in P3 loop."
  - id: R-004
    title: "Security documentation can look stronger than enforced reality"
    level: medium
    trend: improving
    note: "Boundary artifacts are coherent; gap is in runtime enforcement rather than documentation quality."

researchDelta: none_this_cycle

proposedTdeActions:
  - type: signal
    title: "Exec/sandbox posture decision still unresolved — P1 blocked"
    description: >
      The exec/sandbox gap (sandbox.mode=off, exec.security=full, exec.ask=off on px-internal-dev)
      remains the single highest-priority decision. Either tighten to deny cross-domain exec access
      by default, or formally accept exec-based access as a residual risk with a logged decision.
      Acceptance sheet refresh and E2 re-check follow immediately after.
    priority: high
    suggestedOwner: Peter + Lyra (requires human decision on risk acceptance)
    references:
      - products/security/04-execution/RISKS.md
      - products/security/06-architecture/BOUNDARY.md
      - governance/VEGA_ACCEPTANCE_TEST_RUN_SHEET_V1.md
      - products/task-management/04-execution/VEGA_PXS_BOUNDARY_POST_CHANGE_VALIDATION_2026-03-15.md

  - type: signal
    title: "Vega capability-delivery gap inventory still pending — P3 blocked"
    description: >
      The live Vega workflow check against current FS narrowing has not been run.
      This blocks full acceptance sheet refresh and the definition of a minimum promotion-gate
      check set for PXS consumption.
    priority: medium
    suggestedOwner: Lyra (can execute autonomously once P1 decision is made)
    references:
      - products/task-management/04-execution/VEGA_PXS_BOUNDARY_POST_CHANGE_VALIDATION_2026-03-15.md
      - products/security/05-performance/PXS_DEPLOYMENT_BASELINE.md

priorityRefreshStatus: unchanged

evidenceLinks:
  - products/security/04-execution/TOP_PRIORITIES.md
  - products/security/04-execution/PLAN.md
  - products/security/04-execution/RISKS.md
  - products/security/06-architecture/BOUNDARY.md
  - products/security/05-performance/PXS_DEPLOYMENT_BASELINE.md
  - products/security/07-decisions/DECISIONS.md
  - products/security/MODEL.yaml
  - governance/VEGA_ACCEPTANCE_TEST_RUN_SHEET_V1.md
  - products/task-management/04-execution/VEGA_PXS_BOUNDARY_POST_CHANGE_VALIDATION_2026-03-15.md

sourceReferences:
  - artifact: TOP_PRIORITIES.md
    lastUpdated: "2026-03-16"
    assessment: current
  - artifact: PLAN.md
    assessment: current
  - artifact: RISKS.md
    assessment: current
  - artifact: PXS_DEPLOYMENT_BASELINE.md
    lastUpdated: "2026-03-11"
    assessment: current_for_baseline
  - artifact: MODEL.yaml
    assessment: housekeeping_corrected_this_run
  - artifact: BOUNDARY.md
    lastUpdated: "2026-03-11"
    assessment: current
  - artifact: DECISIONS.md
    assessment: current_pending_exec_sandbox_decision
```
