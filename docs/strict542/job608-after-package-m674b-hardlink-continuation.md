# Job608 continuation after package m674b hardlink refusal — 595 MUST NOT APPLY

Supersedes the NEXT pointer of job608-after-package-m674-unknown-continuation.md. All earlier gates, caps, reviews apply.

## What happened (2026-10-30)
- Reconciled m674 completion_unknown: offload up, load 0.19, runs.log has 0 package-m674 entries, no result608-package.
- `cp -al P/stage-package-m674 P/stage-package-m674b` (manifest 352ae639, runner b04abd4d, helper a558db9a), gates 0,
  preflight job608-package-m674b-preflight.json (ad74e78f), independent APPROVE ec4a0184.
- ONE launch ~04:12Z, identical caps. The remote ran to completion (no ssh drop this time). rc 2: `STEP608 builder-fail 2`,
  `REFUSED: hardlink refused: node_modules/.pnpm/@esbuild+linux-x64@0.28.2/node_modules/@esbuild/linux-x64/bin/esbuild`.
  Evidence: job608-package-m674b/. The stage is SPENT; nothing accepted.

## Diagnosis (deterministic source defect, not infrastructure)
- build598.sh:32 (674840b6) runs `pnpm --filter openclaw --prod deploy result598-build/runtime`. pnpm 12 imports packages
  from its content store by hardlink (package-import-method auto), so runtime files have st_nlink > 1.
- application598.py:92 `inventory()` correctly requires st_nlink == 1 (a hardlinked runtime file can be changed through
  its store twin after hashing). This check MUST NOT be removed or relaxed.
- The earlier mode refusal (fixed 674840b6) masked this second refusal in the same inventory pass.

## NEXT (source-only fix, then fresh worker)
1. Fix at its origin in build598.sh: make the deploy materialize independent copies, e.g.
   `pnpm --config.package-import-method=copy --filter openclaw --prod deploy ...` (an explicit reviewed CLI flag; the
   frozen-package608 preflight refuses inherited npm_config_/pnpm_config_ env, so do NOT use env). Update the recorded
   `command` in frozen-package608.py:51 and the build598.sh assertion to match exactly, and add a test in
   test_application598.py / the frozen-package test proving (a) a hardlinked runtime file is still refused and (b) the
   copy-mode deploy command is the only accepted one. Run the relevant unit tests locally (small) and commit.
2. Independent source review of that commit (no other changes; nlink check unchanged).
3. Re-prepare a NEW package stage (`--dest P/stage-package-m674c`, --commit <fix commit>, same --base/--stage package and the
   same four accepted --input results; never replay accepted stages). Storage gate must pass unchanged; the spent m674 and
   m674b exports may be trashed only if their inodes are singly linked (Decision661 lesson; m674b is cp -al of m674).
4. Gates, preflight json, independent preflight APPROVE, ONE launch (14g/4CPU/2460s, bg Bash >= 2800s) as the FIRST heavy
   action of a fresh worker with >= 2655s left, evidence, independent acceptance (incl. zero group/other-writable, nlink 1).
5. Then: final artifact receipt + old/new hash inventory, action/privilege/seal/reseal reviews, automatic queue review,
   genuine ordered HQ595 handoff. 587 fd3/socket transport replaces 586 sudo; never add the 586 rule.

## Update 2026-10-30 (same worker)
- Steps 1-2 DONE: source fix b246ebeb (`frozen-package608.py materialize` after deploy, before receipt; nlink check
  unchanged; copy-mode CLI flag NOT used because .npmrc is pinned and env policy is refused), independent APPROVE 6db9fa81.
- NEXT is step 3 with `--commit b246ebeb` -> P/stage-package-m674c, then step 4 as the FIRST heavy action of a fresh worker.
