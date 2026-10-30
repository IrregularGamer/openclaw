# Independent preflight review: job608 package m674b (preflight ad74e78f)

Reviewed against job608-after-package-m674-unknown-continuation.md and the approved m674 preflight (APPROVE 0a30b8b7 / re-review 3f2790f8). Read-only; nothing launched, stage not modified, remote not contacted.

## Checks (live, 2026-10-30)
1. P/stage-package-m674b exists. sha256: export-manifest.json 352ae639..., run608.sh b04abd4d..., stage608.py a558db9a... — match the json (and m674).
2. `python3 -I -B stage608.py verify-inputs` rc 0; `sh -n run608.sh` rc 0; no __pycache__ under the export (0 before and after).
3. `storage608.py check --root P --stage package` rc 0 (free_bytes 4362915840 = json gates_at_prepare value; reserve 2147483648).
4. P/package-m674b-offload.log and .rc absent; json log/rc point at package-m674b-offload.{log,rc} (not m674 or tail files).
5. Launch argv identical to m674 preflight: `offload run --timeout 2460 --mem 14g --cpus 4 --artifacts result608-package -- timeout -k 15s 2400s sh run608.sh`. Field diff vs m674 json: only run_id, export, prepare, log, rc, gates_at_prepare, and the new reconcile field differ; source_commit 674840b6, hashes, inputs, minimum_worker_seconds 2655, acceptance_extra unchanged.
6. `grep -c package-m674 ~/.local/state/offload/runs.log` = 0; no result608-package in P/stage-package-m674 (nor in m674b).

## Findings
- None blocking. Prepare follows continuation step 2 (cp -al, new slug, unified-5r1 precedent); new run_id avoids reusing the spent m674 slug.
- Note: the export is hard-linked to spent m674, so do not edit files in place in either tree; result608-package will be a new dir, so the launch does not affect this.
- Reminder from the continuation: if completion_unknown repeats, get the remote cause before a third launch.

VERDICT: APPROVE
