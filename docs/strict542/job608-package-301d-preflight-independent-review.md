# Independent review: job608 package 301d preflight (77350895)

VERDICT: APPROVE

Reviewed docs/strict542/job608-package-301d-preflight.json against E=P/stage-package-301d (P=/srv/encrypted/dev-move-98/agentq-source608-20261028-private). Read-only; nothing launched, deleted or modified.

## Evidence
- sha256 matches the JSON: export-manifest.json 025654bd...a8f0, run608.sh b04abd4d...7816, stage608.py 1d2bf411...bffd.
- `cmp`: E/run608.sh is byte-identical to `git show 301d7456:docs/strict542/run-stage608.sh`; E/stage608.py is byte-identical to `301d7456:docs/strict542/stage608.py`.
- Manifest: stage=package, run_id stage608-package-301d, source_commit and runner_commit 301d7456bf5b..., execution_state UNUSED, launch_history none. input_lineage.ancestor_commit is 674840b669c4...
- changed_paths (188) match `git diff --name-only 674840b6 301d7456` and the preflight JSON. Every path is in stage608.LINEAGE_ALLOWED_PATHS or matches docs/strict542/job608-*, so none fall outside.
- Diff 674840b6..301d7456 on frozen-package608.py and stage608.py (+66/-4): frozen-package608 only gains `materialize` and its argv dispatch, and the preflight/receipt logic is unchanged. stage608 only gains lineage_path_allowed/check_lineage, lineage-aware commit/export matching for the native/compiler/tail receipts with pinned digests, and passes input_lineage through into the receipt. Neither file touches archive_build, stage_native or restore.
- Gates: `sh -n run608.sh` rc 0; `python3 -I -B stage608.py verify-inputs` (cwd E) rc 0. There are no *.pyc or __pycache__ files in E before or after. E/result608-package, P/package-301d-offload.log and P/package-301d-offload.rc do not exist.
- `storage608.py check --root P --stage package` rc 0 (free 4319625216, reserve 2147483648, unique 1892988778). `git diff 301d7456 HEAD -- docs/strict542/storage608.py` is empty and FREE_RESERVE=2048*MIB, so the reserve is unchanged.
- The spent stages were pinned before they were deleted: job608-package-m674{,b,c}/export-manifest.pinned.json are present (the m674c pin sha256 starts with 731ba6f7, as the preflight states). P/stage-package-m674* and trash-608/stage-package-m674c* are gone.
- The launch argv is identical to the package m674b preflight (`offload run --timeout 2460 --mem 14g --cpus 4 --artifacts result608-package -- timeout -k 15s 2400s sh run608.sh`). minimum_worker_seconds is 2655 in both.

## Notes (non-blocking)
- Some manifest prose fields were inherited from the base export (for example purpose "...build stage native", source_correction_review, predecessor_package_attempt). They are descriptive only, and verify-inputs/the runner do not key on them.

## Conditions
- ONE run only, using the exact argv above with caps unchanged. Write the log and rc to P/package-301d-offload.{log,rc}.
- Re-check live gates at launch: worker budget >= 2655 s, storage608 check rc 0, verify-inputs rc 0, no pyc in E, no existing result608-package/log/rc, and the manifest/runner/helper sha256 unchanged.
- Any refusal or failure makes this export spent. Do not relaunch it. Prepare a fresh export and get a new review.
- Acceptance additionally requires that the result mode listing shows zero group/other-writable entries and nlink 1.
