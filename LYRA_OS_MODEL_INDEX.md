# Lyra OS Model Index

Status: Active (v1)
Owner: Lyra OS
Date: 2026-03-26

## Purpose
Provide a front door to the Lyra OS Model as the canonical Model-as-Code layer for the system.

Use this artifact when the task is about:
- system-level design authority
- cross-product or cross-runtime design decisions
- portfolio ontology and capability classification
- delivery and consumption design across the system
- runtime operating design
- governance/authority design
- promotion of recurring learning into system-level model change

## Canonical model artifacts
- `LYRA_OS_MODEL_V1.md`
- `LYRA_OS_STRATEGY_MODEL_V1.md`
- `LYRA_OS_PORTFOLIO_AND_CAPABILITY_MODEL_V1.md`
- `LYRA_OS_RUNTIME_AND_OPERATING_MODEL_V1.md`
- `LYRA_OS_GOVERNANCE_AND_AUTHORITY_MODEL_V1.md`
- `LYRA_OS_DELIVERY_AND_CONSUMPTION_MODEL_V1.md`
- `LYRA_OS_LEARNING_AND_EVOLUTION_MODEL_V1.md`

## Use rule
Use the Lyra OS Model when the work would otherwise rely on implicit system design assumptions.

If the question is primarily:
- product-local -> start with the relevant product artifacts
- workspace-local -> start with the relevant workspace package artifacts
- process-local -> start with the owning process artifact
- system-design / cross-model / cross-product / cross-runtime -> start here

## Relationship to other layers
- Model-as-Code: system design authority
- Product-as-Code: capability definition and operation
- Workspace Operating Package: downstream local operation
- Runtime loops: operating mechanisms running within the Model
- Knowledge/evidence/improvement artifacts: learning inputs and promotion candidates for Model evolution

## Change rule
Use `MODEL_CHANGE_PROTOCOL_V1.md` for proposing, reviewing, and accepting model-impacting changes.
