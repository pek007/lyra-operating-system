# TDE S26 Supersession and Sequence-Failure Review

Date: 2026-03-10
Owner: Lyra
Status: Final review

## Executive summary

The work executed on `WO-2026-TDE-KERNEL-S26` on 2026-03-10 should **not** be treated as the current TDE frontier.

It does **not** appear to have damaged the newer TDE runtime or DB-canonical architecture.
However, it **did** create analysis pollution risk because it resumed an older markdown-era canary thread after the repo had already advanced to DB-canonical cutover and later TDE phase work.

Recommended disposition:
- **Keep runtime/code changes that did not break newer behavior**
- **Keep S26 artifacts as historical evidence**
- **Mark S26 explicitly superseded by the DB-canonical frontier**
- **Document the sequence-failure cause and prevention controls**

## What was already true before the 2026-03-10 S26 work

The repo had already advanced beyond markdown-canonical TDE execution:
- DB canonical cutover was executed on 2026-03-09
- `os/runtime/tde_state.sqlite` was the canonical TDE runtime store
- `os/runtime/TASKS_from_db.md` was the runtime projection
- `TASKS.md` was retained only as a legacy/reference markdown board
- later work existed for chaining and post-cutover controls

Primary evidence:
- `knowledge/evidence/2026-03-09__tde-db-canonical-cutover-executed.md`
- `os/tde/INDEX.md`
- `os/sops/TDE_DB_CANONICAL_CUTOVER_GATE_V1.md`
- `os/sops/TDE_CHAINING_CONTRACT_V1.md`
- `governance/TDE_AUTONOMOUS_CHAINING_IMPLEMENTATION_PLAN_V1.md`

## What happened on 2026-03-10

A local session resumed an older S26 line of work and completed it as though markdown-era cutover-readiness were still the active frontier.

That work added:
- an S26 work order
- bounded markdown-era canary scope/readiness/runbook artifacts
- one bounded canary verification sequence
- a closeout note stating "canary proven / expansion held"

The key architectural mismatch is that these artifacts describe a canary where `TASKS.md` is treated as canonical for the slice, while the current TDE architecture already states that canonical runtime state lives in DB.

## Impact assessment

### Runtime impact
Low.

No strong evidence was found that S26:
- reverted DB-canonical execution,
- rewired scheduled runtime away from DB canonical mode,
- modified chaining contracts,
- or damaged current state-store architecture.

### Documentation / analysis impact
Medium to high.

Without explicit supersession marking, the S26 artifacts can mislead future analysis by implying that the markdown-era bounded canary is the active frontier, when it is not.

### Task-state impact
Moderate but recoverable.

Because `TASKS.md` is legacy/reference after DB cutover, edits there are no longer the canonical expression of runtime frontier state. They can still confuse humans and research workflows if left unqualified.

## Root-cause analysis

This sequence failure likely required **multiple conditions to line up at once**:

1. **Frontier reconstruction did not happen before resuming work**
   - The session should have established the latest repo/TDE frontier first.
   - Instead, it accepted an older S26 thread as current.

2. **Context continuity was degraded**
   - The session likely lacked the expected short-term continuity needed to recognize that TDE had already moved far beyond markdown-era S26.
   - Your hypothesis that the context window was effectively wiped is consistent with the observed behavior.

3. **Repo-local state and GitHub frontier were temporarily out of sync**
   - The local branch did not initially reflect the newer remote frontier.
   - That made the older S26 line appear more plausible than it should have.

4. **The repo contained multiple meanings of "S26"**
   - There is an unrelated SEC-AUTO S26 closeout reference and the TDE `WO-2026-TDE-KERNEL-S26` line.
   - This increased ambiguity and made fast frontier reconstruction harder.

5. **No fail-closed "frontier check" existed before TDE execution resumed**
   - There was no explicit rule forcing a check such as:
     - latest TDE slice in repo
     - canonical runtime store
     - whether the proposed slice is superseded

## Findings about current TDE frontier

The current frontier is **not** S26.

The repo shows materially later progress including:
- S27 sandbox guardrail
- S28-S30 DORA/proxy maturity work
- S31-S35 durable state + shadow ledger path
- S36 DB canonical cutover gate
- S37-S38 daily cutover readiness operations
- DB cutover executed on 2026-03-09
- chaining contract and implementation planning on 2026-03-09

This means any future TDE planning/research should start from the DB-canonical + chaining frontier, not from S26.

## Prevention controls

To avoid repetition, adopt these controls immediately for TDE work:

### 1. Mandatory frontier check before resuming any TDE thread
Before any new TDE execution, explicitly verify:
- current `origin/main` head
- latest TDE runtime model (markdown vs DB canonical)
- latest closed/open TDE-related slices
- whether the intended slice is already superseded

### 2. Treat GitHub `origin/main` as frontier authority for Deep Research preparation
When preparing research or architectural analysis, first ensure local state is rebased/pulled and compare against remote frontier.

### 3. Mark superseded-but-valuable artifacts explicitly
Historical evidence should not be deleted casually, but it must be labeled when later architectural decisions supersede it.

### 4. Add a fail-closed TDE resume rule
If the session cannot confidently answer:
- what is the canonical TDE store now?
- what is the latest TDE phase now?
- is this slice still frontier work?
then it should not continue implementation; it should switch to frontier reconstruction first.

### 5. Prefer canonical runtime projection over legacy board for frontier inspection
For post-cutover TDE work, inspect:
- `os/runtime/TASKS_from_db.md`
- `os/runtime/tde_state.sqlite`-backed evidence
- latest TDE SOP/index/governance artifacts
before relying on `TASKS.md`.

## Final recommendation

- Keep S26 as historical evidence.
- Mark it superseded relative to the DB-canonical frontier.
- Do not treat S26 as the active next-step basis for future TDE work.
- Use this review as the control note for avoiding future sequence failures.
