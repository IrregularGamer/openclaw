# job608 unified-1 m674 at 674840b6 — actual run (evidence; NOT yet independently accepted)

- Stage P/stage-unified-1-m674 (P=/srv/encrypted/dev-move-98/agentq-source608-20261028-private), manifest
  d0db834fc98f9f09489059103fcf533910851c5eb69fdbbbd6eece6432d38965, source_commit 674840b6,
  stage_inputs = native m674 (addon 0b6607e7, accepted 5a412599) + runtime m674 (checkpoint 6178cfd9, accepted 388d36b8).
  Preflight 14e9d421 (d4555073 + recorded --base fix), independent APPROVE 12e8caac.
- Fresh gates at launch (see launch.txt): health up, no competing run, verify-inputs 0, sh -n 0,
  storage608 check --root P --stage unified-1 0 (free 4732301312), ~3000s left (>= 2655).
- Launch (same caps as tsccwdf6a4): offload run --timeout 2460 --mem 14g --cpus 4 --artifacts result608-unified-1
  -- timeout -k 15s 2400s sh run608.sh. Background Bash with timeout 2800s; offload client rc captured: 0 (unified-1-offload.rc).
- Result: exit-code.txt 0, STEP608 unified-1-build-done +443s, unified-1-pass.
- Mode check: `find result608-unified-1 -perm /022` = 0 entries; checkpoint listing (`tar -tvzf`, not extracted)
  29 entries (same name set as tsccwdf6a4 unified-1), 0 group/other-writable. checkpoint.tar.gz
  4208af9f795f5a64a311e7670b8330582c019f4a1986f25335dff5b10b24b9f7 (kept in P only, not committed; build.log likewise).
  result-files.sha256 lists every returned file.
- Next: independent acceptance, then unified-2 m674 in a fresh worker (one launch per worker) with
  --input native m674 + runtime m674 results. 595 MUST NOT APPLY. No install/seal/root/unit/sudo/service changes.
