# Independent preflight review: job608 unified-5r1 tsccwdf6a4 retry stage

Reviewer: independent (did not produce 4191978f). Scope: commit 4191978f
(job608-unified-5-tsccwdf6a4-lease-revoked/, job608-unified5r1-tsccwdf6a4-continuation.md).
P = /srv/encrypted/dev-move-98/agentq-source608-20261028-private. All checks read-only;
no offload or build launched.

1. Spent unified-5 evidence: committed `unified-5-offload.log.gz` zcat sha256 =
   P/unified-5-tsccwdf6a4-offload.log sha256 = 6a7f685c6511...c957; both rc files = 75.
   Log ends with `[offload-agent] job lease expired or revoked` and
   `{"offload_status": "remote_lease_denied", "local_execution": false, ...}` after
   build-start +22s. No result608-unified-5 in P/stage-unified-5-tsccwdf6a4 or P. PASS.
2. P/stage-unified-5r1-tsccwdf6a4 exists; `diff -r` vs spent stage rc 0; no result*,
   *.rc, or offload logs inside (only stage608-inputs/runtime/build.log, a pinned input);
   P/unified-5r1-* absent. export-manifest.json sha256 a63306a5...81e4 =
   preflight stages[4].manifest_sha256 (stage unified-5, verify_inputs_rc 0). PASS.
3. `sh -n run608.sh` rc 0 in 5r1. Writes in run608.sh go to `$RESULT`
   (result608-$STAGE, created with mkdir), source/, native-source/, .native608/,
   strict542-checks/; stage608.py writes only under result/ and .native608 (copyfile
   from inputs, not into them). One note: `releaseConsumedArchives` unlinks consumed
   archives in the stage root (fs.unlinkSync) - unlink, not truncate, so a hardlinked
   sibling is unaffected, and it runs on the remote copy anyway. Hardlinks safe. PASS.
4. `python3 -I docs/strict542/storage608.py check --root $P --stage unified-5` rc 0
   (unique 1965744761 B, free 5357756416 B). Root disk free 7.9G (>=1GB). PASS.
5. `offload status`: friend VPS up, load 0.3, 13502 MB free, no active run listed;
   `offload health`: up. PASS (re-check right before launch per gates).
6. Launch block identical to accepted unified-4 pattern
   (job608-after-unified3-tsccwdf6a4-continuation.md) except stage dir
   (stage-unified-5r1-...) and log/rc names (unified-5r1-...); artifacts name stays
   result608-unified-5 (correct: run608.sh derives RESULT from STAGE). Single-shot,
   14g/4CPU/--timeout 2460, inner timeout 2400s. No 5r2 in same worker. PASS.
7. Preflight verify-inputs step: `python3 -I stage608.py verify-inputs` (cwd = stage,
   local, no network) run in 5r1: rc 0, 28.5s wall (encrypted-disk IO). PASS.

Remaining launch-time gates: >=2655s worker time left, fresh health/no competing run.

VERDICT: APPROVE
