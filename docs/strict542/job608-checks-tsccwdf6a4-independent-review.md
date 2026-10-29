# job608 independent review: f6a4de2e test-cwd correction + checks preflight tsccwdf6a4

Reviewer: independent (read-only; no offload/build/service run). Date 2026-10-29.

## 1. f6a4de2e correction (usage-window-types608.test.mjs)
- Diff is a single hunk: spawnSync options gain `cwd: root` (the mkdtemp dir) plus
  a comment. encoding/timeout/maxBuffer unchanged. tsc argv unchanged
  (--strict --noUncheckedIndexedAccess --target es2022 --module esnext
  --typeRoots root --skipLibCheck --noEmit input). Assertions unchanged
  (error undefined, signal null, status 0). No --ignoreConfig added.
- Real parser bytes still checked: readFileSync("src/gateway/strict542/usage-preflight.ts")
  and the type/boundary extraction run in process cwd BEFORE spawn; tsc path is
  path.resolve(...) (absolute, resolved against repo cwd) and input is
  path.join(root, ...) (absolute). Changing the child's cwd does not change what is compiled.
- Evidence (docs/strict542/job608-checks-label49d31/): checks-offload.rc=1; the log
  has fail 0 in other suites and exactly one failing test,
  usage-window-types608.test.mjs:10, TS5112. tsconfig-red.log.gz: old test fails
  with TS5112 (1 !== 0); tsconfig-green.log.gz: pass 1 fail 0. red.rc=1, green.rc=0.
  README describes it accurately (stage SPENT, no replay).

## 2. Diff scope
- 49d3fe33..f6a4de2e: 33 files; the only executable source change is the 6-line
  test hunk above. Everything else is evidence/inventory/review/preflight docs and logs.
- f6a4de2e..34dd332f: only job608-checks-tsccwdf6a4-preflight.json (+50).

## 3. Stage $P/stage-checks-tsccwdf6a4
- sha256: export-manifest.json c22d7696..., run608.sh 715e53bd..., stage608.py
  a558db9a..., successor598.tar 88fc8d3f..., all match the preflight.
- `python3 -I -B stage608.py verify-inputs` exit 0; `sh -n run608.sh` exit 0.
- Manifest: execution_state UNUSED, run_id stage608-checks-tsccwdf6a4,
  source_commit f6a4de2ebc6924d16fe559f9858bf8c50dce1eba.
- Streamed `git archive f6a4de2e -- <888 successor_paths> | sha256sum` =
  88fc8d3f1934c00d65e75324b79d8745f743a6fe426aaa98ecd50d38bef69ac9 (match). The
  corrected test is in successor_paths, and the tar member's sha (d729ffb2...)
  equals f6a4de2e's blob.
- Absent: result608-checks, $P/checks-tsccwdf6a4-offload.log, $P/checks-tsccwdf6a4-offload.rc.

## 4. Launch command
- Preflight `launch` is exactly:
  `offload run --timeout 1200 --mem 14g --cpus 4 --artifacts result608-checks -- timeout -k 15s 1140s sh run608.sh`

## VERDICT
VERDICT: APPROVE the f6a4de2e test-cwd correction and the tsccwdf6a4 checks launch
preflight, CONDITIONAL on fresh live gates at launch (health up, no competing run,
verify-inputs 0, storage 0, no result/log/rc, remaining >= 1575s). ONE run only, no
unchanged replay after admission. This is not acceptance; acceptance needs the run's
own result. 595 MUST NOT APPLY.
