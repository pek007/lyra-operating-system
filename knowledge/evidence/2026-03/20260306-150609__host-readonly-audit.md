# Host read-only audit snapshot

Generated at: 2026-03-06T15:06:09.357524+00:00

## `lsof -nP -iTCP -sTCP:LISTEN`
```
SKIPPED: command not found: lsof
```

## `socketfilterfw --getglobalstate`
```
Firewall is enabled. (State = 1)
```

## `pfctl -s info`
```
SKIPPED: command not found: pfctl
```

Manual escalation: if PF status remains unavailable, run `sudo pfctl -s info` directly on host and attach output.
