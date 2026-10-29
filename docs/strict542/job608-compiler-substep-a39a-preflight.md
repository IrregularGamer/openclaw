# job608 compiler a39a preflight (UNUSED)

SOURCE ONLY; **595 MUST NOT APPLY.** One compiler-test stage, no build/package,
application, installation, seal or privilege authority.

- Freeze `a39ad5ee95609193502850d0dbb87b5dcbb5e3e3`; common source export
  `d28756248bc60436831085e9c03b7738795efc6dd1fc4ad79de2e216c0ef3f62`.
- Export `/srv/encrypted/dev-move-98/agentq-source608-20261028-private/stage-compiler-substep-a39a`.
  Prepared 2026-10-29 using committed preparer SHA256
  `1e701de05d9ccdfccee532cfef8bcc93ba0fc8f9937caf86d689cfc3eda216f2`,
  `--base <private>/base --commit a39ad5ee... --stage compiler --input
  <private>/stage-native-substep-a39a/result608-native --dest <export>` under
  `ulimit -v 524288` and `timeout -k 15s 480s`; actual preparation exit 0.
  Preparation began after the unified-0 upload ended; no concurrent upload or
  second offload. Source exports contain no runtime auth/config/credentials.
- Before preparation storage check exit 0: 1332848309 unique bytes,
  5992353792 free bytes, 2147483648 reserve, 4294967296 aggregate cap,
  16777216 compiler return cap.
- Manifest SHA256 `4efd8ffa753ec52428c9786fc032cfbb5cb2fcb8fdc60fd58f36af3c960fa5a2`;
  controlling stage compiler, execution_state UNUSED, run_id
  stage608-compiler-a39a, required_checks 14. Inherited purpose text still
  describes native; it does not select execution.
- Runner `e2ed7e1337f5d0564b56e61174d0837440655cd38f75416608bff3de82780605`,
  helper `a558db9afacd22111fb5c2590fe902298b12ea06910eac6efab43f4aa27c0de4`:
  exact same frozen committed source as accepted checks/native/runtime and the
  running unified-0. Overlay remains `e44987e3f3563be689dfd2cc80005e6ac91aa71b18aedbe4e0ddf509df1ed474`;
  large archive pins retain the independently approved unified-0 preflight.
- Exactly four staged native inputs, from independent acceptance `4f54ce46`:
  receipt `a301fb35b8da76283393d3b8420028c75d95a50bdde34bf5429392ad0a120f93`,
  compile receipt `4a651254152b051476758d1a1a9156d87c535ce8242f30b7213f94862931ed9e`,
  libtests receipt `2f81179f5d1bf14d1519cf446935a3cd783da0e28e79a69067c85e5f873dd946`,
  addon `0b6607e73d6f68da2401f79ba06e0a1d8659ca28ab1648aebd98844be60de042`.
  `python3 -I -B stage608.py verify-inputs` exits 0.

The runner retains all five compiler test invocations, stock/native equality,
lazy-barrel modes and worker/minifier refusal checks. The prior owned compiler
stage used this shorter outer600/inner540 command (launch `63796ee2`, result
`63bef460`, independent acceptance is recorded in
`job608-compiler-owned-outcome-continuation-review.md`).
That run's five groups each passed two tests; those results do not accept a39a.
This shorter deadline removes no test or resource/refusal gate. No source,
wrapper, floor, cancellation, settlement, privilege or ownership change.

Launch only after independent exact preflight approval, successful accepted
unified-0 evidence, settlement of its offload, live health up, current storage
check, and no other offload. A live worker deadline >=975s is required:
600s outer +195s mandatory settlement +180s observed transfer allowance.
If insufficient, leave this export UNUSED and launch FIRST in a fresh worker.

```sh
set -eu
cd /srv/encrypted/dev-move-98/agentq-source608-20261028-private/stage-compiler-substep-a39a
sha256sum export-manifest.json run608.sh stage608.py
python3 -I -B stage608.py verify-inputs
offload health
offload deadline
test ! -e result608-compiler
test ! -e ../compiler-substep-a39a-offload.log
test ! -e ../compiler-substep-a39a-offload.rc
set +e
offload run --timeout 600 --mem 4g --cpus 1 --artifacts result608-compiler -- timeout -k 15s 540s sh run608.sh > ../compiler-substep-a39a-offload.log 2>&1
status608=$?
printf '%s\n' "$status608" > ../compiler-substep-a39a-offload.rc
exit "$status608"
```

After success require actual client/result 0, storage608.py result --stage
compiler --result <export>/result608-compiler, exact manifest/source/common/
inputs/receipt/output digests, complete returned inventory, all five actual
Node summaries and zero failed/cancelled/skipped/todo, committed evidence and
independent acceptance. No assumed total substitutes for actual membership.
Then unified-1 through unified-5, middle, sdk-0/1, tail, package at SAME freeze;
remaining final artifact/action/privilege/seal/automatic-review and genuine HQ
handoff gates in job608-after-substep-budget-continuation.md remain mandatory.
On timeout/failure mark SPENT, preserve actual client log/rc, diagnose before
any changed attempt; never replay. Exit76 before admission preserves UNUSED;
75/95 retain ordinary refusal/reconciliation rules, no bypass or local fallback.
