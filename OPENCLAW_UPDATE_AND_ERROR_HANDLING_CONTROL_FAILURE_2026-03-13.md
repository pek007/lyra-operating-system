# OpenClaw Update and Error-Handling Control Failure Report

## Header
- Error ID: ERR-2026-03-13-OC-001
- Date: 2026-03-13
- Title: OpenClaw update regression was not caught by post-update verification, and the follow-up handling initially bypassed the formal error process
- Type: control_failure / process_failure
- Scope: system_level
- Owning product or owner: Shared system / Lyra Operations
- Affected products/contexts: OpenClaw runtime, memory search, operator trust, improvement loop discipline
- Status: mitigated
- Review / closure date: 2026-03-20

## Summary
- OpenClaw was updated from 2026.3.8 to 2026.3.12.
- After the update, memory search became unavailable because local embeddings were configured (`agents.defaults.memorySearch.provider = "local"`) but the optional dependency `node-llama-cpp` was not installed by the update path.
- This regression was not caught immediately because the update was not followed by a targeted post-update smoke test for memory search.
- A second-order process failure then occurred: the incident was initially logged only in daily memory rather than being routed through the formal error/improvement process.

## Impact
- Actual impact:
  - Memory search was unavailable until manually repaired.
  - The agent reported that memory search was unavailable due to a local embeddings setup issue.
  - The first response to the incident used the wrong retention/control layer.
- Potential impact:
  - Reduced answer quality or continuity on questions requiring memory recall.
  - Lower trust in post-update stability.
  - Reinforcement of weak-loop behavior where incidents are remembered but not structurally processed.

## Detection
- How was it detected?
  - Peter noticed the message: "I checked memory first, but memory search is currently unavailable due to a local embeddings setup issue..."
  - Investigation confirmed memory search was configured for local embeddings and the missing package was `node-llama-cpp`.
- Detection gap, if any:
  - No explicit post-update verification step checked memory search availability after the OpenClaw update.
  - No immediate control forced routing of this meaningful incident into the formal error reporting loop.

## Root cause
- Primary root cause:
  - The OpenClaw update path did not leave the local embeddings dependency installed, while the runtime remained configured to depend on it.
- Contributing factors:
  - `node-llama-cpp` is an optional peer dependency rather than a guaranteed installed dependency of the OpenClaw package.
  - Post-update verification was incomplete.
  - Behavioral guidance did not explicitly say that meaningful incidents must not stop at memory notes.

## Immediate mitigation
- What was done immediately?
  - Installed the missing dependency with `npm i -g node-llama-cpp@3.16.2`.
  - Verified that `memory_search` worked again using the local provider.
  - Logged the incident in daily memory for continuity.
  - Updated `AGENTS.md` to state that meaningful incidents must follow the formal error/improvement process and not stop at daily memory.

## Corrective actions
- [x] Repair the broken memory-search dependency and verify memory search works again.
- [x] Create a formal shared/system error report for the incident and the follow-on handling failure.
- [x] Add an explicit operating rule in `AGENTS.md` to route meaningful incidents through the error process.
- [ ] Add a lightweight post-update smoke-test checklist covering `openclaw status`, one `memory_search` test, and one Codex/ACP smoke test.
- [ ] Decide where the canonical recurring update/verification runbook should live.

## Preventive changes
- What should change to reduce recurrence?
  - Post-update verification should become explicit, not implicit.
  - Meaningful incidents should automatically trigger the closed-loop improvement questions:
    1. What happened?
    2. Who owns it?
    3. What changes now?
    4. Which artifact/control layer changes?
    5. How will we verify the change worked?
    6. Where is the learning retained?
  - Local-memory configurations should be treated as requiring dependency verification after OpenClaw updates.

## Linked artifacts
- Related tasks:
  - To be created if the smoke-test checklist/runbook needs separate execution tracking.
- Related decisions:
  - None yet.
- Related evidence:
  - OpenClaw update from 2026.3.8 to 2026.3.12.
  - Successful reinstall of `node-llama-cpp@3.16.2`.
  - Successful `memory_search` verification after repair.
- Related product/shared artifacts:
  - `AGENTS.md`
  - `CLOSED_LOOP_IMPROVEMENT_MODEL_V1.md`
  - `ERROR_REPORTING_STANDARD_V1.md`
  - `memory/2026-03-13.md`

## Closure criteria
- What must be true before this is considered closed?
  - The incident is captured in the formal error system.
  - The AGENTS-level control is updated.
  - A canonical post-update smoke-test rule/checklist exists.
  - The next relevant update uses the checklist successfully, or the checklist is otherwise explicitly verified.

## Closure note
- Final outcome / verification:
  - Incident mitigated on 2026-03-13 by reinstalling `node-llama-cpp` and confirming working memory search.
  - Process-level closure remains open until the checklist/runbook control is in place and verified.
