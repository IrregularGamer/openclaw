# Independent inventory scratch correction review608

**VERDICT: APPROVE EXACT SOURCE CORRECTION ONLY.** No material finding.
Reviewer: Rook `/root/review_runtime`, 2026-10-28 UTC, independent of the
implementation lane. Exact reviewed commit:
`41ee9e9fd56494da6b1a4815f4fb31d2718d26e9`. All four changed files match
committed bytes. This is not a completed-build, artifact/action/privilege/seal,
automatic queue or application review.

The executable diff is limited to bounded-build-checkpoint608.mjs. It moves the
existing hashing body into a private helper accepting scratch storage. Each
workspaceInventory608 invocation owns one lazily allocated 1 MiB buffer shared
only by its synchronous file traversal. There is no module-global buffer or
exported caller-controlled scratch parameter. Nested inventories and standalone
shaFile608 calls allocate independent storage. A new hash object is still
created for every file; only bytes actually read enter that hash. Reusing the
storage after each synchronous hash update cannot reuse the previous digest.

The old and new helper retain the same O_RDONLY|O_NOFOLLOW open, regular-file
check, chunk order, before/after size/mtime/ctime checks and finally-close.
Traversal order, exclusions, ancestry, lstat/mode/link identity, hardlinked-output
refusal, full source/output inventory and all checkpoint write/restore/identity/
phase/ancestry validators are unchanged. No digest/stat/path cache, source
membership exclusion, weaker comparison, owner/transport/cancellation/settlement
change, lower admission floor or budget change is introduced. The standalone
entry still freshly opens and hashes its file with its own buffer.

I independently executed all three complete focused files using:

`node --test --test-concurrency=1 --test-reporter=tap docs/strict542/checkpoint-scratch608.test.mjs docs/strict542/build-checkpoint608.test.mjs docs/strict542/declaration-checkpoint608.test.mjs`

All 17 tests pass, zero failed/cancelled/skipped/todo, approximately 1.62 seconds.
This was a tiny direct worker check, not a full or heavy suite. The new tests
meaningfully compare exact content/mode/link results, exercise multi-chunk then
short/empty files, recursively trigger a separate inventory and standalone read
between an outer read and hash update, and require mutation/hardlink refusals
and closed descriptors after an injected read error. These cover both stale
scratch content and accidental sharing between traversals.

As an independent negative control, I copied the exact unchanged parent helper,
its small declaration-helper dependency and new regression into a disposable
/var/tmp fixture. The allocation-bound case correctly fails there: two 32-file
inventories allocate 67,108,864 scratch bytes against a 2,097,152-byte limit.
That expected old-source failure confirms the regression distinguishes the
reported problem; it is not an unresolved assertion in corrected source.
The fixture was removed after the check. `sh -n` on the new focused offload
runner and `git diff --check 41ee9e9f^ 41ee9e9f` also pass. The runner records
Node/source hashes and actual test output, writes success only after all three
files pass, and requires the existing admitted secretless offload path.

The correction note properly limits the profiling claim. Inclusive sampled wall
times overlap, and allocation churn does not prove all historical declaration
CPU/wait cost is solved. The earlier diagnostic timed out deliberately and ran
the child compiler for only 168.4 seconds, not another full 2400-second attempt.
This source review does not independently reaccept that diagnostic outcome or
claim improved end-to-end timing. No changed-source full declaration build ran.

The executable change requires a new reviewed freeze/export and newly valid
native/checks/compiler/runtime/declaration/middle/SDK/tail/package evidence.
5f predecessor receipts remain historical 5f evidence and cannot be relabelled.
Every full affected check, deterministic artifact/native/tree/old-new inventory,
source/action/privilege/seal review and REAL automatic queue review remains.
The ordered genuine foreground nonqueue HQ natural-gap procedure, complete
backup/rollback/reseal gates and fresh genuine post-restart owner binding AND
accepted-run acknowledgements remain mandatory. No root/unit/sudoers/seal/
service/gateway/provider action ran. **595 MUST NOT APPLY from this review.**
