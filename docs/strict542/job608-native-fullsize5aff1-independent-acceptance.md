# Independent native fullsize5aff1 acceptance

Reviewer: Rook /root/native_runtime_review, separate from preparation/execution.
**VERDICT: ACCEPT exact native stage EVIDENCE ONLY. 595 MUST NOT APPLY.**

Independently inspected the actual private export
`stage-native-fullsize5aff1`, returned `result608-native`, and sibling client
log/rc after terminal settlement. Actual client rc and result exit-code are
both0. Client log ends `STEP608 native-rebuild-pass`; its2121bytes hash to
5709e6e065057ea86940777cbd244047d407b96458ac81bd56597903e9f72424.

Manifest301a3b3c62bfedf3b40896cb7fb01f595acb9ba5d29449ad338bfb2c07ad72c6
remains the exact independently approved preflight. Runner e2ed7e1337f5d0564b56e61174d0837440655cd38f75416608bff3de82780605
and helper a558db9afacd22111fb5c2590fe902298b12ea06910eac6efab43f4aa27c0de4
match both manifest pins and committed frozen source. Common identity recomputes
from canonical identity JSON. Large archives retain the exact independent
preflight's pins; they were not redundantly rehashed for this terminal review.

Stage receipt435ef3f26d1045eaca54ea9e8057737a812a5e279681e2c3bdd278f30fb62515
has kind JOB608_STAGE_RECEIPT, stage native, exit_code0,
run_id stage608-native-fullsize5aff1, source
5aff81feb4098654ce07e7ff09e336119770be85, common export
230f79f5b6f95826a02a15f1c5fdd9d1fbc5a7abd60064b33e3d1776af0f086d,
the exact manifest hash and {}stage_inputs. Its exact three-entry output map
matches streamed actual file hashes:

- compile receipt4a651254152b051476758d1a1a9156d87c535ce8242f30b7213f94862931ed9e;
- libtests receipt2f81179f5d1bf14d1519cf446935a3cd783da0e28e79a69067c85e5f873dd946;
- addon0b6607e73d6f68da2401f79ba06e0a1d8659ca28ab1648aebd98844be60de042,
  24303312bytes.

Both JSON receipts match the independently pinned native608-stages inputs.
Their complete/lifetime/compaction/retention fields pass; the pinned libtests
receipt records native_lib_tests_exit0. The rebuilt compile receipt/addon also
match the duplicate returned result598-native files byte-for-byte. The consumer
rebuilds compile and its lifetime/compaction checks, then carries forward the
accepted libtests receipt; this is not a claim that the complete libtests stage
ran again in this consumer.

The returned native-rebuild log26495bytes hashes to
4e76ec0345c21ccee49c8de187c929ace4becf285aa0502fe43cd635b5f5802b.
It records7positive lifetime cases,7passed/0failed. The real native test log
records ecma_compiler::basic_test and
ecma_ast::compact_arena_tests::compact_clone_reclaims_abandoned_arena_and_preserves_scan_identity,
2passed/0failed. Cargo reports9m48s for that test build and20m31s for the addon.
The deliberate retention-negative log records its expected3failures/4passes;
the completed compile receipt confirms retention_negative_detected=true.
Its expected FAILED text is negative-control evidence, not a failed stage.

Fresh independent `python3 -I -B stage608.py verify-inputs` returns0.
Exact10-file returned inventory has no symlinks. Fresh independent
`storage608.py result --stage native` returns0:48652056logical bytes,
below67108864bytes. No tests, build, offload, installed mutation, service,
root/unit/sudo, live provider or queue-state action was performed by this review.

Evidence commite5481f2d also checked against private originals: all three JSON
receipt copies are byte-identical; all four gzip logs decompress to exact raw
hashes; outcome.json lists the exact10files with matching hashes/sizes and sum,
client/result0, source/common/run/manifest identity and launch command. README's
two real native cases are basic+compaction as named above.

The export is SPENT/SUCCESS; never replay its immutable prelaunch UNUSED label.
A NEW runtime-fullsize5aff1 export may consume only this producing-stage receipt
and these exact native outputs at the SAME5aff/common230f identity. The unchanged
preparer1e701de05d9ccdfccee532cfef8bcc93ba0fc8f9937caf86d689cfc3eda216f2
and helper enforce its exact four native inputs. Runtime needs a separate exact
preflight review, storage/input/admission checks, and FIRST launch in a fresh
worker: offload2460s/14g/4CPU, inner2400s with15s kill grace, at least2655s
remaining after preflight (prefer2895s including observed transfer). Its frozen
build budget remains2280s from stage start. No changed timeout or source freeze
is required for evidence-only commits.

Remaining NEW graph: runtime, unified-0, compiler, unified-1..5, middle, sdk-0/1,
tail, package, with exact STAGES/OUTPUTS and independently accepted predecessors.
Full package/tree/build, final source/artifact/action/privilege/whole-original-and-next-seal
reviews, actual automatic queue approval and ordered genuine foreground HQ595
handoff remain incomplete. Preserve original seal51170230 and reconcile any
drift; historical candidate95 command pins need explicit reconciliation to the
eventual5aff package/action. Natural settlement/gap, fresh post-restart owner AND
accepted-run acknowledgements, backups/rollback/poison/reseal gates remain.
No package, application, installation or production authority is inferred.
