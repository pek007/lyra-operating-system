# GPT-5.4 Shakedown Battery v1

Date: 2026-03-08
Owner: Lyra
Status: Ready to run
Purpose: Validate that the move to GPT-5.4 plus prompt updates improves real operating performance, not just prompt aesthetics.

## 1) Battery design principles

This is a short operational battery, not a benchmark suite.

It is designed to test the four behaviors most likely to matter for us:
- format adherence
- completeness on multi-step work
- tool/use-of-evidence discipline
- calibrated autonomy (not too passive, not too eager)

## 2) Test set (4 tests)

### Test 1 — Codex planning discipline
**Lane:** Claude Code / planning
**Purpose:** Confirm GPT-5.4 produces a clean plan without leaking into implementation.

**Prompt shape:**
- Use `prompts/claude-code/WO_plan.md`
- Give a medium-complexity multi-file change request
- Require explicit verification plan and rollback notes

**Pass criteria:**
- Returns exactly planning sections requested
- No file edits or implementation output
- Identifies prerequisite files/contracts/tests before proposing action
- Verification plan is concrete, not generic

**Failure modes to watch:**
- starts implementing
- shallow file touch list
- skips dependency inspection
- vague verification steps

---

### Test 2 — Codex execution completeness
**Lane:** Claude Code / execution
**Purpose:** Confirm GPT-5.4 completes a bounded implementation task end-to-end with proper verification.

**Prompt shape:**
- Use `prompts/claude-code/WO_execute.md`
- Pick one reversible, internal, multi-file task with test coverage
- Require handoff artifact references

**Pass criteria:**
- Inspects current behavior first
- Completes requested implementation without scope drift
- Runs or explicitly accounts for verification checks
- Marks any incomplete item as `[blocked]` rather than silently omitting it
- Final output matches requested deliverable structure

**Failure modes to watch:**
- incomplete execution presented as done
- too little verification
- over-eager extra changes outside scope
- verbosity drift in handoff

---

### Test 3 — Deep research public synthesis
**Lane:** Deep Research / public
**Purpose:** Confirm GPT-5.4 produces a compact, decision-ready, evidence-backed external synthesis.

**Prompt shape:**
- Use `prompts/deep-research/RO_public.md`
- Ask a current, decision-relevant external question
- Require recommendation plus citations

**Pass criteria:**
- Clean separation between evidence, trade-offs, and recommendation
- Non-trivial claims are cited
- Uncertainty is explicit where evidence is weak/conflicted
- Stops at “enough evidence,” rather than sprawling

**Failure modes to watch:**
- overlong output with little incremental value
- recommendation not grounded in cited evidence
- false certainty
- weak option comparison

---

### Test 4 — Deep research private mapping
**Lane:** Deep Research / private
**Purpose:** Confirm GPT-5.4 can map findings to our architecture/process landscape without inventing current-state facts.

**Prompt shape:**
- Use `prompts/deep-research/RO_private.md`
- Provide 1 external finding set + 3-5 internal artifacts
- Ask for implications, options, recommendation, and controls

**Pass criteria:**
- Resolves internal current-state from artifacts before proposing changes
- Distinguishes current state vs proposed target state
- Escalates contradictions or missing artifacts explicitly
- Gives a recommendation usable in the next 1-2 sprints

**Failure modes to watch:**
- hallucinated current architecture
- recommendation detached from actual workspace reality
- weak risk/control section
- missing citations to internal artifacts

## 3) Scoring rubric

Score each test 1-5 on each dimension.

### A. Format adherence
- 5 = exactly follows requested structure/order
- 3 = mostly follows, minor drift
- 1 = substantial structure failure

### B. Completeness
- 5 = covers all requested elements; blocked items explicitly marked
- 3 = mostly complete; one notable omission
- 1 = materially incomplete

### C. Evidence / tool discipline
- 5 = appropriate inspection/retrieval/verification; no obvious skipped prerequisite
- 3 = adequate but light
- 1 = weak grounding or skipped necessary steps

### D. Judgment / autonomy calibration
- 5 = proceeds appropriately, asks only when warranted, avoids scope drift
- 3 = usable but slightly too passive or too eager
- 1 = poor calibration

### E. Concision / signal density
- 5 = compact, clear, high-signal
- 3 = useful but somewhat bloated or terse
- 1 = noisy or under-specified

## 4) Release thresholds

### Green
- No test below 4 on Format Adherence
- Average score >= 4.2
- No critical failure mode observed

### Yellow
- Average 3.6-4.1 or one notable failure mode
- Keep GPT-5.4 live, but patch prompt or workflow before broad confidence claims

### Red
- Any test <= 2 on Completeness or Evidence/Tool Discipline
- More than one major failure mode
- Revisit prompt layer and agent operating defaults

## 5) Minimal evidence pack to capture

For each test, save:
- prompt used
- output returned
- short evaluator note (what passed/failed)
- dimension scores
- recommended change, if any

Store under:
- `knowledge/evidence/2026-03/`

Recommended naming:
- `2026-03-08__gpt54-shakedown__test1-codex-plan.md`
- `2026-03-08__gpt54-shakedown__test2-codex-execute.md`
- `2026-03-08__gpt54-shakedown__test3-dr-public.md`
- `2026-03-08__gpt54-shakedown__test4-dr-private.md`
- `2026-03-08__gpt54-shakedown__scorecard.md`

## 6) Recommended execution order

1. Test 1 — Codex planning
2. Test 2 — Codex execution
3. Test 3 — Public research
4. Test 4 — Private mapping

Reason: planning/execution issues should surface first; research issues next.

## 7) Expected likely findings

Most likely with GPT-5.4:
- better adherence to explicit structure
- better completion if completeness criteria are stated
- stronger long-horizon work
- still needs explicit control against over-search / over-verbosity
- still benefits from explicit dependency checks early in the task

## 8) Decision after run

After running the battery, choose one:
- **Accept** — GPT-5.4 prompt layer stable
- **Accept with patch** — keep model, refine prompts
- **Hold** — keep model but limit claims/use cases until patched

## 9) Recommended operator stance

Do not ask “is GPT-5.4 better?” in the abstract.
Ask:
- Is it better for our actual lanes?
- Is it better with our updated prompt contracts?
- Where does it still need guardrails?
