# Product Model Template Pack v1

Use this template pack when creating a new product model under `products/<slug>/`.

---

## `PRODUCT.md`

```md
# <Product Name>

- Product ID: `<ID>`
- Product name: `<Name>`
- Owner: `<Owner>`
- Domain: `<OS|PX>`
- Type: `<Internal|External|Platform|Service|Capability>`
- Status: `<Active|Paused|Retired|Discovery>`

## Purpose
<Why this product exists>

## Why this product matters
<Why it matters in the broader company/portfolio context>

## Scope
This product includes:
- ...

## Product model
Canonical product model artifacts:
- `MODEL.yaml`
- `01-identity/VISION.md`
- `01-identity/CUSTOMER.md`
- `02-strategy/STRATEGY.md`
- `02-strategy/DISTRIBUTION_MODEL.md`
- `03-operating-model/OPERATING_MODEL.md`
- `03-operating-model/GOVERNANCE.md`
- `04-execution/ROADMAP.md`
- `04-execution/PLAN.md`
- `04-execution/RISKS.md`
- `05-performance/METRICS.md`
- `06-architecture/INTERFACES.md`
- `07-decisions/DECISIONS.md`

## Current mandate
- ...

## Current focus
1. ...
```

---

## `MODEL.yaml`

```yaml
id: <ID>
slug: <slug>
name: <name>
type: internal
owner: <owner>
status: active
lifecycle: incubation

domain: OS
purpose: >
  <purpose>

users:
  primary:
    -
  secondary:
    -

strategic_role:
  portfolio_role: enabling
  linked_company_goals:
    -

value_logic:
  creates_value_by:
    -
  captures_value_by:
    -
  success_conditions:
    -

operating_model:
  cadence: <cadence>
  planning_horizon: <planning horizon>
  release_mode: <release mode>
  governance_level: medium

dependencies:
  upstream:
    -
  downstream:
    -
  critical_constraints:
    -

artifacts:
  product: PRODUCT.md
  vision: 01-identity/VISION.md
  customer: 01-identity/CUSTOMER.md
  strategy: 02-strategy/STRATEGY.md
  operating_model: 03-operating-model/OPERATING_MODEL.md
  governance: 03-operating-model/GOVERNANCE.md
  distribution_model: 02-strategy/DISTRIBUTION_MODEL.md
  roadmap: 04-execution/ROADMAP.md
  plan: 04-execution/PLAN.md
  risks: 04-execution/RISKS.md
  metrics: 05-performance/METRICS.md
  interfaces: 06-architecture/INTERFACES.md
  decisions: 07-decisions/DECISIONS.md

metrics:
  north_star:
    -
  health:
    -
  guardrails:
    -

review:
  review_cadence: <cadence>
  last_reviewed: YYYY-MM-DD
```

---

## `01-identity/VISION.md`

```md
# Vision

<What future this product exists to create>
```

## `01-identity/CUSTOMER.md`

```md
# Customer

## Primary customers
- ...

## Secondary customers
- ...

## Jobs to be done
- ...
```

## `02-strategy/STRATEGY.md`

```md
# Strategy

## Strategic objective
...

## Strategic choices
1. ...

## What we are optimizing for
- ...

## What we are not optimizing for yet
- ...

## Current strategic risks
- ...
```

## `02-strategy/DISTRIBUTION_MODEL.md`

```md
# Distribution Model

## Primary distribution path
...

## Adoption model
1. ...

## Distribution mechanisms
- ...

## Workspace consumption requirements
- What must a downstream workspace receive, adopt, or instantiate locally?
- Are there required operating-package artifacts, local front doors, or adopted assemblies?
```

## `03-operating-model/OPERATING_MODEL.md`

```md
# Operating Model

## Product owner
...

## Mandate
- ...

## Core loops
- reliability loop
- adoption loop
- governance loop
```

## `03-operating-model/GOVERNANCE.md`

```md
# Governance

## Governance posture
...

## Core governance controls
- ...

## Escalation triggers
- ...
```

## `04-execution/ROADMAP.md`

```md
# Roadmap

## Horizon 1
...

## Horizon 2
...
```

## `04-execution/PLAN.md`

```md
# Current Plan

## Current objectives
1. ...

## Current workstreams
### Workstream 1
- ...
```

## `04-execution/RISKS.md`

```md
# Risks

### R-001 — <risk name>
- Description:
- Consequence:
- Mitigation:
```

## `05-performance/METRICS.md`

```md
# Metrics

## North star
...

## Health metrics
- ...

## Guardrails
- ...
```

## `06-architecture/INTERFACES.md`

```md
# Interfaces

## Upstream interfaces
- ...

## Downstream interfaces
- ...

## Interface design rules
1. ...
```

## `07-decisions/DECISIONS.md`

```md
# Decisions

### D-001 — <decision>
- Decision:
- Why it matters:
```
```
