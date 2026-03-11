---
title: "Capability Model and Product Structure for Lyra OS Enabling Company-as-Code in PXS"
date: 2026-03-11
source: deepresearch
ingest_from: "telegram attachment deep-research-report_68---584ee832-cfd4-4e96-9abd-4508c88fde37.md"
tags: [external-analysis, deepresearch, product-structure, capability-model, lyra-os, pxs, company-as-code]
decision_relevance: high
confidence: high
status: archived-source
---

# Capability Model and Product Structure for Lyra OS Enabling Company-as-Code in PXS

## Context and intent

You have an explicit architectural separation: PXS is intended to own product logic/domain model and product workflows, while the OS repository owns the agent operating model, orchestration/prompting policies, and cross-project operational standards, with a simple boundary rule: “product behavior belongs in PXS; operating-system behavior belongs in the OS repo.” This separation is reinforced by an accepted decision to keep PXS as a standalone repository while retaining the OS workspace as the governance layer, trading off cleaner ownership boundaries for cross-repo coordination overhead.

At the same time, “company-as-code” sets a very specific bar: the system must make strategic decisions executable by default (owner, next action, due date, status), and Phase 1 success is defined around traceable decisions, visible/reliable execution, and a cadence the system supports rather than humans remembering to do. The PXS v1 scope is explicitly about delivering at least one full vertical slice from decision → task → completion evidence.

Within Lyra OS, you’ve created seven “products” (Control Panel, Task Management, Security, Improvements, Delivery, Interfaces, Governance). In parallel, you also have a newer operating model that treats the platform itself as an internal product (“P-PLATFORM”) and requires every process to have an owning product (including interface processes owned by the dominant product with co-approvers).

The design goal you stated is a classic tension: you want the product partition to be MECE (mutually exclusive, collectively exhaustive), roughly equal in “size/importance,” future-proof, but pragmatic enough to evolve with maturity differences.

## Key capabilities Lyra OS must provide to make PXS “company-as-code”

A useful way to reason about required capabilities is to separate *planes* (what changes state) rather than named products. In platform engineering terms, it’s the difference between the internal platform (capabilities) and the stream-aligned product (value delivery), with clear interaction modes and minimal handoffs.

Below is a capability model that is MECE at the “plane” level, but still practical to implement incrementally.

### Governance and policy control plane

This plane answers: **“What is allowed, under what constraints, and who can approve exceptions?”**

Concrete OS capabilities implied by your current governance artifacts include:

- **System direction and decision rights**: explicit mission/objectives, trade-off order, and decision rights (“Ask first / Never / Allowed by default”), plus how enforcement happens (config, agent rules, processes, task/decision engine).
- **Least-privilege by role**: defined agent permission envelopes (read/write/tool scopes, approval requirements).
- **Tooling and external-service governance**: default-deny for high-impact actions, managed secrets, request/response controls, structured audit records, promotion gates for new integrations.
- **Config and change control for the runtime environment**: classifying OpenClaw config risk and enforcing preview/approval/rollback steps.
- **System-wide security posture management**: making security “an owned product capability” with explicit boundaries, usable guardrails, and evidence-backed risk reduction—especially with PXS as an internal customer.

Externally, this plane maps well to established “policy decision vs policy enforcement” separation: a policy decision point (PDP) computes allow/deny based on policies; a policy enforcement point (PEP) enforces it at the access boundary. The same separation is central in policy-as-code tools like Open Policy Agent, which explicitly decouple policy decision-making from enforcement and provide APIs for other systems to query decisions.

### Work and execution plane

This plane answers: **“What work exists, how it moves, and what evidence proves it is done?”**

Capabilities needed:

- **Canonical “execution state” as a system of record (SoR)**: A-007’s stated goal is for TDE to be the trusted operational SoR for active execution state, blockers, decisions, and completion evidence—explicitly rejecting “chat-only operational state.”
- **Decision visibility**: blocked items classified as decisional vs operational, with explicit decision records for meaningful trade-offs.
- **Cadence support**: PXS success criteria include weekly operating cadence being system-supported.
- **Evidence generation and traceability loops**: your Delivery and Improvement products explicitly anchor on acceptance criteria, verification discipline, and evidence-backed closure.

### Interfaces and distribution plane

This plane answers: **“How do capabilities cross boundaries (products, repos, workspaces, tools) without creating coupling debt or unsafe privilege paths?”**

Two constraints shape this plane:

- You’ve defined a **service boundary architecture**: shared codebase, separate instances per domain (`os` and `px`), with strict isolation requirements (data dirs, logs, secrets namespaces, routing policies), and no cross-domain reads by default.
- OpenClaw strongly orients around **skills** and **plugins** as portable capability units. Skills have clear locations and precedence, and plugins can register tools, background services, RPC, HTTP handlers, and can ship skills via the plugin manifest—while running in-process with the gateway and therefore needing to be treated as trusted code.

In practice, this plane must provide:

- **Versioned capability bundles** (skills packs and/or plugins) so PXS can “consume” OS capabilities without importing the OS repo wholesale.
- **Stable interface contracts** (schemas, expected inputs/outputs, idempotent mutation patterns, audit hooks).
- **Integration connectors** with clear promotion gates and credential boundaries.

### Observability and operator experience plane

This plane answers: **“Can an operator see what’s happening, what changed, what matters next—and drill down to source truth?”**

Your Control Panel view spec is already framed this way: “Now/Next/Watch/Change Feed,” sourcing from task state, evidence, runbooks/registries, risk registers, and git history; explicitly non-goaling into a heavy app.

### Continuous improvement plane

This plane answers: **“Does the system get better as a default consequence of operating it?”**

You already have a concrete, product-owned incident-to-improvement loop under A-005: stabilize → record → decide prevention → route → verify → portfolio learning, with explicit triggers and mandatory outputs.

## How these capabilities map to your current seven products

The report argues your current product set is directionally valid but has two structural frictions:

- overlap between Governance, Security, and Interfaces
- overlap between Task Management and Improvements

High-level fit:

- **Control Panel** fits observability/operator experience.
- **Task Management** is the execution plane core.
- **Security** is concentric with governance/tool governance/posture.
- **Improvements** may be more of a platform-wide loop than a standalone product line.
- **Delivery** is delivery system + verification discipline.
- **Interfaces** should become packaging + contracts + connectors rather than a residual bucket.
- **Governance** overlaps heavily with Security and platform-level process ownership.

## Recommended product structure changes

The report recommends collapsing from seven products to **four** aligned to planes:

1. **Platform Control Plane** (merge Governance + Security + core policy machinery)
2. **Work Orchestration** (merge Task Management + Improvement)
3. **Delivery and Integrations** (merge Delivery + Interfaces)
4. **Operator Experience** (Control Panel and operator-facing portal surfaces)

Alternate simpler option suggested:
- Platform
- Work Orchestration
- PXS

But the report warns that this may create an oversized “platform blob.”

## Proposed product visions and strategy themes

### Platform Control Plane
- policy, permissions, tool governance, config/change control, security posture
- near-term recommendation: consolidate governance + security into one canonical control-plane pack
- medium-term: move selectively toward policy-as-code

### Work Orchestration
- TDE as the canonical work/decision/evidence kernel
- absorb Improvement as a first-class workflow rather than separate product line
- near-term: ship one full decision → task → completion evidence vertical slice for PXS

### Delivery and Integrations
- release discipline, verification, packaging, versioning, external connectors, domain separation mechanics
- near-term: define a minimal OS export boundary for PXS consumption
- medium-term: formalize capability bundle versioning

### Operator Experience
- Control Panel views and operator workflows
- near-term: implement a lightweight read-first, write-rare operational surface
- medium-term: evolve toward a portal-like operator experience

## Migration path suggested by the report

1. **Rename by charter first, not folders**
2. **Adopt one boundary rule per product**
3. **Make interfaces explicit through contracts**
4. **Create engineering vs production consumption lanes**
5. **Use a small, maturity-appropriate set of delivery metrics**

## Bottom line from the report

The report’s main thesis is that Lyra OS should be structured less as seven roughly equal “boxes” and more as a smaller number of compounding loops or planes:
- control
- work
- delivery/integration
- operator experience

That is a strong platform-engineering framing and a meaningful challenge to the current seven-product structure.
