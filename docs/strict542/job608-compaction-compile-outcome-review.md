# Independent compaction compile outcome — APPROVE native compile only

Exact retained evidence commit b804d3ed, source2f6788455aea5051cdc5b748cd06554f3ab039a1,
manifest0e3404864bf45469a9b859555200492475436461a7537e9af099080b22836584,
slot tmp-export608-native-compact1-d32634d0. Foreground session66549 was reported
settled exit0 at02:30:33Z; outcome records broker_exit0. Independently inspected
pulled artifact files in export608-native-compact1/result-native608-compile,
verified all five retained evidence hashes and byte identity of receipt/build/
ecmascript-test/negative logs with their originals. Disposable source/native
working directories are absent after normal runner cleanup.

Complete compile receipt SHA256
4a651254152b051476758d1a1a9156d87c535ce8242f30b7213f94862931ed9e.
Actual24303312-byte addon SHA256
0b6607e73d6f68da2401f79ba06e0a1d8659ca28ab1648aebd98844be60de042,
replacing historical diagnostic addon
17df206117097742019de475e8cd194fb1022f48d9c2b507195100abd13eb627.
Independently hashed the actual addon and receipt. All four owner-input hashes
match exact source2f. Recomputed all six prepared-source hashes from pinned
upstream originals and the committed preparation owner. They match receipt and
outcome; the historical four generation/last-use hashes remain identical, with
only AST compaction and scan-to-link owner files newly present. Historical
owner/addon fields match the retained recovered17df receipt.

Observed9positive tests pass:7 standalone lifetime checks, and both complete
ecmascript lib tests including the exact named
compact_clone_reclaims_abandoned_arena_and_preserves_scan_identity regression.
The latter executes real parsing/semantic construction, unchanged generated
code and IDs, allocator used-byte/capacity reduction, retained-policy comparison,
and validity after dropping the original arena. Retain-through-codegen mutation
produces exactly3expected failures (early reader union, repeated-module final
use, unused pre-render release), with4other checks passing. These expected
negative-control failures do not indicate a failed implementation assertion.
Ecmascript release compilation9m40s and addon release20m21s are recorded.
No local native build or heavy test was performed by this review.

This accepts ONE source-only native compilation and its real regression proof.
It does NOT prove deterministic rebuild equality, full rolldown libtests,
config46 resource fit, all57main/fourworkers, the complete typed frozen package,
or application/action/privilege-policy/seal/automatic-queue gates. Original
baseline drift remains unresolved; no new install/reseal/HQ owner authority is
created. Only the separately conditionally reviewed matching future libtests
stage may follow, in a fresh worker with>=51min, outer2700s+15s and ordinary
2GiB1CPU admission. This worker has insufficient time for that next stage.
No unchanged compile retry or concurrent stage is authorized by this review.
