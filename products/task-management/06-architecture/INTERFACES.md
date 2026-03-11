# Interfaces

## Purpose
Define how Task Management interacts with upstream governance/runtime elements and downstream consumers.

## Upstream interfaces
### Governance
Provides:
- policy and boundary conditions
- readiness and evidence expectations
- escalation rules for material changes

### Lyra runtime
Provides:
- agent execution environment
- jobs, sessions, memory, and operating context
- automation pathways for product execution

### TDE contract artifacts
Provide:
- intake/output expectations
- task/decision operating semantics
- readiness and evidence patterns

## Downstream interfaces
### `pxs` workspace
Consumes:
- task/decision management capability
- operating patterns and delivery mechanisms
- future explicit interfaces for invoking or embedding product functionality

## Current interface problems
- some boundaries are still documented indirectly across multiple artifacts
- some product behavior still depends on workspace context rather than explicit contracts
- downstream consumption path is clear strategically but not yet fully formalized operationally

## Interface design rules
1. No hidden cross-workspace coupling.
2. Product responsibilities must be explicit.
3. Consumer adoption should rely on documented interfaces, not tribal knowledge.
4. Where possible, prefer stable contracts over chat-history assumptions.

## Named downstream interface
### `pxs` consumption interface
Canonical artifact:
- `06-architecture/PXS_CONSUMPTION_INTERFACE.md`

This interface defines:
- what `pxs` consumes from Task Management
- what remains internal to the product
- consumer obligations
- provider obligations
- what evidence makes the interface operationally usable

## Next interface work
- map current TDE artifacts to the product interface surface
- add clearer operational examples for `pxs` usage
- decide whether a capability-pack or service boundary is the better long-term distribution shape
