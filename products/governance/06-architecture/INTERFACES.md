# Interfaces

## Upstream interfaces
- governance records and portfolio artifacts

## Downstream interfaces
- shared rules, decision-rights logic, and boundary constraints applied across products
- adopted governance artifacts consumed by downstream workspaces such as `pxs`
- governance assembly consumers and reviewers
- shared policy/compliance consumers using local workspace authority surfaces to adopt Governance-defined policies

## Shared policy distribution rule
When Governance defines a shared policy family that is intended to apply across Lyra OS and downstream workspaces, the rollout path should be:
1. explicit capability anchoring in the Governance product model
2. canonical policy/standard artifacts under Governance
3. downstream adoption through the consuming workspace operating package (`SOURCE_OF_TRUTH.md`, `PROCESS_DISCOVERY_INDEX.md`, local `AGENTS.md`, and related authority surfaces)
4. selective validation/evidence loops where machine-checkability is worth the cost
5. runtime/config/plugin enforcement where bypass would create unacceptable risk

This keeps policy application explicit, localizable, and governable rather than assuming a central artifact automatically becomes operational everywhere.

## Product vs assembly relationship
Governance must answer two related but different questions clearly:
- product state: what Governance is trying to achieve now as a product
- assembly state: what Governance v0.1 exports for downstream adoption

These should remain linked but not conflated.

## Workspace package implication
When Governance is consumed in a downstream workspace, the consumer should have enough local operating-package structure to make governance authority usable locally.
That typically means explicit local front doors for:
- source-of-truth
- process discovery
- decision/escalation

Governance should shape those routes, not replace the workspace's local operating package.

## Minimum improvement interface
### Governance -> Improvement interface
- governance operating-model drift, completed proof-case retirement misses, and recurring protocol/authority ambiguity must not remain prose-only observations
- when those gaps are material or repeated, Governance should route them into canonical TDE-linked improvement work rather than a parallel tracker
- the linked improvement intake should carry `source_system`, `source_reference`, `product_scope`, `evidence_links`, `improvement_type`, and `expected_closure_evidence`
- closure requires linked evidence plus explicit source-to-closure trace
- open Governance-origin improvement items should remain visible in recurring product review until dispositioned or closed

### First bounded deployment rule
- initial deployment scope for the minimum product-side improvement interface is completed proof-case retirement and durable protocol formalization
- seed reference: `OPS-2026-068`
- canonical path: Governance review/protocol surfaces detect the hygiene gap; TDE holds the task state; Improvement governs the source-to-closure discipline

## Key boundary rule
Governance owns system-level rules and coordination constraints, not the internal day-to-day operating processes of each product.
