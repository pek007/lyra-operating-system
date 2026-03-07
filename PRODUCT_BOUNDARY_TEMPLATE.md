# Product Boundary Template v1.0

## Product Identity
- Product ID:
- Product Name:
- Domain (OS / PX):
- Owner:
- Type (Internal / Client-facing / SaaS candidate):

## 1) Product Mission
- Core problem solved:
- Primary users:
- Success outcome(s):

## 2) Ownership Boundary
- What this product **owns**:
- What this product **reads but does not own**:
- What this product **must never own**:

## 3) Data Boundary
- Data classes handled:
- Sensitive/customer data handling:
- Tenant model:
- Retention/audit requirements:

## 4) Runtime Boundary
- Runtime/deployment unit:
- Secrets boundary:
- Failure isolation expectations:

## 5) Dependency Policy
- Allowed dependencies:
- Prohibited dependencies:
- Required ADR triggers for dependency exceptions:

## 6) Interface Contracts
- Inbound interfaces (API/events):
- Outbound interfaces (API/events):
- Contract versioning strategy:

## 7) Reuse Strategy
- Candidate shared components:
- Why shared (vs duplicate):
- Support/maintenance owner:

## 8) Product Assembly (Required)
- Artifact types included (service / skill-pack / policy-pack / schema-pack / ops-pack):
- Versioning strategy per artifact:
- Consumer-facing package/version identifier:

## 9) Distribution & Activation (Required)
- Distribution lane per artifact (daemon/cron, workspace-skills/managed-skills/extraDirs/plugin, submodule/subtree/release):
- Activation mechanism per artifact:
- Override precedence and conflict policy:

## 10) Operational Controls
- Required metrics:
- Required audit artifacts (WO/CA/ADR):
- Security controls:
- Required enforcement gates/checks:

## 11) Commercialization Readiness (if relevant)
- What blocks external release today:
- Steps to SaaS readiness:
- Regulatory/compliance considerations:

## 12) Decision Log
- ADR links:
- Open decisions:
- Next review date:
