# job608 checks 301d at 301d7456 — independent acceptance

Reviewer: independent, read-only (no offload/builds). Evidence 8d368786; precedent 406f410c (b246). P=/srv/encrypted/dev-move-98/agentq-source608-20261028-private.

## 1. Receipt and hashes
- `sha256sum -c result-files.sha256` in P/stage-checks-301d and in the evidence dir: 7/7 OK; live result dir holds exactly those 7 files.
  Committed checks/installed.json, stage-receipt.json, exit-code.txt, strict542-checks/installed.json byte-identical to live (cmp). exit-code.txt = 0.
- sha256(P/stage-checks-301d/export-manifest.json) = 1a5d47a7...a9ee = receipt manifest_sha256 = preflight manifest_sha256.
- Receipt: kind JOB608_STAGE_RECEIPT, stage checks, run_id stage608-checks-301d, exit_code 0, stage_inputs {},
  source_commit 301d7456bf5b0c4179b27d0db97eac7b07143f4a (= `git rev-parse 301d7456`), source_export_sha256 99add7e1...291d (= manifest = preflight).
- Receipt outputs equal actual files: checks/installed.json 9a770924...af50, checks/tests.log c1cc7a70...139de.
- Note: installed.json is vitest JSON with no source_commit field (same as precedent); its commit binding is via the receipt output digest + receipt source_commit 301d7456.

## 2. Tests
- installed.json: 17/17 suites, 272 passed, 0 failed, 7 pending, success true; write-unified-entry-dts.test.ts 14/14 passed (= manifest/preflight required_checks 14).
- checks-offload.log (gz copy identical to live P/checks-301d-offload.log): 14 ✔, 0 ✖, `ℹ pass 39`/`ℹ fail 0`, `STEP608 installed-checks-pass` once, last line; offload rc 0.
- checks/tests.log: 179 ✔, 0 ✖; node summaries fail 0 / cancelled 0; 12 unittest runs all OK (15/18/13/19/17/3/5/2/8/14/17/14); no FAIL/ERROR/Traceback;
  test_prepare_stage608_export ran 14 (7 InputLineageTest incl. refuses_non_ancestor/tampered_lineage_record + 7 LinkInputTest), all ok; vitest Test Files 7 passed (7).

## 3. Modes, links, caps
- `find result608-checks -perm /022`: empty (dirs 755, files 644). `find -type f -links +1`: empty (live and evidence).
- launch.txt caps (--timeout 1200 --mem 14g --cpus 4, timeout -k 15s 1140s sh run608.sh) equal preflight `launch` exactly; one launch.

VERDICT: ACCEPT
