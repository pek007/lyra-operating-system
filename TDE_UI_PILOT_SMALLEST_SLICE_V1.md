# TDE UI Pilot Smallest Slice v1

Status: Draft active
Owner: Peter / Lyra
Date: 2026-03-12
Related pilot: `ONE_ITERATION_TDE_UI_PILOT_V1.md`
Related Delivery contract: `products/delivery/04-execution/TDE_UI_PILOT_DELIVERY_CONTRACT_V1.md`
Related Task Management note: `products/task-management/04-execution/TDE_UI_PILOT_SCOPE_ALIGNMENT_NOTE_V1.md`

## Purpose
Define the smallest acceptable GUI slice for iteration one of the TDE UI pilot.

This artifact exists to force a real scope boundary before implementation broadens by default.

## Operator problem to solve
The first operator problem is:

**An operator cannot yet see canonical TDE state, blockers, and decision-needs through a simple graphical surface that is usable enough to support real operational judgment.**

The first slice does not need to solve full TDE interaction.
It needs to make the current operational picture visible enough to support real use.

## Smallest acceptable slice
The smallest acceptable slice for iteration one is a **read-first operator view** that:
1. displays canonical TDE items from the current canonical source,
2. shows basic status/state for those items,
3. surfaces blocked items and explicit decision-needs where available,
4. is deployable in a real runtime/environment,
5. is usable for one narrow real operator purpose.

## Narrow real operator purpose
For iteration one, the narrow real operator purpose should be:

**Allow the operator to inspect the current TDE work picture and quickly identify what is active, what is blocked, and what appears to require a decision.**

That purpose is intentionally diagnostic and operational rather than broadly managerial.

## Included in scope
Iteration one should include only what is needed to satisfy the narrow operator purpose:
- a basic graphical screen/view,
- rendering of canonical TDE items,
- visible item state/status,
- visible blocked/decision-needed signals if present in the source or derived view,
- enough deployment/release work to count as a real production slice,
- enough verification to support an explicit readiness decision.

## Explicit non-goals
Iteration one should not attempt to include:
- broad write/edit workflows,
- generalized task creation or workflow mutation,
- full role-based product portfolio views,
- rich analytics/reporting,
- advanced filtering and customization,
- polished design-system work beyond basic usability,
- a final long-term UI architecture for TDE,
- solving all multi-product orchestration inside the UI.

## Initial decision set required before implementation
Before implementation begins in earnest, the pilot should make these decisions explicit:
1. **Canonical source decision** — what exact TDE source/view will the GUI read from?
2. **Decision-needed signal decision** — what counts as a visible decision-needed signal in iteration one?
3. **Blocked-state decision** — how will blocked items be represented from the current source?
4. **Deployment target decision** — what real runtime/environment counts as production for this slice?
5. **Release evidence decision** — what minimum verification/readiness evidence is required before release?

## Minimum evidence expectations
At minimum, iteration one should produce evidence that:
- the GUI reads from the intended canonical source,
- the main view reflects current state consistently enough to be operationally useful,
- blocked and decision-needed signals are visible according to the agreed interpretation,
- the slice is deployed in the agreed target environment,
- a release/readiness decision was made explicitly rather than implied.

## Boundary logic
This slice is intentionally read-first because it tests the most important early question first:

**Can Lyra OS turn canonical TDE state into a usable operator surface with explicit delivery and decision discipline?**

If that answer is weak, broader interaction scope would only hide the more important gap.

## Current recommendation
Proceed with iteration one as a read-first operational inspection slice.

Do not expand into write-heavy or architecture-heavy ambition until the system proves it can:
- define a smallest slice,
- ship it,
- verify it,
- and release it with a clean audit trail.
