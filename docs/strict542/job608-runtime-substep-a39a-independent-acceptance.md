# job608 runtime a39a: independent acceptance

SOURCE ONLY; **595 MUST NOT APPLY**. Reviewed evidence commit
`8a4b1f56a62e6b2eec21e845728469046625b2f7` against the actual private
`stage-runtime-substep-a39a/result608-runtime` and sibling client log/rc.
This accepts runtime stage evidence only; no package, application, install,
reseal or production authority. No tests, offload, services or root actions.

Verified independently:

- Client `runtime-substep-a39a-offload.rc` and returned `exit-code.txt` both 0.
- Export manifest remains exactly the approved preflight's
  `df2f0a367ab77a16a597baa0c9756d9853c7090642ac1f20c3c276fe46395243`.
  Runner `e2ed7e13…780605` and helper `a558db9a…7c0de4` match manifest pins
  and frozen committed source at `a39ad5ee95609193502850d0dbb87b5dcbb5e3e3`.
  Unchanged large source archives were not rehashed; independent preflight
  approval `b2c98f20` covers those exact export identities.
- Receipt SHA256
  `eb4488f2e5ef31baca3580ae5542d56302d2b15c53a622b4b26abd4e9a92e81b`:
  kind JOB608_STAGE_RECEIPT, stage runtime, exit_code 0,
  run_id stage608-runtime-a39a, source a39ad5ee, common source export
  `d28756248bc60436831085e9c03b7738795efc6dd1fc4ad79de2e216c0ef3f62`.
  Its manifest and exact four-entry stage_inputs map equal the approved
  manifest. All native input hashes match, including accepted native receipt
  `a301fb35b8da76283393d3b8420028c75d95a50bdde34bf5429392ad0a120f93`.
  Fresh `python3 -I -B stage608.py verify-inputs` exits 0. The committed
  runtime receipt is byte-identical to the private receipt.
- Streaming output SHA256 matches both receipt pins:
  checkpoint.tar.gz, 88503525 bytes,
  `85f3d1e3b92da6803c810a099c14d10286feac8475fef133cce4350054d95991`;
  build.log, 64366 bytes,
  `13ed360ce36c3ff73fb3f5b83dd5ea335267909742e159e52c8078705ce8d969`.
  The streamed checkpoint inventory contains 8959 entries, all under the
  runtime owner. No full checkpoint buffering or extraction was used.
- Both committed gzip copies decompress to the private logs' exact hashes:
  build.log as above; runtime-offload.log, 2283 bytes,
  `f8aca75901c47a5f748fb1b0dab7f3dd38c02add10c0b418de07ce240ddcb7eb`.
- Ordered client markers: native-start +9s, restore-build-done +10s,
  build-start +17s with 2263s budget, build-done +1191s, runtime-pass.
  The elapsed build interval is 1174s, within its inner budget and the
  approved 2400s / 2460s launch bounds. No FAIL/not-ok/stage-fail markers.
  All 58 BOUNDED_PACKAGE_COMPILER records report status 0, no signal, timeout
  or error. Existing web-tree-sitter eval warnings are present without failure.
- Build phase timings match the result note: total 15m 16s; packages 7m 57.4s,
  unified 6m 1.6s, ai 1m 2s. These are runtime emissions; separate declaration
  stages remain outstanding.
- Fresh `storage608.py result --stage runtime --result <private result>`
  exits 0: 88568912 logical return bytes < 134217728-byte cap.

The export is spent successfully; never replay it despite its immutable
pre-launch manifest's UNUSED field. This acceptance permits using the pinned
runtime result as input to a new independently reviewed unified-0 export at the
same a39a freeze. Remaining compiler/declaration/package, artifact, action,
privilege, seal, automatic-review and genuine HQ gates remain open. It makes
no two-build reproducibility claim.

**VERDICT: ACCEPT**
