# Delivery Research Domain Map

Status: Active
Product: Delivery (`A-006`)
Owner: Lyra
Date: 2026-03-15

## Purpose
Define the full domain surface Delivery should monitor so the product stays broad enough to avoid blind spots while concentrating depth only where decision value is highest.

## Scope rule
Default posture:
- broad watch across the full relevant delivery surface
- deeper work in a few currently critical themes
- explicit acknowledgment of out-of-focus areas rather than silent omission

## Domain map

### Core domains
1. **Delivery-as-Code architecture and controls**
   - delivery units, canonical state, rendered outputs, policy binding, lifecycle control

2. **Verification and release-readiness design**
   - acceptance logic, verification surfaces, promotion rules, pass/fail semantics

3. **Evidence packaging, traceability, and auditability**
   - evidence packs, proof surfaces, decision traceability, inspectable delivery records

4. **Gate contracts, policy binding, and state transitions**
   - machine-checkable gates, transition guards, workflow discipline, deterministic criteria

5. **Rollback, recovery, and change safety**
   - rollback credibility, blast-radius control, recovery expectations, narrow change discipline

6. **Delivery metrics, review loops, and improvement systems**
   - scorecards, feedback loops, recurring review, improvement based on evidence rather than anecdote

### Adjacent domains
7. **Deployment and rollout patterns for consuming environments**
   - consumption into PXS and similar environments, adoption friction, operational distribution

8. **Developer-agent-and-runtime collaboration models**
   - assigned work, handoff, workflow orchestration, role boundaries, autonomous execution constraints

9. **Supply-chain and build-pipeline risk relevant to delivery**
   - dependency trust, build integrity, automation safety, release-surface security implications

10. **External practices material to AI-native software delivery**
    - emerging release, verification, and operations patterns relevant to AI-agent environments

### Peripheral-but-relevant domains
11. **General software-delivery commentary without architectural implications**
12. **Large-scale enterprise CI/CD patterns not yet relevant to our operating model**
13. **Compliance detail not yet connected to delivery controls or evidence requirements**

## Current priority themes for depth
1. **End-to-end Delivery v0.1 pilot proof**
2. **Gate contract hardening**
3. **Delivery scorecard and review operationalization**

## Out-of-focus but watched
- broad DevOps trend chatter without clear implications
- tooling news that does not affect our control/evidence model
- process fashions that add ceremony without stronger delivery outcomes

## Review rule
Reassess this domain map monthly or whenever a major product, runtime, or deployment change suggests the current scope is too narrow or misweighted.
