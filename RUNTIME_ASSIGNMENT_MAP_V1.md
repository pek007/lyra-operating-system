# RUNTIME_ASSIGNMENT_MAP_V1.md

Status: Active draft v1  
Owner: Lyra via Control Panel  
Date: 2026-03-10

## Purpose
Translate `RUNTIME_TOPOLOGY_MAP_V1.md` into explicit current-state vs target-state runtime assignments for the currently visible Lyra OS product/session structure.

## Scope
This map covers:
- central Control Panel runtime
- currently visible Lyra product-session lanes
- Vega / `pxs`
- recommended wake-up model per area
- recommended coordination path per area
- candidate threshold calls for future dedicated runtime evaluation

## Reading guide
- **Current placement** = where the area effectively lives now
- **Target placement** = recommended placement under the hybrid runtime model
- **Runtime class** = A / B / C from `RUNTIME_TOPOLOGY_MAP_V1.md`
- **Dedicated runtime threshold** = whether the area already appears to justify evaluation for a separate persistent runtime

## Assignment matrix

| Area / Product | Current placement | Target placement | Runtime class | Wake-up model | Coordination default | Dedicated runtime threshold now? | Notes |
|---|---|---|---|---|---|---|---|
| Control Panel (`CP-001`) | Main Lyra runtime; current session/topic focus | Central oversight runtime | Central / B-like core role | Heartbeat for awareness + cron only for specific governance loops | Central coordinator; `sessions_send` out to target lanes | No | Keep central by design |
| Task Management (`A-001`) | Main Lyra runtime + product session lane | Main runtime execution lane | B | Cron for product/task loops; direct session nudges for handoffs | `sessions_send` + job bundle updates | Not yet | Good candidate to test real job-memory portability first |
| Governance (`A-002`) | Main Lyra runtime + product session lane | Main runtime execution lane | B | Cron for scheduled reviews/checks; heartbeat only for escalations to central view | Structured handoff + decision artifact updates | Not yet | Governance should remain close to central runtime unless boundary need grows |
| Security (`A-004`) | Main Lyra runtime + product session lane | Main runtime execution lane (for now) | B | Cron for audits/checks; central heartbeat for high-signal surfacing | Evidence artifacts + `sessions_send` | Borderline later, not now | Could become Class C if trust/tool boundary materially diverges |
| Improvement (`A-005`) | Main Lyra runtime + product session lane | Main runtime execution lane | B | Cron for autonomous sweeps; central heartbeat for surfaced leverage | Improvement log + task routing + `sessions_send` | No | Naturally cross-cutting; keep near central runtime |
| Delivery (`A-006`) | Main Lyra runtime + product session lane | Main runtime execution lane | B | Cron only where deterministic delivery checks matter; otherwise event-driven | Handoff + evidence + status reply | Not yet | Likely better solved by stronger artifacts than separate runtime |
| Interfaces (`A-007` or interface lane) | Main Lyra runtime + product session lane | Main runtime execution lane | B | Event-driven; cron only if recurring verification emerges | Interface artifacts + direct session messaging | Not yet | Should stay lightweight until repeated coordination pain proves otherwise |
| Other Lyra OS product lanes without visible session starters | Likely implicit/main runtime handling | Main runtime execution lane unless proven otherwise | B by default | Case-by-case; prefer cron over thread-dependent wake-ups | Job/product artifact + `sessions_send` | Unknown | Need explicit mapping as next pass |
| PX / Company-as-Code (`pxs`) via Vega | Separate persistent `px-internal-dev` runtime | Remain separate persistent runtime | C | Product/domain-local cron + local operating loops | Explicit handoff across domain boundary | Yes (already true) | Existing isolated model appears correct |

## Current-state diagnosis by lane

### Control Panel
- Already acting as the de facto central oversight lane in this session.
- Should become more explicit as the runtime-governance and coordination owner.
- Should not be reduced to just another product thread.

### Product session lanes in Lyra OS
Visible lanes today:
- control-panel
- task-management
- delivery
- governance
- improvement
- security
- interfaces

Diagnosis:
- useful as human-facing conversation lanes
- too weak as durable runtime boundaries
- should remain as operating surfaces, but not as the sole identity carrier

### Vega / `pxs`
- strongest current example of a justified separate runtime
- demonstrates correct use of explicit workspace/state/memory separation
- should be treated as the reference case for future durable runtime boundaries

## Recommended wake-up assignments

### Central Control Panel runtime
Primary wake-up model:
- heartbeat for cross-product awareness batching
- selective cron for central governance/maintenance loops only

Questions it should answer:
- what is blocked?
- what needs escalation?
- which lane should act next?
- what should be surfaced to Peter?

### Product execution lanes in main Lyra runtime
Primary wake-up model:
- cron for exact/recurring work detection and product-local sweeps
- direct `sessions_send` for targeted nudges and handoffs
- avoid depending on human posting in the topic to restart momentum

### Dedicated runtime lanes
Primary wake-up model:
- local cron and local operating loops within that runtime
- structured handoff back to Control Panel when cross-product awareness is needed

## Recommended coordination assignments

### Default intra-Lyra pattern
- Control Panel = coordinator
- Product lane = executor/owner for product-local work
- Job bundle = durable continuity store
- `sessions_send` = default direct bridge
- copy-paste = fallback only

### Durable coordination rule
If a handoff affects more than one step or more than one work cycle, the coordination must update at least one durable artifact:
- job `STATE.md`
- job `HANDOVER.md`
- product decision/plan artifact
- evidence note

## Candidate areas for future dedicated runtime evaluation

### Not recommended yet
The following should **not** get separate persistent runtimes yet unless stronger evidence appears:
- Task Management
- Governance
- Improvement
- Delivery
- Interfaces

Reason:
- current pain appears solvable first through better job memory, wake-up discipline, and cross-session coordination
- persistent-runtime sprawl would likely outrun current governance maturity

### Possible future candidate
- Security

Reason:
- if security work increasingly demands materially different tool policy, trust boundary, or isolation discipline, it may justify separate runtime evaluation later
- current evidence is not yet strong enough to force that move

### Confirmed dedicated runtime
- Vega / `pxs`

## Immediate operating recommendations

### 1. Keep all currently visible Lyra OS product lanes in the main runtime for now
But stop treating the Telegram topic itself as the durable boundary.

### 2. Pick one lane as the first proof case for the new model
Recommended first proof case:
- **Task Management**

Why:
- it is execution-heavy
- it naturally benefits from cron wake-ups
- it is close to TDE and job portability
- it is a good place to validate that stronger artifacts reduce thread-dependence

### 3. Define the lightweight intra-Lyra handoff protocol next
This is the missing piece between topology and actual coordination behavior.

### 4. Make current-vs-target mapping explicit for actual Telegram topics
A future pass should attach:
- topic id / conversation label
- current product owner lane
- target runtime class
- wake-up owner
- coordination path

## Open implementation gaps
1. No populated live job bundles yet for active product/job flows.
2. No lightweight handoff protocol yet for intra-Lyra coordination.
3. No explicit registry tying Telegram topics to products/jobs/runtimes.
4. No product-by-product wake-up schedule registry yet.

## Initial conclusion
The currently visible Lyra OS product/session structure should remain inside the main Lyra runtime **for now**, but under a stronger operating model:
- product sessions are conversation lanes, not the architecture
- Control Panel is the central oversight runtime
- Vega remains the model for justified dedicated-runtime separation
- Task Management is the best first candidate for testing the improved coordination/runtime pattern without creating a new persistent runtime

## Version
- v1.0
- Date: 2026-03-10
