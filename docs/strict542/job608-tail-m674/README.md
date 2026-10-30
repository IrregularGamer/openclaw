# job608 tail m674 at 674840b6 — actual run (evidence; NOT yet independently accepted)

- Stage P/stage-tail-m674 (P=/srv/encrypted/dev-move-98/agentq-source608-20261028-private), manifest
  4a3b28338621b250cc6c7e8c509b63eff75edbe9aa0a618eb943fc3309983629, source_commit 674840b6,
  stage_inputs = native m674 (5a412599), middle m674 (dc75babf), sdk-0 m674 (0eb29365), sdk-1 m674 (6603e1ea).
  Preflight b7d710e3 (no stray __pycache__), independent APPROVE 9658c9c9.
- Fresh gates at launch (launch.txt): health up, no competing run, verify-inputs 0, sh -n 0,
  storage608 check --root P --stage tail 0, 3233s left (>= 2655).
- Launch (same caps as tail tsccwdf6a4 README line 12): offload run --timeout 2460 --mem 14g --cpus 4
  --artifacts result608-tail -- timeout -k 15s 2400s sh run608.sh. Background Bash timeout 2800s; offload client rc 0 (tail-offload.rc).
- Result: exit-code.txt 0, STEP608 tail-build-done +236s (tsccwdf6a4: +237s), tail-pass. The only
  error/fail/cancel match in build.log is the asset filename `update-failure-report-*.js` (same as tsccwdf6a4).
  build.log tail: "[build-all] phase timings: total 1m 43.1s". Result 161608377 bytes, under the 192 MiB return cap.
- Mode check: `find result608-tail -perm /022` = 0 entries. Checkpoint listing (`tar -tvzf`, not extracted):
  18159 entries = 15907 files + 1069 dirs + 1183 relative in-tree symlinks, 0 group/other-writable files/dirs.
  Entry count equals the tail tsccwdf6a4 checkpoint; the name sets differ only in content-hashed
  `tail/data/dist/control-ui/assets/*-<8 char hash>.{js,css}[.br|.gz|.map]` names (diff after normalizing that
  hash suffix is empty).
  checkpoint.tar.gz 54b49d6895c96d4bed2f372038e3b0fef2d60b9e79038c24dedf92489175c40b (kept in P only, not committed).
  result-files.sha256 lists every returned file; offload log gzip -n.
- Next: independent acceptance, then package m674 in a fresh worker (one launch per worker). 595 MUST NOT APPLY.
  No install/seal/root/unit/sudo/service changes.
