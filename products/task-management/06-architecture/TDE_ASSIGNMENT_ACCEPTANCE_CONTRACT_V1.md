# TDE Assignment Acceptance Contract v1

Status: Draft active
Owner: Peter + Lyra
Product: Task Management (`A-007`)
Date: 2026-03-14
Related:
- `products/task-management/06-architecture/TDE_INTAKE_INTERFACE_CONTRACT_V1.md`
- `products/task-management/errors/ERR-2026-03-14-control-panel-assignment-silent-limbo.md`
- `schemas/tde_assignment_packet/v1.0.0.schema.json`
- `tools/tde_assignment_accept.py`

## Purpose
Define the first thin contract for assignment acceptance into TDE.

This contract exists because a task row appearing in canonical state is not enough to count as operational acceptance.
TDE must be able to distinguish:
- assignment received
- assignment accepted
- assignment accepted but no runner exists
- assignment accepted but binding/policy context is incomplete
- assignment rejected as invalid

## Core rule
Direct task-state insertion does not count as assignment success.

A producer should only treat an assignment as accepted when TDE returns an explicit acceptance result.

## Packet type
Canonical input packet:
- `tde_assignment_packet@1.0.0`

Defined in:
- `schemas/tde_assignment_packet/v1.0.0.schema.json`

## Why this contract is distinct from generic intake
Generic intake answers:
- what work/signal/decision entered TDE?

Assignment acceptance answers:
- did TDE actually accept operational responsibility for this assignment?
- can the current runtime/binding path pick it up?
- what feedback should the producer receive immediately?

## Required result states
At minimum, TDE should return one of:
- `accepted`
- `accepted_no_runner`
- `accepted_pending_binding`
- `rejected_invalid_assignment`
- `duplicate`

Optional later states may include:
- `started`
- `blocked`
- `completed`

## Initial v1 semantics
### `accepted`
Use when:
- assignment packet is valid
- task state can be created/updated canonically
- runtime path has enough binding/policy context for a runner to pick it up normally

### `accepted_no_runner`
Use when:
- assignment packet is valid
- task state can be created/updated canonically
- but no known runner/execution path is currently available

### `accepted_pending_binding`
Use when:
- assignment packet is valid
- task state can be created/updated canonically
- but required binding/policy/objective context is missing or incomplete

### `rejected_invalid_assignment`
Use when:
- packet validation fails
- assignment is malformed
- or required semantics are missing

### `duplicate`
Use when:
- the same stable assignment id has already been accepted with the same content

## Persistence expectations
TDE should persist:
- the raw assignment packet
- the acceptance result
- the created/updated task id where applicable
- any runner/binding/path reason attached to the acceptance state

## Immediate implementation stance
The first thin runtime path may still create/update canonical task rows directly.
But it must no longer leave the producer guessing whether that meant anything operationally.

The acceptance result is therefore the first critical fix, even before full Control Panel adapter work lands.

## Bottom line
A task row is not an acceptance receipt.

The producer needs an explicit assignment result from TDE.
That is the first boundary that prevents silent limbo.
