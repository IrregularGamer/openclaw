# Independent exact API-phase prelaunch review608

Reviewer: Rook/Codex independent `phase_prelaunch_review` agent; source author:
separate `phase_launcher` agent. Review time: 2026-10-28T23:45Z.

Verdict: APPROVE ONE FINITE DIAGNOSTIC ONLY for source
`2cf46c119c32b3399e56a86ca1861f22d9be5fea` and preflight `7fe4229f`.
The exact export is the private `stage-api-phase608-next` directory named in
`job608-native-api-phase-preflight.json`. Its manifest SHA256 is
`ab506ff33c625943be405669f1911ed44888bbfe1d97aab42d66c83af34eaa92`.
All six preflight pins independently match actual files: launcher
`60ed1de80517068f420fcad1f530daa859f8940ca291ac6a4f0f462720347d12`,
observer `f50191444745bf8710fe513b66d36a2cfb16b50f9427d5875bb1aba8a68be87d`,
preload `87fb06525b6baa62adf05a8308f5281271659a952422126582c1d14b7c307d83`,
runner `eac266cfaab7efef7c92ed94c53a0a55e75303b8ee4810bc15f21f243a76b8ee`,
helper `a558db9afacd22111fb5c2590fe902298b12ea06910eac6efab43f4aa27c0de4`,
and the manifest above. The three external files equal committed source bytes;
runner/helper equal exact frozen `1bed4d1bb53eff145f724cc6a448dc73b3609015`.

I independently verified source/common identity (`1bed4d1b` / full
`5d7e9d57fb660e2b54f5595e81ddf332027e21b303937c2cd6bc7f718f311263`),
stage `unified-0`, state UNUSED, and all seven actual native/runtime input
hashes against the manifest and preflight. Both producing stage receipts are
byte-identical to committed accepted `job608-native-1bed/stage-receipt.json`
and `job608-runtime-1bed/stage-receipt.json`. I independently executed
`python3 -I -B stage608.py verify-inputs` in the export: exit 0. No previous
diagnostic/result directory existed. I did not rehash the large base source
archives: the unchanged pinned runner verifies their complete streaming
digests before extraction or execution.

I independently reran the focused launcher suite on exact `2cf46c11`:
11 passed, 0 failed/skipped in 2.480 seconds. Coverage includes refusal,
unchanged runner/build boundaries, frozen install plus both preflights,
actual failure/timeout status retention, cancellation, and an actual
TERM-ignoring grandchild. The initial draft only waited for the timeout
leader; that finding was corrected before commit. The reviewed collector now
checks live process-group members, kills survivors, and finitely checks
settlement. Zombies are excluded because they cannot execute. Cgroups and
offload containment remain unchanged. Progress forwarding accepts only fixed
observer fields and the smoke marker.

The exact preflight command is approved only through admitted offload with
`--timeout 1740 --mem 4g --cpus 1 --artifacts native-api608`, invoking
`python3 -B diagnose-native-api608.py` once, after the normal deadline check.
Internal setup/probe is bounded to 1500 seconds, installed preload smoke to
30, compiler observation to 900, with existing kill grace. The reviewed
external observer source is `da316fb6`; actual installed smoke remains
required and unproven until this diagnostic runs. The unchanged owned entry
retains source membership, diagnostics, owner predicates and all original
checks. The runner suppresses archive-build and stage receipt publication.
Actual inner status is retained separately: 124 permits diagnostic artifact
collection only; other failures and cancellation remain failures.

This approves no compiler success, checkpoint, deterministic package,
installation, action/privilege/seal review, queue review, owner binding,
restart acknowledgement, or release. No root, unit, sudoers, installed,
sealed, runtime auth/config or provider action was performed. Interpret the
actual smoke and phase output independently before any correction or split;
an unchanged retry is not approved. All original application gates remain.
**595 MUST NOT APPLY.**
