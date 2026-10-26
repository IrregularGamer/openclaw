# Exact608 continuation after compile2 — 2026-10-26

Supersedes the next-run section of job608-resume-after-lifetime.md.

## Done this round
- Lifetime-only rerun (export608-native-lifetime2, source33335af7, review
  job608-lifetime2-export-review.md): rc0, helper 7/7, retention negative
  detected (3 named FAILED). ACCEPTED: job608-native-lifetime2-receipt.json. SPENT.
- Compile2 (export608-native-compile2, source bd8a3a9f, review
  job608-compile2-export-review.md): rc1, rustc E0282 at the untyped
  `should_finalize` closure inserted by prepare-native608.py. No addon. SPENT.
- Fix 40947f38: closure typed `|idx: rolldown_common::ModuleIdx|`; predicate
  otherwise byte-identical. RED->GREEN in job608-finalizer-type-{red,green}.txt.
  Independently reviewed with fresh export: job608-compile3-export-review.md.

## Ordered next steps (default 2g/1CPU; launch only with >=35 min worker left)
1. ONE run of the APPROVED export /home/deploy/agentq/tmp/export608-native-compile3
   (manifest job608-native-compile3-export.json, tar 5eb5a44e…):
   `cd export608-native-compile3 && offload run --artifacts result-native608-compile -- timeout -k 15s 2700s sh run608.sh compile`
   Accept only rc0, complete receipt, new addon_sha256. Any rustc/borrowck
   error: fix in prepare-native608.py with a RED->GREEN test and a new reviewed
   export; never rerun a spent export.
2. Fresh reviewed libtests export from the same commit (~31 min run).
3. ONE combined native-worker-lazy diagnostic (all checks + 57 configs incl.
   worker46), needs >=55 min worker, per job608-resume-after-workers.md.
4. Then steps 3+ of job608-resume-after-lifetime.md (package wiring, receipt,
   hashes, IPC refusal/cancellation tests, action/privilege/seal reviews,
   automatic queue review, job608-to595.md HQ handoff).
4352MiB guard, 1625784320-byte floor and all application gates unchanged. No
install, seal, unit, sudoers, service, credential transfer or provider call.
