# job608 compiler 301d independent acceptance

Checked (read-only, nothing rerun):
- manifest sha256 d0af6061... equals preflight and receipt; run608.sh (b04abd4d...) and stage608.py (1d2bf411...) equal preflight pins.
- Receipt: kind JOB608_STAGE_RECEIPT, stage compiler, run_id stage608-compiler-301d, source_commit 301d7456..., source_export_sha256 99add7e1... (= preflight), exit_code 0; output tests.log digest matches file; stage_inputs (4 native files) equal sha256 of stage-native-301d/result608-native/native/*.
- `stage608.py verify-inputs` exit 0, no new files.
- result-files.sha256 (6 files) `sha256sum -c` all OK from the stage dir; live result608-compiler has exactly those 6 files; diff -r with committed copy identical; exit-code.txt = 0; result tree has no group/other-writable entries, files nlink 1. (Group/other-writable files exist only in staged inputs/tarballs, not results.)
- offload.rc = P/compiler-301d-offload.rc = 0; compiler-offload.log.gz decompresses identical to P log; runs.log has exactly one entry (06:52:00Z rc=0 247s); log ends with STEP608 compiler-checks-pass; no secret/.env transfer lines found. Test log shows all listed tests pass, 0 fail. (The count of 14 checks was not separately enumerated in the log; the single pass marker is present.)

VERDICT: ACCEPT
