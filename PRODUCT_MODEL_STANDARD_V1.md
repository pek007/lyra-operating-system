# Product Model Standard v1

Status: Draft active standard
Owner: Peter / Lyra
Date: 2026-03-11
Reference implementation: `products/task-management/`

## Purpose
Define the canonical Product-as-Code standard for PX Strategy products.

The aim is to make each product an explicit, versioned, inspectable management model rather than a loose collection of markdown files. The standard should improve product clarity, agent usability, governance discipline, and portfolio consistency without creating unnecessary bureaucracy.

## Design principle
Use a hybrid model:
- markdown for explanation, judgment, and operational thinking
- lightweight structured metadata for consistency, automation, and validation

This means every product should have:
1. a human-facing front door
2. a machine-readable model
3. a small set of typed artifacts with distinct jobs

## Core idea
A product is not just a backlog or a folder.
A product is a managed system consisting of:
- identity
- strategy
- operating model
- execution model
- performance model
- interface model
- decision memory

Products are the producer-side unit in the architecture.
They define capabilities, interfaces, and delivery choices.
Downstream workspaces are the consumer-side unit of local operation.
Those workspaces should be treated as Workspace Operating Packages: local assembled environments that make consumed product capabilities usable through explicit sources of truth, process discovery, and operating routes.

Product-as-Code should therefore be read together with:
- delivery-mode selection for how capabilities are distributed
- workspace operating package design for how capabilities are actually consumed in a local scope

## Standard folder structure
Each product should live at:
`products/<slug>/`

Recommended structure:

```text
products/<slug>/
  PRODUCT.md
  MODEL.yaml

  01-identity/
    VISION.md
    CUSTOMER.md

  02-strategy/
    STRATEGY.md
    DISTRIBUTION_MODEL.md

  03-operating-model/
    OPERATING_MODEL.md
    GOVERNANCE.md

  04-execution/
    ROADMAP.md
    PLAN.md
    RISKS.md

  05-performance/
    METRICS.md

  06-architecture/
    INTERFACES.md

  07-decisions/
    DECISIONS.md
```

Optional extensions may add more files, but the core structure should remain stable.

## Mandatory artifacts
Every PX product should have these artifacts.

### 1. `PRODUCT.md`
Purpose:
- human-facing front door to the product
- quick orientation for both humans and agents

Must contain:
- product identity
- purpose
- why it matters
- scope
- link/list of canonical model artifacts
- current mandate or focus

### 2. `MODEL.yaml`
Purpose:
- machine-readable product backbone
- canonical metadata for automation and agent reasoning

Must contain at least:
- id
- slug
- name
- owner
- type
- status
- lifecycle
- domain
- purpose
- users
- strategic role
- dependencies
- artifacts
- metrics summary
- review cadence

### 3. `01-identity/VISION.md`
Purpose:
- define the future state the product exists to create

### 4. `01-identity/CUSTOMER.md`
Purpose:
- define who the product serves and what jobs they need done

### 5. `02-strategy/STRATEGY.md`
Purpose:
- capture the product’s core strategic choices
- define what it is optimizing for and what it is deliberately not optimizing for

### 6. `02-strategy/DISTRIBUTION_MODEL.md`
Purpose:
- define how the product gets adopted or consumed
- for internal products, this means enablement/adoption/distribution into consuming environments
- make explicit what a downstream workspace must receive or instantiate in order to consume the product coherently, including any required workspace-package implications

### 7. `03-operating-model/OPERATING_MODEL.md`
Purpose:
- define how the product runs, improves, and is managed over time

### 8. `03-operating-model/GOVERNANCE.md`
Purpose:
- define controls, escalation conditions, and review model

### 9. `04-execution/ROADMAP.md`
Purpose:
- define the sequence of meaningful changes over time

### 10. `04-execution/PLAN.md`
Purpose:
- define the current planning horizon and active workstreams

### 11. `04-execution/RISKS.md`
Purpose:
- define current strategic, operational, and adoption risks

### 12. `05-performance/METRICS.md`
Purpose:
- define success, health, and guardrail metrics

### 13. `06-architecture/INTERFACES.md`
Purpose:
- define upstream and downstream interfaces, dependencies, and boundary rules

### 14. `07-decisions/DECISIONS.md`
Purpose:
- define the major product decisions and preserve rationale outside chat history

## Optional artifacts
These are allowed when they clearly add decision value.
They should not be added by default unless the product needs them.

Examples:
- `MISSION.md`
- `VALUE_PROPOSITION.md`
- `POSITIONING.md`
- `BUSINESS_MODEL.md`
- `DELIVERY_MODEL.md`
- `DECISION_RIGHTS.md`
- `RITUALS.md`
- `GOALS.md`
- `BACKLOG.md`
- `KPI_TREE.md`
- `HEALTH.md`
- `CAPABILITIES.md`
- `DEPENDENCIES.md`
- `STACK.md`
- `MEMORY.md`
- `HANDOVER.md`
- ADR subfolder under `07-decisions/`

## Artifact design rules

### Rule 1: one artifact, one job
Each file should have a clear role. Do not mix vision, governance, roadmap, and daily plan in the same document.

### Rule 2: product artifacts must drive decisions
If an artifact does not support prioritization, ownership, readiness, review, or learning, it is probably not worth keeping.

### Rule 3: separate durable from volatile
Usually:
- durable: vision, customer, strategy, operating model, governance, interface model
- more volatile: roadmap, plan, risks, metrics narrative

### Rule 4: use linking rather than duplication
A product model should behave like a system, not a pile of repeated text.

### Rule 5: internal products still need distribution
For internal products, distribution means adoption into real operating environments and workflows.

### Rule 6: product boundaries must stay explicit
A product may interact with governance, runtime, and other products, but those interfaces should be documented rather than assumed.

### Rule 7: products own their own recurring processes
Recurring operating processes should normally be owned and defined inside the product model unless they are genuinely cross-product coordination mechanisms. Avoid creating central/shared artifacts that duplicate product-owned process logic.

### Rule 8: product distribution must account for workspace consumption
A product is not fully specified if it defines capability and delivery mode but leaves the downstream workspace operating package implicit. Product models should make clear what local consumer-side artifacts, routes, or package components are required for successful adoption and operation.

## Canonical metadata schema
`MODEL.yaml` should follow this shape:

```yaml
id: string
slug: string
name: string
type: internal | external | platform | service | capability
owner: string
status: active | paused | retired | discovery
lifecycle: concept | incubation | scaling | mature | sunset

domain: OS | PX
purpose: string

users:
  primary: []
  secondary: []

strategic_role:
  portfolio_role: core | enabling | experimental | support
  linked_company_goals: []

value_logic:
  creates_value_by: []
  captures_value_by: []
  success_conditions: []

operating_model:
  cadence: string
  planning_horizon: string
  release_mode: string
  governance_level: low | medium | high

dependencies:
  upstream: []
  downstream: []
  critical_constraints: []

artifacts:
  product: path
  vision: path
  customer: path
  strategy: path
  operating_model: path
  governance: path
  distribution_model: path
  roadmap: path
  plan: path
  risks: path
  metrics: path
  interfaces: path
  decisions: path

metrics:
  north_star: []
  health: []
  guardrails: []

review:
  review_cadence: string
  last_reviewed: YYYY-MM-DD
```

## Review and maintenance rules
Each product owner should keep the model alive enough that they can answer, at minimum:
- What is this product for?
- Who does it serve?
- What is the current strategy?
- What is the current plan?
- What are the main risks?
- How is success judged?
- What interfaces and dependencies matter?
- What has already been decided?

Minimum expected upkeep:
- `PLAN.md`: refresh when the near-term plan materially changes
- `RISKS.md`: refresh when a meaningful risk changes or is discovered
- `ROADMAP.md`: refresh when sequence or major bets change
- `METRICS.md`: refresh when product health logic changes materially
- `MODEL.yaml`: refresh when ownership, lifecycle, dependencies, or artifact set changes
- `PRODUCT.md`: refresh when front-door orientation is stale

## Relationship to portfolio and company model
The Product Model Standard sits below Company-as-Code and portfolio governance.

Hierarchy:
- Company model
- Portfolio model
- Product models
- Capability/process/runtime models

This means a product model should inherit strategic direction and governance constraints from the company level while defining how one product creates value and operates in practice.

## Reference implementation
The first reference implementation is:
- `products/task-management/`

It should be used as the practical benchmark for what the standard means in real use.

## Adoption recommendation
Roll this standard out in two stages:
1. use Task Management as the proving ground and refine the standard from actual use
2. apply the standard across the remaining products with lightweight adaptation, not blind cloning

## Non-goal
This standard does not require every product to become elaborate. The goal is clarity and control, not document inflation.
