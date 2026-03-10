# Control Panel — Plan

## Now
- Initiative ID: CP-I1 Framework rollout
  - Problem: Product teams lack a single standard for vision/goal/plan/improvement artifacts.
  - Expected outcome: All products can adopt one common structure with minimal friction.
  - Dependencies: Product list and owners confirmed.
  - Acceptance criteria: Framework doc published; template available; first product instantiated.
  - Evidence required: File paths + registry references.

## Next
- Initiative ID: CP-I2 Product adoption support
  - Problem: Inconsistent adoption quality across product owners.
  - Expected outcome: Repeatable onboarding and quality checks for each product.
  - Dependencies: CP-I1 complete.
  - Acceptance criteria: Adoption checklist used by at least one additional product.
  - Evidence required: Completed checklist + decision notes.

- Initiative ID: CP-I4 Memory capability formalization
  - Problem: Memory exists across many layers, but without one formal process, ownership model, activation standard, or roadmap.
  - Expected outcome: Memory becomes a managed Control Panel capability with clear scope, ownership, activation model, and implementation priorities.
  - Dependencies: Product ownership framing and terminology clarified.
  - Acceptance criteria: `MEMORY_PROCESS_V1.md` published; `SITUATIONAL_AWARENESS.md` updated; Control Panel management artifacts reflect memory capability ownership; follow-on tasks captured.
  - Evidence required: File paths + task references + decision note.
  - Current implementation artifacts: `MEMORY_IMPLEMENTATION_ROADMAP_V1.md`, `MEMORY_ACTIVATION_MAP_V1.md`

- Initiative ID: CP-I5 Runtime topology design
  - Problem: Current product handling depends too much on Telegram session context, creating role drift, weak wake-up semantics, and manual cross-session coordination.
  - Expected outcome: Lyra OS has an explicit runtime topology map with central-vs-dedicated runtime criteria, wake-up strategy by class, and a clear migration path away from session-only product identity.
  - Dependencies: Decision memo `DEC-2026-015` adopted and reflected in Control Panel governance.
  - Acceptance criteria: `RUNTIME_TOPOLOGY_MAP_V1.md` published; runtime-topology tasks created; Control Panel artifacts updated to reflect topology work as active design.
  - Evidence required: Topology map path + decision reference + task references.
  - Current implementation artifacts: `RUNTIME_TOPOLOGY_MAP_V1.md`, `RUNTIME_ASSIGNMENT_MAP_V1.md`, `INTRA_LYRA_HANDOFF_PROTOCOL_V1.md`, `TASK_MANAGEMENT_PROOF_CASE_V1.md`

## Later
- Initiative ID: CP-I3 Quality automation
  - Problem: Manual governance checks are fragile.
  - Expected outcome: Lightweight validation of required artifacts and minimum quality fields.
  - Dependencies: Stable template usage patterns.
  - Acceptance criteria: Basic validator detects missing required sections.
  - Evidence required: Validator run output + remediation notes.

- Initiative ID: CP-I6 Product runtime embodiment
  - Problem: Products are documented and increasingly governed, but not yet consistently embodied as deployed capabilities using Skills, Cron, and deeper runtime packaging where appropriate.
  - Expected outcome: A first product runtime embodiment framework exists, with initial packaging priorities defined for Control Panel, Task Management, and Governance.
  - Dependencies: Runtime topology and handoff standardization work completed to baseline.
  - Acceptance criteria: `PRODUCT_RUNTIME_EMBODIMENT_FRAMEWORK_V1.md` and `PRODUCT_RUNTIME_EMBODIMENT_MAP_V1.md` published; first-wave embodiment priorities identified.
  - Evidence required: Framework/map paths + linked follow-on tasks.
  - Current implementation artifacts: `PRODUCT_RUNTIME_EMBODIMENT_FRAMEWORK_V1.md`, `PRODUCT_RUNTIME_EMBODIMENT_MAP_V1.md`, `SKILL_CONCEPTS_FIRST_WAVE_V1.md`