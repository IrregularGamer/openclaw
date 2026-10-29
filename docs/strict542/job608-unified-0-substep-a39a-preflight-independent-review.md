# job608 unified-0 a39a preflight: independent review

SOURCE ONLY; **595 MUST NOT APPLY**. Reviewed all three documentation files in
`d04bdd9f7bd12860cb211507d48a8e724d8e10eb`, the unchanged exact preflight and
UNUSED private `stage-unified-0-substep-a39a` export, and the separately recorded
historical-heading clarification `36db1d4d3673016b1ed611dc4c0e95764efadb53`.
No executable change, offload, build, test suite, service or root action.

Verified independently:

- Manifest SHA256
  `900edc324f8e2068521a9d4fc19b0c80d0fbca91cfa01ba5c618d2528fb0b4fd`;
  stage unified-0, UNUSED, run_id stage608-unified-0-a39a, required_checks 14,
  launch_history none. Source/runner freeze remains
  `a39ad5ee95609193502850d0dbb87b5dcbb5e3e3`; common source-export identity
  `d28756248bc60436831085e9c03b7738795efc6dd1fc4ad79de2e216c0ef3f62`
  recomputes from canonical JSON and equals the accepted native/runtime identity.
- Runner `e2ed7e1337f5d0564b56e61174d0837440655cd38f75416608bff3de82780605`
  and helper `a558db9afacd22111fb5c2590fe902298b12ea06910eac6efab43f4aa27c0de4`
  match manifest pins, accepted runtime export and frozen committed source.
  The unmodified committed preparer remains `1e701de0…216f2`.
- Archive pins equal the accepted runtime export: source598 `e79a0e45…743de3`,
  native598 `d73e4e35…701de`, compiler upstream `203aa483…58ac`. These three
  are the same device/inodes 395540–395542 as the independently reviewed
  runtime archives; their large bytes were not needlessly rehashed. The newly
  generated successor overlay was streamed and matches
  `e44987e3f3563be689dfd2cc80005e6ac91aa71b18aedbe4e0ddf509df1ed474`.
  Native compile/libtests receipt pins also match. The unchanged common-base
  source-example/synthetic-fixture qualification in `b2c98f20` still applies.
- Exactly seven staged inputs match the preflight table and accepted producer
  receipts (`4f54ce46` native; `9f5d4331` runtime): native receipt
  `a301fb35…a120f93`, compile `4a651254…31ed9e`, libtests `2f81179f…dd946`,
  addon `0b6607e7…0de042`; runtime receipt `eb4488f2…a92e81b`, build.log
  `13ed360c…e8d969`, checkpoint `85f3d1e3…95991`.
  Native files share producer inodes 395804–395807 (3 links); runtime files
  share 395831–395833 (2 links). Both producing stage receipts are byte-identical
  to committed accepted copies. Fresh `python3 -I -B stage608.py verify-inputs`
  exits 0, verifying every input digest and producing source/export/output map.
- No result608-unified-0, sibling unified-0-substep-a39a offload log/rc,
  __pycache__, symlink or loose .env/.db/key/pem file exists.
- Fresh storage check exits 0: unique 1332846071 B, free 5992357888 B,
  reserve 2147483648 B, aggregate cap 4294967296 B, return cap 33554432 B.
  Preflight figures describe its earlier pre-preparation measurement.
- Launch retains outer 2460 s / 4 GiB / 1 CPU, inner 2400 s + 15 s kill
  grace, fixed build deadline at stage +2280 s + 15 s kill grace, and 195 s
  settlement allowance: 2460 + 195 = 2655 s. The frozen runner retains
  progress markers and failure log tails. No budget, floor or owner changes.
  Launch is authorized only as the first heavy step of the NEXT fresh worker,
  after a live deadline check >=2655 s; never in the current worker.
- The current continuation/HQ status correctly distinguishes accepted
  checks/native/runtime from unified-0 and all remaining compiler, unified-1–5,
  middle, sdk-0/1, tail and package stages. The historical next-step heading
  is now explicitly superseded. Candidate95 command pins and the 669-path
  inventory remain historical blocked templates, requiring reconciliation to
  the eventual complete successful package/freeze and exact final reviews.
  Artifact/action/privilege/seal, actual automatic queue review, ordered genuine
  nonqueue HQ/natural-gap, fresh post-restart dual acknowledgement, backup,
  rollback and reseal gates remain outstanding and intact.

Inherited purpose text says stage native; the controlling field correctly selects
unified-0. This known template wording is non-blocking.

Approval covers one bounded unified-0 attempt of this exact UNUSED export only.
It does not accept a future result or grant package/application/install/reseal
permissions. On timeout/failure, preserve the exact log/rc and never rerun
unchanged. Success requires storage-return validation, complete checkpoint-owner
and receipt/output checks, committed evidence and independent acceptance.

**VERDICT: APPROVE**
