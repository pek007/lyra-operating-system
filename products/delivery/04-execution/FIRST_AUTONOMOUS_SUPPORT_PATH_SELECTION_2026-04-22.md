# First Autonomous Support Path Selection

Date: 2026-04-22
Owner: Lyra
Status: Selected

## Purpose
Convert the Delivery / TDE / PXS Tools integration initiative from rich but still-open design into one explicit first thin-slice autonomous support path.

## Selected first path
The first thin-slice autonomous support path is:

**Delivery-governed evidence-completeness gate + TDE-tracked execution-support loop for a bounded internal PXS Tools slice.**

## Why this path first
This path is selected first because it is the thinnest realistic autonomous-support move that:
- is strategically central to the Delivery / TDE / PXS Tools integration objective
- exercises real workflow progression rather than only producing more design notes
- aligns directly with `MINIMUM_AUTONOMOUS_DELIVERY_LOOP_V0_1_2026-04-03.md`
- does not depend on premature autonomous coding or a generalized workflow engine
- can reduce repeated procedural prompting even before full implementation-lane automation exists

## What the path includes
The selected path covers only the bounded support loop around a real internal slice:
1. bounded slice trigger appears
2. required artifact/evidence expectations are recognized automatically
3. kickoff/support state is explicit in TDE
4. Delivery checks evidence completeness with explicit pass/fail output
5. unresolved gaps become explicit follow-up state rather than chat-memory residue
6. the cycle ends with a compact evidence packet and a clear completion/follow-up judgment

## What is explicitly out of scope
This first path does **not** mean:
- autonomous software development in the broad sense
- generalized workflow-engine behavior
- autonomous architecture judgment
- replacing human scope/go-no-go decisions
- proving all of Delivery, TDE, or PXS Tools integration at once

## First proving-case rule
The first proving case should be:
- internal
- bounded
- low-blast-radius
- capable of producing code/change + verification/evidence output
- small enough that the support loop can be tested without depending on a heavy or manual 3PP implementation lane

If CRM remains the intended proving case, the implementation target repo must be present and analyzed before implementation begins.

## Pass condition for the first test
This first autonomous-support path counts as validated only if one real bounded slice moves through:
- explicit kickoff/support state
- explicit verification capture
- Delivery evidence-completeness check
- explicit evidence packet
- explicit completion/follow-up judgment

## Failure condition
The first test should be treated as failed or incomplete if:
- the loop still depends on repeated manual “ok do that” progression for routine steps
- evidence completeness is implied rather than checked
- unresolved issues remain prose-only rather than explicit state
- the implementation target is missing or unknown and the loop pretends otherwise

## Recommended next move
Use this selection as the canonical narrowing decision, then choose one actual bounded internal PXS Tools slice and run the first test of the support loop against it.

## Bottom line
The initiative is no longer blocked by lack of design.
It is now explicitly narrowed to one first autonomous support path: **evidence-completeness + TDE-tracked support state for a bounded internal slice.**
