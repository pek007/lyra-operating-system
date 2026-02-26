# ARTIFACT_ACTIVATION_MODEL_V1.md

Status: Active draft v1  
Owner: Peter (governance), Lyra (orchestration), Engineering role (implementation)

## Objective
Ensure every Markdown/JSON artifact in the Lyra OS is either actively integrated into runtime behavior or explicitly marked as archival.

## Core principle
An artifact is “real” only if it has an activation path.

---

## 1) Activation classes (required)

Every artifact must be assigned one class:

1. **Injected Kernel**
   - Always loaded into runtime context each run
   - Must be short, stable, and truncation-safe

2. **Retrieval Module**
   - Indexed and queryable on demand
   - Used via explicit retrieval/citation flow

3. **Controller Input**
   - Read by a reconciler/compiler
   - Translated into enforceable runtime config/state

4. **Archive**
   - Human-readable reference only
   - No direct runtime dependency

No unclassified artifacts allowed in governed directories.

---

## 2) Activation Registry schema

Create and maintain: `knowledge/registries/ARTIFACT_ACTIVATION_REGISTRY.md`

Minimum fields per entry:
- `artifact_id` (stable ID)
- `path` (workspace-relative)
- `artifact_type` (`policy|registry|runbook|memory|evidence|report|other`)
- `activation_class` (`kernel|retrieval|controller|archive`)
- `consumers` (`agent_runtime|control_panel|cron|controller|human`)
- `enforcement_mode` (`advisory|tool_policy|sandbox|approval|n/a`)
- `namespace` (`os|px|shared`)
- `owner`
- `review_cadence` (`weekly|monthly|quarterly`)
- `last_reviewed_at` (RFC3339/date)
- `status` (`active|deprecated|candidate`)

Optional:
- `index_priority` (`high|medium|low|excluded`)
- `compile_target` (runtime policy target)
- `deprecation_note`

---

## 3) Kernel policy (Injected Kernel)

### Rules
1. Kernel files must fit injection budget and avoid truncation of critical lines.
2. Cross-agent non-negotiables belong in kernel-safe artifacts.
3. Persona/voice content is allowed but cannot replace enforceable policy.

### Validation
- Context inspection must verify:
  - file present
  - size under cap
  - no critical-line truncation

### Design guidance
- Keep kernel content concise and evergreen.
- Move operational detail to retrieval/controller layers.

---

## 4) Retrieval module policy

### Rules
1. Retrieval modules must be indexed and namespace-scoped.
2. High-risk decisions require retrieval-backed references.
3. Retrieval outputs should include path/line provenance where possible.

### Indexing guidance
- Prefer indexing distilled, decision, and policy artifacts first.
- Exclude noisy/inbox sources by default unless explicitly enabled.

### Quality controls
- Track retrieval hit rate and citation coverage.
- Detect stale modules via low-use + low-relevance signals.

---

## 5) Controller input policy

### Intent
Controller-input artifacts are declarative desired state.
A controller compiles/reconciles them into enforceable runtime controls.

### Required compile outputs (examples)
- tool allow/deny policies
- sandbox/workspace access constraints
- approval gate mappings
- scheduling/runtime policy updates

### Rules
1. Compile must be deterministic and versioned.
2. Compile failures block promotion for affected changes.
3. Effective runtime state must be inspectable and auditable.

---

## 6) Archive policy

### Rules
1. Archive artifacts are not assumed by runtime behavior.
2. Archive artifacts must be clearly labeled to avoid false confidence.
3. Archived items can be promoted to active classes via review + registry update.

---

## 7) Activation lifecycle

1. Draft artifact
2. Classify activation class
3. Register in activation registry
4. Add tests/validators (class-specific)
5. Promote to active use
6. Monitor usage/health
7. Reclassify or deprecate as needed

---

## 8) Verification and KPIs

Track weekly/monthly:
- % artifacts classified (target: 100% for governed dirs)
- Kernel truncation incidents (target: 0)
- Retrieval citation coverage on policy/risk decisions
- Controller compile success rate
- Drift between declared policy and effective runtime controls
- Archive false-assumption incidents (using archived file as if active)

---

## 9) CI and runtime checks

### CI checks
- registry schema lint (required fields)
- no unclassified artifacts in governed paths
- compile dry-run for controller-input artifacts
- retrieval index inclusion/exclusion policy check

### Runtime checks
- context budget/truncation diagnostics for kernel
- retrieval provenance logging
- policy compile status visibility in control panel

---

## 10) Rollout plan (3 weeks)

Week 1:
- Create activation registry and seed current artifacts
- Classify top-level OS/control artifacts
- Add initial lint rule for unclassified files

Week 2:
- Mark kernel candidates and trim for truncation safety
- Define retrieval module set and indexing priorities
- Add citation requirement for high-risk decision outputs

Week 3:
- Define first controller compile target (e.g., tool policy mapping)
- Add compile dry-run + status reporting
- Publish first activation coverage report

---

## 11) Done definition (v1)

v1 is complete when:
1. Activation registry exists and covers governed artifacts.
2. Every active artifact has one explicit activation path.
3. Kernel content passes truncation-safe checks.
4. Retrieval modules are indexed with namespace boundaries.
5. At least one controller compile path is operational and auditable.
6. Control panel can display activation status and exceptions.
