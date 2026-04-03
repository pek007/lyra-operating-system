# Lint / Health Check Spec V1

Pilot: AI Tools Landscape
Date: 2026-04-03
Status: draft

## Purpose
Define the first bounded lint / health-check pass for the AI Tools Landscape knowledge-compiler pilot.

The goal is not abstract quality theater. The goal is to detect early structural weaknesses before the pilot becomes larger and harder to maintain.

---

## 1. Scope of the lint pass
The lint pass should review only the pilot corpus under:
- `raw/`
- `compiled/`
- `outputs/` when relevant

It should **not** attempt to rewrite or govern unrelated workspace artifacts.

---

## 2. Primary lint questions

### A. Coverage
- Does each important raw source have a compiled source summary?
- Are important compiled artifacts missing for recurring themes?

### B. Traceability
- Does each compiled source summary link back to its raw source?
- Do concept and synthesis pages link back to the relevant source summaries?
- Are any claims or pages presenting synthesis with weak or missing source grounding?

### C. Structure
- Are indexes current with the files that actually exist?
- Are there orphan pages that nothing points to?
- Are there duplicate or near-duplicate concept pages emerging?

### D. Quality / usefulness
- Are compiled pages materially distinct, or are they repetitive paraphrases?
- Are concept pages saying something reusable, or only restating single-source summaries?
- Are synthesis notes actually synthesizing, or merely stacking summaries?

### E. Confidence and caution discipline
- Are weaker sources/pages marked as lower confidence?
- Are speculative interpretations being stated too strongly?

### F. Pilot-boundary discipline
- Is the pilot staying distinct from governed operational truth?
- Are we accidentally letting the compiled layer behave like the source of truth for plans, decisions, or operating state?

---

## 3. First lint output categories
Every finding should be classified as one of:
- `fix_now`
- `improve_soon`
- `watch`
- `no_issue`

### Meaning
- `fix_now`: structural or trust issue that meaningfully weakens the pilot today
- `improve_soon`: worthwhile improvement, but not a current blocker
- `watch`: not yet a problem, but could become one as the corpus grows
- `no_issue`: healthy enough for current pilot scale

---

## 4. Specific checks for V1

### Check 1 — Raw-to-summary coverage
Rule:
- every selected raw source should have a compiled source summary

### Check 2 — Summary-to-source traceability
Rule:
- every compiled source summary must reference a raw source file

### Check 3 — Concept grounding
Rule:
- every concept page should point to at least one relevant compiled source summary
- stronger concept pages should ideally be supported by more than one source over time

### Check 4 — Synthesis grounding
Rule:
- every synthesis note should link to the source summaries and concepts it relies on

### Check 5 — Index freshness
Rule:
- indexes should match actual current files in the pilot

### Check 6 — Weak-source transparency
Rule:
- known weak sources should remain marked as lower confidence until strengthened or replaced

### Check 7 — Pilot-boundary protection
Rule:
- no compiled page should imply that it is the canonical source of truth for governance, priorities, or state outside the pilot knowledge domain

---

## 5. Initial pass thresholds
At the current pilot scale, the lint pass should stay lightweight.

### Good enough for now
- raw/source/summary coverage is complete for the initial selected sources
- concept and synthesis pages are source-linked
- indexes are current
- weak confidence is clearly marked where needed

### Not required yet
- automated duplicate detection
- advanced citation granularity scoring
- graph-level provenance verification
- heavy automation or scoring infrastructure

---

## 6. Recommended lint output format
The lint run should produce a short markdown artifact under:
- `logs/lint-runs/YYYY-MM-DD-lint-check.md`

Suggested structure:
1. corpus state checked
2. findings by category
3. `fix_now` items
4. `improve_soon` items
5. `watch` items
6. bottom line

---

## 7. V1 working philosophy
The lint pass should optimize for:
- trust
- maintainability
- compounding usefulness
- avoiding quiet structural decay

It should not optimize for:
- bureaucratic scoring
- maximum check count
- premature complexity

---

## 8. Immediate next use
Run the first manual lint pass once the pilot has:
- an initial source layer
- initial concept pages
- at least two synthesis notes

That threshold has now been reached.
