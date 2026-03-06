# Incident Report — GitHub Push Failure (Token Scope Mismatch)

Date: 2026-03-06  
Owner: Peter / Lyra  
Status: Resolved

## Summary
Pushes to `pek007/lyra-operating-system` failed with HTTP 403 after credential changes made during `pxs` setup.

## Symptoms
- `git push origin main` failed with:
  - `Permission to pek007/lyra-operating-system.git denied to pek007`
  - HTTP 403
- Local branch showed commits ahead of remote.

## Root Cause
A newer fine-grained GitHub token replaced the previously cached credential but only covered `pxs` scope. The shared cached credential was then used for `lyra-operating-system`, causing authorization failure.

## Corrective Actions Taken
1. Created a new fine-grained token with access to both repositories:
   - `lyra-operating-system`
   - `pxs`
2. Included required permission level for operations:
   - Contents: Read/Write
   - Workflows/Actions: Read/Write
3. Re-authenticated local Git credential flow and confirmed pushes.
4. Scheduled token renewal reminder:
   - Job: `github-token-renewal-reminder`
   - Reminder date: 2026-05-21 (before 2026-06-04 expiry)

## Verification
- `git push --dry-run origin main` -> `Everything up-to-date`
- `workspace` repo now at parity with origin (`HEAD == origin/main`)
- `pxs` repo dry-run push also reports up-to-date

## Prevention (Standard)
1. Keep a token inventory with owner, scope, expiry, and repos covered.
2. Use one of:
   - One token per repo (least blast radius), or
   - One explicit multi-repo token documented with all covered repos.
3. After token changes, run this verification checklist:
   - `git push --dry-run origin main` in `~/.openclaw/workspace`
   - `git push --dry-run origin main` in `pxs`
4. Keep expiry reminder at least 14 days before expiration.

## Terminal Quick-Fix Procedure (if it recurs)
```bash
security delete-internet-password -s github.com -a pek007 ~/Library/Keychains/login.keychain-db
cd ~/.openclaw/workspace && git push origin main
# re-enter username + PAT when prompted
```
