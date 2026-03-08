# A-006 — Plan

Status: Active

## Now
- Initiative ID: A-006-I1
  - Problem: Delivery exists as an assembly and set of research inputs, but not yet as an activated product management system with current priorities and rules.
  - Expected outcome: A-006 becomes the canonical operating layer for Delivery in this workspace, with an active vision, goals, plan, scorecard, and decision log.
  - Dependencies:
    - Existing product management template
    - Existing A-006 assembly artifacts
    - Existing delivery/process research in the library
  - Acceptance criteria:
    - A-006 management artifacts are populated with non-placeholder product content
    - A-006 is explicitly identified as Delivery in the product portfolio registry
    - Initial decisions and improvement hypotheses are recorded
  - Evidence required:
    - Updated files under `products/A-006/management/`
    - Updated `PRODUCT_PORTFOLIO_REGISTRY.md`

- Initiative ID: A-006-I2
  - Problem: Delivery work can still drift into ad hoc execution without a sufficiently explicit operating model for intake, verification, and improvement.
  - Expected outcome: The product has a clear practical stance: hybrid flow-based delivery with risk-aware gates, evidence-backed completion, and reuse of existing DoD/gate/process assets.
  - Dependencies:
    - `SOFTWARE_DELIVERY_PROCESS_3PP_OS.md`
    - `STD-001_DEFINITION_OF_DONE.md`
    - `DELIVERY_GATE_CHECKLIST.md`
    - Relevant delivery research
  - Acceptance criteria:
    - The A-006 product artifacts explicitly describe how Delivery should work
    - Current and future Delivery work can be mapped to clear goals and initiatives
  - Evidence required:
    - Updated `VISION.md`, `GOALS.md`, `PLAN.md`, and `DECISIONS.md`

## Next
- Initiative ID: A-006-I3
  - Problem: Delivery lacks a lightweight but concrete scorecard and baseline for tracking flow, quality, risk, and improvement.
  - Expected outcome: A-006 uses a small scorecard with initial baseline definitions and an agreed measurement approach that can evolve into stronger DORA-style telemetry.
  - Dependencies:
    - Existing delivery research on DORA, verification debt, and flow metrics
    - Availability of evidence sources in workspace/repo processes
  - Acceptance criteria:
    - Scorecard categories are defined with operational meaning
    - At least one metric/baseline note exists for each scorecard dimension
  - Evidence required:
    - Updated `SCORECARD.md`
    - Supporting decision or improvement-log references where needed

- Initiative ID: A-006-I4
  - Problem: Delivery improvement work is likely to remain opportunistic unless it gets an explicit cadence and trigger model.
  - Expected outcome: A lightweight recurring improvement rhythm is defined, potentially with cron support for periodic Delivery-system review.
  - Dependencies:
    - Product owner decision on cadence and reporting expectations
    - Review of existing cron/job patterns in the workspace
  - Acceptance criteria:
    - Improvement cadence is defined in product artifacts
    - If automated, at least one low-noise recurring review job is specified with clear output rules
  - Evidence required:
    - Updated `IMPROVEMENT_LOG.md` and/or `DECISIONS.md`
    - Optional cron job spec or live cron entry

## Later
- Initiative ID: A-006-I5
  - Problem: Development-management visibility is fragmented across docs, repos, and operator memory.
  - Expected outcome: Delivery defines the requirements for an internal development-management/control surface when the need justifies building it.
  - Dependencies:
    - Sufficient operational pain or management demand
    - Inputs from other products and process owners
  - Acceptance criteria:
    - Opportunity/problem statement exists
    - Boundaries and user decisions to support are explicit before implementation starts
  - Evidence required:
    - Decision memo, product brief, or opportunity packet

- Initiative ID: A-006-I6
  - Problem: Delivery capability still relies heavily on manual discipline rather than machine-checked evidence and enforcement.
  - Expected outcome: Key delivery controls become automated over time, including better traceability, checks, and release-readiness evidence.
  - Dependencies:
    - Tooling capacity
    - Stable artifact contracts and process choices
  - Acceptance criteria:
    - At least one delivery control is automated without raising operational noise unacceptably
    - Manual governance burden is reduced while preserving quality
  - Evidence required:
    - Tool/code change artifacts
    - Improvement log entries with before/after result