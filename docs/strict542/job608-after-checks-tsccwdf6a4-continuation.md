# Job608 continuation after checks tsccwdf6a4 — 595 MUST NOT APPLY

Supersedes the checks/native sections of job608-after-label-correction-continuation.md.

- checks-label49d31 (49d3fe33): SPENT_FAILURE rc1, only usage-window-types608
  failed with TS5112 (root tsconfig discovery). Evidence job608-checks-label49d31/.
- Correction f6a4de2e (tsc spawned with cwd = temp dir; flags/inputs/assertions
  unchanged), RED/GREEN evidence, independent review 4ce3e771.
- NEW checks stage608-checks-tsccwdf6a4 (manifest c22d7696, source export
  e81e07d2, successor 88fc8d3f, runner 715e53bd, helper a558db9a): remote rc0
  in 871s, 279 vitest (272 pass/7 baseline Windows-only skips/0 fail), all 14
  required checks, strict542 root supervisor IPC refusal/cancellation/settlement
  cases ok, result 309501 B. Evidence 92aeda26, independent ACCEPT d9a3822e.
- Prior native-label49d31 stage/preflight (61c98062, 49d3) is SUPERSEDED: never launch it.

## NEXT FRESH WORKER, FIRST heavy step: native at f6a4de2e

Prepared UNUSED 13:2xZ: P/stage-native-tsccwdf6a4, manifest
b51a34e949a4322f891b34d200c7d87f58333ab854209c0e4b4c2f5703a9f9f6, inputs empty,
verify-inputs 0, sh -n 0. NOT yet independently reviewed: get an exact
independent preflight review (same checklist as 4ce3e771 applied to this stage)
before launch. Then require fresh health up, no competing run, storage608.py
check --stage native 0, no result608-native/log/rc and >=2655s left (prefer 2895):

```sh
cd /srv/encrypted/dev-move-98/agentq-source608-20261028-private/stage-native-tsccwdf6a4
offload run --timeout 2460 --mem 14g --cpus 4 --artifacts result608-native -- timeout -k 15s 2400s sh run608.sh > ../native-tsccwdf6a4-offload.log 2>&1
printf '%s\n' "$?" > ../native-tsccwdf6a4-offload.rc
```

Do not `git pull` in workers (it hung 13:1xZ, no tty credentials); the
reviewer commits in the same checkout. After native: runtime, unified0
(must pass + acceptance before compiler), compiler, unified1..5, middle,
sdk0/1, tail, package at f6a4de2e through the unchanged gates; then final
artifact/action/privilege/seal/automatic reviews and job608-final-HQ-HANDOFF.md
bound to the actual package. No install/seal/root/unit/sudo/service changes.
