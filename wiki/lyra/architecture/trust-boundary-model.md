# Trust Boundary Model

Status: draft wiki page
Date: 2026-04-03
Domain: Architecture

## Summary
The trust boundary model explains where Lyra should treat content, actions, users, systems, or runtimes as within or outside a given trust boundary.

## Why it matters
Architecture and security are tightly linked here. A runtime or workflow is not safe just because it works technically; it also depends on whether trust assumptions are explicit and valid.

## Architectural role
The trust boundary model shapes:
- channel bindings
- runtime authority
- approval expectations
- shared vs personal runtime assumptions
- credential exposure risk
- multi-user vs single-user operating assumptions

## Current practical understanding
Lyra currently operates in an environment that is primarily designed around a personal-assistant trust model, but some surfaces show shared or multi-user characteristics. That makes boundary clarity more important, not less.

## Key implications
- mixed-trust environments need stronger separation
- broad runtime authority is riskier in shared-boundary contexts
- external content and external actions should be evaluated through trust-boundary logic, not only convenience

## Related pages
- [Runtime Model](./runtime-model.md)
- [Prompt Injection Defense](../controls-security/prompt-injection-defense.md)
- [Operational Truth vs Compiled Knowledge Boundary](../governance-authority/operational-truth-vs-compiled-knowledge-boundary.md)
