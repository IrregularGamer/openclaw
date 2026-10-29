# job608 finite API observer a39a rebind: independent source review

SOURCE ONLY; **595 MUST NOT APPLY.** Reviewed exact commit
`4f6cf9c9fab2535532055cdd368d467f8b454391` against
`11c1673e1067bca8c65b56c755241a11b834bd34`: five changed/added paths.
Reviewer: Rook `/root/review_compiler_preflight`, 2026-10-29 UTC.

The diagnostic helper's complete diff is exactly three identity-pin changes
(FREEZE, COMMON, RUNNER) and corresponding module-description/refusal text.
All remaining helper bytes and behavior are unchanged. Helper SHA256 is
`3d64c73fd9d938f2fd8769713c78fec993e037b61afe65263d830642dca84f6c`;
working helper equals the exact committed file.

New profile selects source
`a39ad5ee95609193502850d0dbb87b5dcbb5e3e3`, common export
`d28756248bc60436831085e9c03b7738795efc6dd1fc4ad79de2e216c0ef3f62`
and runner
`e2ed7e1337f5d0564b56e61174d0837440655cd38f75416608bff3de82780605`.
These agree with the exact a39a frozen source and attempted/accepted-stage
profile. Independently hashed frozen source confirms unchanged supporting pins:

- run-build-stage608.sh: `e6c1270bf3e41e53e80f904fcf054df0636966e4b5f75c46ffaf890243ca326c`
- stage608.py: `a558db9afacd22111fb5c2590fe902298b12ea06910eac6efab43f4aa27c0de4`
- native-api-phases608.mjs: `f50191444745bf8710fe513b66d36a2cfb16b50f9427d5875bb1aba8a68be87d`
- install-native-api-phases608.mjs: `87fb06525b6baa62adf05a8308f5281271659a952422126582c1d14b7c307d83`

The added test exercises the REAL validate() function with explicit current,
historical and wrong-common manifests. File digests are deliberately mocked;
this tests the profile-selection boundary, not actual export integrity. Current
profile is accepted; historical and mixed common identities are refused. The
recorded RED shows the new current-profile case failing against the old1bed
helper (12 tests, one error). Recorded GREEN shows12 tests passing; the separate
unchanged-observer record shows10 passes with zero failed/cancelled/skipped/todo.
I inspected test source and recorded results; I did not rerun those tests.
Fresh in-memory Python syntax compilation of helper and test succeeds.

Unchanged diagnostic-only behavior remains appropriate: exact frozen runner,
build/helper and observer pins; complete native/runtime input restoration and
verification; frozen install and both preflights before preload;30 s smoke,
900 s compiler observation,1500 s setup/probe limit; no caller-selected command;
whole-process-group cancellation/settlement; actual inner result distinct from
collection status; source/stage checkpoint receipt publication suppressed.
The external observer preserves native method receiver/arguments/result/error
and records only the fixed metadata fields. An observed timeout may be collected
as diagnostic evidence and must never become successful build evidence.

No product/frozen source, root/config/unit/service/budget or acceptance boundary
changed. This review covers the helper source rebind only. It is not approval
of a particular future export, diagnostic result, product source, package,
application action, installed target or seal, and not automatic queue review.

A NEW UNUSED diagnostic export still needs exact independent preflight against
these pins and current accepted native/runtime inputs. Do not launch from the
spent build export or historical diagnostic export. Future launch requires live
health/storage, no other offload, settlement and sufficient worker life for
outer1740 s plus195 s reserve (and any separately required transfer allowance).
That launch does not fit the current worker and must occur FIRST in a fresh
worker after its gates. No export or offload was prepared/launched in this
review. Any native diagnostic outcome remains unaccepted until separately
inspected and committed.

**VERDICT: APPROVE DIAGNOSTIC HELPER SOURCE REBIND ONLY.** No material finding;
exact export preflight and all later evidence/installation gates remain open.
