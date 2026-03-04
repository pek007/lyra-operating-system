---
title: "Policy-as-Code Decision Rights for Lyra TDE"
date: 2026-03-01
source: deepresearch
ingest_from: "telegram attachment file_97"
tags: [external-analysis, deepresearch, policy-as-code, opa, task-decision-engine]
decision_relevance: "mutation authority and approval governance model"
confidence: tbd
status: archived-source
---

# Policy-as-Code Decision Rights for Lyra TDE

## Policy domain model

A practical policy-as-code (PaC) model for Lyra’s Task & Decision Engine (TDE) should treat **decision rights** and **mutation authority** as first-class, machine-checkable constraints, while keeping “what should we do?” (recommendation) explicitly separate from “what are we allowed to do?” (authority/approval). This separation is a core requirement for auditability: recommendations can be probabilistic or heuristic; authority must be deterministic and enforceable.

### Subjects

In this model, the “subject” is not just a user or an agent—it’s the combination of **who is acting**, **which durable job they are acting under**, and **what execution surface is being used**.

**Actor identity (the caller)**
- **Human**: authenticated person (e.g., Peter).
- **Agent runtime**: a persistent control-tower agent, a spawned sub-agent, or an external lane executor (e.g., a coding workbench).
- **Service account**: non-interactive caller (e.g., scheduled reconciler).

**Job context (the durable responsibility contract)**
- **Job**: stable scope of responsibility and decision rights (“Head of Security”, “Software Developer”, “Auditor”, etc.). Jobs express: allowed scopes, escalation triggers, evidence standards, and acceptable side effects.
- **Assumption/delegation**: a job can be “assumed” by an execution surface (agent/sub-agent), similar to how role assumption works in other security models: you audit both the actor and the assumed job.

**Roles (policy grouping)**
- Functional governance roles (Security, Finance, Operations, Research, Product, etc.)—useful for routing decisions and for approvals.
- Execution roles (Control Tower, Build Agent, Security & Audit agent, Ops/Control agent, Content Delivery agent, etc.)—useful for per-surface permission envelopes.

The practical result is that a policy decision should be computed from **(actor × job × execution surface)** rather than only actor. This prevents a common failure mode in agentic systems: “the same agent sometimes behaves like an admin,” without a durable, auditable reason.

### Resources

The resources below match Lyra’s stated operating primitives (tasks, decisions, evidence, change artifacts, actions) and are designed to be policy-addressable.

**Task**
- Durable work item with a lifecycle (e.g., inbox → triage → active → waiting → done → archived), owner, and required readiness/done criteria.
- Policy-relevant attributes: owner, lane/job, status, door type (Type 1 / Type 2), risk class, dependency state, evidence/link completeness.

**Decision**
- A governance object that represents a question to be decided, options, recommendation (advisory), and approval requirements.
- Policy-relevant attributes: decision type (approve/reject/choose/escalate/review), risk level, urgency, required evidence freshness, required approver roles/count.

**Evidence**
- An object validating claims used in decisions or changes.
- Policy-relevant attributes: evidence type, source, collection method, freshness timestamp, confidence, sensitivity.

**Work Order / Change Artifact**
- Structured intent (“Work Order”) and structured record of what changed and why (“Change Artifact”).
- Policy-relevant attributes: risk class, verification plan/evidence, deviation flags, sign-off status.

**Action**
- Atomic side-effect that a runtime might execute (send message, modify config, merge PR, enable skill, write file, call external API).
- Policy-relevant attributes: side-effect class, environment scope, tool identity, target system, target data class.

### Actions

Keep actions small and enumerable. The minimum action vocabulary to start:

- **create**: create a new resource instance (task/decision/evidence/change/action record).
- **update**: mutate fields not represented as lifecycle transitions (metadata updates, evidence annotation).
- **transition**: state machine transitions (task status changes, decision status changes).
- **approve**: record approvals that unblock other actions.
- **reject**: reject proposals/decisions/changes.
- **execute**: perform a side effect (tool invocation, merge, send, config change).

In practice, you will also want **propose** (non-mutating request to stage a change) as a safer default for agent autonomy; “execute” should often be blocked pending approval for high-risk contexts.

### Context

OPA-style PaC works best when policies rely on explicit, stable attributes. For Lyra TDE, the minimum context dimensions are:

- **Risk level**: low / medium / high / critical.
- **Decision door type**: Type 1 (hard-to-reverse) vs Type 2 (reversible).
- **Data class**: a small initial taxonomy (example: public / internal / confidential / restricted). This should be treated as *an initial assumption* until Lyra defines a canonical classification standard in governance.
- **Environment**: sandbox vs production; and the target system boundary (local workspace, OpenClaw config, external systems).
- **Time**: current time, SLA windows (e.g., evidence freshness SLA), and “emergency mode” windows.
- **Request metadata**: correlation ID, idempotency key, execution lane (persistent vs spawned vs external), and whether the request is a replay/retry.

## Decision rights matrix

The goal of the decision rights matrix is to define a **default safe operating stance** that is both machine-enforceable and low-theatre: it should describe what is actually allowed to happen automatically, what must be staged for human approval, and what is forbidden regardless of rationale.

This initial matrix assumes three control layers:

- **Worker agents**: bounded executors (specialists).
- **Control Tower**: orchestration and gate enforcement.
- **Human decision owner**: ultimate authority, especially for high-risk actions.

### Autonomous allowed actions

Autonomous actions are those that can execute without human approval, provided policy conditions are met (context, scope, evidence, and limits).

**Read-only operations**
- Read tasks/decisions/evidence/change history.
- Run queries, generate summaries, and compute recommendations (recommendation logic is always allowed, but must be labeled as advisory).

**Governance state shaping (low-risk)**
- Create tasks in inbox/triage, propose decompositions, propose transitions.
- Create decision drafts and evidence requests, but not approve high-risk decisions.
- Attach non-sensitive evidence records and compute freshness/confidence (no external side effects implied).

**Internal documentation hygiene**
- Low-risk internal documentation improvements (clarity, consistency) **within** the agent’s/write scope and without crossing trust boundaries (no credentials, no external publishing).

**Execution of pre-approved, low-risk runbooks**
- “Auto-fix” routines explicitly whitelisted as safe and deterministic (the whitelist must be policy data, not an LLM judgment call).

### Approval-required actions

These are allowed only “with obligations” (i.e., permitted in principle, but blocked until approval obligations are satisfied).

**External communications and publishing**
- Sending email, creating calendar events, posting to external channels, or publishing client-facing deliverables.

**Trust boundary and security boundary changes**
- Expanding access, rotating credentials (except incident break-glass), modifying security posture, changing tool allowlists, adding new integration endpoints.

**Production-affecting mutations**
- OpenClaw gateway configuration changes (routing, auth, channel policy, tool policy, sandbox boundaries).
- Enabling new skills/tools in production runtime contexts.
- Merging code / releases when changes are not explicitly “low risk” or lack required change artifacts and verification evidence.

**Cost-bearing decisions**
- Any action that commits spend beyond a predefined micro-budget, changes subscription posture, or increases recurring usage risk.

### Forbidden actions

Forbidden actions should be rare, crisp, and non-negotiable: they define the “hard walls” that automation cannot cross.

- Exfiltration of private data or bypassing configured safeguards/trust boundaries.
- Executing production changes using unverifiable/unaudited pathways (e.g., “just run a shell command” without an action record and policy decision).
- Creating direct hard runtime dependencies across product boundaries without an explicit architecture decision record (ADR).
- Performing irreversible or high-impact actions when required evidence freshness or required approvals are absent (no implied “it’s probably fine”).

### Emergency override path

Emergency overrides are necessary in real systems; the critical design point is that overrides are **structured**, **rare**, and **post-audited**.

A practical break-glass design:

- **Trigger condition**: an explicit `emergency=true` context plus a linked incident identifier (resource: incident record or decision record).
- **Scope**: override grants a narrow set of permissions (e.g., credential rotation, service shutdown, rollback) for a limited time window and environment.
- **Obligations** (blocking after the fact, if needed):
  - Immediate notification to human decision owner.
  - Mandatory creation of a decision record and evidence artifact within a fixed SLA (e.g., 24 hours).
  - Mandatory post-incident review that either ratifies the action or flags it as a policy violation for remediation.

This maps well to “allow-with-obligations”: the policy can allow execution *only* if the emergency context is present, and can require a follow-up action set as obligations.

## Policy evaluation flow and audit logging

### Architectural flow

OPA-style integration is best implemented as a **Policy Decision Point (PDP)** that is queried by multiple **Policy Enforcement Points (PEPs)**:

- TDE API (all mutations and executions go through here).
- Tool gateway wrappers (for defense-in-depth: ensure high-risk tools cannot execute without TDE authorization).
- Scheduled jobs (reconciliation, sweeps) as first-class subjects.

For OPA integration, deploying entity["organization","Open Policy Agent","policy engine"] as a sidecar or host-level daemon is the recommended default for low-latency, high-availability decisions. citeturn0search3

A minimal enforcement sequence:

1. **Request received**: actor requests `{action, resource}`.
2. **Normalize context**: derive effective risk class from action type + target environment + resource attributes (do not trust caller-provided risk classification for gating).
3. **Policy query**: call OPA Data API with structured input (named decision). citeturn0search3turn0search1
4. **Decision handling**:
   - allow → execute/mutate.
   - deny → reject, return reasons.
   - allow-with-obligations → create/stage decision record, start approval workflow, block side effect until obligations satisfied.
5. **Audit**: log request, policy decision, and resulting state transition (including denies).
6. **Execution**: for side effects, execute with idempotency keys and record outcome.

### Policy input schema

OPA decisions are computed from a caller-provided `input` document. The key to auditability is making this input **self-contained**, **stable**, and **minimally sufficient**.

A practical v1 input shape:

```json
{
  "request": {
    "request_id": "req_...",
    "idempotency_key": "idem_...",
    "correlation_id": "corr_...",
    "timestamp": "2026-03-01T12:34:56Z",
    "source": "tde_api|scheduled_job|tool_gateway",
    "lane": "persistent|spawned|external",
    "dry_run": false
  },
  "subject": {
    "kind": "human|agent|service_account",
    "id": "peter|lyra-main|agent-sec-001|svc-reconciler",
    "roles": ["control_tower", "security_audit", "build_agent"],
    "job": {
      "job_id": "JOB-SEC-001",
      "delegation": "assumed|direct"
    },
    "auth": {
      "method": "jwt|mtls|local",
      "assurance": "low|high",
      "break_glass": false
    }
  },
  "resource": {
    "type": "task|decision|evidence|change|action",
    "id": "OPS-2026-014|DEC-2026-0012|WO-...",
    "domain": "os|px|shared",
    "owner": "peter|lyra",
    "attributes": {
      "risk_level": "low|medium|high|critical",
      "door_type": "type1|type2",
      "data_class": "public|internal|confidential|restricted",
      "environment": "sandbox|prod",
      "status": "inbox|triage|active|waiting|done|archived"
    }
  },
  "action": {
    "type": "create|update|transition|approve|reject|execute",
    "name": "task.transition|decision.approve|openclaw.config.change|send.email",
    "params": {
      "to_status": "active",
      "fields": ["owner", "priority"],
      "tool": "github|shell|telegram"
    }
  },
  "context": {
    "time": {
      "local_tz": "Europe/Stockholm",
      "now": "2026-03-01T13:34:56+01:00"
    },
    "limits": {
      "max_cost_usd": 25,
      "max_actions": 1
    },
    "emergency": {
      "enabled": false,
      "incident_id": null
    }
  }
}
```

### Decision outputs

OPA is typically queried for a “named decision” and returns a result. The PaC framework for Lyra should standardize three outcomes:

- **allow**: action may proceed now.
- **deny**: action must not proceed.
- **allow-with-obligations**: action may proceed only after obligations are satisfied (an approval workflow, evidence refresh, additional logging, etc.).

While OPA’s core query response is whatever you define in policy, the system should standardize the decision shape returned by your policy package:

```json
{
  "allow": false,
  "decision": "deny|allow|allow_with_obligations",
  "reasons": ["missing_required_approval", "evidence_stale"],
  "obligations": [
    {
      "type": "require_approval",
      "approvers": ["peter"],
      "minimum_count": 1,
      "expires_at": "2026-03-02T00:00:00Z"
    },
    {
      "type": "require_evidence_freshness",
      "evidence_type": "security_audit",
      "max_age_hours": 24
    }
  ],
  "policy": {
    "package": "lyra.authz",
    "rule": "decision",
    "bundle_revision": "gitsha_or_semver",
    "issued_at": "2026-03-01T12:34:56Z"
  }
}
```

### Audit log schema

Auditability requires logging both:

1. **Policy evaluation** (why allowed/denied).
2. **Execution** (what actually happened).

OPA can emit decision logs that include the policy path queried, input, result, and bundle revision metadata, and can generate a `decision_id` per decision. citeturn0search0 This is especially valuable for offline debugging and audits, because it lets you correlate an application’s action with the exact policy bundle revision used at the time. citeturn0search0turn0search2

For correlation, OPA’s Data API supports a `decision_id` parameter; when decision logging is enabled, that identifier is included in the decision log event so you can join “TDE audit event” ↔ “OPA decision log event.” citeturn0search1turn0search0

A TDE-first audit event should minimally contain:

- `audit_event_id` (UUID)
- `timestamp`
- `request_id`, `correlation_id`, `idempotency_key`
- `actor` (subject identity + job context)
- `resource` (type/id + pre/post pointers or event IDs)
- `action` (type/name/params)
- `policy_decision`:
  - `decision` (allow/deny/allow_with_obligations)
  - `reasons[]`
  - `obligations[]`
  - `opa_decision_id` (if using OPA decision logs)
  - `policy_bundle_revision`
  - `policy_path` (OPA decision logs include `path`) citeturn0search0
- `approvals[]` (captured approvals, approver identity, timestamps)
- `execution`:
  - `executed` boolean
  - `tool_invocations[]` (tool name, target, outcome, duration)
  - `side_effect_summary`
  - `rollback_ref` (if applicable)

Because decision logs may include sensitive input, OPA supports a masking policy (`data.system.log.mask`) to erase or redact fields before logs are exported. citeturn0search0

## OPA and Rego policy examples and rollout

### Representative Rego snippets

These snippets illustrate the patterns that matter for Lyra: default deny, explicit allow, and allow-with-obligations for approvals.

**Default deny with structured decision**

```rego
package lyra.authz

default decision := {
  "allow": false,
  "decision": "deny",
  "reasons": ["default_deny"],
  "obligations": [],
}

# Helper: allow-with-obligations
allow_with_obligations(obligations, reasons) := {
  "allow": false,
  "decision": "allow_with_obligations",
  "reasons": reasons,
  "obligations": obligations,
}
```

**Read-only always allowed (low risk)**

```rego
package lyra.authz

decision := {
  "allow": true,
  "decision": "allow",
  "reasons": [],
  "obligations": [],
} if {
  input.action.type == "execute"
  input.action.name == "read.only"
}
```

**High-risk external send requires human approval (obligation)**

```rego
package lyra.authz

decision := allow_with_obligations(
  [{"type": "require_approval", "approvers": ["peter"], "minimum_count": 1}],
  ["external_send_requires_approval"]
) if {
  input.action.name == "send.email"  # could also include calendar, publish, etc.
}
```

**OpenClaw configuration changes: deny or require approval based on risk**

```rego
package lyra.authz

# Treat unknown as high risk: require approval
decision := allow_with_obligations(
  [{"type": "require_approval", "approvers": ["peter"], "minimum_count": 1}],
  ["openclaw_config_change_requires_approval"]
) if {
  input.action.name == "openclaw.config.change"
}

# Optional: allow low-risk (pure formatting) changes if explicitly labeled and scoped.
decision := {
  "allow": true,
  "decision": "allow",
  "reasons": [],
  "obligations": [{"type": "audit_required"}],
} if {
  input.action.name == "openclaw.config.change"
  input.resource.attributes.risk_level == "low"
  "control_tower" in input.subject.roles
}
```

**Emergency break-glass: allow only with incident linkage + post-audit obligation**

```rego
package lyra.authz

decision := {
  "allow": true,
  "decision": "allow",
  "reasons": ["break_glass_emergency"],
  "obligations": [
    {"type": "notify_owner", "who": "peter", "immediate": true},
    {"type": "create_decision_record", "within_hours": 24}
  ],
} if {
  input.context.emergency.enabled == true
  input.context.emergency.incident_id != null
  input.subject.auth.break_glass == true
  input.action.name == "security.credential.rotate"
}
```

### Versioning and rollout strategy

A rollout strategy that remains enforceable and audit-friendly in practice:

**Use OPA bundles, not ad hoc API updates**
- OPA documentation explicitly recommends bundles as the preferred way to update policies for most use cases, and bundles support updating policy and data without restarting OPA. citeturn0search1turn0search2

**Bundle contents and constraints**
- Bundles are `.tar.gz` archives that contain Rego policies and data that is loaded into OPA. citeturn0search2turn6search0
- OPA only loads bundle data files named `data.json` or `data.yaml` (other JSON/YAML files are ignored), and YAML data is converted to JSON. citeturn6search0turn6search1

**Integrity and provenance**
- Bundles can be digitally signed; OPA verifies signatures before activating a new bundle and retains the old bundle on verification failure, providing a strong integrity control against policy tampering. citeturn0search2turn6search0

**Progressive deployment**
- Maintain separate bundle channels (dev → staging → prod).
- Shadow mode: evaluate policy for every request but treat deny/obligations as advisory in non-prod until stable; compare “shadow decisions” vs observed actions to calibrate.
- Canary: roll a small subset of TDE instances (or a subset of action types) onto the new bundle revision; review deny/override rates before full rollout.

**Recovery**
- OPA can persist activated bundles to disk so it can start with the most recently activated bundle if the bundle server is temporarily unavailable. citeturn6search0

### Policy testing approach

Policy is software. Treat it as such:

**Unit tests with `opa test`**
- OPA provides a native testing framework where rules prefixed with `test_` are discovered and run; you can target subsets with `--run`, and you can fail builds if no tests executed using `--fail-on-empty`. citeturn1search0turn1search5
- Use coverage reporting to avoid “dead policy paths” that are never exercised. citeturn1search0

**Config and integration test tooling**
- entity["organization","Conftest","opa policy testing tool"] is widely used to test structured configuration against Rego policies and can complement `opa test` by testing real config artifacts used in deployments. citeturn1search6turn1search0

**Minimal test examples**
- Create fixtures representing: low-risk read-only, medium-risk internal changes, high-risk prod actions, emergency break-glass.
- Validate both the decision class (allow/deny/allow-with-obligations) and obligations content (approvers, evidence refresh, notification).

## Governance operations model

A PaC governance model is only “real” if it runs as an operational practice, not just a set of files.

### Policy review cadence

A pragmatic cadence that balances speed and stability:

- **Weekly operational review**: inspect top policy denials, approval latency, and break-glass events; tune obligations and defaults.
- **Monthly governance review**: authorize policy bundle upgrades to production; review job scopes and permission envelopes; incorporate learnings into policy tests.
- **Post-incident review**: mandatory for any break-glass execution; ensure follow-up obligations were satisfied; decide whether policy must change or whether a violation occurred.

OPA decision logs explicitly support auditing and offline debugging by capturing the decision, input, and bundle metadata; this makes weekly/monthly review materially easier than relying on scattered application logs. citeturn0search0

### Change control

A low-theatre, high-enforcement change control loop:

- All policy changes go through versioned change requests (PRs).
- Mandatory checks before merge:
  - `opa test` passes (and `--fail-on-empty` enabled).
  - Coverage threshold meets a minimum bar.
  - Policy bundle builds successfully and is signed (if you adopt signature verification). citeturn0search2turn1search0
- One responsible approver group (human decision owner or delegated senior approver role) owns “prod rollout” approval.
- Every production policy rollout records:
  - bundle revision identifier,
  - rollout time window,
  - rollback trigger.

OPA’s bundle approach supports frequent updates without restarts and discourages manual policy “hot edits,” which reduces the audit surface area. citeturn0search2turn0search1

### Policy drift detection

Drift is “policy says X but system behavior effectively does Y.” Detect it by instrumenting the enforcement boundary:

**Decision-log-based drift signals**
- Spike in denials for a class of actions.
- Frequent allow-with-obligations decisions that never get obligations satisfied (approval workflow stall).
- Increased break-glass usage (policy too strict or system too fragile).
- Unexpected decision paths or unknown action names.

OPA decision logs include `decision_id`, decision `path`, input, result, and bundle revisions, enabling correlation and trend analysis. citeturn0search0

**Control-plane drift signals**
- TDE action executed without an associated policy decision record (should be impossible if PEP is correct).
- Tool gateway invocation without TDE authorization (defense-in-depth violation).
- Approval recorded without matching obligation (approval system bug).

**Sensitive data controls**
- Enforce masking for known sensitive fields in decision logs to avoid turning audit logs into a data leak vector. citeturn0search0

## Recommendation for Lyra

### Lightweight initial implementation path

A v1 that is enforceable, auditable, and low-friction should do three things well:

**Adopt OPA as the single PDP**
- Deploy entity["organization","Open Policy Agent","policy engine"] alongside the TDE as a local daemon/sidecar and require all TDE mutation/execute endpoints to query it. This follows OPA’s integration guidance to keep decisions fast and highly available. citeturn0search3

**Focus enforcement on high-risk side effects first**
- Gate these action families immediately:
  - external sends/publishing,
  - production configuration changes,
  - enabling/expanding tools/integrations,
  - merges/releases/deployments.
- Leave low-risk internal “recommendation” and “proposal” flows autonomous, but require the system to create structured decision records when obligations appear.

**Make audit correlation non-negotiable**
- Each policy check should emit:
  - TDE audit event,
  - OPA `decision_id` correlation, and
  - policy bundle revision identifier.
- Use OPA decision logs as the canonical policy-evaluation ledger and store only a minimal “join key + outcome” in the TDE action ledger. citeturn0search0turn0search1

**Data layer approach (practical)**
- Treat job/role/permission envelopes and skill risk classes as **policy data**, not scattered logic.
- Build a bundle pipeline that produces `data.yaml`/`data.json` (bundle-compliant naming) and Rego modules, signs the bundle, and publishes it to a bundle server. OPA’s bundle loader only loads `data.json` or `data.yaml` as named files in the expected structure. citeturn6search0turn0search2

### Migration path to a stricter model

After v1 proves stable (low override rate, manageable approval latency, few false denials), tighten the model along three axes:

**From role-centric to job-centric ABAC**
- Expand from “agent role” → “job contract” as the main authorization input.
- Require explicit job assumption/delegation tokens so execution surfaces cannot implicitly “inherit” authority.

**Richer obligations and separation of duties**
- Introduce multi-approver rules for the highest-risk classes (e.g., security boundary changes + financial commitments).
- Make “risk downgrade” itself a governed action (only specific roles can reduce risk classifications).

**Stronger rollout controls**
- Signed bundles everywhere, with automated rollback on activation failures. citeturn0search2turn6search0
- Canary and shadow evaluation for policy changes affecting high-frequency decisions.
- Increase test rigor: coverage thresholds, regression tests for past incidents, and performance benchmarks for frequently evaluated rules. citeturn1search0turn1search4

**Operationalize drift detection as a product feature**
- Build a weekly “policy health” report powered by decision logs: top denies, top obligations, approvals SLA, break-glass events, and bundle revision distribution. OPA decision logs are explicitly structured to enable auditing and offline debugging of decisions. citeturn0search0