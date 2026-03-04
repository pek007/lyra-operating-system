# Sandbox Governance & Operations Framework for OpenClaw with Docker Sandboxes

## Executive summary

- Your failure mode is a **silent context split**: the host shows the expected repos, but the active runtime is in a different (often fresh or stale) sandbox workspace, so expected repo paths are missing and operator trust collapses. fileciteturn52file0L7-L33 citeturn8search0
- OpenClaw sandboxing is **Docker-based tool isolation**: the gateway stays on the host; tool execution happens inside a container, and *workspace visibility* depends on `workspaceAccess` plus any extra binds. citeturn8search0turn0search2
- The critical durability fix is **governed determinism**: a single canonical workspace layout + explicit mount contracts + a fail-closed preflight gate that prevents tool execution when mounts, identities, or policies don’t match. fileciteturn52file0L69-L131 citeturn9search0
- Your March 3 incident is a textbook “governance gap” outage: sandbox mode was enabled while Docker was unavailable, generating repeated failures amplified by autonomous jobs and config churn. fileciteturn52file0L9-L63
- “Minimal sandbox containing only bootstrap files” is often **expected** when `workspaceAccess: "none"` (default) is used; you must choose and document when sandboxes should and should not see repos. citeturn8search0turn0search5
- Fix drift by operationalizing the official primitives: `openclaw sandbox explain`, `openclaw sandbox list`, and (when needed) `openclaw sandbox recreate` to force containers to align with current config and images. citeturn9search0turn8search4
- For group channels, assume **shared delegated authority**: if multiple people can message a tool-enabled agent, they can steer the same permission set; separate trust boundaries with separate agents/workspaces or separate gateways. citeturn4view0turn5view2
- Convert “security audit flags group-channel posture risks” into concrete controls using OpenClaw’s audit-guided hardening, especially `security.trust_model.multi_user_heuristic` and “open groups + tools” findings. fileciteturn45file0L13-L20 citeturn5view2turn4view0
- Treat bind mounts as **high-impact**: they can let processes in a container modify the host unless explicitly read-only; they also hard-couple your runtime to host path structure. citeturn0search7turn8search0
- The operator-friendly model: one **“enter/exit ramp”** per risk profile (personal/shared/high-assurance), with clear “green/yellow/red” context indicators and one-command diagnostics.
- The implementation plan is front-loaded: in 24 hours you can install/verify Docker, standardize the workspace/repo layout, and add a fail-closed gate + runbooks; in 30/60/90 days you evolve toward policy-as-code, drift monitoring, and (if needed) split gateways.

## Architecture and threat model

**Reference architecture (what is what)**  
- **Host**: macOS on entity["company","Apple","consumer tech company"] hardware; this is the *policy enforcement root* for a personal-assistant model (OS user + filesystem + process permissions). citeturn4view0  
- **Gateway service**: the OpenClaw gateway process runs on the host, terminates channels, routes messages, enforces tool policies, and manages sandboxes (itself is not “inside” the sandbox). citeturn8search0turn2search0  
- **Agent runtime(s)**: OpenClaw runs an embedded agent in the gateway; tools operate relative to a workspace directory, and the workspace is central to both context injection and file/tool actions. citeturn0search4turn0search0  
- **Workspace**: default `~/.openclaw/workspace`; contains “operating/context files” like `AGENTS.md`, `SOUL.md`, `TOOLS.md`, `IDENTITY.md`, `USER.md`, and memory files under `memory/YYYY-MM-DD.md`. citeturn0search0turn0search8  
- **State directory** (`$OPENCLAW_STATE_DIR`, default `~/.openclaw/`): config, credentials, agent sessions; these are explicitly *not* part of the workspace repo and must be migrated/backed up separately. citeturn0search0turn11search6  
- **Sandbox**: a Docker container that runs tool execution; OpenClaw can run one container per session or per agent; containers persist until pruned or recreated. citeturn0search5turn9search0  
- **Docker backend**: entity["company","Docker","container platform"] is required for OpenClaw tool sandboxing; the gateway can be host-native while tools are containerized. citeturn0search2turn8search0  
- **Channel surfaces**: e.g., entity["company","Telegram","messaging platform"] group chats; group activation is normally mention-gated and should be allowlisted per trust boundary. citeturn1search0turn1search3  
- **Project repos**: ideally stored under the workspace (or mounted explicitly) so sandbox behavior is deterministic; code hosting is typically entity["company","GitHub","code hosting platform"]. citeturn0search7turn8search0

**Trust boundaries (draw them explicitly)**  
- **TB0: External senders → channel provider** (untrusted content, mixed-trust participants, potential prompt injection).  
- **TB1: Channel provider → Gateway** (OpenClaw must enforce allowlists, group policy, mention gating before the message is processed). citeturn1search3turn2search3  
- **TB2: Gateway control plane → Tool execution plane** (tool allow/deny + sandbox decision; *deny wins*). citeturn10search0turn8search0  
- **TB3: Sandbox container → Host filesystem** (only via explicitly mounted paths; bind mounts can bypass isolation). citeturn8search0turn0search7  
- **TB4: Gateway host/config boundary**: OpenClaw’s official model is “one trusted operator boundary per gateway”; it is not designed as hostile multi-tenant isolation for adversarial users sharing a gateway. citeturn4view0turn5view2

**Threat model (practical, for your environment)**  
- **T1 — Context confusion / wrong workspace execution**: running tools in a sandbox that cannot see expected repos (or sees the wrong ones) causes incorrect builds, wrong patches, or misleading diagnostics. *Observed directly as missing paths and stale/minimal sandboxes.* fileciteturn52file0L24-L33 citeturn8search0  
- **T2 — Drift via sticky containers**: containers can keep old images/configs indefinitely if they are regularly used; OpenClaw only prunes on idle/age thresholds unless you explicitly recreate. citeturn9search0turn8search4  
- **T3 — Dependency mismatch**: enabling sandbox modes without Docker availability (or without required binaries inside the sandbox image) yields cascading failures and retry storms, especially with cron. fileciteturn52file0L9-L43 citeturn0search2  
- **T4 — Group-channel delegated authority**: if multiple users can trigger a tool-enabled agent, any one can steer tool usage within the agent’s permissions; OpenClaw’s security audit explicitly flags “multi-user heuristic” configurations. citeturn5view2turn4view0  
- **T5 — Host exposure via bind mounts**: bind mounts default to writeable; a compromised or misled agent can modify/delete host files in mounted paths. citeturn0search7  
- **T6 — Configuration churn / unsafe changes**: ad-hoc toggles to sandbox modes during active operations extends outages; your own incident writeup identifies this as a core amplifier. fileciteturn52file0L34-L63
- **T7 — “Escape hatches” used casually**: Elevated mode runs exec on the host (bypasses sandbox); this is a break-glass control that should be tightly gated. citeturn2search1turn2search0

**Data flow (inbound message → execution context → file access)**  
1) Inbound message arrives via Telegram DM/group. citeturn1search0  
2) Gateway applies **DM policy / group allowlist / group mention gating** (block early, before tool exposure). citeturn1search3turn2search3  
3) Gateway picks **session key** and routes to an agent via bindings (routing ≠ authorization). citeturn4view0  
4) Agent context is built from workspace files; missing bootstrap files only inject markers and do not stop execution by default (you must add your own fail-closed controls if you want hard stops). citeturn0search0turn11search7  
5) When tools are invoked, tool policy is evaluated; if sandboxing is enabled for the session/agent, tool execution occurs in a Docker sandbox container. citeturn8search0turn0search5  
6) File access in sandbox depends on `workspaceAccess` and `docker.binds`. citeturn8search0turn0search5  
7) Outputs are returned; any writes land in either sandbox workspace (default) or mounted host paths (if rw). citeturn8search0turn0search7

**Recommended topology patterns (private, shared, high/low trust)**  
- **Private/personal (highest productivity)**: one gateway, loopback-bound, DM pairing; main agent may use rw repo access, but group sessions are sandboxed and tool-restricted by default. citeturn4view0turn2search3  
- **Shared/group (guarded)**: separate agent + separate workspace that contains only business-scoped context (no personal memory), sandbox mode “all,” workspaceAccess none/ro + explicit read-only binds to specific repos. citeturn4view0turn8search0turn1search3  
- **High-assurance**: split trust boundaries with separate gateways (ideally separate OS users/hosts) for any mixed-trust or externally exposed surface; treat “shared gateway for adversarial users” as out-of-model. citeturn4view0turn5view2  
  - Practical note: if you need remote access, prefer tailnet-style remote access rather than direct public exposure; the OpenClaw security docs explicitly frame public exposure as high risk. citeturn5view2turn12view1  
  - Mention once: entity["company","Tailscale","vpn provider"] is referenced in OpenClaw’s own hardening guidance for private remote access patterns. citeturn5view2turn4view0

## Control framework

This section is organized as **Prevent / Detect / Respond / Recover**, with implementation-ready controls. Each control includes: **risk addressed, tradeoff, and failure mode if omitted**.

**Prevent: Canonical workspace + mount contracts (Workspace & Mount Strategy)**  
**Control P1 — Canonical workspace layout “one root, predictable paths”**  
- **What to implement**: Standardize *every* runtime-relevant repo path under the agent workspace root, by convention:  
  - Host path (default): `~/.openclaw/workspace/` (or per-agent workspaces) citeturn0search8turn11search6  
  - Inside workspace:  
    - Operating files at root (`AGENTS.md`, `SOUL.md`, `TOOLS.md`, etc.) citeturn0search0turn0search4  
    - Repos under `repos/` (e.g., `~/.openclaw/workspace/repos/<repo-name>/`)  
    - A single file `WORKSPACE_MANIFEST.json` (template below) listing required repos and expected mount points  
- **Risk addressed**: Eliminates “host has it, sandbox doesn’t” ambiguity by reducing mount complexity to a single tree (or a small explicit set of binds).  
- **Tradeoff**: You are co-locating code with agent “memory” under one root; this requires clear subdirectory hygiene and sometimes separate agent workspaces for shared contexts.  
- **If omitted**: You will continue to see missing repo paths whenever sandbox workspaces are fresh (`workspaceAccess: none`) or when mounts/symlinks don’t carry through.

**Control P2 — Explicit sandbox workspace access policy per trust level**  
- **What to implement**: Define (and document) when each agent/channel uses:  
  - `workspaceAccess: "none"` (default): tools see a sandbox workspace under `~/.openclaw/sandboxes` (minimal/fresh sandbox). citeturn8search0turn0search5  
  - `workspaceAccess: "ro"`: agent workspace mounted read-only at `/agent`; write/edit/apply_patch blocked. citeturn8search0turn12view1  
  - `workspaceAccess: "rw"`: agent workspace mounted read/write at `/workspace`. citeturn8search0turn0search5  
- **Risk addressed**: Makes “why is the sandbox empty?” a predictable policy outcome, not a mysterious failure.  
- **Tradeoff**: `"ro"` breaks workflows that expect to write into workspace (including memory updates); `"rw"` increases blast radius to mounted host paths.  
- **If omitted**: Operators will keep seeing “stale/minimal sandbox” and will “fix” it ad-hoc (often by over-widening mounts), increasing both outage rate and security risk. fileciteturn52file0L24-L33

**Control P3 — Binds are allowed only via an allowlisted, documented mount table**  
- **What to implement**: Use `agents.defaults.sandbox.docker.binds` (and per-agent overrides) only for *named, documented* mounts, with explicit `:ro`/`:rw`. OpenClaw supports binds in `host:container:mode` format, and warns that binds bypass sandbox filesystem isolation. citeturn8search0turn0search7  
  - Default stance: mount repos **read-only** for shared/group, and mount a separate **staging output** directory read/write if needed for artifacts.  
  - Never mount `~/.openclaw/credentials` or `~/.ssh` into a sandbox.  
- **Risk addressed**: Prevents accidental exposure of host secrets/system paths; reduces “it works on my laptop” mount drift.  
- **Tradeoff**: Slightly slower setup (you must curate mounts) and occasional need to promote files from staging into repos via review.  
- **If omitted**: A single mis-specified bind can turn a sandbox into a host file editor (or worse), and troubleshooting remains opaque. citeturn0search7turn8search0

**Control P4 — Symlinks across trust boundaries are discouraged; external paths are forbidden without binds**  
- **What to implement**:  
  - **Allowed**: symlinks *within* the workspace tree (pure convenience).  
  - **Discouraged**: symlinks from `~/.openclaw/workspace/repos/...` → outside the workspace; container sees the symlink but not the target unless separately mounted.  
  - **Forbidden**: relying on symlinks to bridge from workspace into sensitive state directories (`~/.openclaw/...`) or user home.  
- **Risk addressed**: Avoids “path exists but points nowhere in sandbox” and reduces accidental secret leakage through symlink traversal.  
- **Tradeoff**: You lose a convenience workaround many engineers rely on; you must either clone repos into workspace or explicitly bind mount them.  
- **If omitted**: You will keep producing “ENOENT” and “missing repo” failures that are hard to reproduce and diagnose. fileciteturn52file0L24-L33

**Prevent: Sandbox lifecycle governance (create/rotate/archive/prune)**  
**Control P5 — Treat container stickiness as a first-class drift source**  
- **What to implement**: Standard operating rule: *any sandbox config/image change must include an explicit recreate step*. OpenClaw provides `openclaw sandbox recreate` for this exact reason. citeturn9search0turn8search4  
- **Risk addressed**: Eliminates “stale container runs old config forever” (particularly for frequently used agents). citeturn9search0  
- **Tradeoff**: Recreate invalidates caches and may slow the next run (package caches, git clones).  
- **If omitted**: You will see “works after restart sometimes” behavior and ambiguous drift during incident response.

**Control P6 — Allowed scopes: `session` or `agent`; `shared` is forbidden except in explicitly documented dev experiments**  
- **What to implement**:  
  - Default for shared/low-trust: `scope: "session"` (max isolation). citeturn0search1turn8search3  
  - Default for personal/dev productivity: `scope: "agent"` (stable tool environment). citeturn0search5turn8search3  
  - Do not use `scope: "shared"` in production-like environments, because it disables cross-session isolation. citeturn0search2turn8search3  
- **Risk addressed**: Prevents cross-session contamination (state bleed, accidental repo mixups) and reduces blast radius of compromised sessions.  
- **Tradeoff**: More containers and potentially more disk usage.  
- **If omitted**: One compromised or misled session can poison all sessions sharing a container/workspace.

**Prevent: Channel posture and trust boundary separation**  
**Control P7 — Group channels must be allowlisted and mention-gated; sender allowlists are mandatory in shared contexts**  
- **What to implement**:  
  - `channels.*.groupPolicy: "allowlist"` + explicit group lists, and `requireMention: true` by default; OpenClaw documents mention gating and group allowlists as separate layers. citeturn1search3turn2search2turn2search3  
  - For Telegram specifically: keep bot privacy mode consistent with your intended behavior; bots default to privacy mode; turning it off requires `/setprivacy` and re-adding the bot to groups. citeturn1search0turn1search8  
- **Risk addressed**: Reduces accidental activation in noisy rooms and reduces the probability that untrusted participants steer tool execution.  
- **Tradeoff**: More friction (“why didn’t it respond?”) and operational overhead to maintain allowlists.  
- **If omitted**: OpenClaw’s own audit flags “open groups with tools” as critical/warn because it creates prompt-injection paths. citeturn5view2turn12view0

**Control P8 — Split personal vs shared runtimes by design (separate agent + separate workspace; separate gateway for high assurance)**  
- **What to implement**:  
  - For shared-team usage, create a dedicated agent with a dedicated workspace that contains **no personal memory**, and lock it to guarded tool/sandbox settings.  
  - For mixed-trust or adversarial-user risk, split by trust boundary using separate gateways/hosts; OpenClaw explicitly states it is not a hostile multi-tenant boundary. citeturn4view0turn5view2  
- **Risk addressed**: Prevents unintended personal-data exposure via shared channels; reduces the consequences of multi-user control.  
- **Tradeoff**: Operational overhead: more gateways/agents, more updates, more monitoring.  
- **If omitted**: You will repeatedly get `security.trust_model.multi_user_heuristic` and remain exposed to “shared delegated authority” risk. citeturn5view2turn4view0

**Detect: Fail-closed environment integrity controls (preflight gate)**  
Your incident shows what happens without a gate: sandbox mode flipped without Docker, and cron amplified the failure. fileciteturn52file0L9-L63

**Control D1 — A fail-closed preflight gate that blocks execution on environment mismatch**  
- **What to implement**: A single “preflight” step that must pass before: (a) enabling sandbox mode, (b) starting high-autonomy cron, or (c) executing any repo-mutating tool operation.  
  - Minimum checks (implementation-ready):  
    1) **Sandbox dependency check**: if sandbox mode ≠ off, require Docker available in PATH. fileciteturn52file0L9-L23 citeturn0search2  
    2) **Effective sandbox config evidence**: `openclaw sandbox explain --json` captured and logged. citeturn9search0  
    3) **Container drift check**: `openclaw sandbox list` must report image/config match (or you must recreate). citeturn9search0  
    4) **Repo visibility check**: each required repo path in `WORKSPACE_MANIFEST.json` exists **both** on host and at intended container path (when repos are required for the job).  
    5) **Permission mode check**: if job requires writes, ensure you are not in `workspaceAccess: "ro"` (which disables write/edit/apply_patch). citeturn8search0turn12view1  
    6) **Toolchain check inside sandbox**: verify required binaries (e.g., `git`, `python3`) exist in the sandbox image; your incident recorded “git/python3/openclaw not found” as a real failure mode. fileciteturn52file0L24-L33  
    7) **Trust-model check**: if shared channel is enabled, require the “Shared-Team Guarded” profile or stricter; treat `security.trust_model.multi_user_heuristic` as *stop-the-world until resolved/acknowledged*. citeturn5view2turn4view0  
- **Risk addressed**: Prevents silent execution in the wrong context; prevents outage loops from dependency mismatch.  
- **Tradeoff**: Adds latency and occasional “false stops” when the environment is legitimately changing.  
- **If omitted**: You will keep shipping invisible context mismatches and repeat change-control outages. fileciteturn52file0L69-L131

**Control D2 — Standard error states (“ENVIRONMENT_MISMATCH” taxonomy)**  
- **What to implement**: Make every preflight failure map to a deterministic category and operator action. Recommended categories:  
  - `ENV_DOCKER_MISSING` (sandbox enabled, docker absent)  
  - `ENV_SANDBOX_IMAGE_DRIFT` (container image/config mismatch)  
  - `ENV_WORKSPACE_ACCESS_TOO_RESTRICTIVE` (job needs write but ro/none)  
  - `ENV_REQUIRED_REPO_MISSING_HOST` / `ENV_REQUIRED_REPO_MISSING_SANDBOX`  
  - `ENV_BIND_MISMATCH` (expected binds absent or wrong mode)  
  - `ENV_TOOLCHAIN_MISSING` (git/python3/jq absent in sandbox)  
  - `ENV_SECURITY_PROFILE_VIOLATION` (channel/profile mismatch; multi-user heuristic unresolved) citeturn5view2turn4view0  
- **Risk addressed**: Replaces “it feels broken” with “it is deterministically blocked for reason X”.  
- **Tradeoff**: You must maintain the taxonomy and keep it aligned with reality as your setup evolves.  
- **If omitted**: Troubleshooting remains tribal knowledge and reintroduces risky ad-hoc workarounds.

**Detect: Monitoring and auditing (continuous + scheduled)**  
**Control D3 — Daily “security + drift” audit cadence**  
- **What to implement**:  
  - Daily: `openclaw security audit --json` (or `--deep` after major changes). citeturn4view0turn1search7  
  - Daily: `openclaw sandbox list --json` (drift, age, mismatch). citeturn9search0  
  - Weekly: `openclaw sandbox recreate --all` in a maintenance window if you value determinism over caching. citeturn9search0  
- **Risk addressed**: Early drift detection before an operator notices missing repos mid-task.  
- **Tradeoff**: Operational overhead and occasional compute/disk churn.  
- **If omitted**: Drift will accumulate silently; outages will reappear during “important moments.”

**Respond / Recover: Change control and resilience**  
**Control R1 — Sandbox mode flips are “production changes” with rollback**  
- **What to implement**: You already have a config change SOP and checklist; enforce it for **any** changes to `agents.defaults.sandbox.*`, channels, auth, and routing. fileciteturn44file0L1-L44 fileciteturn53file0L1-L18  
- **Risk addressed**: Prevents mode thrash and extended disturbance windows. fileciteturn52file0L34-L63  
- **Tradeoff**: Slower iteration; requires explicit approvals and more artifacts.  
- **If omitted**: You repeat the exact incident dynamic: toggles + restarts + cron amplification. fileciteturn52file0L34-L63

**Control R2 — Skills and external tool governance as an enforcement layer**  
- **What to implement**: Adopt the repo’s skills governance policy and policy-as-code defaults: new skills default to sandbox + disabled; S2/S3 require approvals and version pinning. fileciteturn43file0L1-L52 fileciteturn41file0L1-L40  
- **Risk addressed**: Reduces blast radius of supply chain / skills escalation and unexpected network/credential exposure in shared contexts.  
- **Tradeoff**: Slower enablement and more up-front evaluation.  
- **If omitted**: You widen your capability surface faster than you can audit it.

**Control R3 — Backup/restore as true recovery (not hope)**  
- **What to implement**: Keep a tested restore path for workspace and state; your OPS-001 and restore runbooks already define RTO/RPO targets and a monthly restore test. fileciteturn46file0L8-L33 fileciteturn63file0L1-L82  
- **Risk addressed**: Ensures recoverability after gateway reinstall/reset, corruption, or operator error.  
- **Tradeoff**: Ongoing discipline: tests, logs, and occasional interruptions.  
- **If omitted**: A gateway reset becomes an extended outage with uncertain data loss.

**Operator UX / Human factors (make it hard to do the wrong thing)**  
**Control UX1 — “No jargon” operational language + one-command diagnostics bundle**  
- **What to implement**: A single `openclaw-env doctor` wrapper script (design below) that prints:  
  - “Where am I?” (host workspace path vs sandbox workspace path)  
  - “Which container?” (name/image/age/mounts)  
  - “Can I see the repos?” (manifest check)  
  - “Am I allowed to do writes here?” (workspaceAccess/tool policy summary)  
  - “Is this channel safe for this?” (profile + allowlist summary)  
- **Risk addressed**: Reduces panic debugging and prevents accidental “fixes” that widen access.  
- **Tradeoff**: Requires maintaining one small script and ensuring operators run it.  
- **If omitted**: Operator confidence remains low, and the system will keep being perceived as nondeterministic.

**Implementation plan (30/60/90 days)**  
- **30 days (hardening foundation)**: enforce canonical workspace layout + manifest; implement fail-closed preflight; adopt profiles for personal vs shared; daily audit cadence; “one-command diag”; formalize maintenance windows. citeturn9search0turn5view2turn8search0  
- **60 days (governance integration)**: policy-as-code checks for high-risk config keys; automated drift alerts (containers older than N days; image mismatch; security audit warns); job compatibility matrix tied to sandbox mode. citeturn9search0turn5view2  
- **90 days (high assurance option)**: split gateways per trust boundary (or per OS user), reduce tool surfaces for shared agents, and consider “repo snapshot into sandbox + reviewed patch export” for truly low-trust channels. citeturn4view0turn0search7  

## Runbooks

All runbooks follow: **diagnosis tree → safe commands (read-only first) → fix → rollback → verify**. Commands assume macOS + Docker backend; when in doubt, verify CLI availability with `openclaw --help` and `openclaw sandbox --help`. citeturn9search0turn11search5

### Runbook: Runtime cannot see expected repo

**Symptom**: agent claims repo path missing; sandbox contains only bootstrap or unrelated files. fileciteturn52file0L24-L33 citeturn8search0  

**Diagnosis tree (fast)**  
1) Is this session sandboxed?  
- Yes → go to (2)  
- No → check host filesystem paths and workspace location. citeturn0search4turn11search6  

2) Is `workspaceAccess` set to `"none"` (default) or `"ro"`?  
- `"none"` → repo won’t exist unless explicitly bound. citeturn8search0  
- `"ro"` → repo might be available at `/agent/...` but writes are blocked. citeturn8search0turn12view1  
- `"rw"` → repo should be visible at `/workspace/...` if it’s inside the workspace. citeturn8search0  

3) Are required binds configured (and allowed) when repos live outside the workspace?  
- No → fix is to move/clone repos under workspace, or add binds. citeturn8search0turn0search7  

**Safe commands (read-only first)**  
```bash
# 1) Confirm workspace + state dir info
openclaw status

# 2) See effective sandbox settings for the failing context (agent/session)
openclaw sandbox explain --json

# 3) List sandbox containers and spot mismatches
openclaw sandbox list --json

# 4) Host-side: confirm repo exists where you think it does
ls -la ~/.openclaw/workspace
ls -la ~/.openclaw/workspace/repos
```
citeturn11search6turn9search0turn0search8  

**Fix sequence (choose one; prefer A for long-term determinism)**  
A) **Move/clone repo under workspace (canonical)**  
- Clone/copy repo into `~/.openclaw/workspace/repos/<repo>` and update any internal references to use that path.  
- **Risk addressed**: eliminates cross-mount confusion.  
- **Tradeoff**: duplicates repos if you previously kept them elsewhere.  
- **Failure if skipped**: recurring missing-path errors in sandboxes.  

B) **Keep repo outside workspace but add explicit bind mounts**  
- Add `agents.defaults.sandbox.docker.binds` (or per-agent binds), mounting the repo to a stable container path like `/repos/<repo>:ro` for shared contexts or `:rw` for personal build agents. citeturn8search0  
- Recreate sandbox container(s) to apply the binds:  
```bash
openclaw sandbox recreate --agent <agentId>
```
citeturn9search0  

C) **Adjust `workspaceAccess` if repo is inside workspace but not visible**  
- Set to `"rw"` for the agent that needs repo write access (never for low-trust shared agents). citeturn8search0turn12view1  
- Recreate containers:  
```bash
openclaw sandbox recreate --agent <agentId>
```
citeturn9search0  

**Rollback sequence**  
- Restore previous config from the latest known-good backup (`~/.openclaw/openclaw.json.bak-*`) and restart gateway; follow your config-change SOP. fileciteturn44file0L45-L70  
- Recreate containers again if you changed sandbox settings. citeturn9search0  

**Post-fix verification checklist**  
- `openclaw sandbox explain` shows intended `workspaceAccess` and binds. citeturn9search0  
- Repo is visible at the intended container path (`/workspace/repos/...` or `/repos/...`).  
- If shared context: write attempts are blocked (expected). If personal build context: writes succeed only in intended repo paths.

### Runbook: Sandbox stale or outdated content

**Symptom**: container has old tools/config; fixes “don’t take”; image mismatch reported; agent still sees old environment. citeturn9search0turn8search4  

**Diagnosis tree**  
1) Does `openclaw sandbox list` show **image mismatch** or very old age? citeturn9search0  
- Yes → recreate required  
- No → go to (2)

2) Did you change sandbox config, image, binds, or setupCommand recently?  
- Yes → recreate required (containers can persist indefinitely if active). citeturn9search0  
- No → drift likely from manual Docker cleanup or external mutation.

**Safe commands**  
```bash
openclaw sandbox list
openclaw sandbox list --json
openclaw sandbox explain
```
citeturn9search0  

**Fix sequence**  
```bash
# Recreate all sandbox containers (prompts for confirmation)
openclaw sandbox recreate --all

# If you need to skip confirmation (automation windows only)
openclaw sandbox recreate --all --force
```
citeturn9search0  

If the sandbox image itself is outdated, follow OpenClaw’s documented “update image then recreate” flow (pull/tag/update config → recreate). citeturn9search0turn8search3  

**Rollback sequence**  
- Revert image/config to the previous known-good value, then `openclaw sandbox recreate --all`.  
- If you can’t determine drift cause, prefer “rollback to known-good config” rather than ad-hoc Docker commands (OpenClaw explicitly recommends recreate over `docker rm`). citeturn9search0  

**Verification**  
- `openclaw sandbox list` reports image/config matches and recent creation time. citeturn9search0  
- Toolchain check passes inside sandbox for required binaries (git/python). fileciteturn52file0L24-L33  

### Runbook: Workspace mount mismatch

**Symptom**: container mounts unexpected host paths; repo appears but points to wrong content; “works in one session but not another.”

**Diagnosis tree**  
1) Are there symlinks from workspace → outside paths?  
- Yes → treat as suspect; either eliminate symlink or add explicit binds.  
2) Are binds defined differently per agent?  
- Yes → check precedence and merged binds; document per-agent overrides. citeturn8search0turn8search3  
3) Is Docker Desktop file sharing blocking the host path?  
- Possible on macOS; if the path isn’t shared, mounts can behave unexpectedly. (Verify in Docker Desktop settings; do not assume.) citeturn0search7  

**Safe commands**  
```bash
openclaw sandbox explain --json
openclaw sandbox list --json

# Host-side truth
realpath ~/.openclaw/workspace
ls -la ~/.openclaw/workspace

# Optional: inspect mounts directly (advanced; read-only)
docker ps --format 'table {{.Names}}\t{{.Image}}\t{{.Status}}' | grep openclaw
docker inspect <container_name> --format '{{json .Mounts}}' | jq .
```
citeturn9search0turn0search7  

**Fix sequence**  
- Normalize: move repos under workspace **or** bind them explicitly; remove symlinks that cross mount boundaries.  
- Ensure every bind explicitly ends with `:ro` or `:rw`, and that container paths are stable (`/repos/...`). citeturn8search0turn0search7  
- Recreate the specific agent’s sandbox container(s). citeturn9search0  

**Rollback**  
- Restore previous bind table from config backup; recreate. fileciteturn44file0L61-L70  

**Verification**  
- `docker inspect` mount list matches the documented mount table.  
- Repo manifest check passes (see preflight template in Policy Templates).

### Runbook: Security audit warning — shared-channel exposure

**Symptom**: security audit warns about multi-user posture or open groups with tools, e.g. `security.trust_model.multi_user_heuristic`. fileciteturn45file0L13-L20 citeturn5view2  

**Diagnosis tree**  
1) Is the gateway bound beyond loopback, or reverse proxied without trusted proxies?  
- If yes, resolve network exposure first (highest risk class). citeturn5view2turn5view2  
2) Are group policies “open” or allowlists too broad (`"*"` in the wrong places)?  
- Tighten groupPolicy and group allowlists; keep mention gating on. citeturn2search2turn1search3  
3) Are high-impact tools enabled for shared contexts (runtime/fs/elevated, cron, gateway)?  
- Deny these in shared profiles. citeturn5view2turn10search0  

**Safe commands**  
```bash
openclaw security audit
openclaw security audit --deep
openclaw security audit --json
```
citeturn4view0turn1search7  

**Fix sequence (shared contexts)**  
- Enforce group allowlists + mention gating; for Telegram, ensure `channels.telegram.groups` is explicit and `groupPolicy: "allowlist"` for production-like shared usage. citeturn1search3turn2search2turn1search0  
- Split personal vs shared agents/workspaces; do not let shared agents load personal memory files. citeturn4view0  
- For shared agents: set sandbox.mode `"all"`, scope `"session"` (or `"agent"` if you accept less isolation), and workspaceAccess `"none"` or `"ro"` plus only the minimal necessary binds. citeturn0search1turn8search0turn8search3  
- Disable elevated mode for shared agents. citeturn2search1turn5view2  

**Rollback**  
- If you accidentally lock yourself out of an operational channel, revert the last config backup and restart gateway, per SOP. fileciteturn44file0L45-L70  

**Verify**  
- `openclaw security audit --deep` returns no critical findings, and the multi-user warning is either resolved (by splitting) or explicitly accepted with documented “shared-team guarded” compensating controls. citeturn5view2turn4view0  
- Your own evidence indicates a loopback bind + loopback trusted proxies posture is valid; keep it explicit. fileciteturn45file0L21-L33  

### Runbook: Recovery after gateway reinstall/reset

**Symptom**: gateway is reinstalled, config/state missing, workspace not present, channels not working.

**Diagnosis tree**  
1) Can the gateway start and report status?  
- No → fix base runtime first (don’t restore data into a broken runtime). fileciteturn63file0L18-L31  
2) Do you have your state directory backup (`~/.openclaw/`) and workspace backup (`~/.openclaw/workspace/`)?  
- If either missing → invoke incident process; recovery may not meet RPO. fileciteturn46file0L8-L33  

**Safe commands**  
```bash
openclaw gateway status
openclaw status
```
fileciteturn63file0L18-L31 citeturn11search5  

**Fix sequence (use your existing runbook, with one added sandbox step)**  
- Follow `restore.md` phases (base system → restore workspace → rebuild skills/tools → restore secrets → run security audit → smoke tests → re-enable automations). fileciteturn63file0L1-L92  
- After restoring config or sandbox settings, immediately run:  
```bash
openclaw sandbox list --json
openclaw sandbox recreate --all
```
citeturn9search0  

**Rollback (when restore goes wrong)**  
- Restore into a *new* test location first (never overwrite production until verified). This aligns with your OPS-001 restore-test discipline. fileciteturn46file0L34-L41  

**Verification**  
- Run `openclaw security audit --deep` and fix critical findings before re-enabling cron/automation. fileciteturn63file0L60-L82 citeturn4view0  
- Confirm backup/restore tests are recorded (RTO/RPO discipline). fileciteturn46file0L8-L33  

## Policy templates

These are copy/paste starters. Replace placeholders and keep them in version control (workspace repo) *except* secrets and `openclaw.json` under state dir. citeturn0search0turn11search6

### Workspace layout standard

**Template: workspace directory (host)**  
```
~/.openclaw/
  openclaw.json                 # config (NOT in workspace git)
  credentials/                  # tokens/keys (NOT in workspace git)
  agents/<agentId>/sessions/    # transcripts (NOT in workspace git)
  workspaces/
    main/                       # personal agent workspace
      AGENTS.md
      SOUL.md
      TOOLS.md
      USER.md
      IDENTITY.md
      memory/YYYY-MM-DD.md
      repos/
        lyra-operating-system/  # OS repo (and others)
      WORKSPACE_MANIFEST.json
    team/                       # shared/team agent workspace (no personal memory)
      ...
```
- Why: OpenClaw centers tool cwd and context injection around the workspace; keeping repos here makes sandbox mounts deterministic. citeturn0search4turn8search0  
- Risk addressed: missing repo paths + opaque mounts.  
- Tradeoff: larger workspace tree; need multiple workspaces for trust separation.  
- If omitted: you keep debugging “host has it, sandbox doesn’t.”

**Template: `WORKSPACE_MANIFEST.json` (minimal)**  
```json
{
  "workspaceLayoutVersion": 1,
  "requiredRepos": [
    {
      "name": "lyra-operating-system",
      "hostPath": "~/.openclaw/workspaces/main/repos/lyra-operating-system",
      "sandboxPaths": ["/workspace/repos/lyra-operating-system", "/repos/lyra-operating-system"],
      "required": true,
      "access": "ro"
    }
  ],
  "requiredBinaries": ["git", "python3", "jq"],
  "requiredSandboxWorkspaceAccess": ["ro", "rw"],
  "notes": "Update with explicit per-agent requirements."
}
```
- Risk addressed: makes “expected repo paths” an explicit contract.  
- Tradeoff: some up-front curation.  
- If omitted: “expected” becomes implicit and brittle.

### Preflight gate framework (fail-closed)

**Template: “preflight” shell wrapper (operator-run + cron-run)**  
```bash
#!/usr/bin/env bash
set -euo pipefail

echo "[preflight] $(date -u +%FT%TZ)"

# 1) Capture effective sandbox config
openclaw sandbox explain --json > /tmp/openclaw-preflight-sandbox-explain.json

# 2) If sandbox mode is enabled, Docker must exist
if grep -q '"mode": "off"' /tmp/openclaw-preflight-sandbox-explain.json; then
  echo "[preflight] sandbox.mode=off"
else
  command -v docker >/dev/null || { echo "[ENV_DOCKER_MISSING] docker not found"; exit 20; }
  docker version >/dev/null || { echo "[ENV_DOCKER_UNUSABLE] docker version failed"; exit 21; }
fi

# 3) Drift check
openclaw sandbox list --json > /tmp/openclaw-preflight-sandbox-list.json

# 4) Workspace + repo contract check (example)
test -d "$HOME/.openclaw/workspace/repos" || { echo "[ENV_REPO_ROOT_MISSING]"; exit 30; }

echo "[preflight] OK"
```
- Risk addressed: blocks the exact failure you saw (sandbox mode enabled without Docker) and catches obvious repo-root absence. fileciteturn52file0L9-L23 citeturn0search2  
- Tradeoff: needs local tailoring to your chosen paths and agent IDs.  
- If omitted: sandbox-mode changes remain footguns and cron amplifies incidents. fileciteturn52file0L69-L131

### Security posture profiles

Each profile specifies sandbox stance, channel policy, credential exposure constraints, cadence, and capability blocks. Use separate agents/workspaces for different profiles. citeturn4view0turn8search0turn10search0

**Conservative Personal (default for a single trusted operator)**  
- **Sandbox stance**: `mode: "non-main"` so group/non-main sessions sandbox by default; personal main session can remain host-like if desired. citeturn0search1turn2search0  
- **Channel triggers**: DM pairing; groups allowlisted + require mention. citeturn1search3turn2search3  
- **Credentials**: stored only under state dir; never mounted into sandbox; rotate on exposure. citeturn0search0turn4view0  
- **Cadence**: weekly `security audit --deep`; daily `sandbox list`. citeturn4view0turn9search0  
- **Blocked capabilities**: elevated mode off by default; cron/gateway tools denied in shared sessions. citeturn2search1turn5view2  

**Shared-Team Guarded (shared channel, same trust boundary but not personal)**  
- **Sandbox stance**: `mode: "all"`, `scope: "session"`, `workspaceAccess: "none"` + explicit `binds` for only necessary repos at `:ro`. citeturn8search0turn8search3  
- **Channel triggers**: strict allowlists (`groupPolicy: "allowlist"`, explicit group IDs, `requireMention: true`, and sender allowlist). citeturn2search2turn1search3  
- **Credentials**: only team-scoped credentials; no personal identities logged in on that runtime; align with personal-assistant trust model guidance. citeturn4view0turn5view2  
- **Cadence**: daily `security audit --json`, weekly container recreate. citeturn4view0turn9search0  
- **Blocked capabilities**: `tools.elevated` disabled; deny `cron`, `gateway`, `sessions_send`, `sessions_spawn` unless explicitly needed. citeturn5view2turn10search0  

**High-Assurance (mixed trust or high-risk surfaces)**  
- **Sandbox stance**: as Shared-Team Guarded plus: no `:rw` binds to repos; use staging + reviewed patch promotion; optionally separate gateway/host per boundary. citeturn4view0turn0search7  
- **Channel triggers**: allowlist-only, mention-gated, minimal tool profile, and explicit “read-only mode” composition (OpenClaw documents this pattern). citeturn12view0turn1search3  
- **Credentials**: shortest-lived credentials possible; no broad tokens; secrets never written to logs; follow skills governance S2/S3 rules. fileciteturn41file0L21-L40 citeturn4view0  
- **Cadence**: daily deep audit during initial rollout; monthly access review; monthly restore test. fileciteturn56file0L1-L19 fileciteturn46file0L34-L41 citeturn4view0  
- **Blocked capabilities**: no elevated; no gateway config tools; no cron writes from chat; default deny.

### Change management and maintenance windows

**Policy**: Any change to sandbox modes, binds, channel policies, auth, routing is **high risk unless proven otherwise**; your SOP already encodes this. fileciteturn44file0L15-L27  

**Template: maintenance window checklist (time-boxed)**  
- Preconditions (must be true):  
  - Preflight gate passes (Docker present; sandbox drift known). fileciteturn52file0L69-L90  
  - Cron/high-autonomy jobs paused (incident lesson). fileciteturn52file0L69-L90  
  - Config backup created (`openclaw.json.bak-*`). fileciteturn44file0L33-L40  
- Allowed break-glass:  
  - Elevated mode only with written justification and immediate rollback plan. citeturn2search1turn2search0  
- Compensating controls:  
  - Tighten groups/DMs during the window (disable open groups; keep mention gating). citeturn2search2turn1search3  
- Re-hardening steps:  
  - `openclaw sandbox recreate --all` after applying sandbox-related config. citeturn9search0  
  - `openclaw security audit --deep` before declaring success. citeturn4view0  

**Template: sign-off record (copy/paste)**  
```
Change ID:
Date/time (start-end, Stockholm):
Scope:
Risk class (default high):
Approved by:
Preflight passed (attach artifact):
Backup created (path):
Change diff:
Validation steps run:
Rollback checkpoint verified:
Post-change audit results:
Notes/Follow-ups:
```
- Risk addressed: prevents untracked drift and mode thrash. fileciteturn52file0L34-L63  
- Tradeoff: more paperwork.  
- If omitted: changes become unreviewable and outages last longer.

## KPI and metrics dashboard

A practical dashboard measures **reliability (context correctness)** and **security (exposure + policy adherence)**.

**Reliability KPIs**  
- **Sandbox context correctness rate**: `% of runs where preflight passes + manifest repos visible` (target ≥ 99.5%).  
  - Risk addressed: directly measures the “missing repo in runtime” class.  
  - If omitted: you can’t tell if you’re improving beyond anecdotes.  
- **Sandbox drift incidents per week**: count of runs where `openclaw sandbox list` reports image mismatch or containers older than threshold without recreate. citeturn9search0  
- **Mean time to restore correct context (MTTR-C)**: time from “repo missing” alert to verified repo visibility.  
- **Autonomous job failure amplification**: number of repeated failures per lane per 15 minutes (your incident recommends alerting on repeated sandbox/dependency errors). fileciteturn52file0L96-L113  

**Security KPIs**  
- **Security audit critical count (daily)**: must be 0; warn count tracked trendline. citeturn4view0turn5view2  
- **`security.trust_model.multi_user_heuristic` status**: open/closed with documented compensating controls (or eliminated via split gateways). citeturn5view2turn4view0  
- **Open groups + tools exposure**: count of times audit reports open group surfaces with runtime/fs/elevated. citeturn12view0turn5view2  
- **Secrets hygiene**: number of secret-scan findings; number of “secret rotated due to exposure” events (should be low but non-zero over time). citeturn4view0turn11search2  

**Operations KPIs**  
- **Change success rate**: % of config changes that pass immediate validation (`gateway status`, `status --deep`, channel checks) without rollback. fileciteturn44file0L41-L70  
- **Backup/restore compliance**: monthly restore test completed (yes/no) and time to complete (target consistent with RTO). fileciteturn46file0L34-L41  
- **Access review compliance**: monthly access review completed (yes/no). fileciteturn56file0L1-L19  

## Assumptions, unresolved unknowns, and validation plan

**Assumptions (state explicitly)**  
- You are using Docker-based OpenClaw sandboxing (not a non-Docker sandbox backend). citeturn8search0turn0search2  
- The observed “minimal sandbox” state is often the default `workspaceAccess: "none"` behavior unless you opt into repo visibility via rw/ro or binds. citeturn8search0turn0search5  
- Your gateway is intended to remain local-only (loopback bind) unless a documented remote-access pattern is in place; your own evidence shows a loopback bind posture with trusted proxies on loopback. fileciteturn45file0L21-L33 citeturn4view0  

**Unknowns (must verify locally; do not guess)**  
- Exact container image customizations currently in use (default image vs custom image; presence of `git/python3/jq`), because your incident showed missing binaries. fileciteturn52file0L24-L33  
- Whether your repos currently live inside `~/.openclaw/workspace/repos` or outside (and whether symlinks are involved).  
- The exact OpenClaw config for channel group policies and tool denies in your current `openclaw.json` (we can provide templates, but you must compare to your actual file). citeturn11search5turn2search3  
- Whether cron/high-autonomy jobs can be paused via built-in controls or require manual disablement; your incident recommends pausing before risky changes, but the mechanism depends on your cron setup. fileciteturn52file0L69-L90  

**Validation plan (concrete, short)**  
1) Run `openclaw sandbox explain --json` and confirm: mode/scope/workspaceAccess match your intended profile. citeturn9search0  
2) Run `openclaw sandbox list --json` and confirm: image/config match; note container ages. citeturn9search0  
3) Run `openclaw security audit --deep` and confirm: no critical findings; triage any warnings starting with open groups/tools and `multi_user_heuristic`. citeturn4view0turn5view2  
4) Pick one “repo-required” workflow and verify repo visibility under both:  
   - a main/private session and  
   - a group session (which is typically non-main and will be sandboxed in `mode: non-main`). citeturn2search0turn1search3  
5) Force determinism: `openclaw sandbox recreate --all`, then repeat steps 1–4. citeturn9search0  

## First ten actions tomorrow morning

1) **Stabilize the environment**: confirm Docker availability on the host *before* any sandbox mode changes.  
```bash
command -v docker && docker version
```
Risk addressed: prevents the exact “sandbox requires Docker but docker not found” outage. Tradeoff: none. If omitted: recurrence is likely. fileciteturn52file0L9-L23 citeturn0search2  

2) **Snapshot current state** (so you can always roll back):  
```bash
cp ~/.openclaw/openclaw.json ~/.openclaw/openclaw.json.bak-$(date +%Y%m%d-%H%M%S)
openclaw status
openclaw sandbox list --json > /tmp/sbx-list.json
openclaw sandbox explain --json > /tmp/sbx-explain.json
```
Risk addressed: safe rollback + evidence. Tradeoff: minor overhead. If omitted: recovery becomes guesswork. fileciteturn44file0L33-L70 citeturn9search0turn11search6  

3) **Define your canonical repo location**: create `~/.openclaw/workspace/repos/` (or per-agent workspace equivalent) and start moving/cloning active repos there.  
Risk addressed: removes mount ambiguity. Tradeoff: moving repos. If omitted: persistent “repo missing in sandbox” class.

4) **Pick your primary profiles** (at minimum: Conservative Personal + Shared-Team Guarded) and assign each channel to a specific agent/workspace.  
Risk addressed: prevents personal memory exposure in shared channels. Tradeoff: extra agent/workspace. If omitted: `multi_user_heuristic` stays open and risk persists. citeturn5view2turn4view0  

5) **Lock down group triggers**: ensure groupPolicy allowlist + require mention; for Telegram, confirm privacy mode matches your intent.  
Risk addressed: reduces accidental activation in groups. Tradeoff: mention friction. If omitted: open-group tool exposure risk. citeturn1search3turn1search0turn2search3  

6) **Implement a minimal preflight gate script** (even if operator-run first) and run it before enabling any autonomous loop.  
Risk addressed: fail-closed behavior. Tradeoff: extra step. If omitted: silent mismatch remains.

7) **Run `openclaw security audit --deep` and act on the top finding**, not the easiest one. Treat “open groups + tools” and `multi_user_heuristic` as high-priority posture issues.  
Risk addressed: reduces real attack paths. Tradeoff: time. If omitted: audit becomes theatre. citeturn4view0turn5view2  

8) **Force-reconcile sandbox drift** after any config change touching sandbox settings:  
```bash
openclaw sandbox recreate --all
```
Risk addressed: removes stale containers. Tradeoff: rebuild time. If omitted: old containers persist. citeturn9search0  

9) **Write a one-page “Mount Contract” note for operators**: “In this profile, repos appear at X; if not, run diagnostics; do not apply ad-hoc binds.”  
Risk addressed: reduces panic fixes. Tradeoff: 15 minutes writing. If omitted: tribal knowledge persists.

10) **Schedule the recurring governance loops**: daily sandbox list + security audit; weekly recreate (optional); monthly restore test and access review.  
Risk addressed: drift + recoverability. Tradeoff: routine ops. If omitted: regressions return quietly. fileciteturn46file0L34-L41 fileciteturn56file0L1-L19 citeturn9search0turn4view0