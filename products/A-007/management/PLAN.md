# A-007 — Plan

Status: Active
Product: Task Management / TDE
Product Owner: Lyra
Last updated: 2026-03-09

## Now
- Initiative ID: A-007-I1
  - Title: Activate product-owner operating model for TDE
  - Problem: TDE product governance exists, but the product’s own goals, decisions, improvement loop, and review posture were not fully instantiated in its management artifacts.
  - Expected outcome: The TDE product itself operates under explicit goals, active plan, decision visibility, evidence expectations, and continuous-improvement discipline.
  - Dependencies:
    - `governance/TDE_PRODUCT_OWNER_OPERATING_INSTRUCTION_V1.md`
    - `governance/TDE_PRODUCT_OWNER_WEEKLY_REVIEW_TEMPLATE_V1.md`
    - `governance/LYRA_CONTINUOUS_IMPROVEMENT_OPERATING_INSTRUCTION_V1.md`
  - Acceptance criteria:
    - Product management artifacts are populated and no longer placeholder-only
    - Current work is linked to explicit goals
    - Initial improvement items and decisions are represented in management records
  - Evidence required:
    - Updated product management files
    - Commit history showing activation changes

- Initiative ID: A-007-I2
  - Title: Define v1 consumer interface for `pxs`
  - Problem: TDE may be internally capable while still lacking a practical consumer interface for downstream use.
  - Expected outcome: A minimal, documented request/output interface exists for first `pxs` pilot consumption.
  - Dependencies:
    - `products/A-007/management/INTERFACES.md`
    - `governance/LYRA_OS_PXS_INTEGRATION_PLAN_V1.md`
    - Current TDE kernel/runtime constraints
  - Acceptance criteria:
    - Minimal inbound/outbound contract defined
    - Transport path for v1 pilot selected
    - Validation/error semantics identified for first pilot scope
  - Evidence required:
    - Updated interface documentation
    - Pilot-ready request/output examples

- Initiative ID: A-007-I3
  - Title: Standardize blocker-to-decision and evidence rules
  - Problem: Product work quality degrades when blocked items stay vague and completions lack evidence.
  - Expected outcome: The TDE product uses explicit rules for blocker classification, decision escalation, and minimum completion evidence.
  - Dependencies:
    - TDE product-owner governance docs
    - Live examples from current product work
  - Acceptance criteria:
    - At least one blocker-to-decision rule documented
    - Minimum evidence rule defined for meaningful completions
    - Rules applied to at least one live item
  - Evidence required:
    - Decision records
    - Updated operating docs or management artifacts
    - Example item showing rule application

## Next
- Initiative ID: A-007-I4
  - Title: Run first `pxs` consumption pilot
  - Problem: Product usability remains hypothetical until a downstream consumer uses TDE through the intended interface.
  - Expected outcome: `pxs` completes a first real pilot use case through the documented TDE interface.
  - Dependencies:
    - I2 complete enough for pilot
    - Readiness and boundary checks satisfied
  - Acceptance criteria:
    - Pilot scenario executed
    - Outcome payload and evidence returned successfully
    - Gaps captured as follow-up work rather than left informal
  - Evidence required:
    - Pilot artifact set
    - Findings and follow-up list

- Initiative ID: A-007-I5
  - Title: Establish weekly TDE product-owner review cadence
  - Problem: Product review quality depends too much on ad hoc recollection instead of compact evidence-based inspection.
  - Expected outcome: Weekly review becomes a normal control loop for goals, active work, blockers, evidence, and improvement capture.
  - Dependencies:
    - `governance/TDE_PRODUCT_OWNER_WEEKLY_REVIEW_TEMPLATE_V1.md`
  - Acceptance criteria:
    - Review template used against current product state
    - Follow-up actions created from review output
  - Evidence required:
    - Completed weekly review artifact
    - Updated management files or TDE items from review

## Later
- Initiative ID: A-007-I6
  - Title: Harden product-facing compatibility and versioning model
  - Problem: Broader adoption will become fragile without clearer interface versioning and compatibility expectations.
  - Expected outcome: Consumers can rely on versioned, understandable interface behavior.
  - Dependencies:
    - Learning from first pilots
    - Stabilized request/output contracts
  - Acceptance criteria:
    - Compatibility/versioning note published
    - Change-handling expectations documented
  - Evidence required:
    - Updated interface spec
    - Example versioned contract

- Initiative ID: A-007-I7
  - Title: Strengthen product scorecard with measurable signals
  - Problem: Product health is still assessed more qualitatively than quantitatively.
  - Expected outcome: A practical scorecard tracks value, reliability, flow, risk, and efficiency signals for the TDE product.
  - Dependencies:
    - More mature runtime and pilot evidence
  - Acceptance criteria:
    - Scorecard fields populated with real signals
    - Review cadence linked to scorecard usage
  - Evidence required:
    - Updated scorecard
    - At least one review using it
