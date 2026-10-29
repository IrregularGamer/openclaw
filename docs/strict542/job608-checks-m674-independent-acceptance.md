# job608 checks m674 at 674840b6 — independent acceptance

Reviewer: independent (source only; no launches, installs, service/sudo/seal changes).
Evidence commit: df554bc5. Preflight: 2e9a908c (manifest 24fea139f68e2a4a6fb171d3d5895eb457dd3dcd074e4ebed3087bd4fa4baf29).
P=/srv/encrypted/dev-move-98/agentq-source608-20261028-private. Model: job608-checks-tsccwdf6a4-independent-acceptance.md,
job608-native-m674-independent-acceptance.md.

## 1. Receipt and hashes
- sha256(P/stage-checks-m674/export-manifest.json) = 24fea139...af29 = receipt manifest_sha256 = preflight manifest.
- Receipt: kind JOB608_STAGE_RECEIPT, stage checks, run_id stage608-checks-m674, source_commit
  674840b669c43af54a62e30b4028f219f4a428c9, stage_inputs {}, exit_code 0.
- Receipt outputs match actual files: checks/installed.json b2eec91d...74cf, checks/tests.log 4b8bbe31...2f12.
- All 7 entries of committed result-files.sha256 match the files in P/stage-checks-m674/result608-checks (no extra
  or missing files). Committed copies of installed.json, stage-receipt.json, exit-code.txt and
  strict542-checks/installed.json are byte-identical to P. exit-code.txt = 0.

## 2. Tests
- P/checks-m674-offload.log: 14 ✔, 0 ✖ (the 14 required write-unified-entry-dts assertions, matching manifest
  required_checks 14 as in the tsccwdf6a4 model), `ℹ fail 0`; `STEP608 installed-checks-pass` present exactly once (last line).
- result checks/tests.log: 179 ✔, 0 ✖; every node summary block reports fail 0 / cancelled 0 (102, 28, 39, 1 ...);
  python unittest lines matching "fail" are test names ending in `... ok`.
- installed.json: 17/17 suites, 272 passed, 0 failed, 7 pending, success true.

## 3. Modes
- `find P/stage-checks-m674/result608-checks -perm /022` is empty (dirs 755, files 644).

## 4. Disclosed deviation (offload client rc file not captured)
Offload client (/home/deploy/.local/bin/offload, read-only) `cmd_run`: after `run_teed` returns the remote rc,
rc 255 -> completion_unknown, 95 -> remote_lease_denied, INFRA/mismatch -> remote_environment_blocked; only
`if rc == 0` does it call `pull_artifacts` (rsync copy-back), and only after a successful pull does it call
`log_run(... rc ...)`. Therefore:
- artifacts are copied back only after the remote command has settled with rc 0; a non-zero remote exit (including
  the inner `timeout -k 15s 1140s sh run608.sh` failing or timing out) returns no artifacts and hence no receipt in P;
- the receipt itself is written by `stage608.py receipt` only at the end of run608.sh's success path.
- Stronger than the missing rc file: ~/.local/state/offload/runs.log has exactly one entry for this stage,
  `2026-10-29T21:15:44Z run remote rc=0 811s .../stage-checks-m674` (21:02:11 launch + 811s consistent), written by
  the client itself after successful artifact pull. `offload status`: friend VPS up, no failure indicated.
- Exactly one launch: launch.txt / P/checks-m674-launch.txt record one launch plus the parent-shell SIGKILL note;
  runs.log shows one run for this stage.
- No relabelling: the tsccwdf6a4 checks receipt is unchanged (sha256 573936...052e, still identical to the copy in
  stage-package-tsccwdf6a4 inputs) and differs from the m674 receipt (f2097d...4fc5), which carries the m674
  manifest, source_commit 674840b6 and run_id stage608-checks-m674.

Judgment: the rc file was a convenience capture of the client's return value; the client's own runs.log rc=0
entry, the rc==0-gated artifact copy-back, inner exit-code 0 and receipt exit_code 0 are sufficient completion
evidence. The SIGKILL hit only the wrapping bash, not the offload client or remote run. Procedural note only.

VERDICT: ACCEPT
