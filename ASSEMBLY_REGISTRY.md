# Assembly Registry v0.1

Purpose: define versioned Product Assemblies that transfer Lyra OS value into PXS with explicit distribution, activation, and enforcement.

## Registry Fields
- Assembly ID
- Name
- Status (`draft` | `candidate` | `stable` | `deprecated`)
- Owner
- Value Promise
- Artifact Types (`service` | `skill-pack` | `policy-pack` | `schema-pack` | `ops-pack`)
- Distribution Lane
- Activation Lane
- Enforcement Checks
- Current Version
- Consumer(s)
- Compatibility Notes

---

## A-001 — Task Management Assembly
- **Status:** draft
- **Owner:** Peter/Lyra
- **Value Promise:** deterministic task/decision operating kernel with safe operator procedures.
- **Artifact Types:** `service`, `skill-pack`, `ops-pack`
- **Distribution Lane:** service via domain runtime + cron; skill via workspace skills; ops docs via versioned pack
- **Activation Lane:** domain-scoped config (`domain=px`/`domain=os`) + isolated cron jobs + operator skill enabled
- **Enforcement Checks:** contract test pass, fail-closed check pass, evidence writeback present
- **Current Version:** v0.1 (planned)
- **Consumer(s):** PXS (planned)
- **Compatibility Notes:** requires separated instance boundary (`os` vs `px`)

## A-002 — Governance
- **Status:** candidate
- **Owner:** Peter/Lyra
- **Value Promise:** safe authority, tooling, and operating controls packaged for direct PXS adoption.
- **Artifact Types:** `policy-pack`, `ops-pack`
- **Distribution Lane:** git-pinned dependency (submodule/subtree/release)
- **Activation Lane:** referenced in PXS operating docs + mandatory checklist in change workflow
- **Enforcement Checks:** policy presence check, checklist completion, approval-gate evidence for high-risk changes
- **Current Version:** v0.1
- **Consumer(s):** PXS
- **Compatibility Notes:** no runtime dependency; documentation/governance layer only

## A-003 — Boundaries
- **Status:** draft
- **Owner:** Peter/Lyra
- **Value Promise:** explicit product/instance boundaries to prevent coupling and drift.
- **Artifact Types:** `policy-pack`, `schema-pack`
- **Distribution Lane:** git-pinned dependency + template sync
- **Activation Lane:** required fields in product records and boundary docs
- **Enforcement Checks:** boundary template completeness check; dependency-policy conformance check
- **Current Version:** v0.1 (planned)
- **Consumer(s):** PXS
- **Compatibility Notes:** aligns with ADR-0001 (repo separation)

## A-004 — Security
- **Status:** candidate
- **Owner:** Peter/Lyra
- **Value Promise:** preventive security controls + response procedures + learning loop to reduce repeated failures.
- **Artifact Types:** `policy-pack`, `ops-pack`
- **Distribution Lane:** git-pinned dependency (target) / interim controlled copy-sync (temporary)
- **Activation Lane:** mandatory references in PXS change flow for prompt/tool/config/risk-impacting work
- **Enforcement Checks:** injection-defense checklist present, incident runbook present, post-incident learning log updated
- **Current Version:** v0.1
- **Consumer(s):** PXS
- **Compatibility Notes:** compatible with repo separation and assembly lock model

## A-005 — Improvement
- **Status:** candidate
- **Owner:** Peter/Lyra
- **Value Promise:** turns reviews and lessons into repeatable system upgrades with clear cadence, ownership, and evidence.
- **Artifact Types:** `policy-pack`, `ops-pack`, `skill-pack`
- **Distribution Lane:** git-pinned dependency (target) / interim controlled copy-sync (temporary)
- **Activation Lane:** scheduled review cadence + mandatory improvement-log updates for material incidents/retros
- **Enforcement Checks:** cadence checklist present, improvement log updated, follow-up tasks linked to decisions/work orders
- **Current Version:** v0.1
- **Consumer(s):** PXS
- **Compatibility Notes:** compatible with assembly lock model and repo separation

## A-006 — Delivery
- **Status:** candidate
- **Owner:** Peter/Lyra
- **Value Promise:** operationalize secure, testable, evidence-backed delivery for both software and broader system/process changes.
- **Artifact Types:** `policy-pack`, `ops-pack`, `skill-pack`
- **Distribution Lane:** git-pinned dependency (target) / interim controlled copy-sync (temporary)
- **Activation Lane:** required release/change gates in execution workflow
- **Enforcement Checks:** checklist gates passed, evidence artifacts recorded, post-release review completed
- **Current Version:** v0.1
- **Consumer(s):** PXS
- **Compatibility Notes:** complements security + continuous-improvement assemblies

## A-007 — Interfaces
- **Status:** candidate
- **Owner:** Peter/Lyra
- **Value Promise:** standardize operational handoff surfaces across human↔agent, agent↔model, and agent↔tool/provider execution.
- **Artifact Types:** `policy-pack`, `ops-pack`, `skill-pack`
- **Distribution Lane:** git-pinned dependency (target) / interim controlled copy-sync (temporary)
- **Activation Lane:** interface contracts referenced in project start packets and delivery routines
- **Enforcement Checks:** interface contract used, routing rationale recorded, provider workflow checklist completed
- **Current Version:** v0.1
- **Consumer(s):** PXS
- **Compatibility Notes:** sits on top of governance/security controls
