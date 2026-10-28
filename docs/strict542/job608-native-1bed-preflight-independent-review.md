# job608 native 1bed preflight: independent review (of a287d878)

**VERDICT: APPROVE** the UNUSED native export
`/srv/encrypted/dev-move-98/agentq-source608-20261028-private/stage-native-1bed` for one launch as planned. This review is source-only and read-only; it ran no offload and no build. It grants no install, package, application or reseal authority. **595 MUST NOT APPLY.**

Checked independently on 2026-10-28:
1. The export-manifest.json sha256 is 31330bc3...6931f. The manifest has stage=native, execution_state=UNUSED, run_id=stage608-native-1bed, source_commit and runner_commit 1bed4d1bb53e...9015, source_export_sha256 5d7e9d57...1263, and stage_inputs {}.
2. `cmp` shows run608.sh and stage608.py are byte-identical to `git show 1bed4d1b:docs/strict542/run-stage608.sh` and `:docs/strict542/stage608.py`. Their sha256 values match the pins: runner eac266cf...b8ee and helper a558db9a...0de4.
3. These files match their manifest keys:
   - successor598.tar = ea5b2c39... (successor_archive_sha256)
   - native598.tar = d73e4e35... (native_export_sha256)
   - rolldown608-source.tar.gz = 203aa483... (compiler_upstream_archive_sha256)
   - compile/receipt.json = 4a651254... and libtests/receipt.json = 2f81179f... (native_stage_outputs)
   - native608-stages holds exactly those 2 files.
   - source598.tar has the same inode (395540) as ../base/source598.tar, so it is a hard link of the digest-verified base.
4. Compared with ../base/export-manifest.json (its sha256 is 20111ce5, which matches the new predecessor_manifest_sha256), only four keys changed: stage (checks->native), run_id, predecessor_manifest_sha256 and predecessor_package_attempt. All four are on the allowed stage-identity list. No other key differs.
5. In stage608.py at 1bed, `STAGES['native']=[]`, so verify_inputs requires an empty stage_inputs set, and the manifest has one. run-stage608.sh has a `native)` case branch that runs `timeout -k 15s 2400s prepare-native-consumer608.py` and returns only native/{receipt,libtests-receipt,addon}.
6. The planned launch matches job608-after-carrier-continuation.md: `offload run --timeout 2460 --mem 4g --cpus 1 --artifacts result608-native -- timeout -k 15s 2400s sh run608.sh`, only with at least 2655 s of worker life left, in a fresh worker, as the first launch. The preflight also keeps two rules: no unchanged rerun after a failure or timeout, and `storage608.py result --stage native` before the result is accepted.

Notes (not blocking):
- The continuation doc gates native on "storage genuinely reconciled". The encrypted staging approved in review 1e4c30d0 is the reconciliation. The preflight reports 6614769664 B free against the 6442450944 B floor, a margin of only about 164 MiB, so re-run `storage608.py check --stage native` right before launch.
- The manifest's inherited purpose/required_checks prose is historical. The exact runner and stage define what runs.
- The root /opt capacity question is still 595's separate obligation.
