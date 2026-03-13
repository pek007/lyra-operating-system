# TDE Intent Intake and Formation Policy v1

Status: Draft
Owner: Peter + Lyra
Product: Task Management (`A-007`)
Date: 2026-03-13
Related:
- `products/task-management/07-decisions/TDE_DECISION_TO_ADVANCEMENT_POLICY_V1.md`
- `products/task-management/07-decisions/TDE_DECISION_POLICY_RUNTIME_EMBODIMENT_V1.md`
- `DECISION_SCHEMA_V1.md`

## Purpose
Define the missing front-end layer of TDE: how a human-submitted vision, goal, request, or intent becomes a professionally useful first objective/workflow/task formation inside TDE.

This policy exists because TDE should not depend on Peter and Lyra manually designing the decomposition in chat for ordinary work.

## Core principle
TDE must not be expected to read minds.

But TDE **should** be able to:
- accept incomplete input,
- infer a professionally reasonable first version,
- state assumptions explicitly,
- ask only the minimum high-value clarifying questions,
- and produce a valuable first objective/workflow/task formation.

## Design goal
Enable TDE to move from:
- "Peter has an intent"
to:
- "TDE has a structured, governable first work system"

with bounded ambiguity, explicit assumptions, and auditable shaping logic.

## What this layer is for
This layer sits **before** the current decision-to-advancement/runtime loop.

It is responsible for:
1. interpreting the request,
2. assessing completeness,
3. deciding whether to proceed, ask, or propose options,
4. producing a formation artifact,
5. handing the result into objective/workflow/task generation.

## Canonical intake truth
The input is not assumed to be complete.

The system should classify requests into one of three broad states:
- sufficiently specified
- partially specified
- underspecified

The system should then choose the appropriate shaping behavior.

## Input mode model
### Mode 1 — Fully specified request
Example:
- "Build a simple internal TDE GUI that reads DB-canonical state, shows active/parked/research/escalated tasks, and is validated in staging first."

Expected TDE behavior:
- proceed directly to structured objective/workflow/task formation
- do not ask unnecessary questions
- preserve the user's explicit constraints

### Mode 2 — Partially specified request
Example:
- "Create a basic GUI for TDE."

Expected TDE behavior:
- infer a reasonable v1 scope
- state assumptions
- identify major unknowns
- ask only questions that materially change scope/quality/risk
- still produce a useful first formation artifact

### Mode 3 — High-level aspiration
Example:
- "I want TDE to autonomously pursue high-level goals."

Expected TDE behavior:
- interpret the aspiration into candidate objectives
- propose a phased strategy
- identify major unknowns and architectural gaps
- avoid pretending the request is already execution-ready

## Intake classification
Every request should be classified across at least these dimensions:

### A. Request type
One of:
- aspiration
- objective request
- initiative request
- implementation request
- bug/fix request
- decision request
- review/audit request
- research request

### B. Specificity level
One of:
- high
- medium
- low

### C. Ambiguity type
Zero or more of:
- missing scope
- missing constraints
- missing quality bar
- missing environment/release expectations
- missing audience/consumer
- missing authority/risk posture
- missing success criteria

### D. Actionability status
One of:
- executable now
- executable with assumptions
- needs clarification
- needs strategic framing first

## Shaping policy
### TDE should proceed directly when:
- the request is specific enough to define a bounded first version,
- missing information is non-critical,
- assumptions can be made safely,
- and there is no material ambiguity about risk/authority.

### TDE should proceed with assumptions when:
- the request is incomplete but still bounded,
- the assumptions are low-risk and reversible,
- and the system can make them explicit in the formation artifact.

### TDE should ask clarifying questions when:
- the missing information would materially change the solution,
- authority/risk boundaries are unclear,
- external/public impact is possible,
- or multiple very different professional interpretations exist.

### TDE should escalate strategic framing when:
- the request is aspiration-level rather than execution-level,
- multiple competing goals must be balanced,
- or the work would establish a new operating direction rather than just execute within an existing one.

## Minimum-question rule
TDE should ask for the **minimum additional information required to produce a professionally valuable first result**.

This means:
- do not ask everything up front,
- do not pretend missing information does not matter,
- and do not block on details that can be safely assumed.

## Assumption policy
When proceeding with assumptions, TDE must:
- keep assumptions explicit,
- make them reviewable,
- prefer reversible assumptions,
- avoid assumptions that create major external/risk consequences,
- and treat assumptions as part of the formation artifact.

## Formation artifact
Before work enters the runtime decision/execution loop, TDE should produce a formation artifact containing at least:
- interpreted intent
- request type
- specificity assessment
- actionability status
- assumptions
- known unknowns
- proposed objective
- proposed success criteria
- proposed workflow family
- proposed first stage set
- proposed first task set
- required clarifications if any
- recommended next action

## Suggested formation outputs by mode
### For fully specified requests
Primary output:
- objective + workflow/task formation

### For partially specified requests
Primary output:
- objective + workflow/task formation with explicit assumptions

Secondary output if needed:
- 1–3 high-value clarifying questions

### For aspiration-level requests
Primary output:
- framing note or strategy proposal
- candidate objective set
- recommended first bounded slice

## Professional quality rule
Even when the input is incomplete, the output should still be:
- valuable,
- bounded,
- professionally structured,
- explicit about assumptions,
- and governable through normal TDE policy/runtime mechanisms.

The acceptable first result is not "magic certainty".
The acceptable first result is "a useful, honest, professionally framed first work system".

## Relationship to downstream TDE layers
This policy feeds into later layers:

- **Intent intake / formation** answers:
  - what does Peter mean?
  - what should be formed?
  - what is missing?
  - can we proceed now?

- **Decision-to-advancement** answers:
  - now that work exists, how does it continue?

- **Execution** answers:
  - how is the bounded unit of work performed?

## Non-negotiables
1. TDE must not assume mind-reading as a design premise.
2. TDE should aim to ask the fewest questions needed for a professional first result.
3. TDE must make assumptions explicit when proceeding under ambiguity.
4. TDE should not block on non-critical detail if a bounded, reversible first version is possible.
5. TDE should not pretend underspecified strategic requests are execution-ready when they are not.
6. The output of intake/formation must be durable and auditable, not just conversational.

## Suggested next follow-on work
1. Decide where this shaping layer lives in runtime architecture (Task Management, Interfaces, or a dedicated formation service inside TDE).
2. Decide whether formation should output only a formation record first, or also create canonical objective/task artifacts in the same cycle.
3. Expand beyond the initial small request-class table toward a more general shaping layer.
4. Decide when to introduce clarification dialogues for partially specified requests instead of assumption-first formation.

## Machine-readable contract added
The first v1 schema for the intent intake / formation artifact is now defined in:
- `schemas/tde_intent_formation_record/v1.0.0.schema.json`

## First creation mapping added
The first workflow-family mapping from formation output into canonical objective/task creation is now defined in:
- `products/task-management/07-decisions/TDE_FORMATION_TO_CANONICAL_CREATION_MAPPING_V1.md`

## First thin intake runtime added
A first thin request-class-based intake utility now exists at:
- `tools/tde_intent_intake.py`

Current supported request classes:
- `basic_tde_gui`
- `internal_tool`
- `runtime_hardening`
- `research_request`
- `review_audit_request`

## Bottom line
The next missing TDE layer is not just more execution logic.
It is the ability to turn human intent into a professionally useful first work system.

That means TDE must be able to:
- accept incomplete but meaningful input,
- infer a bounded first version,
- ask only the highest-value questions,
- and generate the first objective/workflow/task formation with explicit assumptions and governance.

That is the practical meaning of **intent-to-objective-to-task formation inside TDE**.