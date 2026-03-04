# Trust Boundary Policy Record — 2026-03-04

Status: Active
Owner: Peter/Lyra

## Policy decision
Default trust-boundary architecture is **Option A: hardened single trusted operator boundary** for the current gateway/runtime.

## Boundary statement
- One gateway = one trusted operator boundary.
- Trusted operator set for this boundary: Peter (primary), Lyra acting on Peter’s authority.
- Telegram group interaction is permitted only under explicit allowlists.

## Enforcement posture (runtime)
- `agents.defaults.sandbox.mode = off` (main execution lane stability)
- `tools.fs.workspaceOnly = true`
- `gateway.bind = loopback`
- `gateway.trustedProxies = ["127.0.0.1", "::1"]`
- `channels.telegram.groupPolicy = allowlist`
- `channels.telegram.groupAllowFrom = [8283124284]`
- Group-specific allowFrom remains explicit for `-1003804530741`.

## Residual warning stance
Accepted residual warning: `security.trust_model.multi_user_heuristic` under this declared single-trust boundary.

## Reopen triggers (A -> B split boundary)
1. Group membership expands beyond mutually trusted operators.
2. Additional identities/users need high-impact tool steering.
3. Gateway exposure requirements expand beyond local trusted posture.
4. Security audit returns critical findings or unguarded runtime/fs contexts.

## Change governance
- Boundary changes are ceiling-impacting and require explicit approval + change-window discipline.
- Runtime mechanism changes follow `OPENCLAW_CONFIG_CHANGE_SOP_V1.md` + checklist.
