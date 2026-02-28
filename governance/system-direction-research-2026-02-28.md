# Setting Direction in a Multi-Agent OpenClaw System
**Research report + recommendations (updated for a multi-agent architecture)**

## Executive summary
In a multi-agent OpenClaw setup, direction has **two scopes**:

1. **System direction**: what the overall system is for, what it should optimize for, which trade-offs are non-negotiable, and which boundaries are mandatory across agents.
2. **Agent direction**: what each individual agent is responsible for, how it contributes to the system, where it should escalate, and which playbooks or tools it should use.

That distinction matters because OpenClaw does **not** provide a single built-in global policy file that is automatically injected into every agent. Each agent has its own workspace, sessions, and state, while hard controls live in `~/.openclaw/openclaw.json`. OpenClaw auto-injects recognized bootstrap files such as `AGENTS.md`, `SOUL.md`, `TOOLS.md`, `IDENTITY.md`, `USER.md`, and `HEARTBEAT.md`; skills are loaded on demand; and arbitrary file names like `policies.md` are not part of the default always-on prompt path. `TOOLS.md` is guidance only and does not control availability. [OC1][OC2][OC3][OC4]

That leads to a clear recommendation:

- Treat **Layers 1-4** as mostly **system-level source material**.
- Then **compile or translate** those layers into **per-agent runtime files**, primarily `AGENTS.md`, plus `SOUL.md`, `USER.md`, and config.
- Keep **Layer 5** where it already lives: existing playbooks, process notes, and skill files.
- Treat **Layer 6** as a separate **task and decision management engine**, not as another pile of bootstrap markdown.

In other words: **do not create four new always-injected markdown files** named things like `vision.md`, `principles.md`, `policies.md`, and `guardrails.md` and expect OpenClaw to treat them as first-class runtime context. Use a **human-side governance layer** as the source of truth, then map it into the **built-in OpenClaw files** and **gateway config**.

---

## 1) The core clarification: what belongs to the system vs the individual agents

Your intuition is directionally right: in a multi-agent system, the higher layers belong primarily to the **system**, while the lower layers become more **agent-specific**. But the useful refinement is this:

- The top layers are not merely "global ideas."
- They need to be **translated into agent charters** so that each agent knows its role in the larger system.

That translation step is where most multi-agent systems either become coherent or drift.

### Recommended scope by layer

| Layer | What it is | Primary scope | Secondary scope |
|---|---|---|---|
| 1 | Mission / vision / north star | System | Referenced by every agent |
| 2 | Strategic objectives | System | Derived into agent-specific contribution goals |
| 3 | Operating principles | System | Agent-specific refinements where needed |
| 4 | Guardrails / approval rules / decision rights | System | Agent-specific stricter rules |
| 5 | Playbooks / SOPs / repeated workflows | Agent or shared capability | Shared when multiple agents use the same workflow |
| 6 | Task and decision management engine | System capability | Accessed by agents through an interface contract |

### The practical implication
For a multi-agent OpenClaw deployment, **Layers 1-4 should be designed centrally once**, and then each agent should receive a **derived version** of them that answers five questions:

1. What is my role in the system?
2. Which system objectives am I helping advance?
3. Which principles matter most in my lane?
4. What am I allowed to do without approval?
5. When do I hand off, escalate, or defer to another agent or the task/decision engine?

That derived artifact is what should primarily live in the agent's `AGENTS.md`.

---

## 2) What is probably missing today
Based on your description, the likely gap is not Layer 5 or Layer 6.

- **Layer 5** already exists in some form: you already have a large number of markdown files that tell agents how to work.
- **Layer 6** is something you intend to build separately as a task and decision management engine.

So the immediate problem is probably that the system lacks a coherent **decision spine** in Layers 1-4:

1. **Mission:** what the whole system is fundamentally for.
2. **Strategic objectives:** what the system should optimize for now, in ranked order.
3. **Operating principles:** how the system should resolve ambiguity and common friction points.
4. **Guardrails:** what requires approval, what is forbidden, and which agent has which decision rights.

Without those top layers, existing playbooks become local optimizers. Each agent may follow its own process correctly, while the overall system still drifts.

---

## 3) The right mental model for a multi-agent OpenClaw deployment

The best way to think about this is as a **two-tier direction architecture**:

### Tier A - Human governance documents
These are your source-of-truth documents. They are for **you and your operators**, not primarily for direct prompt injection.

They define:
- the system's purpose
- the system's priorities
- shared policies
- agent roles
- interface contracts
- classification of processes and playbooks

### Tier B - Agent runtime context
These are the files and config surfaces that OpenClaw actually uses at runtime.

They include:
- `AGENTS.md`
- `SOUL.md`
- `USER.md`
- `TOOLS.md`
- `HEARTBEAT.md`
- `~/.openclaw/openclaw.json`
- shared or per-agent skills

This separation matters because OpenClaw auto-injects only recognized bootstrap files, and each agent has its own workspace and sessions. There is no built-in global `SYSTEM.md` that every agent automatically shares. [OC2][OC8]

### The key design principle
**Write direction once at the human governance level; execute it many times at the agent level.**

That avoids both failure modes:
- **No direction**: agents drift because there is no shared operating logic.
- **Too much duplication**: every agent has a hand-edited wall of prose that diverges over time.

---

## 4) Where Layers 1-4 should be implemented in OpenClaw

## 4.1 The short answer
No: **Layers 1-4 should not each become separate new always-on markdown files**.

Instead, they should be split across three implementation surfaces:

1. **Human-side governance docs**  
   Source of truth for system direction. Good for version control and discussion, but not relied on as direct runtime context.

2. **Per-agent built-in bootstrap files**  
   The runtime expression of that direction, especially `AGENTS.md`, and secondarily `SOUL.md` and `USER.md`.

3. **Gateway config (`~/.openclaw/openclaw.json`)**  
   The place for hard enforcement: routing, tool policies, sandboxing, channel rules, session scope, and agent-specific access profiles. [OC4][OC7][OC8]

## 4.2 The recommended mapping

### Layer 1 - Mission / vision
**Canonical home:** `governance/system-charter.md`  
**Runtime home:** a concise version in every relevant agent's `AGENTS.md`

Why:
- The mission should be centrally authored and stable.
- But every agent needs to see the same short north star at runtime.

### Layer 2 - Strategic objectives
**Canonical home:** `governance/system-charter.md`  
**Runtime home:** each agent's `AGENTS.md`, with the relevant objective subset or contribution statement

Why:
- Objectives are system-level.
- Agents need a translated version: "which objectives do I serve, and in what priority order?"

### Layer 3 - Operating principles
**Canonical home:** `governance/system-charter.md` or `governance/policy-register.md`  
**Runtime home:** primarily `AGENTS.md`; secondarily `SOUL.md` for tone/persona-aligned principles

Why:
- Principles are usually cross-agent rules for resolving ambiguity.
- If a principle must govern sub-agents, do not rely on `SOUL.md` alone because sub-agent context injects only `AGENTS.md` and `TOOLS.md`. [OC5][OC6]

### Layer 4 - Guardrails / approval matrix / decision rights
**Canonical home:** `governance/policy-register.md`  
**Runtime home:** both `AGENTS.md` and `~/.openclaw/openclaw.json`

Why:
- The prose version belongs in `AGENTS.md` so the agent can reason about it.
- The non-negotiable version belongs in config so the system can enforce it.

Examples of config-level implementation:
- channel and DM policy
- group mention rules
- per-agent tool allow/deny
- sandbox settings
- per-agent access profiles
- sub-agent defaults
- session scoping and reset behavior [OC4][OC7][OC8]

### Important conclusion
For Layers 1-4, the right implementation is usually **not new runtime file types**.  
It is:

- **one or two source-of-truth governance docs**, plus
- **compiled or manually synchronized content inside `AGENTS.md`**, plus
- **config enforcement in `openclaw.json`**

---

## 5) The recommended file architecture

## 5.1 Human-side governance layer (source of truth)
These files are for governance, editing, review, and version control.

```text
governance/
  system-charter.md
  policy-register.md
  agent-catalog.md
  playbook-inventory.md
  task-decision-engine-contract.md
```

### `governance/system-charter.md`
This is the main home for Layers 1-3:

- mission / vision
- ranked strategic objectives
- operating principles
- system-level trade-off logic

### `governance/policy-register.md`
This is the main home for Layer 4:

- guardrails
- approval thresholds
- escalation rules
- decision rights
- system-wide risk policy

### `governance/agent-catalog.md`
This should define, for each agent:

- role
- responsibilities
- non-responsibilities
- inputs
- outputs
- handoff rules
- dependencies on other agents
- tool profile and risk profile

This is where system direction becomes a portfolio of roles.

### `governance/playbook-inventory.md`
Do not rewrite all existing playbooks. Instead, inventory and classify them:

- which are reusable playbooks
- which are policies
- which are standards
- which are instructions
- which are references

### `governance/task-decision-engine-contract.md`
This is the interface definition for your planned Layer 6 engine.

It should specify:
- what counts as a task
- what counts as a decision
- required fields
- ownership model
- read/write expectations for agents
- when the engine is the source of truth vs when `MEMORY.md` is enough

This avoids building a second memory system by accident.

---

## 5.2 Agent runtime layer (what OpenClaw actually uses)
Each agent should still rely on the built-in OpenClaw files.

```text
<agent-workspace>/
  AGENTS.md
  SOUL.md
  USER.md
  TOOLS.md
  HEARTBEAT.md
  skills/
```

### `AGENTS.md` - the main runtime home for Layers 1-4
This should be the **agent charter**, not a generic note file.

For a multi-agent system, each agent's `AGENTS.md` should contain:

1. A short system mission excerpt
2. The system objective hierarchy that matters to this agent
3. The agent's role and non-role
4. The principles it should use when making trade-offs
5. Its approval and escalation rules
6. Its handoff rules
7. How it should use shared playbooks
8. How it should use the future task/decision engine

This is the most important runtime file because `AGENTS.md` is the natural home for behavior, priorities, and memory use, and because sub-agents receive `AGENTS.md` while they do not receive `SOUL.md` or `USER.md`. [OC2][OC6]

### `SOUL.md` - identity, tone, and stable persona boundaries
Use this for:
- identity
- tone
- voice
- stable interaction boundaries

Do **not** make this the sole home for mandatory system rules.

### `USER.md` - what good output looks like for the user
Use this for:
- user preferences
- output standards
- quality bar
- formatting and drafting expectations

This is especially useful when several agents serve the same user but produce different kinds of outputs.

### `TOOLS.md` - tool conventions only
Use this for:
- local tool notes
- environment quirks
- workflow hints
- path conventions

Do **not** use `TOOLS.md` as if it were a security or policy layer. OpenClaw explicitly says it does not control tool availability. [OC2]

### `HEARTBEAT.md`
Keep this small. It is for periodic reminders, not for carrying your system strategy.

---

## 5.3 Config layer (hard control)
Use `~/.openclaw/openclaw.json` for everything you do **not** want to leave to model interpretation.

In a multi-agent system, that usually includes:

- which agents exist
- which channels or senders route to which agents
- which tools each agent can use
- sandbox mode per agent
- session scoping
- DM and group policy
- mention requirements
- sub-agent settings
- automation such as hooks and heartbeat [OC4][OC7][OC8]

OpenClaw also supports `$include`, so large configs can be split into multiple files. That is useful when you want to manage agents, bindings, and policies separately. [OC7]

Recommended pattern:

```text
~/.openclaw/
  openclaw.json
  agents.json5
  bindings.json5
  access-policies.json5
```

---

## 5.4 Shared playbooks
Because OpenClaw is multi-agent, shared playbooks should usually live in **shared skills**, not be copied into every workspace.

OpenClaw supports:
- per-agent skills in `<workspace>/skills`
- shared skills in `~/.openclaw/skills`
- additional shared skill directories via `skills.load.extraDirs` [OC9]

That means your existing Layer 5 material should generally be handled as follows:

- if several agents use it, put it in shared skills or a shared process library
- if only one agent uses it, keep it in that agent's workspace skill set
- if it is human governance rather than executable procedure, keep it out of always-on prompt context

---

## 6) A practical process for establishing Layers 1-4 first

Because your real problem is probably the missing top four layers, the process should be designed to produce those before you touch playbooks.

## Step 1 - Map the system as it exists now
Create a baseline inventory:

- Which agents exist?
- What does each agent actually do today?
- Which channels or triggers route to which agents?
- Which tools can each agent access?
- What playbooks already exist?
- Where has drift shown up?

Output:
- first draft of `governance/agent-catalog.md`
- a short drift log with 10-20 recent examples

This is important because principles and guardrails should come from real friction, not abstract ideals.

## Step 2 - Define the system mission
Write one paragraph that answers:
- What is the system primarily for?
- What is it not for?
- What does "improved state" mean over the next 30-90 days?

Example prompts to answer:
- Is the system mainly for strategic research support?
- Client deliverable production?
- Executive assistance and coordination?
- A hybrid, with one clearly dominant mode?

The mission must be specific enough that agents can self-correct.

Output:
- `governance/system-charter.md` version 0.1, mission section

## Step 3 - Rank the system objectives honestly
Pick 3-5 objectives and rank them.

This ranking is not cosmetic. It defines what the system should do when it cannot optimize everything at once.

Questions to force honesty:
- If speed and correctness conflict, which wins?
- If autonomy and caution conflict, which wins?
- If polished output and reduced cognitive load conflict, which wins?
- If local agent optimization hurts system coherence, which wins?

Output:
- `governance/system-charter.md` objective section

## Step 4 - Derive principles from actual failure modes
Do not brainstorm principles in the abstract.  
Instead, review drift incidents and convert them into rules.

Pattern:
- "The system tends to over-act without asking" -> principle about approval thresholds
- "The system optimizes for polished prose instead of moving work forward" -> principle about action over polish
- "Agents duplicate work instead of handing off cleanly" -> principle about ownership and interfaces
- "The system forgets why something was decided" -> principle about decision rationale capture

Output:
- 5-7 operating principles in `governance/system-charter.md`

## Step 5 - Define the guardrail matrix
Write explicit rules under three headings:

- **Ask first**
- **Never**
- **Allowed by default**

Then define:
- which agent can make which kinds of decisions
- which actions are reversible vs irreversible
- which actions require a human checkpoint
- which actions are delegated to the future task/decision engine

Output:
- `governance/policy-register.md`
- config changes for `openclaw.json`

## Step 6 - Derive the agent charters
For each agent, write a short derived charter with:

- role
- non-role
- objective contribution
- local decision rights
- escalation triggers
- interfaces and handoffs
- shared playbooks it should use
- expected relationship to the task/decision engine

This is the content that should become the agent's `AGENTS.md`.

Output:
- one charter per agent
- compiled runtime bootstrap files

## Step 7 - Run, observe, tighten
Run the system for a week. Then review drift incidents.

When a failure occurs, ask:
1. Was the system mission unclear?
2. Were objectives ranked wrongly?
3. Was a principle missing?
4. Was a guardrail missing?
5. Was the problem really a playbook issue?
6. Should the future task/decision engine own this instead?

This avoids patching every problem at the wrong layer.

---

## 7) How to classify the existing markdown files you already have

Since you already have many markdown files, the main need is probably **classification**, not wholesale rewriting.

Use this taxonomy:

| Type | What it means | Best home | Runtime treatment |
|---|---|---|---|
| Policy | Mandatory rule, threshold, or approval requirement | `governance/policy-register.md` | Distill into `AGENTS.md` and config |
| Standard | Quality bar or output standard | `governance/` or shared docs | Distill into `USER.md` or skill output specs |
| Process | Cross-agent or multi-step operating flow | shared process library | Read on demand or convert to shared skill if executable |
| Playbook | Repeatable executable workflow | shared skills or workspace skills | Keep as Layer 5 |
| Instruction | Narrow task or tool note | `TOOLS.md` or skill appendix | Keep local and concise |
| Reference | Background knowledge | docs/reference area | Not always-on; read when needed |

### The key recommendation
Do not reclassify files just for tidiness. Reclassify them only when that changes **how they are injected, enforced, or invoked**.

For example:
- A true **policy** should influence `AGENTS.md` and maybe config.
- A true **playbook** should live in skills.
- A **reference note** should not consume always-on context.

---

## 8) How to treat Layer 6 without duplicating it

You said you want Level 6 to become a **task and decision management engine**. That is the right direction.

The mistake to avoid is building a second, shadow version of that system in markdown.

### Recommended approach
Treat Layer 6 as a **separate system capability** with an interface contract, not as a long prompt file.

Your direction documents should define:
- when agents must consult the engine
- when they must update it
- what belongs there vs what belongs in memory
- what must be recorded about decisions, including rationale

A useful rule of thumb:

- **Operational state** belongs in the task/decision engine.
- **Durable preferences and identity-level context** belong in `MEMORY.md`.
- **Runtime behavior rules** belong in `AGENTS.md`.
- **Hard enforcement** belongs in config.

### Minimal runtime contract to put in `AGENTS.md`
Until the engine exists, the wording can be simple:

- Before acting on multi-step work, check the task/decision system if available.
- After making or receiving a substantive decision, record the outcome and the reasoning in the task/decision system.
- Do not treat `MEMORY.md` as the source of truth for active tasks.

That keeps Layer 6 conceptually present without duplicating it.

---

## 9) The direct answer to your file-structure question

### Should Layers 1-4 become new markdown files like `policies.md`?
**Not as primary runtime files.**

You can absolutely create governance docs with names like:
- `system-charter.md`
- `policy-register.md`
- `agent-catalog.md`

But those should be treated as **human-governed source documents**, not as the main always-injected runtime mechanism.

### What should be built into the actual OpenClaw runtime?
Primarily:

- `AGENTS.md`
- `SOUL.md`
- `USER.md`
- `TOOLS.md`
- `HEARTBEAT.md`
- `~/.openclaw/openclaw.json`

### Which built-in file carries the most weight?
`AGENTS.md`

That is where the derived agent charter should live:
- mission excerpt
- objective hierarchy
- principles
- guardrails
- handoffs
- interaction with playbooks and the task/decision engine

### What belongs in config instead of markdown?
Anything where "please follow this" is not good enough:
- tool access
- sandboxing
- routing
- channel rules
- group mention gating
- session scoping
- risky outbound behavior constraints [OC4][OC7][OC8]

---

## 10) Recommended minimal operating model
If you want the simplest robust setup, use this:

### Human-side source docs
```text
governance/
  system-charter.md
  policy-register.md
  agent-catalog.md
  playbook-inventory.md
  task-decision-engine-contract.md
```

### Per-agent runtime files
```text
workspace-<agent>/
  AGENTS.md
  SOUL.md
  USER.md
  TOOLS.md
  HEARTBEAT.md
  skills/
```

### Gateway config
```text
~/.openclaw/
  openclaw.json
  agents.json5
  bindings.json5
  access-policies.json5
```

### Operating rule
- Write direction centrally.
- Render it into each agent.
- Enforce it in config.
- Keep playbooks where they already live.
- Let the future task/decision engine own operational state.

If you have more than a few agents, automate the rendering of `AGENTS.md`, `SOUL.md`, and `USER.md` from the governance docs. If you have only a small number of agents, manual synchronization is acceptable at first, but the governance docs should still be the source of truth.

---

## 11) Optional advanced mechanisms in OpenClaw
If you want a more sophisticated setup later, OpenClaw gives you some options:

- **Shared skills** in `~/.openclaw/skills` for common playbooks across agents [OC9]
- **`bootstrap-extra-files` hook** to inject additional recognized bootstrap basenames from configured paths, though this is an advanced pattern and still preserves the sub-agent allowlist [OC5]
- **Config `$include`** to split large multi-agent configurations into manageable files [OC7]

These are useful, but they are not a substitute for getting the governance architecture right first.

---

## 12) Final recommendation
For your situation, I would focus the next round on one concrete deliverable:

**Create a system-level direction package for Layers 1-4, then derive agent charters from it.**

That means:

1. Define the system mission
2. Rank the system objectives
3. Convert actual friction into operating principles
4. Write a guardrail and approval matrix
5. Derive each agent's charter
6. Implement the hard parts in config
7. Leave existing playbooks in place
8. Treat the future task/decision engine as a separate capability with an interface contract

That is the cleanest way to add direction without duplicating your existing process documentation or pre-building a second decision engine.

---

# Appendix A - Minimal template: system charter
```md
# System mission
What the overall OpenClaw system is for, what "better" means, and what it is explicitly not for.

# Strategic objectives (ranked)
1. ...
2. ...
3. ...

# Operating principles
- When trade-offs appear, prefer ...
- When uncertainty is material, ...
- When work crosses agents, ...
- When a decision is made, ...

# Trade-off order
Guardrails > Objectives > Principles > Style

# Notes
What has frustrated us so far, and what this charter is designed to prevent.
```

# Appendix B - Minimal template: policy register
```md
# Ask first
- ...

# Never
- ...

# Allowed by default
- ...

# Decision rights
- Agent A may ...
- Agent B may ...
- Human approval required for ...

# Enforcement map
- Config enforced:
- AGENTS enforced:
- Playbook enforced:
- Task/decision engine enforced:
```

# Appendix C - Minimal template: agent charter
This is the material that should be compiled into an agent's `AGENTS.md`.

```md
# System mission excerpt
...

# Agent role
What this agent owns.

# Agent non-role
What this agent should not own.

# Objective contribution
Which system objectives this agent primarily serves, in order.

# Operating principles for this agent
- ...
- ...

# Guardrails and escalation
- Ask first:
- Never:
- Hand off when:

# Interfaces
- Inputs from:
- Outputs to:
- Shared playbooks:
- Task/decision engine usage:
```

# References
- **[OC1] OpenClaw System Prompt** - workspace bootstrap injection and skill loading  
  https://docs.openclaw.ai/concepts/system-prompt

- **[OC2] OpenClaw Agent Workspace** - what `AGENTS.md`, `SOUL.md`, `USER.md`, `TOOLS.md`, and `HEARTBEAT.md` mean  
  https://docs.openclaw.ai/concepts/agent-workspace

- **[OC3] OpenClaw Token Use and Costs** - injected bootstrap files and prompt size implications  
  https://docs.openclaw.ai/reference/token-use

- **[OC4] OpenClaw Configuration / Configuration Reference** - config, tool policy, sandboxing, routing, and `$include`  
  https://docs.openclaw.ai/gateway/configuration  
  https://docs.openclaw.ai/gateway/configuration-reference

- **[OC5] OpenClaw Hooks** - `bootstrap-extra-files` behavior and limits  
  https://docs.openclaw.ai/automation/hooks

- **[OC6] OpenClaw Sub-Agents** - sub-agent context only injects `AGENTS.md` and `TOOLS.md`  
  https://docs.openclaw.ai/tools/subagents

- **[OC7] OpenClaw Multi-Agent Routing** - per-agent workspace, sessions, and routing  
  https://docs.openclaw.ai/concepts/multi-agent

- **[OC8] OpenClaw Security** - trust-boundary model and why hard controls belong in config  
  https://docs.openclaw.ai/gateway/security

- **[OC9] OpenClaw Skills** - per-agent vs shared skills  
  https://docs.openclaw.ai/tools/skills
