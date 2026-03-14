# Workspace Operating Package Standard v1

Status: Draft standard
Owner: Lyra OS
Date: 2026-03-14

## Purpose
Define the minimum architectural standard for a workspace as an operable downstream environment under Lyra OS.

A workspace is not just a folder or a chat context. It is a local operating package: a defined, inspectable, evolvable bundle of artifacts that allows work to be executed coherently, safely, and repeatably.

This standard exists to ensure that new workspaces can be bootstrapped intentionally, existing workspaces can be assessed and upgraded, and downstream consumers receive a complete enough operating package rather than ad hoc fragments.

## Scope
This standard applies to workspaces that consume one or more Lyra OS product capabilities.

It does not replace Product-as-Code. Instead, it defines the consumer-side operating package that sits downstream of product delivery.

## Relationship to Product-as-Code
Products remain the canonical unit of capability definition.

Products define:
- purpose
- boundaries
- interfaces
- delivery modes
- downstream consumption requirements

Workspaces are the canonical unit of local operation.

A workspace operating package instantiates what a specific workspace needs in order to consume those product outputs correctly.

## Core definition
A Workspace Operating Package is the local assembled bundle of operating artifacts required for a workspace to:
- understand its purpose and authority boundary
- know which sources are authoritative
- discover applicable official processes
- execute work through the intended task/decision/error paths
- consume delivered capabilities without relying on hidden thread memory or internal-only assumptions

## Design principles
1. Assembly, not improvisation
   - A workspace package should be intentionally assembled from product outputs and local operating needs.

2. Local authority
   - Each workspace must have its own local operating artifacts for what is authoritative in that scope.

3. No parallel central process layer
   - Product-local recurring processes remain owned by products/domains.
   - Shared standards should define only genuine cross-product coordination mechanisms.

4. Small front doors, deep owned artifacts
   - Front-door artifacts should be concise and routing-oriented.
   - Detailed instructions should live with the owning artifact or domain.

5. Operability over documentation theater
   - A workspace package is only valid if it improves execution reliability and decision quality.

## Mandatory package components
Every serious workspace should have, at minimum, the following components.

### 1. Workspace profile
Recommended artifact:
- `WORKSPACE_PROFILE.md`

Purpose:
- define workspace purpose
- define owner/stakeholder boundary
- define major consumers/users
- define what the workspace is for and what it is not for

Minimum content:
- workspace name
- purpose
- authority boundary
- primary stakeholders
- major consumed products/capabilities

### 2. Source-of-truth map
Recommended artifact:
- `SOURCE_OF_TRUTH.md`

Purpose:
- make key operating authority explicit

Minimum content:
- where tasks live
- where decisions live
- where official processes live
- where errors/incidents live
- where key status/continuity artifacts live

### 3. Process discovery index
Recommended artifact:
- `PROCESS_DISCOVERY_INDEX.md`

Purpose:
- provide the local front door for finding official process artifacts

This artifact is a locator, not a process encyclopedia.

### 4. Local top-level agent instructions
Recommended artifact:
- local `AGENTS.md` or equivalent

Purpose:
- define top-level local operating rules
- require process discovery before non-trivial operational actions where appropriate
- anchor local approval and boundary behavior

### 5. Error and incident handling path
Recommended artifact:
- local artifact or explicit pointer to the approved standard

Purpose:
- ensure material failures are routed into the intended learning/control loop

### 6. Decision and escalation path
Recommended artifact:
- local artifact or explicit pointer to the approved standard

Purpose:
- make local decision authority and escalation flow explicit

## Optional package components
Depending on workspace maturity and function, a workspace package may also include:
- local runbooks
- local policy packs
- local schema packs
- local ops packs
- local capability manifest
- local readiness scorecard
- local review cadence
- local handover conventions
- local environment/bootstrap notes

## Ownership model
### Lyra OS owns
- workspace package standards
- templates/scaffolds
- bootstrap and retrofit protocols
- package assessment logic

### Products own
- capabilities
- delivery modes
- product-local recurring processes
- downstream consumption interfaces

### Workspaces own
- their local package instance
- their local authority map
- their local process discovery index
- their local adaptations needed for real operation in that workspace

## Minimum viability standard
A workspace should not be treated as operationally mature unless:
- its purpose and authority boundary are explicit
- its main sources of truth are explicit
- official process discovery is explicit
- task/decision/error routes are explicit enough to follow without thread-memory dependence
- major consumed capabilities can be understood from artifacts rather than hidden assumptions alone

## Maturity model
### Level 0 — Ad hoc
- work possible only through thread history and implicit memory
- no reliable front-door operating artifacts

### Level 1 — Minimal
- profile, SoR map, and process discovery front door exist
- major local operating routes are identifiable

### Level 2 — Operable
- key local runbooks/standards exist
- major consumed capabilities are locally understandable
- audit/retrofit gaps are explicit

### Level 3 — Reliable
- package is reviewed and maintained deliberately
- changes are versioned and validated
- major local workflows are resilient to context transfer

## Validation rules
A valid workspace package should:
- avoid duplicating detailed product-local process content centrally
- point to the most specific applicable authoritative artifacts
- distinguish local authority from shared/internal authority
- be small enough to use and explicit enough to reduce ambiguity

## Change rules
Changes to a workspace operating package should be treated as architecture/operating-model changes, not casual note edits, when they alter:
- source-of-truth placement
- process authority
- escalation paths
- major workspace boundaries
- consumer/provider assumptions

## Relationship to bootstrap and retrofit
This standard defines what a workspace package is.
Bootstrap and retrofit protocols define how a package is created, assessed, and upgraded over time.

## Version
- v1.0
- Date: 2026-03-14
- Owner: Lyra OS
