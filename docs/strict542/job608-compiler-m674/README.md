# job608 compiler m674 at 674840b6 — actual run (evidence; NOT yet independently accepted)

- Stage P/stage-compiler-m674 (P=/srv/encrypted/dev-move-98/agentq-source608-20261028-private), manifest
  0807dbe2a6ebf2e45ab9d421bc9cbe12a1e7b896e53a2c84715d7a5a442354ba, source_commit 674840b6,
  stage_inputs = native m674 (addon 0b6607e7, accepted 5a412599). Preflight independent APPROVE 8566c2b9.
- Fresh gates at launch (22:33Z): health up, no competing run, no result/log/rc, verify-inputs 0, sh -n 0,
  storage608 check --root P --stage compiler 0 (free 4879486976), 3565s left (>= 975).
- Launch (same caps as tsccwdf6a4): offload run --timeout 600 --mem 14g --cpus 4 --artifacts result608-compiler
  -- timeout -k 15s 540s sh run608.sh. Run in the foreground; offload client rc captured: 0 (offload.rc).
- Result: exit-code.txt 0, stage-receipt exit_code 0, STEP608 compiler-checks-pass, compiler tests 2/2 pass.
- Mode check: `find result608-compiler -perm /022` = 0 entries; compiler stage returns no checkpoint tarball.
  Result 26738 B. result-files.sha256 lists every returned file.
- Next: independent acceptance, then runtime m674 (2460/2400s, 14g/4CPU) with --input P/stage-native-m674/result608-native
  in a fresh worker. 595 MUST NOT APPLY. No install/seal/root/unit/sudo/service changes.
