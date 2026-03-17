# Sandbox Operating Framework (v1)

## Objective
Run OpenClaw with predictable execution context, clear trust boundaries, and fast incident recovery.

## Core principles
1. **Deterministic context** — every run must know where repos and operating files live.
2. **Fail-closed execution** — if environment checks fail, stop before doing work.
3. **Least privilege by channel** — shared/group contexts use stricter sandbox and tool policy than private contexts.
4. **Recreate on sandbox config change** — avoid sticky container drift.
5. **Reversible operations** — backup before high-risk changes, document rollback path.

## Workspace model
- Keep operating files at workspace root (`AGENTS.md`, `SOUL.md`, `USER.md`, memory files).
- Keep project repositories under `workspace/repos/*`.
- Avoid symlinks that point outside workspace unless explicitly mounted.
- Use documented bind mounts only (`:ro` by default in shared contexts).

## Recommended profiles
### Conservative Personal
- sandbox mode: `non-main`
- private main workflow may use RW where justified
- group sessions remain sandboxed and constrained

### Shared-Team Guarded
- sandbox mode: `all`
- scope: `session`
- workspace access: `none` or `ro`
- explicit minimal read-only binds
- elevated tooling disabled

### High-Assurance
- split trust boundary (separate gateway/host or OS user)
- no RW repo binds from shared contexts
- reviewed promotion path for changes

## Mandatory preflight (fail-closed)
- Docker available (if sandbox mode != off)
- `openclaw sandbox explain --json` captured
- `openclaw sandbox list --json` shows no unresolved drift
- required host repo paths exist
- required sandbox repo paths exist
- required binaries present (`git`, `python3`, etc.)
- workspace access mode supports intended action
- trust profile/channel policy is compliant

## Standard mismatch codes
- `ENV_DOCKER_MISSING`
- `ENV_SANDBOX_IMAGE_DRIFT`
- `ENV_REQUIRED_REPO_MISSING_HOST`
- `ENV_REQUIRED_REPO_MISSING_SANDBOX`
- `ENV_BIND_MISMATCH`
- `ENV_TOOLCHAIN_MISSING`
- `ENV_SECURITY_PROFILE_VIOLATION`

## Operational cadence
- Daily: `openclaw security audit --json` + `openclaw sandbox list --json`
- Weekly: scheduled sandbox reconcile/recreate window
- Monthly: restore test + access review
