# Overnight Ledger Task-Layer Representation Trigger — 2026-03-26

Date: 2026-03-26
Owner: Lyra
Selected overnight priority: `CT-2026-03-26-IMPROVEMENT-OVERNIGHT-LEDGER-THIRD-CYCLE`
Linked intake / current work anchor:
- `control/tde-intake/improvement-overnight-ledger-third-cycle-2026-03-26.json`
Prior canonical execution evidence:
- `products/improvement/04-execution/OVERNIGHT_LEDGER_THIRD_CYCLE_DISPOSITION_CHECK_2026-03-26.md`
- `control/runtime/overnight-ledger/2026-03-26.json`

## Purpose
Convert the already-explicit escalation threshold into an inspectable task-layer representation trigger so the 2026-03-26 selected priority ends with a concrete control outcome, not just a warning about future reuse.

## Why this is the right next step
The 2026-03-26 Control Tower synthesis selected Improvement Priority 3 specifically to test third-cycle sufficiency while keeping the anti-inertia rule explicit. That test is now complete:
- the selected priority remained explicit;
- a fresh intake/current-work anchor was created;
- a fresh canonical ledger record exists;
- the third-cycle disposition was published.

At this point, the highest-value authorized next step is not a fourth representation-only restatement. It is to make the promotion condition explicit enough that the next operator can either bind a later reuse to a more concrete downstream proof/closure move or promote the work into stronger task-layer representation without ambiguity.

## Trigger decision
### Decision
Treat the third-cycle result as the **final clean compact-only cycle** for this control.

### Consequence
If the overnight loop selects this same control theme again without a more concrete downstream proof/closure move attached, the operator should **promote it into stronger explicit task-layer representation immediately** rather than recording another representation-only execution note.

## Minimum representation requirement for that promotion
A stronger task-layer representation should, at minimum, make these fields explicit in one canonical work artifact:
1. the selected portfolio priority / synthesis reference;
2. the linked intake/current-work anchor;
3. the concrete downstream proof or closure surface being pursued;
4. the expected closure evidence;
5. the disposition rule for when the promoted item can be retired or folded back into the compact ledger path.

## Explicit bridge from selected priority to next representation rule
- **Selected priority:** `CT-2026-03-26-IMPROVEMENT-OVERNIGHT-LEDGER-THIRD-CYCLE`
- **Current work anchor:** `control/tde-intake/improvement-overnight-ledger-third-cycle-2026-03-26.json`
- **Current canonical ledger:** `control/runtime/overnight-ledger/2026-03-26.json`
- **Current execution evidence:** `products/improvement/04-execution/OVERNIGHT_LEDGER_THIRD_CYCLE_DISPOSITION_CHECK_2026-03-26.md`
- **New concrete execution evidence from this step:** this artifact, which turns the anti-inertia rule into a concrete promotion trigger rather than leaving it implicit in prose elsewhere

## Outcome
The highest-value authorized overnight item advanced one more concrete step: the 2026-03-26 cycle now ends with an explicit task-layer representation trigger, preserving the full selected-priority -> current-work -> execution-evidence chain and making the next threshold operational instead of advisory.

## Peter-facing status
No urgent blocker before morning. The important result is not a decision request; it is that the compact overnight-ledger path now has a crisp stop condition and promotion trigger.