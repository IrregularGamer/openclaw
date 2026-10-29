# Independent acceptance: job608 tail tsccwdf6a4 actual run and storage608 tail cap correction

Reviewer: independent. I did not produce this evidence or the correction. Scope: evidence commit
`836b3d66` (`job608-tail-tsccwdf6a4/`) and source-only correction `8f4fb3b3` (storage608 tail cap
128MiB -> 192MiB). P = /srv/encrypted/dev-move-98/agentq-source608-20261028-private. Result
directory P/stage-tail-tsccwdf6a4/result608-tail. All checks were read-only. I launched no
offload and modified nothing under /srv. I read the checkpoint through python tarfile and `tar -tzf`
only and never extracted it.

## Evidence (836b3d66)

- PASS: manifest. The SHA256 of `P/stage-tail-tsccwdf6a4/export-manifest.json` is
  `add772f5f0e861bf1a28f8ecdf1d616aea4a505af745579e192bc9e17fe3bbdb`, matching the README pin and the
  receipt manifest_sha256. The manifest stage is `tail`. The staged `stage608.py` is `cmp`-identical to
  `docs/strict542/stage608.py`.
- PASS: return codes. The private `P/tail-tsccwdf6a4-offload.rc`, the committed `tail-offload.rc`, and
  both copies of `exit-code.txt` (private and committed) all contain `0`.
- PASS: offload log. The decompressed committed `tail-offload.log.gz` is `cmp`-identical to the
  private log (7 lines). The STEP608 lines are tail-stage-native-start +11s,
  tail-restore-build-done +24s, tail-build-start, `tail-build-done +237s` and `tail-pass`.
- PASS: result file hashes. The private result contains exactly 5 regular files and nothing else.
  Run from P/stage-tail-tsccwdf6a4, `sha256sum -c result-files.sha256` reports OK for all 5.
- PASS: committed copies. exit-code.txt, strict542-checks/pnpm-path.txt and tail/stage-receipt.json are
  `cmp`-identical to the private originals. build.log and checkpoint stay private and are bound by
  result-files.sha256 and the receipt.
- PASS: stage receipt. SHA256 `8df9caa8...ae61`. kind `JOB608_STAGE_RECEIPT`, stage `tail`,
  exit_code 0, run_id `stage608-tail-tsccwdf6a4`, source_commit
  `f6a4de2ebc6924d16fe559f9858bf8c50dce1eba`, source_export_sha256 `e81e07d2770ad597...8145`,
  manifest `add772f5...bdb`. Its outputs are tail/build.log `7272c306...204a` and
  tail/checkpoint.tar.gz `b5b8f9ff...dca7`, and both equal the actual file SHA256.
- PASS: stage inputs. The receipt lists 13 stage_inputs: middle (build.log 9d1fdaf9, checkpoint
  32ea0475, stage-receipt 9eb3083c), native (libtests-receipt 2f81179f, receipt 4a651254, rolldown
  binding 0b6607e7, stage-receipt 10474857), sdk-0 (766e2130, 09f9d2b8, stage-receipt 08530815) and
  sdk-1 (ab5dfafc, f31068ea, stage-receipt e57265f3). Each equals both its staged copy and the accepted
  P/stage-*-tsccwdf6a4/result608-* original.
- PASS: build.log (829 lines). The only case-insensitive error/fail/cancel match is line 448, the
  asset filename `update-failure-report-BOWrK2mD.js`, which is not a failure. The log ends with the
  build-all phase timings (total 1m 45.8s).
- PASS (scrutinised): checkpoint. It is 161524783 bytes. `tar -tzf` exits 0 and lists 18159
  entries: 15907 files, 1069 dirs and 1183 symlinks. There are no hardlinks, device or FIFO entries,
  setuid/setgid/sticky modes or non-root owners. No entry name is absolute or contains `..`, and every
  entry is under `tail/`. All 1183 symlinks are under `tail/data/dist-runtime/` and use relative
  `../` targets. Once normalised, every target resolves inside `tail/data/` to an existing archive
  member, so none escapes and none dangles. This is the same dist-runtime overlay pattern that
  stage608.py's restore validator explicitly admits (`expected+'/data/'`). Uncompressed size is
  484168658 bytes, mostly tail/data/dist (426.5MB): package-update-activation-recovery.mjs 66.4MB,
  worker/worker.mjs 55.3MB, worker/sqlite-store.worker.mjs 49.4MB, plus dist-runtime 19.8MB,
  extensions 18.1MB, receipt.json 13.7MB and packages 6.0MB. That is real dist output, so the
  ~154MiB compressed size is explained.

## Cap correction (8f4fb3b3)

- PASS: the gate failure is real and correctly attributed. The result's logical size
  (`du -sb --apparent-size`) is 161610911 bytes. Run against this result, the pre-correction
  storage608 (from 836b3d66) exits 1 with `finite stage return cap exceeded` (161610911 > 134217728).
  The diff changes only `CAPS['tail']` 128->192MiB and the matching test expectation 2784->2848MiB.
- PASS: forecast arithmetic. 696548381 + 16*16MiB + 2848MiB + 128MiB = 4085546013 <= MAX_STORE
  4294967296, which leaves 209421283 bytes (~199.7MiB) of headroom. `forecast()` still raises above
  4GiB.
- PASS: `python3 -I -B docs/strict542/test_storage608.py` runs 7 tests, OK.
- PASS: `storage608.py result --result P/stage-tail-tsccwdf6a4/result608-tail --stage tail` exits 0
  with `{"logical_return_bytes": 161610911, "return_cap_bytes": 201326592}`.
  `check --root P --stage tail` also exits 0 now.
- PASS: safety. The correction does not weaken any safety property. The per-stage cap is a planning
  bound on staging storage. The hard protections are unchanged: the MAX_STORE aggregate check in
  `check_room`, FREE_RESERVE 2GiB, the 4GiB `forecast` refusal, and every build, hash, receipt and
  path check in stage608. 192MiB still leaves ~30MiB of headroom over the observed return.
- PASS: applying it post hoc is legitimate, and no rerun is required. The result is byte-for-byte
  unchanged (hashes and receipt verified above). The cap gates storage accounting, not build
  correctness or security, and the corrected cap admits it. A rerun would spend a worker to produce
  the same ~154MiB output and would fail the old cap the same way.
- NOTE (non-blocking, provenance): the private `P/storage-receipt.json` still records the tail cap as
  134217728 and helper_sha256 `2cf48a3b...`, while the current storage608.py hashes to
  `7c97f0fa...`. No code re-verifies that receipt, so this does not block acceptance. Future reviews
  should read 8f4fb3b3 as the authoritative cap table.

## Forward note: package check_room (non-blocking)

- FAIL (not blocking this acceptance): `storage608.py check --root P --stage package` exits 1 with
  `aggregate staging cap would be exceeded`. Current bytes_used(P) is 2318654419 (~2211.2MiB). Adding
  2048MiB + 16MiB + 128MiB gives 4617133011, which is ~307.2MiB over MAX_STORE. Free space on the
  volume is 5004468224. Real usage of P is above what the stage-by-stage forecast assumed, and the
  tail cap change plays no part in this, because check_room charges only the package cap. Before the
  package stage, someone must either reclaim private staging space under P (with the user's approval)
  or make a reviewed plan correction.

VERDICT: ACCEPT
