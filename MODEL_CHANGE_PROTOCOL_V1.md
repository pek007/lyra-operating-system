# Model Change Protocol v1

Status: Draft protocol
Owner: Lyra OS / Control Panel
Date: 2026-03-26

## Purpose
Define a lightweight protocol for proposing, reviewing, and applying model-impacting changes in Lyra OS.

This protocol exists to prevent the Lyra OS Model from either:
- drifting silently through local edits and operating habit, or
- becoming static because no one knows how to change it safely.

## Scope
Use this protocol when a change materially affects:
- strategic direction
- governance or authority logic
- portfolio and capability ontology
- delivery and consumption design
- runtime and operating design
- learning and evolution design

## Core rule
If the change would alter how Lyra OS is designed to work across the system, treat it as a model-impacting change.

## Inputs that may trigger a model change
- product review findings
- workspace retrofit/adoption friction
- runtime-loop learning
- error reports / corrective actions
- repeated local adaptations
- governance ambiguity
- architecture or portfolio design tension
- explicit strategic decision

## Change classes
### Class M1 — Clarifying
- improves wording, structure, or explicitness
- no meaningful design/authority delta

### Class M2 — Design-impacting
- changes intended system behavior, operating design, or capability ontology
- requires explicit review and decision recording

### Class M3 — Governance/boundary-impacting
- changes authority logic, control posture, or major architectural boundaries
- requires strongest review posture and explicit acceptance

## Minimum change flow
1. Detect candidate change
2. Record candidate in the most relevant surface (product, workspace, runtime, or Control Panel review)
3. Decide whether it is model-impacting
4. If yes, create/update a model change proposal
5. Review under Control Panel / relevant governing authority
6. Record decision
7. Update Model artifacts if accepted
8. Propagate any required product/workspace/process changes

## Minimum proposal content
A model change proposal should include:
- title
- trigger / evidence
- proposed change
- affected model artifacts
- why this matters
- impact scope
- next step / review need

## Decision rule
A model change should not be considered accepted merely because it appears in a local artifact or runtime behavior.

Acceptance requires:
- explicit review
- explicit decision or approved update
- update to the relevant canonical model artifact(s)

## Propagation rule
If a model change is accepted, check whether any of the following also need updating:
- product artifacts
- workspace operating package artifacts
- process artifacts
- runtime loop prompts or control surfaces
- knowledge or review references

## Ownership
Control Panel owns the operator-facing stewardship of the Lyra OS Model and should help:
- surface model drift
- route model change proposals
- maintain model review visibility
- keep the relationship between runtime reality and model authority explicit

Detailed domain substance may still be owned by more specific products or governing artifacts.
