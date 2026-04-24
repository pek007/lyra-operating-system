# Model Change Decision — Thinking-Level Operating Design

Date: 2026-04-24
Decision class: M2
Status: Accepted
Sponsor / approval source: Peter Eklind
Reviewed by: Lyra

## Decision

Accept the model change that treats thinking level / reasoning depth as part of Lyra OS runtime operating design rather than as an informal prompt preference.

## Scope of acceptance

Accepted as:
- shared cross-runtime doctrine for work-performing runtimes
- explicit runtime operating rule in the canonical Lyra OS Model
- OpenClaw implementation guidance through lane-pattern and prompting artifacts

Not accepted as:
- a requirement that all runtimes use identical local defaults forever
- a reason to create extra persistent agents only to hold different thinking defaults
- a doctrine that thin system/control runtimes should become their own deep-reasoning operators

## Runtime applicability decision

- Applies to Lyra
- Applies to Vega at the doctrine level, with room for runtime-local bindings
- Does not primarily target thin system/control runtimes except as a dispatch/orchestration rule

## Propagation completed

Canonical model artifacts updated:
- `LYRA_OS_MODEL_V1.md`
- `LYRA_OS_RUNTIME_AND_OPERATING_MODEL_V1.md`
- `LYRA_OS_LEARNING_AND_EVOLUTION_MODEL_V1.md`

Implementation artifacts updated:
- `integrations/openclaw/prompting-guides/THINKING_LEVEL_OPERATING_POLICY_V1.md`
- `integrations/openclaw/THINKING_LEVEL_LANE_PATTERNS_V1.md`
- `AGENT_EXECUTION_SEMANTICS.md`

Cross-runtime handoff created for Vega review:
- `/Users/lyra/.openclaw/workspace-px-internal-dev/handoffs/incoming/HO-20260424-001.yaml`
- `/Users/lyra/.openclaw/workspace-px-internal-dev/handoffs/incoming/HO-20260424-001-thinking-level-operating-design.md`
- `repos/lyra-operating-system/governance/HANDOFF_REGISTER_V1.md`

Supporting proposal artifacts:
- `control/model-change-candidates/2026-04-24-thinking-level-operating-design.md`
- `control/model-change-candidates/2026-04-24-thinking-level-operating-design-proposed-wording.md`

## Follow-through still expected

- Review the policy against real benchmark tasks
- Decide whether Vega should adopt the same initial local bindings as Lyra or a variant
- Keep the system/control runtime thin and enforce delegation in practice
