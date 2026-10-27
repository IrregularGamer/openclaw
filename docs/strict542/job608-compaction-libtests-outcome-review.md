# Independent matching compaction libtests outcome review608

VERDICT: APPROVE the COMPLETE matching native libtests stage only. The export is
SPENT and must not be relaunched. This supplies no combined diagnostic launch,
config46/resource-fit, deterministic addon rebuild, package, application, action,
privilege-policy, seal or automatic queue acceptance.

Reviewed exact retained evidence commit
e843a44350219731ba566d8d5fb646b7f2e024cb, source
2f6788455aea5051cdc5b748cd06554f3ab039a1, manifest
283c9f61f73726295f8de01a6cd127e08ea8d150a0a571deb02f101f8b806d0e,
slot tmp-export608-native-compact-libtests1-79b28780. Independently verified the
export manifest matches the committed accepted libtests manifest byte for byte.

## Evidence and settled outcome

Independently rehashed the five retained evidence files; all match the outcome:

- job608-compaction-libtests-receipt.json:
  2f81179f5d1bf14d1519cf446935a3cd783da0e28e79a69067c85e5f873dd946.
- job608-compaction-libtests-build.txt:
  2b1dc9b211c60c70b0cca424f7a2140d9346f9c7e7890b82746ae018cd9c5cb4.
- job608-compaction-libtests-tests.txt:
  6a53fe85ca5f9d3316242aa8040cf395e4b3d4fdc814aa90cc9a7f8a05bba4f8.
- job608-compaction-libtests-retention-negative.txt:
  bb57ceaa264092e04c35cdb07d0fcf3fa41d973a389693087958dd6ffedfef46.
- job608-compaction-libtests-broker.txt:
  189a8b4181d3c6b8ca7be0bca9b3f81f79072140fc0c66dca1af864e91c368fb.

Receipt, build, ecmascript-test and negative-control evidence are byte-identical
to receipt.json, build.log, compaction-tests.log and
lifetime-retention-negative.log in the original pulled artifacts:
/home/deploy/agentq/tmp/export608-native-compact-libtests1/result-native608-libtests.
The broker output is the exact build-log suffix emitted by the runner's tail -3.
Outcome JSON itself hashes to
569d08a78338c0b9bbbd53b14c45ea51d078ea2d986ebc16d7c3c5d270e7e518.

The local offload runs.log independently records
2026-10-27T03:19:55Z run remote rc=0 2267s for this exact export. The outcome
records successful foreground exec75442 exit0/artifact pull observed03:20:01Z.
The pulled artifacts are present; disposable source/.native608 directories are
absent after normal cleanup. There is no transport-uncertain completion claim.

## Source identity and required tests

The receipt has the exact libtests kind/stage, complete:true,
native_lib_tests_exit:0, lifetime_tests_exit:0, compaction_tests_exit:0 and
retention_negative_detected:true. The build's final JSON equals that receipt.
All12 declared shared source/toolchain fields match accepted compile receipt
4a651254152b051476758d1a1a9156d87c535ce8242f30b7213f94862931ed9e,
whose addon pin is
0b6607e73d6f68da2401f79ba06e0a1d8659ca28ab1648aebd98844be60de042.

All four current owning files hash to the receipt and are unchanged from the
independently reviewed frozen source6d9c429b. The six prepared-source hashes
equal the accepted compile's hashes, independently recomputed from pinned
upstream source during the preceding combined source/skeleton review. That
proof is reused; no native compilation was repeated by this reviewer.

Positive logs show7 lifetime tests,2 complete ecmascript libtests and112 complete
rolldown libtests passing, each with zero failed, ignored or filtered tests.
The exact real regression
ecma_ast::compact_arena_tests::compact_clone_reclaims_abandoned_arena_and_preserves_scan_identity
passes. Its retained log is also present verbatim in the full build log.
Recorded release compilation times are9m38s ecmascript and26m20s rolldown.

The retain-through-codegen negative mutation yields exactly4 passing and3
expected failing lifetime checks: early reader union, repeated-module final
use, and unused AST release before first render. These are the original
ownership assertions detecting the old lifetime, not failed positive tests.

## Remaining gates

This accepts the matching completed libtests receipt for later exact source-only
consumption with the accepted compile receipt. A combined export still needs
its independent exact FINAL manifest/receipt-input review and ordinary
admission, default2GiB1CPU, genuine foreground lifetime>=51min and hard
outer2700s+15s. The inner5400s timeout does not extend that outer bound.
The future consumer must rebuild from source and require exact receipt/addon
byte equality, then pass all240 checks, real parity/trace/lazy/minifier fixtures,
AI and all57main/fourworkers. None of that new execution is proved here.

The full typed frozen package and artifact/action/privilege/seal/automatic queue
reviews remain separate, as do the exact baseline, natural settled gap and fresh
HQ/post-restart owner and accepted-run acknowledgement gates. No old receipt,
historical action or unchanged retry substitutes for these requirements.

Declined to judge: future combined launch/outcome/resource fit, deterministic
rebuild equality, full package, application or any protected action. Review used
only read-only source, artifact, hash and log inspection. No tests, build,
offload, network, runtime/protected or queue mutation was performed. This
recording commit adds only this independent outcome review.
