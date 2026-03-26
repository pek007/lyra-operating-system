# P1 Canonical TDE Substrate — Decision Frame

Date: 2026-03-18
Prepared by: Overnight execution loop
Selected priority source: `control/CT-OVERNIGHT-SYNTHESIS-2026-03-17.md` (priority 3)
Related artifacts:
- `products/improvement/04-execution/P1_CANONICAL_TDE_SUBSTRATE_SESSION_PREP_2026-03-18.md`
- `products/improvement/04-execution/P1_CANONICAL_TDE_SUBSTRATE_VALIDATION_MATRIX_2026-03-18.md`
- `products/improvement/04-execution/P1_CANONICAL_TDE_SUBSTRATE_ENFORCEMENT_SURFACES_2026-03-18.md`

## Purpose
Reduce the next focused P1 session to one explicit substrate decision grounded in the current canonical TDE reality.

This note does **not** approve the substrate. It frames the decision using:
1. the current TDE runtime schema,
2. the currently-ingested live validation set (`OPS-2026-066` through `OPS-2026-069`), and
3. the existing intake packet shape already being used in practice.

## Selected priority -> current work -> decision surface
- **Selected priority:** `products/improvement/04-execution/TOP_PRIORITIES.md` Priority 1 — converge improvement execution into one canonical TDE-first system of record.
- **Current canonical runtime surface:** `os/runtime/tde_state.sqlite` with `tasks(task_id, title, status, checked, version, source, updated_at, metadata_json)`.
- **Current human projection:** `os/runtime/TASKS_from_db.md`.
- **Current live validation set:** `OPS-2026-066` through `OPS-2026-069` are all already present as canonical TDE tasks.
- **Current intake shape already in use:** `products/improvement/04-execution/intake/intake-ops-2026-066-final.json` and peers already carry structured fields such as `source_system`, `source_type`, `source_reference`, `product_scope`, `related_entities`, and `evidence_links`.

## The actual substrate decision
The next focused session should decide between exactly these two models:

### Option A — Dedicated improvement task class
Create a distinct improvement-prefixed task class (or equivalent separate canonical class rule) for improvement work.

**Upsides**
- Improvement work becomes visually and semantically explicit.
- Easier to filter/report on improvement items without relying on metadata discipline alone.
- Could make policy boundaries feel clearer to operators.

**Costs / risks**
- Current canonical TDE task store does not expose a first-class `task_class` column; it only has `task_id`, `source`, and `metadata_json`.
- Introducing a dedicated class cleanly would likely require either new ID conventions, stricter parser/runtime changes, or reliance on encoded semantics in IDs anyway.
- Higher risk of turning P1 into a TDE kernel/data-model change instead of an improvement operating-substrate definition.
- More likely to violate the Control Tower intent of recording a focused next-session preparation rather than triggering ad hoc redesign.

### Option B — Existing canonical task model + mandatory improvement metadata
Keep improvement work inside the current canonical TDE task model and approve a mandatory metadata/linkage/intake contract for any item treated as canonical improvement work.

**Upsides**
- Fits the live canonical schema immediately: `metadata_json` already exists and is already carrying source/product hints for `OPS-2026-066` through `OPS-2026-069`.
- Fits the current intake packet practice already in use under `products/improvement/04-execution/intake/`.
- Keeps P1 scoped to operating discipline, routing rules, and closure evidence — not kernel redesign.
- Lowest-risk path to making the live validation set enforceable quickly.

**Costs / risks**
- Requires strong enforcement discipline; otherwise improvement work may still blur with generic ops work.
- Reporting/filtering depends on canonical metadata presence and consistency.
- If metadata rules are weak, the substrate will exist only on paper.

## Evidence from the live runtime favors one path
### Runtime fact 1
The canonical DB task store currently exposes only:
- `task_id`
- `title`
- `status`
- `checked`
- `version`
- `source`
- `updated_at`
- `metadata_json`

There is no visible first-class improvement-type column in the current canonical schema.

### Runtime fact 2
The live P1 validation set already uses metadata successfully enough to preserve:
- `intake_id`
- `source_system`
- `source_reference`
- `priority_hint`
- `product_scope`

### Runtime fact 3
The intake packets already carry richer structured fields than the task table itself, including:
- source identity
- product scope
- related entities
- evidence links
- requested/proposed action

That means a practical substrate can likely be defined by approving:
1. what must be present in the intake packet,
2. what minimum subset must survive into canonical task metadata, and
3. what closure evidence link must be added before the item can be closed.

## Overnight recommendation for the next focused session
**Recommended default: Option B** — keep the current canonical TDE task model and define a mandatory improvement metadata/linkage contract on top of it.

### Why this is the better next move
- It matches the actual DB-canonical runtime already in use.
- It preserves the Control Tower constraint: focused substrate definition, not ad hoc system redesign.
- It can be validated immediately against `OPS-2026-066` through `OPS-2026-069`.
- It keeps open the possibility of a later dedicated class **if** the metadata-based substrate proves insufficient in real use.

## Minimum approval package implied by Option B
If the next session accepts Option B, it should approve at least:

1. **Canonical routing rule**
   - A signal becomes canonical improvement work when it is represented by a TDE task with the approved improvement metadata contract and linked intake source.

2. **Minimum task metadata contract**
   - `source_system`
   - `source_reference`
   - `product_scope`
   - `improvement_type` or equivalent intent field
   - `expected_closure_evidence`
   - `linked_source_artifact`

3. **Minimum intake packet contract**
   - preserve current packet strengths rather than inventing a new blank schema.
   - define which packet fields are mandatory vs optional.

4. **Closure rule**
   - no canonical improvement item closes without an evidence link and an explicit source-to-closure trace.

5. **Validation pass**
   - re-check `OPS-2026-066` through `OPS-2026-069` against the approved contract and record any missing metadata/evidence gaps.

## What this decision frame intentionally does not do
- It does not mutate the TDE schema.
- It does not approve the metadata contract.
- It does not convert the four validation tasks.
- It does not rewrite product or governance docs yet.

## Immediate overnight outcome
One more concrete overnight step is now complete:
- the P1 follow-through is reduced to a specific next-session choice,
- that choice is grounded in the current DB-canonical TDE schema and live intake packets,
- and the likely low-risk recommendation is explicit: **use the existing canonical task model with mandatory improvement metadata/linkage rules first**.
