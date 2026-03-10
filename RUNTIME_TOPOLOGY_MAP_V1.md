# RUNTIME_TOPOLOGY_MAP_V1.md

Status: Active draft v1  
Owner: Lyra via Control Panel  
Date: 2026-03-10

## Purpose
Provide the first explicit runtime topology map for Lyra OS, covering:
- current runtime situation
- target operating model
- candidate persistent runtime boundaries
- wake-up strategy by class
- cross-session coordination pattern
- migration implications

This artifact operationalizes `DEC-2026-015`.

## Design principle
Do not use Telegram sessions/channels as the primary durable unit of product identity.

Runtime boundaries should be created when they solve a real problem:
- durable mission separation
- routing/account separation
- workspace/data separation
- tool/sandbox policy separation
- trust boundary separation
- sustained execution frequency that justifies a dedicated runtime

## Current-state topology (2026-03-10)

### Runtime layer
- **Lyra / main runtime**
  - workspace: `/Users/lyra/.openclaw/workspace`
  - current role: broad operating runtime across Lyra OS
  - current product focus in this session: **Control Panel**
  - currently also serving multiple Telegram sessions/topics as execution surfaces for different areas/products

- **Vega / px-internal-dev runtime**
  - workspace: `/Users/lyra/.openclaw/workspace-px-internal-dev`
  - current role: separate PX / Company-as-Code foundation runtime
  - boundary model: intentionally isolated, with its own workspace/state/memory

### Session/channel layer
Current Lyra OS product/area handling relies substantially on separate Telegram sessions/topics.

Observed weakness pattern:
- role drift over time
- mission carried in conversational context rather than runtime boundary + durable artifacts
- weak direct wake-up semantics for product-specific work
- cross-session communication often degrades into manual copy-paste

### Artifact/memory layer
Strengths now in place:
- formal memory process exists
- retrieval works with local embeddings
- `jobs/` is now in retrieval scope
- product management structure exists across products

Remaining gap:
- product/session identity is still under-bound to durable runtime topology
- active job bundles are not yet broadly populated

## Target-state topology

### Layer 1 — Central oversight runtime
**Runtime:** Lyra / Control Panel

Primary responsibilities:
- portfolio oversight
- prioritization
- escalation and human interface
- cross-product coordination
- runtime topology governance
- memory governance
- heartbeat-based awareness batching

This runtime is the cognitive home for:
- “what matters now?”
- “what is blocked?”
- “what should happen next?”
- “which product/job/runtime should act?”

### Layer 2 — Selective domain/product runtimes
Persistent runtimes should exist only where justified.

Candidate reasons to create one:
- domain/workspace boundary required
- persistent role drift in shared runtime despite good artifacts
- distinct routing/account/channel ownership required
- durable tool/sandbox policy differences required
- high-frequency operational loop justifies a dedicated runtime

Current confirmed example:
- **Vega / px-internal-dev** for PX / Company-as-Code work

Potential future Lyra OS examples:
- a dedicated runtime for a product area only if it demonstrates durable need under the lifecycle SOP
- not one runtime per product by default

### Layer 3 — Job continuity layer
Jobs must remain portable across runtimes/sessions.

Carrier:
- `jobs/<JOB-ID>/JOB.md`
- `jobs/<JOB-ID>/STATE.md`
- `jobs/<JOB-ID>/MEMORY.md`
- `jobs/<JOB-ID>/HANDOVER.md`

Rule:
- job continuity should not depend on staying in the same Telegram thread or session transcript

### Layer 4 — Coordination layer
Cross-runtime/session coordination should use:
- native `sessions_send`
- structured handoff artifacts where appropriate
- product/job state artifacts
- central Control Panel awareness summaries

Copy-paste should be treated as fallback, not default operating design.

## Runtime classification framework

### Class A — Session-only context
Use when:
- temporary focus area
- no durable boundary needed
- same tools/workspace/policies as main runtime
- low coordination burden

Default mechanism:
- same runtime, fresh session/topic if helpful

### Class B — Product/domain execution lane inside main runtime
Use when:
- ongoing responsibility exists
- product artifacts and job memory are sufficient to hold identity
- no hard workspace/trust boundary needed yet

Default mechanism:
- main runtime + durable product artifacts + job bundles + cron/session messaging as needed

### Class C — Persistent dedicated runtime
Use when:
- sustained durable mission separation is needed
- routing/workspace/policy/trust boundary matters
- repeated evidence shows the session-only model is insufficient

Default mechanism:
- separate persistent agent/runtime with explicit workspace/state/bindings and acceptance checks

## Initial runtime recommendations by area

### 1. Control Panel
Recommended placement:
- **central oversight runtime** (main Lyra)

Rationale:
- this is the orchestration and governance layer
- should remain central rather than split away prematurely

### 2. Lyra OS product areas currently handled via Telegram topics
Recommended placement for now:
- **Class B** (stay in main runtime, but stop treating topic alone as identity)

Required upgrades:
- stronger product/session starter artifacts
- real job bundles
- explicit wake-up rules
- cross-session communication pattern

### 3. PX / Company-as-Code (`pxs`)
Recommended placement:
- **Class C** dedicated runtime (already true via Vega)

Rationale:
- clear domain boundary
- separate workspace/state is already beneficial
- reusable capability can be shared through governed dependency rather than merged runtime

## Wake-up strategy by class

### A. Central awareness / governance
Mechanism:
- **heartbeat** on central Lyra / Control Panel runtime

Use for:
- cross-job review
- stalled work checks
- decision queue surfacing
- lightweight situational awareness

Not for:
- detailed per-product execution loops

### B. Product/job exact or isolated loops
Mechanism:
- **cron**

Use for:
- TDE checks
- periodic task claiming
- deterministic product/job sweeps
- isolated reminders or refresh cycles

### C. Direct runtime/session nudges
Mechanism:
- **`sessions_send`**

Use for:
- handoff prompts
- explicit “pick this up now” signals
- cross-session escalation or status request

## Coordination pattern (first-cut)

### Default pattern
1. Control Panel identifies issue, task, blocker, or request.
2. Control Panel sends concise structured message to target session/runtime.
3. Target runtime updates job/product artifact and replies with status/result.
4. Control Panel reflects only high-signal outcome into oversight artifacts.

### Artifact expectation
When the coordination is durable or multi-step, the message should link to or update:
- job bundle state
- product plan/decision artifact
- evidence artifact
- handoff note

## Telegram/session design guidance
Telegram topics remain useful as:
- human-facing interfaces
- interaction surfaces
- local conversational workspaces

But they should not be treated as:
- the primary durable store of mission
- the only wake-up mechanism
- the only coordination bridge
- the main authority boundary

## Migration path (v1)

### Step 1 — Strengthen the main runtime model
- keep Control Panel central
- create real active job bundles
- define cross-session handoff protocol
- use `sessions_send` instead of copy-paste where possible
- define wake-up rules per class

### Step 2 — Identify boundary-failing areas
Look for repeated evidence of:
- role drift
- coordination overhead
- routing confusion
- workspace bleed
- different tool/trust needs

Only then nominate a product/domain for dedicated runtime evaluation.

### Step 3 — Apply lifecycle SOP for any new persistent runtime
For each candidate, evaluate:
- durable memory/context isolation need
- durable tool/sandbox policy differences
- routing/account separation need
- trust boundary need
- longevity/frequency
- operational overhead

### Step 4 — Formalize handoff and runtime map updates
Every approved runtime boundary should update:
- this topology map
- situational awareness
- agent lifecycle records
- routing/session operating guidance

## Current open questions
1. Which current Lyra OS product areas truly require a dedicated runtime rather than better artifacts + coordination?
2. What is the minimum useful lightweight intra-Lyra handoff schema?
3. How should current Telegram topics map to products, jobs, and runtimes explicitly?
4. Which wake-up loops should remain central versus product-local?

## Initial recommendation summary
- Keep **Control Panel** central.
- Keep **Vega / pxs** separate.
- Treat current topic-based product handling in Lyra as transitional.
- Do **not** create one persistent runtime per product by default.
- Build continuity through job memory and coordination protocols first.
- Add new persistent runtimes only where repeated evidence shows the need.

## Version
- v1.0
- Date: 2026-03-10
