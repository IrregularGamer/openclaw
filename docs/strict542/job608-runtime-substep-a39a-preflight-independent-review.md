# job608 runtime a39a preflight: independent review

SOURCE ONLY; **595 MUST NOT APPLY**. Reviewed exact preflight commit
`b6f7801c7b416df453258270566874770f761183` and UNUSED export
`/srv/encrypted/dev-move-98/agentq-source608-20261028-private/stage-runtime-substep-a39a`.
Compared with approved a46c runtime preflight and native a39a acceptance
`4f54ce46`. No runner, offload, install, service, sudo or root-policy action.

Verified independently:

- Manifest sha256 `df2f0a367ab77a16a597baa0c9756d9853c7090642ac1f20c3c276fe46395243`;
  stage runtime, UNUSED, run_id stage608-runtime-a39a, required_checks 14;
  source/runner commit `a39ad5ee95609193502850d0dbb87b5dcbb5e3e3`.
  Common source-export identity
  `d28756248bc60436831085e9c03b7738795efc6dd1fc4ad79de2e216c0ef3f62`
  recomputes from canonical identity JSON and matches the accepted native export.
- Runner `e2ed7e1337f5d0564b56e61174d0837440655cd38f75416608bff3de82780605`
  and helper `a558db9afacd22111fb5c2590fe902298b12ea06910eac6efab43f4aa27c0de4`
  match both manifest pins and `git show a39ad5ee` committed source.
  Committed, unmodified preparer sha256 is
  `1e701de05d9ccdfccee532cfef8bcc93ba0fc8f9937caf86d689cfc3eda216f2`.
- Streaming on-disk archive hashes match manifest pins and accepted native
  a39a identities: source598 `e79a0e45…743de3`, successor598
  `e44987e3…1ed474`, native598 `d73e4e35…701de`, compiler upstream
  `203aa483…58ac`. No full-file buffering was used.
- Exactly four native inputs: stage receipt `a301fb35…a120f93`, compile receipt
  `4a651254…31ed9e`, libtests receipt `2f81179f…dd946`, addon
  `0b6607e73d6f68da2401f79ba06e0a1d8659ca28ab1648aebd98844be60de042`.
  All hashes match pins; link count 2 and inodes 395804–395807 match accepted
  native a39a result files. All three JSON receipts match committed copies.
  `python3 -I -B stage608.py verify-inputs` exits 0.
- Runtime result directory, `runtime-substep-a39a-offload.*`, symlinks and
  `__pycache__` are absent. Manifest launch_history remains none.
- Loose export files contain no .env/.db/key/pem files. Archive inventory
  qualification: the retained source base includes three tracked `.env.example`
  files and six tracked state-corpus SQLite/key fixtures. The base commit's
  `test/fixtures/state-corpus/README.md` explicitly documents isolated synthetic
  state, fake credentials and generated fingerprint keys; no operator state.
  All nine files are byte-identical to the pinned base commit. The successor
  and native archives have no flagged secret paths. Rolldown upstream has no
  flagged secret paths; its 1246 node_modules-named paths are source test
  fixtures under crates/rolldown/tests or packages/rollup-tests/test. These
  inherited fixtures do not constitute live credentials or installed caches.
- Fresh `storage608.py check --stage runtime` exits 0: unique 1229744366 B,
  free 6094123008 B, reserve 2147483648 B, store cap 4294967296 B,
  runtime return cap 134217728 B. The preflight's usage/free figures describe
  its earlier pre-preparation measurement.
- Launch is the approved finite pattern: outer offload 2460 s, 4 GiB / 1 CPU,
  inner `timeout -k 15s 2400s`; 2415 < 2460 and 2460 + 195 = 2655 s.
  The frozen runner additionally bounds the build to 2280 s from stage start,
  with 15 s kill grace and progress/log-tail evidence. No budget or safety
  owner changed. Require a fresh worker and live `offload deadline` >= 2655 s
  immediately before launch; this review does not attest that future deadline.

Non-blocking inherited wording: manifest purpose says stage native, while the
controlling stage field correctly selects runtime; same template wording was
accepted in the a46c review.

Approval covers one bounded runtime attempt of this exact UNUSED export only.
On timeout/failure, do not rerun unchanged. Before accepting a result, run the
runtime storage-return check and apply the existing a46c acceptance rules.
No application, install, package or reseal authority is granted.

**VERDICT: APPROVE**
