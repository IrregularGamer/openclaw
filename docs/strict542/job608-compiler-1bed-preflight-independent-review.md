**VERDICT: APPROVE**

# Independent review: job608 compiler stage preflight (UNUSED export, frozen 1bed)

Reviewed claims in `job608-compiler-1bed-preflight.md` (commit e52d4c4f) against the export
`/srv/encrypted/dev-move-98/agentq-source608-20261028-private/stage-compiler-1bed`. Read-only review: no offload, no build, nothing in the export was changed. source598.tar was not hashed (inode check only, as instructed).

This review grants no install, build-package, application or reseal authority. It only says the compiler export is ready for its one planned launch. **595 MUST NOT APPLY.**

## Findings

1. **Manifest hash matches.** `export-manifest.json` sha256 is 5c39447c52ec9e9a3418420dafa278e024cd713dcfae0822e6cdae6392dab842, as the preflight says.
2. **Manifest fields are correct.** stage `compiler`, execution_state `UNUSED`, run_id `stage608-compiler-1bed`, source_commit and runner_commit both 1bed4d1bb53eff145f724cc6a448dc73b3609015, source_export_sha256 5d7e9d57fb660e2b54f5595e81ddf332027e21b303937c2cd6bc7f718f311263.
3. **The predecessor link is valid.** predecessor_manifest_sha256 20111ce5… equals the sha256 of `../base/export-manifest.json`.
4. **Only the expected keys differ from base.** Both manifests have the same set of keys. Only stage (checks to compiler), run_id, predecessor_manifest_sha256, predecessor_package_attempt and stage_inputs (empty to 4 native entries) have different values. Everything else is identical, including the source, runner, helper and successor digests.
5. **The stage inputs match the manifest and the native result.** All 4 files in `stage608-inputs/native/` hash to the stage_inputs digests (stage-receipt e8198c1d…, receipt 4a651254…, libtests-receipt 2f81179f…, binding .node 0b6607e7…). They are hard links (link count 2) sharing inodes 395570-395573 with `stage-native-1bed/result608-native/native/*`.
6. **The inputs match the accepted native receipt.** `docs/strict542/job608-native-1bed/stage-receipt.json` (committed in 8866a036, unchanged since) hashes to e8198c1d…, the same as the staged stage-receipt. Its `outputs` digests match the other three staged files. Its manifest_sha256 (31330bc3…) equals the sha256 of the native export manifest. Its source_commit and source_export match the compiler manifest. Its exit_code is 0.
7. **The scripts are byte-identical to the frozen commit.** `run608.sh` matches `git show 1bed4d1b:docs/strict542/run-stage608.sh` and `stage608.py` matches `1bed4d1b:docs/strict542/stage608.py` (cmp clean).
8. **The compiler stage depends only on native.** `STAGES['compiler'] == ['native']` in stage608.py, which agrees with the stage_inputs.
9. **source598.tar is the same file as in base.** It has inode 395540, the same as `../base/source598.tar`.
10. **The export is clean.** There is no `result608-compiler` directory, so the export is unused. `find` found no .env, .db or sqlite files, no key, pem or id_* files, and no `__pycache__`.
11. **The planned command is bounded.** `offload run --timeout 2460 --mem 4g --cpus 1 --artifacts result608-compiler -- timeout -k 15s 2400s sh run608.sh`. The inner limit is 2400 s plus a 15 s kill grace, so 2415 s in total. That is 45 s less than the 2460 s offload limit, so the inner timeout fires first and artifacts can still come back. The 2655 s worker-life precondition leaves about 195 s of headroom above 2460 s for storage608 result handling. Memory is capped at 4g and CPU at 1, and there is a single launch with no unchanged rerun.

## Not independently re-run
- `stage608.py verify-inputs` (rc 0) and the `storage608.py check` numbers were not re-run; I relied on the direct hash and inode checks above.
- The preparer's sha256 (1e701de0…) was not re-hashed.
