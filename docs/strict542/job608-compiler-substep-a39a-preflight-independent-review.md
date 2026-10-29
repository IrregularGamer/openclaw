# job608 compiler a39a preflight: independent review

SOURCE ONLY; **595 MUST NOT APPLY.** Independent exact review of
`3d36a23469ba4546584f748d89b684f07f00da96` against
`713ec98171c57df03d6681c0fbb350de85561ae6`: exactly one added document,
`job608-compiler-substep-a39a-preflight.md`, with no executable change.
Reviewer: Rook `/root/review_compiler_preflight`, 2026-10-29 UTC.

Verified the actual UNUSED private export
`/srv/encrypted/dev-move-98/agentq-source608-20261028-private/stage-compiler-substep-a39a`:

- Manifest SHA256
  `4efd8ffa753ec52428c9786fc032cfbb5cb2fcb8fdc60fd58f36af3c960fa5a2`;
  stage compiler, UNUSED, run_id stage608-compiler-a39a, launch_history none,
  required_checks 14. Source and runner freeze both
  `a39ad5ee95609193502850d0dbb87b5dcbb5e3e3`. Canonical JSON recomputes common
  identity `d28756248bc60436831085e9c03b7738795efc6dd1fc4ad79de2e216c0ef3f62`.
- Runner `e2ed7e1337f5d0564b56e61174d0837440655cd38f75416608bff3de82780605`
  and helper `a558db9afacd22111fb5c2590fe902298b12ea06910eac6efab43f4aa27c0de4`
  match their manifest pins, exact frozen committed bytes and unified-0 export.
  Committed preparer SHA256 is the stated `1e701de0…216f2`.
- Streamed successor overlay SHA256 is
  `e44987e3f3563be689dfd2cc80005e6ac91aa71b18aedbe4e0ddf509df1ed474`.
  The three large archives have the same pins and device/inodes 64512/395540,
  64512/395541, 64512/395542 as the unified-0 export independently approved
  in `713ec981`. Those large archive bytes were not rehashed here.
- Exactly four native inputs exist: stage-receipt `a301fb35…a120f93`,
  compile receipt `4a651254…31ed9e`, libtests receipt `2f81179f…dd946`,
  addon `0b6607e7…0de042`. All full digests equal the preflight and manifest.
  All four share the accepted native producer's inodes and bytes; the three
  JSON receipts also match committed accepted copies. Native acceptance
  `4f54ce46` applies to this same source/common identity. Both additional
  native608-stages receipt files match their independent pins.
- Fresh `python3 -I -B stage608.py verify-inputs`, run in this export, exits 0.
  No result608-compiler, sibling compiler-substep-a39a offload log/rc,
  __pycache__, symlink or loose sensitive file exists. The full loose inventory
  contains only the four archives, runner/helper/manifest, two pinned native
  receipts and four staged native inputs, plus their directories.
- Fresh storage check exits 0: unique 1347378519 B, free 5977788416 B,
  free reserve 2147483648 B, aggregate cap 4294967296 B, compiler return cap
  16777216 B. Earlier preflight figures are preparation observations; current
  storage must be checked again immediately before launch.

The entire compiler case is byte-identical to the prior source used by launch
`63796ee2` and accepted outcome `63bef460`: five actual Node invocations retain
worker/minifier refusal, stock/native equality, phase tracing and both lazy-barrel
modes. The historical ten passing checks support the unchanged shorter
outer600/inner540 choice only; they do not accept this a39a result. Manifest
required_checks 14 describes the installed checks inventory, not an assumed
compiler result count. Actual compiler membership and all five summaries must
be checked after this attempt.

The proposed command retains 4 GiB, 1 CPU, outer600 s, inner540 s with 15 s
kill grace, ordinary refusal/cancellation/settlement gates, and no fallback.
Launch requires successful independently accepted unified-0 evidence AND
settlement of that attempt, live health up, current storage room, no other
offload and a live worker deadline of at least975 s (600 +195 settlement +180
transfer allowance). Otherwise leave this export UNUSED and launch FIRST in a
fresh worker after the same prerequisite checks. This review does not claim
those future live launch conditions are already satisfied. The active unified-0
attempt was left untouched.

`sh -n` accepts the documented launch block; exact-commit `git diff --check`
passes. No compiler test, suite, build, offload launch, export mutation, service,
root, config, unit, seal or provider operation ran. The independent bounded
input verifier and storage check above were the only helper operations.

No material finding. Approval covers one bounded compiler attempt of this exact
UNUSED export, subject to the stated launch conditions. It does not accept any
future result or package, grant application/install/reseal authority, or review
any separately generated source inventory. Actual client/result0, complete
return inventory, receipt/output/source/input digests, storage return check,
five passing Node summaries, committed evidence and independent acceptance
remain required. Unified-1–5, middle, SDK, tail, package and all final artifact,
action, privilege, seal, automatic review and genuine HQ handoff gates remain
outstanding. Failure spends the attempt; preserve actual log/rc and diagnose
before a changed attempt. Exit76 before admission preserves UNUSED; ordinary
75/95 reconciliation rules remain intact.

**VERDICT: APPROVE** (exact compiler preflight scope only).
