# Job608 unified-5 tsccwdf6a4: launch SPENT, remote lease revoked (exit 75), NOT a result

P = /srv/encrypted/dev-move-98/agentq-source608-20261028-private. Launched once
(2026-10-29 ~17:09Z, gates in runs/608/NOTES.md: manifest a63306a5, 2885s left)
from P/stage-unified-5-tsccwdf6a4 at 14g/4CPU/--timeout 2460.

- `unified-5-offload.rc` = `75` (sha256 of private original 84b9bb07...c550)
- `unified-5-offload.log.gz` = gzip -9n of private log (sha256 6a7f685c...c957, 2383 B).
  The log shows stage-native-start +11s, restore-build-done +19s, build-start +22s,
  then `[offload-agent] job lease expired or revoked` and
  `{"offload_status": "remote_lease_denied", "local_execution": false, "retry_requires_reconciliation": true}`.
  `offload health` was briefly down around the launch.
- No `result608-unified-5` returned; the stage holds only its original inputs.
- Reconciliation (2026-10-29 ~17:40Z): `offload status` = friend VPS up, load 0.17,
  no active run; `offload health` = up. Nothing local ran (local_execution false).

Unified-5 is NOT accepted and NOT counted. The stage path P/stage-unified-5-tsccwdf6a4
is SPENT (its remote rrsync slug may still be locked; never relaunch it).
Retry continuation: ../job608-unified5r1-tsccwdf6a4-continuation.md.
