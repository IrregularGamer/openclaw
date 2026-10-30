# job608 checks b246 at b246ebeb — independent acceptance

Reviewer: independent (read-only; no launches, installs, offload, service/sudo/seal changes).
Evidence commit: e32837c5. Preflight: job608-checks-b246-preflight.json (independent APPROVE 03dd497a).
P=/srv/encrypted/dev-move-98/agentq-source608-20261028-private. Model: job608-checks-m674-independent-acceptance.md.

## 1. Receipt and hashes
- `cd P/stage-checks-b246 && sha256sum -c result-files.sha256`: all 7 entries OK; the result dir contains exactly
  those 7 files (no extra/missing).
- Committed copies of checks/installed.json, checks/stage-receipt.json (75ef9418...fa8), exit-code.txt and
  strict542-checks/installed.json are byte-identical to P. exit-code.txt = 0.
- sha256(P/stage-checks-b246/export-manifest.json) = 16552908...58ac = receipt manifest_sha256 = preflight manifest.
- Receipt: kind JOB608_STAGE_RECEIPT, stage checks, run_id stage608-checks-b246, source_commit
  b246ebebab7d99f189a1d9cc327b7da1f0fc3f69 (= `git rev-parse b246ebeb`), source_export_sha256 264d042c...3007
  (= export manifest's source_export_sha256 = preflight), stage_inputs {}, exit_code 0.
- Receipt outputs match the files: checks/installed.json 1cb22844...9789, checks/tests.log 0a25139f...fa86aa.

## 2. Tests
- checks-offload.log.gz: 14 ✔, 0 ✖ (the 14 required write-unified-entry-dts assertions; manifest and preflight
  required_checks = 14), `ℹ pass 39` / `ℹ fail 0`; `STEP608 installed-checks-pass` exactly once, last line.
- checks/tests.log: 179 ✔, 0 ✖; all node summaries fail 0 / cancelled 0; 12 python unittest runs all `OK`
  (15/18/13/19/17/3/5/2/8/14/17/7), no `... FAIL`/`... ERROR` lines; the 8 test_frozen_package608 tests all `ok`,
  incl. test_materialize_breaks_store_hardlinks_without_following_symlinks and
  test_materialize_refuses_redirected_runtime; vitest Test Files 7 passed (7).
- installed.json: 17/17 suites, 272 passed, 0 failed, 7 pending, success true.

## 3. Modes, links, rc, caps
- `find P/stage-checks-b246/result608-checks -perm /022`: empty (dirs 755, files 644).
- `find ... -type f -links +1`: empty (all nlink 1).
- offload.rc = 0 (client rc captured; no deviation, unlike m674).
- launch.txt caps `offload run --timeout 1200 --mem 14g --cpus 4 --artifacts result608-checks -- timeout -k 15s 1140s
  sh run608.sh` equal preflight `launch` exactly. One launch recorded.

VERDICT: ACCEPT
