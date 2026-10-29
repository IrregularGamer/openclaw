# job608 compiler m674 at 674840b6 — independent acceptance

Reviewer: independent (source only; no launches, installs, service/sudo/seal changes).
Evidence commit: 17c0ea58. Preflight: a130cb2b, independent APPROVE 8566c2b9 (manifest
0807dbe2a6ebf2e45ab9d421bc9cbe12a1e7b896e53a2c84715d7a5a442354ba).
P=/srv/encrypted/dev-move-98/agentq-source608-20261028-private. Model: job608-checks-m674-independent-acceptance.md,
job608-compiler-tsccwdf6a4-independent-acceptance.md. Rules: job608-after-package-moderefusal-continuation.md.

## 1. Receipt and hashes
- sha256(P/stage-compiler-m674/export-manifest.json) = 0807dbe2...54ba = receipt manifest_sha256 = preflight manifest.
  run608.sh b04abd4d...7816 and stage608.py a558db9a...0de4 still equal the preflight pins.
- Receipt (compiler/stage-receipt.json 90de5690...c9d7): kind JOB608_STAGE_RECEIPT, stage compiler, run_id
  stage608-compiler-m674, source_commit 674840b669c43af54a62e30b4028f219f4a428c9, source_export_sha256
  e1a6de35...4461b (= manifest = preflight), exit_code 0.
- Receipt outputs {compiler/tests.log: 42249f38...779b} = sha256 of the actual compiler/tests.log
  (strict542-checks/tests.log is the same bytes).
- Receipt stage_inputs = manifest stage_inputs, and each equals sha256 of the same path in
  P/stage-native-m674/result608-native (native m674 accepted 5a412599): libtests-receipt.json 2f81179f,
  receipt.json 4a651254, rolldown-binding.linux-x64-gnu.node 0b6607e7...e042, stage-receipt.json 0bb266db.
- `python3 -I -B stage608.py verify-inputs` in the export: exit 0 (inspected first: verify_inputs only reads the
  manifest and staged inputs; -B prevents bytecode writes; no new files appeared in the export).
- Committed result-files.sha256: all 6 entries `sha256sum -c` OK against P/stage-compiler-m674/result608-compiler;
  the live tree has exactly those 6 files (no extra/missing). Committed result608-compiler/ is `diff -r` identical
  to live. exit-code.txt = 0. result598-native/stock-patched-equality.json names addon_sha256 0b6607e7...e042.

## 2. Run completion
- Committed offload.rc = P/compiler-m674-offload.rc = 0. launch.txt cmp-equal to P/compiler-m674-launch.txt
  (one launch, 22:31:56Z, manifest 0807dbe2). compiler-offload.log.gz decompresses byte-identical to
  P/compiler-m674-offload.log.
- ~/.local/state/offload/runs.log: exactly one entry for this stage,
  `2026-10-29T22:36:02Z run remote rc=0 245s .../stage-compiler-m674` (client writes it only after rc 0 and pull).
- Offload log: `STEP608 compiler-checks-pass` exactly once (last line); no error/fail/timeout/denied lines.

## 3. Tests
- compiler/tests.log: five ordered node summaries, each tests 2 / pass 2 / fail 0 / cancelled 0 (10 ✔, 0 ✖),
  same shape as the accepted tsccwdf6a4 compiler log (lazy-barrel config/semantics x2, frozen equality,
  real split worker / minifier).

## 4. Modes and names
- `find P/stage-compiler-m674/result608-compiler -perm /022` = 0 entries (dirs 755, files 644; getfacl shows no
  extra ACL entries). Compiler stage returns no checkpoint tarball, so there is nothing to `tar -tvzf`.
- No secret/key/credential/token/env/pem names in the result tree.

## Notes (non-blocking)
- The continuation note says to run `offload run` in the foreground with a 600000 ms Bash timeout only if
  --timeout <= 420; compiler uses --timeout 600. The run finished in 245s with rc 0 captured, so no effect;
  future runtime launch (2460s) must use the background form with a timeout >= offload --timeout + 300s.
- Manifest execution_state still reads UNUSED (pinned manifest, never hand-edited, as required).

VERDICT: ACCEPT
Reasons: rc 0 (client rc file, runs.log, exit-code.txt, receipt), receipt bound to manifest 0807dbe2, source
674840b6 and accepted native m674 inputs (addon 0b6607e7), outputs hash = tests.log, 10/10 pass 0 fail,
STEP608 compiler-checks-pass, result hashes match live files, zero group/other-writable entries, no secret names.
