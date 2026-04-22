# Auth and Model-Route Failure Recovery Playbook v1

Status: Draft active playbook
Owner: Security
Date: 2026-04-22
Linked artifacts:
- `products/security/03-operating-model/RESILIENCE_INCIDENT_AND_RECOVERY_WORKFLOW_STANDARD_V1.md`
- `products/security/06-architecture/LYRA_OS_CRITICAL_CAPABILITY_HEALTH_MODEL_V1.md`
- `products/security/06-architecture/LYRA_OS_FAILURE_TAXONOMY_AND_COVERAGE_MATRIX_V1.md`
- `IR-001_INCIDENT_MINI_RUNBOOK.md`
- `OPENCLAW_OAUTH_FAILOVER_AND_CONFIG_VALIDATION_INCIDENT_2026-04-08.md`
- `products/improvement/04-execution/OPENCLAW_AUTH_RESILIENCE_CONTROL_VISIBILITY_DISPOSITION_2026-04-09.md`

## Purpose
Provide a bounded recovery playbook for auth and model-route failures in Lyra OS.

This playbook exists to handle situations where the intended primary model path becomes unavailable, unstable, degraded, or silently replaced by fallback behavior.

Typical examples include:
- OAuth refresh failure
- primary model authentication loss
- provider-route drift
- silent fallback to another provider/model
- unexpected cost drain due to fallback routing
- restored service that is not actually back on the intended primary route

## Capability in scope
Primary capability:
- `C2. Primary model auth and route capability`

Common related capabilities:
- `C3. Degraded-mode visibility and cost guardrail capability`
- `C7. Operator-facing health visibility capability`
- `C8. Post-change resilience verification capability`

## Failure-class mapping
Primary failure class:
- `F2. Auth and model-route failure`

Common secondary classes:
- `F3. Silent failover / cost-exposure failure`
- `F7. Detection and visibility failure`
- `F8. Post-change regression`

## When to use this playbook
Use when one or more are true:
- auth refresh or onboarding failure affects the intended primary model path
- the system stops using the intended primary route
- fallback route carries load unexpectedly
- spend/credit behavior suggests hidden fallback usage
- recovery appears successful but primary-route restoration is unverified

## Severity guide

### Use at least R-SEV-2 when:
- primary route is unavailable or non-trustworthy
- hidden fallback may be carrying meaningful load
- cost exposure or degraded-mode ambiguity is present
- unattended or critical automation depends on the affected route

### Use R-SEV-1 when:
- the outage combines with major active cost drain, major multi-lane outage, or no safe bounded recovery path

### Use R-SEV-3 when:
- degradation is contained, visible, and low-risk with a stable workaround

## Workflow

### Step 1. State the symptom clearly
Examples:
- "OpenAI Codex OAuth refresh failed and the primary route is unhealthy"
- "The system appears responsive, but may be serving from fallback rather than the intended primary route"
- "Fallback spend increased during primary-route instability"

## Step 2. Assess capability health honestly
Classify the primary model auth and route capability as:
- `healthy`
- `degraded`
- `failed`
- `unknown`

Guidance:
- if fallback is active but controlled and visible, treat as `degraded`
- if intended primary auth/route is unavailable or non-trustworthy, treat as `failed`
- if route identity cannot be established honestly, use `unknown`

## Step 3. Contain degraded-mode risk
Before pursuing full recovery, contain the most important downside.

Examples:
- stop or limit hidden fallback spend
- mark the system as degraded rather than healthy
- pause non-critical unattended load if route trust is weak
- avoid declaring recovery complete before route verification

## Step 4. Distinguish failure type
Classify which of these is strongest:

### A. Auth failure
Examples:
- OAuth refresh failure
- incomplete re-onboarding
- expired or broken token state

### B. Provider or upstream failure
Examples:
- provider outage
- upstream service instability independent of local auth state

### C. Route drift or fallback activation
Examples:
- primary unavailable, fallback active
- system remains responsive but not on intended route

### D. Post-change regression
Examples:
- upgrade or restart changed behavior
- auth restored but validation/restart introduced new issues

### E. Mixed failure
Examples:
- auth failure plus silent fallback plus config/restart complications

## Step 5. Run bounded diagnostics
Prefer the smallest useful checks.

### Diagnostic set A. Auth-path evidence
Check for:
- refresh or onboarding errors
- evidence of primary-route auth failure
- whether re-auth is actually required

### Diagnostic set B. Route identity
Check for:
- what model/provider is actually being used now
- whether the intended primary route is active again
- whether fallback is still carrying traffic

### Diagnostic set C. Cost/degraded-mode evidence
Check for:
- unexpected fallback credit/spend usage
- signs that degraded mode remained hidden

### Diagnostic set D. Post-change correlation
Check for:
- config validation or restart issues after update
- changes that restored service appearance but not route correctness

## Step 6. Choose recovery path
Use the smallest correct path.

### Recovery path 1. Auth restoration
Use when auth failure is strongest.

Typical pattern:
- re-run auth/onboarding flow cleanly
- ensure credentials are durably saved
- avoid unnecessary unrelated config changes during recovery

### Recovery path 2. Route restoration and fallback containment
Use when the system is running but on the wrong route.

Typical pattern:
- make degraded mode explicit
- contain fallback spend
- restore intended primary route
- verify route identity afterward

### Recovery path 3. Post-change repair
Use when auth recovery is entangled with update/config/restart issues.

Typical pattern:
- fix schema/config blockers
- restart only after the blocking cause is resolved
- verify both service health and route correctness

### Recovery path 4. Controlled degraded mode
Use when immediate restoration is not possible but limited continued operation is justified.

Typical pattern:
- explicitly record degraded mode
- make fallback visible
- define bounded continuation rules
- prevent hidden cost escalation

## Step 7. Verify restoration
Recovery is not complete until the route is verified.

Minimum verification should include:
1. intended primary auth path is healthy again
2. intended primary route is actually active
3. fallback is either no longer active or is explicitly bounded and visible
4. one affected lane or bounded workload proves the restored route in practice

If the system is responsive but route identity remains unclear, classify as `unknown` or `degraded`, not `healthy`.

## Step 8. Route follow-through
Typical follow-through includes:
- incident/error artifact
- TDE corrective work
- control-visibility or guardrail improvement
- fallback-spend control design
- post-change verification improvement
- updated recovery/runbook guidance

## Decision rules

### Stop and escalate when:
- the next step changes credentials, trust boundaries, or high-risk routing behavior beyond approved bounds
- route identity cannot be established confidently
- cost exposure is active and not well bounded
- recovery requires larger architectural choice rather than bounded operational repair

### Mark unresolved when:
- service appears restored but route correctness is not proven
- fallback remains active without clear bounded policy
- the lane requires local wake/reactivation or other manual intervention not yet accounted for

## Minimum output for a meaningful auth/model-route incident
A meaningful incident should usually leave behind:
1. a clear symptom statement
2. a capability health judgment
3. a strongest current diagnosis
4. a chosen recovery path or justified degraded-mode stance
5. explicit route-restoration verification or unresolved status
6. routed follow-through work

## Short conclusion
Auth and model-route failures should be treated as resilience-sensitive incidents, not merely provider hiccups.

The correct pattern is:
- state the symptom clearly
- judge route health honestly
- contain degraded-mode and cost risk
- distinguish auth from route drift from post-change regression
- restore the intended path
- verify actual route restoration
- route follow-through into the operating system
