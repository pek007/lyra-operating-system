# First Autonomous Support Path Test-Case Selection

Date: 2026-04-22
Owner: Lyra
Status: Selected
Related narrowing decision: `products/delivery/04-execution/FIRST_AUTONOMOUS_SUPPORT_PATH_SELECTION_2026-04-22.md`

## Purpose
Choose the first actual bounded test case for the selected autonomous support path.

## Selected test case posture
The first test case should be:

**one bounded internal PXS Tools slice whose implementation target is present, inspectable, low-blast-radius, and capable of producing explicit verification/evidence output.**

## Selection rule
The first test case must satisfy all of the following:
- internal implementation path available now
- actual implementation repo/module is present and inspectable before start
- bounded enough to avoid broad architecture ambiguity
- capable of generating code/change + verification/evidence output
- low enough risk that the support loop can be tested honestly
- small enough that repeated manual orchestration would be visible as waste

## Immediate exclusion rule
A candidate should **not** be selected as the first test case if:
- the real implementation repo is not present
- the implementation target is unknown
- the change depends on heavy manual 3PP handoff to begin
- the slice is broad enough that architecture judgment dominates the test

## Current judgment on CRM
CRM remains a strategically plausible proving case, but it is **not yet the selected first test case** because the actual implementation target repo (`pxs-crm`) is not currently present in the visible workspace and therefore has not yet been analyzed.

That means CRM is currently:
- valid as a candidate
- invalid as the immediate first execution test until repo access and codebase inspection are real

## Recommended first test-case search order
1. bounded internal PXS Tools slice with codebase already present and inspectable
2. reversible maintenance/fix or low-blast-radius implementation slice
3. capable of explicit verification and evidence output without broad product ambiguity
4. only then, if nothing else is cleaner, revisit CRM once `pxs-crm` is present and analyzed

## Pass condition for test-case selection
The first test case is properly selected only when the workspace can point to:
- the actual repo/module path
- the bounded slice definition
- the verification expectation
- the evidence expectation
- the reason this candidate is thinner and safer than alternatives

## Recommended next move
Use this selection rule to identify the first real implementation target already present in the workspace. If none exists, treat missing target access as the next real blocker instead of pretending the autonomous support path is execution-ready.

## Bottom line
The selected autonomous support path is now real, but the first test case must be chosen with stricter truthfulness: **present codebase first, bounded slice second, execution only after inspection.**
