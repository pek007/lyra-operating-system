# PRODUCT_RUNTIME_EMBODIMENT_FRAMEWORK_V1.md

Status: Active draft v1  
Owner: Lyra via Control Panel  
Date: 2026-03-10

## Purpose
Define how Lyra OS products should be embodied at runtime using the right mix of:
- human-guided product management
- Skills
- Cron jobs
- Plugins
- artifacts and evidence

This framework exists to close the gap between:
- product as documented intent
and
- product as deployed operating capability

## Core principle
Do not package behavior just because a mechanism exists.
Package behavior when the product has a repeated operating need that benefits from lower activation cost, higher consistency, or stronger runtime embodiment.

## Embodiment layers

### 1. Human / product-owner layer
Use when:
- judgment is central
- ambiguity is high
- the work is infrequent or strategic
- trade-offs need interpretation

Typical artifacts:
- vision
- goals
- plan
- decisions
- improvement log

### 2. Skill layer
Use when:
- the workflow repeats
- the workflow should be executed consistently
- activation cost is currently too high
- there is a stable reusable operating pattern

Typical examples:
- review/check cycles
- evidence packaging
- coordination routines
- bounded operational procedures

### 3. Cron layer
Use when:
- timing matters
- recurring execution is useful
- the product needs an operating loop without manual prompting
- output can be bounded and low-noise

Typical examples:
- daily/weekly checks
- anti-stall loops
- queue hygiene
- scorecard refresh
- recurring review cycles

### 4. Plugin layer
Use when:
- the capability needs deeper runtime embodiment
- workflows are stable and frequent enough to justify engineering cost
- docs + skills + cron are no longer enough
- the product needs a reusable internal service/capability surface

Typical examples:
- richer memory/retrieval behavior
- coordination/event substrate
- deeper runtime integration surfaces
- reusable product capability APIs

## Product embodiment design questions
For each product, answer:
1. What should stay human/judgment-led?
2. What repeated workflow should become a Skill?
3. What recurring loop should become Cron-driven?
4. What, if anything, might later justify a Plugin?
5. What evidence/output should each layer produce?
6. What should never be embodied in a lighter mechanism because the risk is too high?

## Selection heuristics

### Prefer a Skill when:
- the pattern is repeated more than occasionally
- the procedure is understandable and bounded
- consistency matters more than improvisation
- you want operators to invoke the pattern intentionally

### Prefer Cron when:
- the product needs a standing operating rhythm
- timing matters more than user initiation
- work can run with bounded noise and bounded risk
- the output can be routed or summarized clearly

### Prefer a Plugin only when:
- leverage is high
- repetition is high
- stability is high
- runtime integration need is real
- lower-cost embodiment options have already proven insufficient

## Safety/discipline rules
- Do not use cron to hide ambiguous work that still needs judgment.
- Do not create plugins for unstable processes.
- Do not convert product governance into automation without clear evidence/output expectations.
- Do not let Skills duplicate or bypass canonical system-of-record contracts.
- When a product capability affects other products, define interface/handoff expectations explicitly.

## Required output for each embodied capability
Each packaged capability should define:
- trigger
- owner
- input artifacts
- output/evidence artifacts
- escalation conditions
- review cadence

## Minimal product embodiment template
For each product, define:
- Human-led functions
- Skill candidates
- Cron candidates
- Plugin candidates
- Activation model
- First implementation priority

## Initial portfolio recommendation
Start with Skills and Cron before Plugins.

Recommended first focus:
1. Control Panel
2. Task Management
3. Governance

Reason:
- these are core operating products
- they have clear repeated patterns
- they can produce leverage quickly
- they help the rest of the system operate better

## Version
- v1.0
- Date: 2026-03-10
