# job608 checks 301d at 301d7456 — actual run (evidence; NOT yet independently accepted)

- Stage P/stage-checks-301d (P=/srv/encrypted/dev-move-98/agentq-source608-20261028-private), manifest
  1a5d47a7334ce64f82661121983eb920fae715f12195de56c496712e99efa9ee, source_commit 301d7456 (Option B lineage,
  APPROVE 7beaf342), source_export 99add7e1, stage_inputs {}. Preflight 0edf2b6c, independent APPROVE 80a15857/0cb20a15.
- Gates at launch: offload health up, verify-inputs 0, sh -n 0, storage608 check 0, pycache 0, no log/rc, 3078s left.
- ONE launch with the checks b246/m674 caps (launch.txt). Offload client rc 0 (offload.rc). No deviation.
- Result: exit-code.txt 0; stage-receipt source_commit 301d7456, source_export 99add7e1, exit_code 0, run_id
  stage608-checks-301d; STEP608 installed-checks-pass; tests.log 12 unittest suites all OK (incl. 14
  test_prepare_stage608_export with 7 lineage tests) and vitest 7/7 files passed.
- Result listing: 0 group/other-writable entries, 0 files with nlink>1. File hashes in result-files.sha256.
- Stage is SPENT. Use: exact checks input for the package at 301d7456 (job608-after-lineage-301d-continuation.md).
