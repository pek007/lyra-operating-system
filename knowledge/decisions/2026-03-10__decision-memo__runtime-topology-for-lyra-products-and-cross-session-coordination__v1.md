---
decision_id: DEC-2026-015
title: "Runtime topology for Lyra products and cross-session coordination"
date: 2026-03-10
status: proposed
owner: Peter/Lyra
review_date: 2026-04-10
context: "Current Lyra operating model relies heavily on separate Telegram sessions/channels to hold product/area identity, causing role drift, weak wake-up semantics, and manual cross-session copy-paste coordination. Review also considered transferable patterns from Vega's isolated pxs/Company-as-Code foundation."
options_considered: "Option A: continue with one Lyra agent and channel/session-based product separation; Option B: create one persistent agent per product/area; Option C: hybrid runtime model with central Control Panel runtime, selective persistent runtimes where boundary is justified, portable job memory, and native cross-session communication"
decision: "Adopt Option C as the target operating model."
rationale: "Option C best balances role durability, boundary clarity, operating cost, and coordination quality. It avoids over-relying on Telegram session context while also avoiding premature fragmentation into too many persistent agents."
linked_work_artifacts: "MEMORY_PROCESS_V1.md; MEMORY_IMPLEMENTATION_ROADMAP_V1.md; MEMORY_ACTIVATION_MAP_V1.md; AGENT_LIFECYCLE_SOP_V1.md; SITUATIONAL_AWARENESS.md"
---

# Decision Memo

## Context

Lyra is currently being used across multiple Telegram sessions/channels to represent different areas and products. This has produced visible shortcomings:
- role and mission drift within sessions over time
- excessive dependence on chat history for product identity
- awkward wake-up semantics for product-specific work
- manual copy-paste communication across contexts

At the same time, the Vega / `pxs` setup demonstrates stronger boundary patterns:
- separate persistent runtime identity
- separate workspace/state/memory
- explicit cross-domain handoff discipline
- machine-checkable governance
- governed autonomous sweeps

The architectural question is therefore not just “how many agents should we have?” but “what runtime topology best supports durable mission, clean boundaries, controlled automation, and coordination across products?”

## Options

### Option A — Continue with one Lyra agent + Telegram channel/session separation
Use the current model as the long-term default: one broad Lyra runtime, with channels/topics implicitly carrying product identity and mission.

**Advantages**
- low setup overhead
- simple to operate initially
- minimal new agent/runtime complexity

**Disadvantages**
- weak role persistence
- identity depends too much on session history
- poor wake-up/control semantics for product loops
- cross-session coordination degrades into copy-paste
- boundary enforcement remains mostly social/procedural

### Option B — Create one persistent agent per product/area
Give each product or area its own persistent agent identity by default.

**Advantages**
- stronger mission persistence
- cleaner routing and session ownership
- easier to attach product-specific heartbeat/cron loops

**Disadvantages**
- risk of agent sprawl and management overhead
- duplicated bootstrap/memory/governance unless strongly centralized
- too much fragmentation if boundaries are still immature
- separate runtimes without strong handoff standards can still create coordination friction

### Option C — Hybrid runtime model (recommended)
Adopt a layered model:
- one central Control Panel runtime for oversight, prioritization, escalation, and cross-product coordination
- selective persistent product/domain runtimes only where durable boundaries are justified
- portable job memory bundles for continuity independent of sessions
- native cross-session communication as the default bridge
- heartbeat used centrally for awareness/governance; cron used for precise or isolated product/job loops

**Advantages**
- stronger boundary discipline where needed
- avoids making Telegram sessions the primary identity carrier
- avoids premature explosion of persistent agents
- better fit with existing agent lifecycle guidance
- aligns with lessons from Vega/`pxs`
- enables structured inter-session coordination instead of copy-paste

**Disadvantages**
- requires clearer runtime/ownership mapping
- requires handoff/message discipline and job-memory maturity
- somewhat more architecture work up front than the status quo

## Decision

Adopt **Option C — Hybrid runtime model** as the target operating model.

This means:
1. **Do not use Telegram channels/sessions alone as the primary durable unit of product identity.**
2. **Do not default to one persistent agent per product.**
3. **Use persistent agents selectively**, only when a durable boundary is justified by routing, trust, workspace, tool policy, or sustained mission separation needs.
4. **Keep a central Control Panel runtime** as the cross-product oversight and coordination layer.
5. **Use job bundles and product artifacts** as the durable carrier of mission and continuity, rather than relying on session history.
6. **Use native cross-session communication** (`sessions_send`, structured handoffs, and shared artifacts) instead of copy-paste as the operating default.
7. **Use heartbeat for central awareness and cross-job governance**, and **cron for precise or isolated product/job execution loops**.

## Rationale

This decision best fits both the current evidence and the lifecycle guidance already adopted in Lyra OS.

### 1. It addresses the real failure mode
The current problem is not only lack of sessions; it is that session context is carrying too much durable identity. Option C fixes that without assuming every product needs a separate runtime immediately.

### 2. It matches the agent lifecycle SOP
The adopted lifecycle already says: start with job, then execution profile, then runtime placement; only create a new persistent agent when a durable runtime boundary is actually required. Option C is the direct application of that policy.

### 3. It borrows the right lessons from Vega without over-copying
Vega / `pxs` demonstrates that when boundaries matter, they should be explicit and technical, not merely conversational. But Vega also shows the cost of separation. Option C imports the boundary discipline, shared-core thinking, and handoff rigor without forcing total fragmentation.

### 4. It improves wake-up and coordination semantics
A product loop should not depend on someone posting in a Telegram thread. Option C enables:
- central oversight heartbeat
- product/job cron loops where needed
- direct session-to-session nudges and handoffs
- less dependence on manual relaying

### 5. It keeps the architecture adaptable
Lyra currently operates broadly across Lyra OS, but that may change. Option C is robust to that future change because it separates:
- central oversight
- runtime placement
- job memory
- product identity
- coordination mechanisms

## Consequences

### Immediate consequences
- The current channel/session model should be treated as transitional, not final.
- We need an explicit runtime topology map: which areas remain under central Lyra, and which might justify separate persistent runtimes.
- Product identity should move into durable artifacts and runtime bindings, not stay mostly implicit in chat.

### Operational consequences
- Cross-session communication should become a designed pattern, not a manual workaround.
- Job memory bundles become more important, because they carry continuity across runtimes/sessions.
- Heartbeat and cron design should be clarified by function: central awareness vs local execution.

### Governance consequences
- Persistent-agent creation should stay gated by the lifecycle SOP.
- If separate product runtimes are created, they should follow stronger boundary rules inspired by Vega/`pxs`.
- Shared reusable capability should increasingly be treated as platform-core/shared dependency rather than copied policy text.

## Follow-ups

1. Produce a first-cut **runtime topology map** for Lyra OS:
   - central Control Panel runtime
   - candidate separate runtimes
   - current Telegram/product/session mapping
   - recommended target mapping

2. Define a lightweight **cross-session handoff protocol** for intra-Lyra coordination.

3. Define **wake-up strategy by class**:
   - central heartbeat
   - per-product/job cron loops
   - direct `sessions_send` nudges when needed

4. Create at least one real **active job bundle** and validate end-to-end job-memory portability in the new model.

5. Review whether any current product areas already meet the threshold for a dedicated persistent runtime.
