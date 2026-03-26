# Overnight Ledger Representation Decision Step — 2026-03-24

Date: 2026-03-24
Owner: Lyra
Selected overnight priority: `CT-2026-03-24-IMPROVEMENT-OVERNIGHT-LEDGER`
Linked intake / current work anchor:
- `control/tde-intake/improvement-overnight-ledger-activation-2026-03-24.json`

## Why this step was selected now
The top overnight item has already been activated, linked into the live ledger path, and reflected in the Improvement execution surface. The next bounded gap is representational rather than strategic: decide whether first-cycle overnight-ledger work is currently represented honestly enough through the Control Tower selection + linked intake/current-work anchor + canonical ledger path, or whether a distinct active TDE runtime row is already required to keep the control surface trustworthy.

## Inputs checked
- Policy / bridge: `CONTROL_TOWER_OVERNIGHT_SYNTHESIS_POLICY_V1.md`
- Portfolio decision artifact: `control/CT-OVERNIGHT-SYNTHESIS-2026-03-24.md`
- Linked intake / current work anchor: `control/tde-intake/improvement-overnight-ledger-activation-2026-03-24.json`
- Live compact control record: `control/runtime/overnight-ledger/2026-03-24.json`
- Prior execution evidence: `products/improvement/04-execution/OVERNIGHT_LEDGER_ACTIVATION_STEP_2026-03-24.md`, `products/improvement/04-execution/OVERNIGHT_LEDGER_RUNTIME_LINKAGE_STEP_2026-03-24.md`, `products/improvement/04-execution/OVERNIGHT_LEDGER_LIVE_APPLICATION_STATUS_2026-03-24.md`
- Current canonical runtime projection: `os/runtime/TASKS_from_db.md`
- Minimum control standard and contract: `OVERNIGHT_LOOP_MINIMUM_PERFORMANCE_STANDARD_V1.md`, `OVERNIGHT_LOOP_LEDGER_CONTRACT_V1.md`
- Improvement execution surface: `products/improvement/04-execution/PLAN.md`

## Decision for this cycle
For the first live overnight-ledger cycle, the honest and sufficient representation is still:

Control Tower selected priority -> linked intake/current-work anchor -> canonical overnight ledger entry -> execution evidence notes -> Improvement plan surface.

A separately materialized active TDE runtime row is **not yet required** for this first cycle because:
1. the selected priority is explicit and current, not inferred;
2. the intake packet already supplies the missing current-work anchor;
3. the canonical ledger path is live and inspectable;
4. the current evidence chain makes the absence of a distinct active row explicit instead of hiding it.

## Trigger for stronger task-layer representation
Escalate to a stronger explicit task-layer representation if any of the following becomes true on later cycles:
1. the same overnight-ledger work is reused across repeated cycles but remains hard to identify from the canonical runtime projection alone;
2. the evidence chain stops being compact enough to inspect without rereading multiple narrative notes;
3. a later cycle cannot state the selected-priority -> current-work link plainly using the intake-linked control record;
4. closure / maintenance semantics start to matter enough that recurring work is being silently reopened or hand-waved.

## Concrete change executed
Updated the live overnight ledger record so the execution-loop stage now points to this representation-decision note as the current strongest evidence artifact, and so the blocker language reflects a narrower and more truthful remaining gap: morning brief still pending, but first-cycle representation is now explicit rather than undecided.

## Outcome
The overnight-ledger work now has a stated representation rule for the first live cycle. That keeps the link explicit from selected priority -> current work -> execution evidence, while avoiding premature inflation into a stronger task-layer structure before repeated use demonstrates that it is needed.

## Next bounded follow-through
Reuse the same canonical ledger path on the next overnight cycle and check whether this first-cycle representation rule still holds cleanly after another live pass. If not, promote the representational gap into explicit task-layer follow-up rather than allowing silent ambiguity.
