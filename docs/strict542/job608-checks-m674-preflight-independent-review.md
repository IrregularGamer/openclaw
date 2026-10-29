# job608 independent review: checks preflight m674 at 674840b6

Reviewer: independent (read-only; no offload/build/service run). Date 2026-10-29.
Reviewed: docs/strict542/job608-checks-m674-preflight.json (b134b132) against P/stage-checks-m674
(P=/srv/encrypted/dev-move-98/agentq-source608-20261028-private). C = 674840b669c43af54a62e30b4028f219f4a428c9
(fix APPROVED 017cd166). Models: job608-native-m674-preflight-independent-review.md, job608-checks-tsccwdf6a4-preflight.json.

## 1. Hashes (all match preflight and manifest)
- export-manifest.json 24fea139f68e2a4a6fb171d3d5895eb457dd3dcd074e4ebed3087bd4fa4baf29 (= manifest_sha256)
- run608.sh b04abd4d6d08f2352bd04e5ecc4e3e56d9f6c67223c175a03e98fa44cc0b7816 (= runner_sha256; same as native m674)
- stage608.py a558db9afacd22111fb5c2590fe902298b12ea06910eac6efab43f4aa27c0de4 (= stage_helper_sha256)
- successor598.tar 9374675e9d48f846cfe8a428cb1b32bbc188e41c021bf653224084f0f6190296 (= successor_archive_sha256)
- source598.tar e79a0e45... / native598.tar d73e4e35... / rolldown608-source.tar.gz 203aa483... (= manifest pins)
- Manifest: run_id stage608-checks-m674, stage checks, execution_state UNUSED, launch_history none,
  source_commit = runner_commit = C, source_export_sha256 e1a6de3552e9f3a40cb4fbd9bb13acc63f16d725c21a0994d022ed9f4084461b,
  stage_inputs {}, required_checks 14.
- prepare-stage608-export.py writes run608.sh from `git show C:docs/strict542/run-stage608.sh` and stage608.py from
  `git show C:docs/strict542/stage608.py`; both cmp-equal to the staged files.

## 2. Gates
- `python3 -I -B stage608.py verify-inputs` exit 0; `sh -n run608.sh` exit 0.
- stage608.py STAGES['checks']=[] so empty stage_inputs is correct.
- storage608.py check not rerun here; remains a fresh live gate at launch.

## 3. Launch caps
- `offload run --timeout 1200 --mem 14g --cpus 4 --artifacts result608-checks -- timeout -k 15s 1140s sh run608.sh`,
  identical to job608-checks-tsccwdf6a4-preflight.json; minimum_worker_seconds 1575 unchanged.
- Absent: P/stage-checks-m674/result608-checks, P/checks-m674-offload.log, P/checks-m674-offload.rc.

## 4. Mode fix
- run608.sh has `umask 022` and `tar --no-same-permissions` on source598/successor598/native598 extraction.

## Notes (non-blocking)
- Manifest metadata `purpose` still reads "...stage native..." and `source_correction_review` cites 5ec111ba
  pending; both are inherited carry-over text (identical in the previously used checks-tsccwdf6a4 manifest;
  prepare's purpose replace does not match this base string). Neither field is read by run608.sh or stage608.py.

## VERDICT
Conditional on fresh live gates at launch (health up, no competing run, verify-inputs 0, storage608.py check
--stage checks 0, no result/log/rc, remaining >= 1575s). ONE run only; no unchanged replay after admission.
Not acceptance; acceptance needs the run's own result (14 checks, zero group/other-writable result entries).

VERDICT: APPROVE
