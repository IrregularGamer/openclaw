# job608 unified-2 m674 at 674840b6 — actual run (evidence; NOT yet independently accepted)

- Stage P/stage-unified-2-m674 (P=/srv/encrypted/dev-move-98/agentq-source608-20261028-private), manifest
  b9ae8e5a94fdf6d1c12abff1e8b134dc395d66e8d62206f3a05601bf737c247d, source_commit 674840b6,
  stage_inputs = native m674 (addon 0b6607e7, accepted 5a412599) + runtime m674 (checkpoint 6178cfd9, accepted 388d36b8).
  Preflight c8aef54b (stray import __pycache__ removed before gates), independent APPROVE c10b2716.
- Fresh gates at launch (see launch.txt): health up, no competing run, verify-inputs 0, sh -n 0,
  storage608 check --root P --stage unified-2 0 (free 4711718912), ~3300s left (>= 2655).
- Launch (same caps as tsccwdf6a4): offload run --timeout 2460 --mem 14g --cpus 4 --artifacts result608-unified-2
  -- timeout -k 15s 2400s sh run608.sh. Background Bash with timeout 2800s; offload client rc captured: 0 (unified-2-offload.rc).
- Result: exit-code.txt 0, STEP608 unified-2-build-done +425s, unified-2-pass.
- Mode check: `find result608-unified-2 -perm /022` = 0 entries; checkpoint listing (`tar -tvzf`, not extracted)
  36 entries (same name set as tsccwdf6a4 unified-2), 0 group/other-writable. checkpoint.tar.gz
  de6fd118cfac647273588218bf30727e5c82227159e04b533baeeceeb2cac2d6 (kept in P only, not committed; build.log likewise).
  result-files.sha256 lists every returned file.
- Next: independent acceptance, then unified-3 m674 in a fresh worker (one launch per worker) with
  --input native m674 + runtime m674 results. 595 MUST NOT APPLY. No install/seal/root/unit/sudo/service changes.
