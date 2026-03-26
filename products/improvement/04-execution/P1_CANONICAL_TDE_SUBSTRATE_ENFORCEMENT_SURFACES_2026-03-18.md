# P1 Canonical TDE Substrate — Enforcement Surfaces

Date: 2026-03-18
Prepared by: Overnight execution loop
Selected priority source: `control/CT-OVERNIGHT-SYNTHESIS-2026-03-17.md` (priority 3)
Related artifacts:
- `products/improvement/04-execution/P1_CANONICAL_TDE_SUBSTRATE_SESSION_PREP_2026-03-18.md`
- `products/improvement/04-execution/P1_CANONICAL_TDE_SUBSTRATE_VALIDATION_MATRIX_2026-03-18.md`

## Purpose
Make one more bounded overnight step on the same Control Tower-selected priority without attempting to design the full substrate.

This note answers a narrower but important question for the next focused session:
**once the canonical improvement substrate is defined, which existing artifacts must change for it to become enforceable rather than merely described?**

That keeps the work explicit:
`selected priority` -> `live validation cases` -> `candidate substrate rules` -> `named enforcement/update surfaces`

## Selected priority -> current work -> enforcement link
- **Selected priority:** `products/improvement/04-execution/TOP_PRIORITIES.md` Priority 1 — converge improvement execution into one canonical TDE-first system of record.
- **Current live TDE validation surface:** `OPS-2026-066` through `OPS-2026-069` in `os/runtime/TASKS_from_db.md`.
- **Why enforcement mapping is the next useful step:** P1 is not just a design question. If the next session defines routing/linkage/intake rules but does not name where those rules must live, improvement execution will continue leaking back into ad hoc surfaces.

## Minimum enforcement surfaces the next focused session should update
| Surface | Current role | Why it must be touched when P1 is defined | Minimum expected update |
|---|---|---|---|
| `products/improvement/04-execution/PLAN.md` | states objective truth for the Improvement product | must stop describing P1 as only intent and point to the approved canonical substrate | add the approved routing rule and identify the canonical intake/execution path |
| `products/improvement/03-operating-model/OPERATING_MODEL.md` | defines what Improvement is in relation to Task Management | must state how Improvement uses TDE without collapsing the product boundary | add the operating loop step that converts signal -> canonical TDE improvement work |
| `products/improvement/07-decisions/DECISIONS.md` | records product-shaping choices | required if substrate choices include a real trade-off (e.g. dedicated class vs metadata-on-existing-classes) | capture the chosen substrate model and review triggers |
| `governance/LYRA_CONTINUOUS_IMPROVEMENT_OPERATING_INSTRUCTION_V1.md` | cross-system operating rule for improvement work | currently requires TDE use in principle, but not the exact substrate contract | add or link the mandatory intake/linkage/closure-evidence rule set |
| `os/tde/INDEX.md` | canonical TDE entrypoint index | needed if the substrate introduces a new canonical intake or runtime-facing authority surface | link the canonical improvement intake/contract artifact if one is created |
| `products/improvement/04-execution/intake/` | current practical intake packet location | already contains live stress-test cases; must become explicitly canonical or be superseded | define the approved intake schema/required fields and mark obsolete packet variants clearly |
| `products/improvement/04-execution/TOP_PRIORITIES.md` | portfolio-facing statement of what matters now | should reflect P1 as an approved operating substrate once defined | replace "undefined substrate" language with the approved rule and first rollout path |

## Candidate enforcement rule set implied by live cases
Using `OPS-2026-066` through `OPS-2026-069`, the next focused session should be able to approve or reject at least these enforcement statements:

1. **No material improvement item may remain only in memory notes, nightly reports, or product-local prose once selected for action.**
2. **Every canonical improvement item must have one named intake packet or equivalent canonical intake artifact.**
3. **Every canonical improvement item must declare expected closure evidence at intake time, not only at closeout.**
4. **If the improvement is blocked by judgment, the intake or task record must name the required decision path explicitly.**
5. **Product-local Improvement docs may explain context, but canonical execution status must remain in TDE runtime surfaces.**

These are candidate enforcement rules only; approval belongs to the next focused P1 session.

## Update sequence recommended for the next focused session
1. **Decide the substrate model**
   - dedicated improvement class vs existing classes with mandatory metadata.
2. **Approve the minimum rule set**
   - routing rule, linkage rule, intake fields, closure evidence expectation.
3. **Write one canonical substrate artifact**
   - concise and operational, not a broad process rewrite.
4. **Update enforcement surfaces in the same work cycle**
   - at minimum: `PLAN.md`, `OPERATING_MODEL.md`, and the cross-system operating instruction.
5. **Run first validation on live cases**
   - re-check `OPS-2026-066` through `OPS-2026-069` against the approved rule set and record any gaps.

## Explicit non-goals
- Do not redesign TDE kernel contracts overnight.
- Do not create a parallel improvement-tracking board.
- Do not broaden into A-005 distribution work or Interfaces scheduling decisions.

## Immediate overnight outcome
One more concrete overnight step is now complete:
- the selected P1 follow-through is no longer only framed as a design problem;
- the named enforcement/update surfaces are now explicit for the next focused session;
- the bridge remains clear from Control Tower priority to live TDE validation cases to the docs/runbooks that must change for the substrate to become real.
