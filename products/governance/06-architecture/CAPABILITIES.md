# Governance Capabilities

Status: Draft active capability record
Product: A-008 Governance
Owner: Lyra
Standard: `CAPABILITY_MODEL_STANDARD_V1.md`
Date: 2026-03-17

## A-008.C1 — System governance / change-control rules
- Owning product: Governance
- Purpose: Define system-level rules, decision rights, and change discipline that keep Lyra OS coherent.
- Scope / boundary: Shared/system-level rules only; does not absorb product-local recurring processes
- Primary consumers: all products, `main`, future workspaces
- Delivery mode(s): governance artifacts
- Entrypoint / interface: governance standards, policies, and decision records
- Canonical artifacts: `PRODUCT.md`, `03-operating-model/OPERATING_MODEL.md`, `07-decisions/DECISIONS.md`
- Dependencies: product ownership discipline, authority-change rules
- Constraints / guardrails: must not create a parallel central process layer
- Readiness: usable
- Lifecycle state: active
- Evidence: active governance standards and decision records in daily use
- Known gaps / risks: still fragmented across many artifacts; discoverability improving but not complete
- Upgrade / retirement trigger: upgrade when governance rules are consolidated into clearer product-local capability records

## A-008.C2 — Decision-record discipline
- Owning product: Governance
- Purpose: Make meaningful decisions explicit, durable, reviewable, and connected to authority.
- Scope / boundary: Governs decision quality and capture rules; does not replace product-local substantive ownership
- Primary consumers: all products, operators
- Delivery mode(s): governance artifacts + decision templates/records
- Entrypoint / interface: decision docs, policy records, escalation artifacts
- Canonical artifacts: decision standards and product/shared decision artifacts
- Dependencies: process discovery, local SoR placement, authority clarity
- Constraints / guardrails: decisions should not remain implicit in chat or memory when they materially affect execution
- Readiness: usable
- Lifecycle state: active
- Evidence: decision artifacts across products and recent error corrections
- Known gaps / risks: uneven closure discipline; some decisions still need stronger handoff patterns
- Upgrade / retirement trigger: upgrade when closure and retention rules are consistently verified

## A-008.C3 — Error reporting and control-failure discipline
- Owning product: Governance
- Purpose: Turn incidents, control failures, and near misses into structured learning/control artifacts.
- Scope / boundary: Shared standard and handling logic; product-local errors should still live with owning products where appropriate
- Primary consumers: all products, `main`
- Delivery mode(s): governance artifacts + templates
- Entrypoint / interface: `ERROR_REPORTING_STANDARD_V1.md`, report templates, linked corrective action paths
- Canonical artifacts: error reporting standard/template, shared/system error reports
- Dependencies: Task Management intake/assignment path, closed-loop improvement model
- Constraints / guardrails: reports must produce corrective action, model update, or equivalent operational effect
- Readiness: usable
- Lifecycle state: active
- Evidence: multiple recent error reports filed and converted into policy/task changes
- Known gaps / risks: conversion to canonical follow-through is improving but not yet fully uniform
- Upgrade / retirement trigger: upgrade when product-local and shared error pathways are fully normalized

## A-008.C4 — Workspace operating package standard
- Owning product: Governance
- Purpose: Define the minimum local operating package a downstream workspace must have to consume Lyra OS capabilities coherently.
- Scope / boundary: Defines the standard/template/protocol layer; does not own each workspace’s local package instance
- Primary consumers: `pxs`, future workspaces, operators
- Delivery mode(s): governance artifacts + workspace artifacts + retrofit/validation protocols
- Entrypoint / interface: workspace package standards and bootstrap/retrofit protocols
- Canonical artifacts: `WORKSPACE_OPERATING_PACKAGE_STANDARD_V1.md`, `WORKSPACE_BOOTSTRAP_AND_RETROFIT_PROTOCOL_V1.md`, `PROCESS_DISCOVERY_INDEX_STANDARD_V1.md`
- Dependencies: process discovery model, local workspace ownership
- Constraints / guardrails: must keep local authority explicit and avoid centralizing local operating logic
- Readiness: usable
- Lifecycle state: active
- Evidence: successful retrofit of `pxs` into minimally valid package
- Known gaps / risks: current downstream packages remain Level 1 / minimal; stronger local packages still needed
- Upgrade / retirement trigger: upgrade when downstream workspaces need Level 2/3 package maturity patterns

## A-008.C5 — Skill portfolio governance and lifecycle management
- Owning product: Governance
- Purpose: Keep the skill portfolio owned, classified, capability-linked where relevant, lifecycle-managed, and architecturally coherent.
- Scope / boundary: Governs how skills are created, classified, reviewed, improved, constrained, and retired; does not replace product-specific ownership of the capabilities delivered through skills.
- Primary consumers: Lyra, product owners, future workspaces consuming governed skill packs
- Delivery mode(s): governance artifacts + skill
- Entrypoint / interface: `SKILL_ARCHITECTURE_STANDARD_V1.md`, `SKILL_PORTFOLIO_REGISTRY.md`, `skills/skill-governance/`
- Canonical artifacts: `SKILL_ARCHITECTURE_STANDARD_V1.md`, `SKILL_PORTFOLIO_REGISTRY.md`, `skills/skill-governance/SKILL.md`, `skills/skill-governance/references/lifecycle-checklist.md`
- Dependencies: capability model, delivery-mode framework, product ownership discipline, skill-creator patterns
- Constraints / guardrails: must prevent loose/unowned skills, avoid turning skills into a parallel unmanaged process layer, and avoid forcing skill delivery where another mode is clearly better.
- Readiness: draft
- Lifecycle state: building
- Evidence: first-pass governed skill portfolio artifacts and capability-linked local skill implementation in current workspace
- Known gaps / risks: lifecycle/testing practice is newly formalized and not yet exercised across several real skill changes
- Upgrade / retirement trigger: upgrade when multiple skill create/improve/retire cycles have been executed through the standard; retire or narrow if the capability moves into a different governance mechanism.

## A-008.C6 — Bounded governance verification cycle execution
- Owning product: Governance
- Purpose: Run one bounded Governance VERIFY cycle consistently, with clear evidence output and minimal interpretation drift.
- Scope / boundary: Verifies one governance artifact, process, claim, packaging surface, or control condition at a time; does not broaden into a general governance review or rewrite policy broadly during a bounded cycle.
- Primary consumers: Governance lane, Control Panel, future scheduled governance review loops
- Delivery mode(s): `skill`, supported by governance and assembly verification artifacts
- Entrypoint / interface: `skills/governance-verify-cycle/`; governance and assembly verification surfaces
- Canonical artifacts: `skills/governance-verify-cycle/SKILL.md`, `skills/governance-verify-cycle/references/verify-checklist.md`, `SKILL_CONCEPTS_FIRST_WAVE_V1.md`, `assemblies/governance-policy/v0.1/VERIFY.md`
- Dependencies: governance artifacts, evidence paths, decision/risk records, assembly verification surfaces where relevant
- Constraints / guardrails: no broad policy rewrites during bounded verification; escalate authority/risk issues and material standards/boundary implications; avoid non-deterministic evidence placement
- Readiness: draft
- Lifecycle state: building
- Evidence: first-wave concept defined in `SKILL_CONCEPTS_FIRST_WAVE_V1.md`; governance assembly verification surface already exists in `assemblies/governance-policy/v0.1/VERIFY.md`
- Known gaps / risks: representative live-run evidence still needs to be captured; evidence path conventions may need tightening after first real uses
- Upgrade / retirement trigger: upgrade when multiple real bounded VERIFY cycles complete with reliable outputs and evidence placement; retire or narrow if a stronger runtime-native verification mechanism supersedes skill delivery.
