# Measured checkpoint hashing correction608

Actual diagnostic a71d150f used frozen5f source and original accepted native/
runtime inputs. Client exited0 around deliberate build timeout124; no build
checkpoint was accepted. Six V8 profiles/68proc samples are preserved with exact
raw hashes in job608-unified-diagnostic-outcome.json. The child declaration
compiler ran168.4seconds before the whole diagnostic600second bound. This was
not another full2400second reproduction, and does not fully explain the earlier
32minutes of heartbeat or prove that the declaration compiler now fits.

The first outer profile spans295.487seconds. workspaceInventory608 accounts
for191.162sampled wall seconds inclusively, shaFile608 for170.721; GC has
60.931self seconds and createUnsafeBuffer26.361self seconds. Inclusive values
overlap and must not be summed or presented as exclusive CPU accounting.
Each inventory file previously allocated a new1MiB scratch Buffer. The real
runtime checkpoint alone has8764regular files; repeated inventories therefore
churn many GiB of allocation while retaining only one chunk at a time.

The owning helper now lazily allocates ONE private scratch per synchronous
inventory traversal. A private hash helper receives it. Standalone shaFile608
keeps an independent buffer; nested inventories cannot overwrite each other.
Every file is still opened with O_NOFOLLOW, freshly hashed in the same chunk
order with a new hash state, fstat-checked before/after, and closed in finally.
Source/output/link/mode/inode/mutation checks and all native owner, transport,
cancellation/settlement, admission floors and resource budgets are unchanged.
No digest cache, path-decision cache or source membership exclusion was added.

RED: two32file inventories allocated67108864scratch bytes, exceeding2MiB.
GREEN: the complete three focused files pass17tests with the correction.
New tests cover allocation bounds, multichunk/short/empty digest equivalence,
mode/link identity, nested independent and standalone reads, mutation and
hardlinked-output refusal, and descriptor cleanup after read failure.
run-checkpoint-scratch608.sh runs those same three complete files through an
admitted secretless offload, recording actual Node/source hashes/results.
No dependency installation or native rebuild is needed for these helper tests.

Inner317 profiles also show native/API filesystem CPU cost, including repeated
boundary assertions. These are distinct fresh predicates; removing or caching
them without refusal-equivalence proof is unjustified. No such change is made.
Full declaration completion remains to be established under the original bound.

This executable correction changes the build source. The5f predecessor receipts
remain valid historical5f evidence, and MUST NOT be relabelled for a new freeze.
After exact independent source/outcome review, choose one new freeze and rebuild
required native/checks/compiler/runtime/unified/middle/SDK/tail/package stages
from new committed secretless exports. Keep every full affected check. Final
artifact/old-new inventory/action/privilege/seal and REAL automatic queue reviews
and the ordered genuine nonqueue HQ handoff remain.595 MUST NOT APPLY.
No installed/sealed/root/unit/sudoers/service/gateway/provider change occurred.

The new4regressions are wired into the canonical full checks-stage runner, so
the new complete scoped inventory is482(previous478+4), subject to actual run
reconciliation. A first focused remote export omitted build-artifact-cache.mts
and the writer read by existing fixture tests;15passed/2ENOENT fixture failures.
That export is SPENT/FAILED and grants no acceptance. The corrected NEW export
includes both exact committed fixtures; assertions and scope stay unchanged.
