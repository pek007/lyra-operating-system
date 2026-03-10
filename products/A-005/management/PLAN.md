# A-005 — Plan

Status: Active v1
Owner: Lyra
Last updated: 2026-03-08

## Now
- Initiative ID: A-005-I1
  - Problem: A-005 product management artifacts were placeholders, leaving strategy, goals, and execution unclear.
  - Expected outcome: Improvement Product has an explicit mandate, goals, scorecard, and operating plan.
  - Dependencies: Existing process and assembly docs
  - Acceptance criteria:
    - Vision, Goals, Plan, Decisions, and Scorecard are populated
    - Role and decision rights are documented
    - First improvement cycle is logged
  - Evidence required: Updated product management docs + improvement log entry

- Initiative ID: A-005-I2
  - Problem: A-005 deployment into PXS exists, but verification is pending and the active operating gap is known.
  - Expected outcome: One full verification baseline is completed with evidence and status updates.
  - Dependencies: `assemblies/continuous-improvement/v0.1/*`, `pxs/PXS_ASSEMBLY_LOCK.md`, PXS assembly dashboard
  - Acceptance criteria:
    - VERIFY checklist evaluated against current state
    - Evidence file created
    - Lock/dashboard status updated to reflect reality
  - Evidence required: Verification note under `knowledge/evidence/2026-03/`

- Initiative ID: A-005-I3
  - Problem: Interim-copy is acceptable short-term but creates drift risk without a migration plan.
  - Expected outcome: Pinned-lane migration path is explicit, sequenced, and owned.
  - Dependencies: PXS assembly lock, assembly packaging conventions, PXS docs
  - Acceptance criteria:
    - Migration plan documented
    - Next review and target migration window defined
    - Risks and prerequisites stated
  - Evidence required: Decision record + PXS doc updates

## Next
- Initiative ID: A-005-I4
  - Problem: Improvement process is documented, but product interfaces are not yet operationalized product-by-product.
  - Expected outcome: Standard minimum improvement interface package rolled out to active products.
  - Dependencies: Product owners, management paths, shared templates
  - Acceptance criteria:
    - Active products have an improvement intake/log mechanism
    - Shared minimum fields are standardized
    - Review cadence and escalation triggers are understood
  - Evidence required: Product-by-product adoption checklist

- Initiative ID: A-005-I5
  - Problem: Portfolio-level pattern detection is still manual and fragile.
  - Expected outcome: A lightweight weekly synthesis routine identifies recurring failure patterns and root causes.
  - Dependencies: Improvement logs, task/decision traces, evidence files
  - Acceptance criteria:
    - Weekly synthesis output template exists
    - Top recurring patterns are tracked across weeks
  - Evidence required: First weekly synthesis artifact

- Initiative ID: A-005-I6
  - Problem: Errors and incidents do not yet have a mandatory closed-loop requirement from record to prevention to verification.
  - Expected outcome: Every material incident/repeated near-miss follows a standard A-005 incident-to-improvement loop with required outputs and routing rules.
  - Dependencies: `INCIDENT_LOG.md`, `CONTINUOUS_IMPROVEMENT_PROCESS_V1.md`, product management artifacts, task/decision handling
  - Acceptance criteria:
    - Canonical loop document exists under A-005
    - Required outputs and closure criteria are defined
    - Trigger rules for prevention work and containment actions are explicit
  - Evidence required: A-005 management doc updates + linked improvement log entry

## Later
- Initiative ID: A-005-I7
  - Problem: Continuous improvement is not yet instrumented enough for comparative evaluation.
  - Expected outcome: Improvement telemetry and experiment scorecards support champion-challenger learning.
  - Dependencies: `SELF_IMPROVEMENT_LOOP_V1.md`, run-event schema, evaluation harness
  - Acceptance criteria:
    - A practical telemetry subset is in use
    - At least one controlled improvement experiment can be evaluated
  - Evidence required: Scorecard + decision log

- Initiative ID: A-005-I8
  - Problem: Capability deployment to PXS still depends on interim assembly handling.
  - Expected outcome: Stable pinned assembly distribution becomes the default lane.
  - Dependencies: Capability-pack approach, release semantics, PXS consumption model
  - Acceptance criteria:
    - A-005 consumed through pinned dependency path
    - Interim-copy removed
    - Rollback path tested
  - Evidence required: Lockfile + acceptance evidence
