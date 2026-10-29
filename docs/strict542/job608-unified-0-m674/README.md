# job608 unified-0 m674 at 674840b6 — actual run (evidence; NOT yet independently accepted)

- Stage P/stage-unified-0-m674 (P=/srv/encrypted/dev-move-98/agentq-source608-20261028-private), manifest
  2465e31010967d9374270f3573b80acf76aeb896363c1685f1a8e1ac4fda9c1c, source_commit 674840b6,
  stage_inputs = native m674 (addon 0b6607e7, accepted 5a412599) + runtime m674 (checkpoint 6178cfd9, accepted 388d36b8).
  Preflight independent APPROVE 639aa75c.
- Fresh gates at launch (see launch.txt): health up, no competing run, verify-inputs 0, sh -n 0,
  storage608 check --root P --stage unified-0 0 (free 4752261120), 3330s left (>= 2655).
- Launch (same caps as tsccwdf6a4): offload run --timeout 2460 --mem 14g --cpus 4 --artifacts result608-unified-0
  -- timeout -k 15s 2400s sh run608.sh. Background Bash with timeout 2800s; offload client rc captured: 0 (unified-0-offload.rc).
- Result: exit-code.txt 0, stage-receipt exit_code 0, STEP608 unified-0-build-done +430s, unified-0-pass.
- Mode check: `find result608-unified-0 -perm /022` = 0 entries; checkpoint listing (`tar -tvzf`, not extracted)
  9 entries (same set as tsccwdf6a4), 0 group/other-writable. checkpoint.tar.gz
  b22eb1410cc690897261725c4eeb1e498e0ff8accb3e267cb847e8ba8e36cd07 (kept in P only, not committed).
  result-files.sha256 lists every returned file.
- Next: independent acceptance, then unified-1 m674 in a fresh worker (one launch per worker) with
  --input native m674 + runtime m674 results. 595 MUST NOT APPLY. No install/seal/root/unit/sudo/service changes.
