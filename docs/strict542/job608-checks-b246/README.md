# job608 checks b246 at b246ebeb — actual run (evidence; NOT yet independently accepted)

- Stage P/stage-checks-b246 (P=/srv/encrypted/dev-move-98/agentq-source608-20261028-private), manifest
  16552908c856bff99fde8ae0096b79f1a13d5a511dff9ae45809c21649f658ac, source_commit b246ebeb, source_export 264d042c,
  stage_inputs {}. Preflight 069eebd3, independent APPROVE 03dd497a.
- Gates at launch: offload health up (load 0.23, no competing run), verify-inputs 0, sh -n 0, storage608 check 0,
  no log/rc, 3117s left (>=1575).
- ONE launch with the checks m674 caps (launch.txt). Offload client rc file written: 0 (offload.rc). No deviation.
- Result: exit-code.txt 0; stage-receipt source_commit b246ebeb, source_export 264d042c, exit_code 0, run_id
  stage608-checks-b246; STEP608 installed-checks-pass; tests.log unittest suites all OK (2/8/14/17/7 incl. 8
  frozen-package608 tests with materialize) and vitest 7/7 files passed.
- Result listing: 0 group/other-writable entries, 0 files with nlink>1. File hashes in result-files.sha256.
- Stage is SPENT. Use: checks input for the b246ebeb package only if the package commit equals b246ebeb or a reviewed
  lineage rule admits it (job608-after-package-m674c-binding-continuation.md).
