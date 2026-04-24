# Model Change Candidate — Thinking-Level Operating Design and Runtime Escalation

Status: Accepted on 2026-04-24 and propagated into canonical model artifacts.

## Title
Make thinking-level selection an explicit part of Lyra OS runtime operating design rather than an informal prompting preference.

## Trigger / evidence
During 2026-04-24 operating work, a bounded evaluation of OpenClaw/OpenAI Codex thinking levels (`medium`, `high`, `xhigh`) was run against CRM tasks with the current default model route (`openai-codex/gpt-5.4`).

Observed pattern:
- For a bounded "next slice" CRM task, all three levels converged on the same conclusion, but `high` and `xhigh` produced better framing and boundary discipline than `medium`.
- For a harder CRM architecture tradeoff (durable `MeetingCapture` entity vs lighter structured capture layer), the levels diverged materially:
  - `medium` recommended a thin first-class entity now
  - `high` recommended a lighter structured record layer
  - `xhigh` recommended a lighter structured record layer implemented in a promotion-ready way, preserving future promotion while avoiding premature platform design
- This indicates that thinking level is not just a latency/cost knob. It can change judgment quality and operating outcomes on architecture and tradeoff decisions.

Related local artifacts created during the same work:
- `integrations/openclaw/prompting-guides/THINKING_LEVEL_OPERATING_POLICY_V1.md`
- `repos/lyra-operating-system/integrations/openclaw/GATEWAY_RESTART_RECOVERY_PROCEDURE_V1.md`

Runtime posture also changed the same day:
- global OpenClaw default thinking level was set to `high`

## Proposed change
Clarify the Lyra OS runtime/operating model so it explicitly states that:
1. thinking level is an operating-control dimension, not only a prompt-writing preference
2. the default runtime posture may be set above the minimum when evidence shows under-reasoning is the larger operational risk
3. harder architecture/debugging/review tasks should escalate into stronger reasoning posture through explicit runtime controls or dedicated deep-work lanes
4. reasoning-depth choices should be evaluated empirically on representative tasks and reviewed as part of runtime improvement, rather than chosen only by intuition
5. when a reasoning-level policy becomes recurring and cross-cutting, it should connect to model, workspace, runtime-control, and review surfaces rather than remain only in ad hoc chat behavior

## Affected model artifacts
- `LYRA_OS_RUNTIME_AND_OPERATING_MODEL_V1.md`
- `LYRA_OS_LEARNING_AND_EVOLUTION_MODEL_V1.md`
- potentially `LYRA_OS_MODEL_V1.md` for a short cross-model doctrine statement

Likely downstream propagation targets if accepted:
- workspace operating guidance (`AGENTS.md` / workspace operating package surfaces)
- OpenClaw integration guidance under `repos/lyra-operating-system/integrations/openclaw/`
- review/eval surfaces for periodic validation of reasoning-level policy
- selected workflow-lane conventions for architecture/review/debug sessions

## Why this matters
Without explicit treatment, thinking-level behavior will drift through:
- individual operator instinct
- one-off `/think` switches
- isolated prompt notes
- hidden runtime habit

That creates three risks:
1. **under-reasoning** on hard tasks where judgment quality matters
2. **over-reasoning** on routine work, creating avoidable latency and workflow drag
3. **silent operating drift**, where runtime behavior changes but the system model still acts as if thinking depth is incidental

The 2026-04-24 evaluation suggests the right pattern is neither "always xhigh" nor "leave it informal".
It is:
- higher general default where justified
- explicit escalation on hard tasks
- empirical review from real benchmark tasks

That is operating design, not merely local prompt taste.

## Impact scope
Cross-runtime operating design, workspace operating guidance, and learning/evolution design.

Likely change class: **M2 candidate** (design-impacting).

## Review outcome / propagation
Reviewed and accepted on 2026-04-24.

Decision recorded in:
- `control/model-change-decisions/2026-04-24-thinking-level-operating-design-acceptance.md`

Accepted implementation pattern:
- canonicalize the principle and escalation doctrine in the Lyra OS Model
- keep product/tool-specific command details and lane examples in OpenClaw integration artifacts
- require periodic evidence review from real benchmark tasks so the policy does not harden into untested belief

Supporting draft artifacts created on 2026-04-24:
- `control/model-change-candidates/2026-04-24-thinking-level-operating-design-proposed-wording.md`
- `integrations/openclaw/THINKING_LEVEL_LANE_PATTERNS_V1.md`
