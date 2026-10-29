# Independent runtime fullsize5aff1 acceptance

Reviewer: Rook /root/runtime_acceptance, separate from preparation/execution.
Reviewed committed evidence7f3d613bda917a948a302fb49cae8fae0fbe2003 against
the actual settled private result, after execution ended.
**VERDICT: ACCEPT exact SOURCE-ONLY runtime checkpoint.595 MUST NOT APPLY.**

Independently verified:

- Actual sibling runtime-fullsize5aff1-offload.rc and returned exit-code.txt
  both contain0. The local offload run record reports this exact export remote
  rc0 at2026-10-29T11:54:00Z,1039s. The complete client log ends runtime-pass;
  build-start +16s/budget2264s and build-done +723s agree with the reviewed
  inner deadline. Recorded launch matches the exact preflight command:
  `offload run --timeout 2460 --mem 14g --cpus 4 --artifacts result608-runtime -- timeout -k 15s 2400s sh run608.sh`.
- Actual manifest remains
  46f4f743157f10fa3b64b4256b179c5256b79f51632e17afb8c519b4311995ac.
  Receipt d41a3c6f9b404376f24b97e98f1be30d5ebf7d7ab46174d10156b9432cd5cefb
  has kind JOB608_STAGE_RECEIPT,stage runtime,exit0,
  run_id stage608-runtime-fullsize5aff1,
  source5aff81feb4098654ce07e7ff09e336119770be85 and common export
  230f79f5b6f95826a02a15f1c5fdd9d1fbc5a7abd60064b33e3d1776af0f086d.
  These equal actual manifest and independently approved preflight fields.
  Actual runner e2ed7e13 and helper a558db9a retain exact full preflight hashes.
- All four actual staged inputs match manifest/receipt/preflight pins and
  accepted NEW native73351f27: producing receipt435ef3f2,compile4a651254,
  libtests2f81179f,addon0b6607e7. No historical a39a producer is consumed.
  Accepted checks9d1dfc33 and native73351f27 were not rerun by this review.
- Both actual output digests match receipt and committed evidence:
  checkpoint2a882adb41e4b9338f4b25aa591c528ab457e3bc94417062b5dbb400fae3f0fb
  (88505171B),build log
  d893e900ae20456b5010b10191ad19d17fc04fa1462f312bdf773dfbbf142baf
  (57171B). Complete five-file returned inventory matches outcome.json,
  including exit-code.txt and strict542-checks/pnpm-path.txt.
- Streamed the entire checkpoint without filesystem extraction or full archive
  buffering. All8959 unique entries own only runtime:runtime/,runtime/data/,
  runtime/receipt.json and exactly8956 outputs (8764regular files,192directories).
  Every output content digest and mode equals the internal receipt inventory;
  no links, special entries, escaping paths, privileged modes, duplicates or
  parent redirects exist. Internal schema/status are
  strict542-build-checkpoint608-v1/CHECKPOINT_NOT_BUILT;stage runtime,
  ancestors[] and deleted[]. Source/common/native identities match exact pins.
- All five canonical phases occur once,in order,and have status ran:
  clean:dist,plugins:assets:build,tsdown-ai,tsdown-packages,tsdown-unified.
  Inspected the full456-line raw build log and every compiler record.
  Exactly58 ordered records cover ai,packages main-config0..14 and unified
  main-config15..56. Every actual status is0,signal/error/fatalUnresolvedImport
  null,timedOut/hasIneffectiveDynamicImport false;capacity usageKnown true and
  unresolved false. No failed or missing compiler record was hidden by the
  successful final receipt. Existing TypeScript API/plugin timing and direct
  eval warnings are visible in the retained full log. Phase total10m19.9s
  agrees with all five completed phases.
- Fresh independent storage608.py result check exits0:
  logical_return_bytes88563372<134217728(runtime128MiB cap).
  Committed manifest/stage receipt/rc are byte-identical to actuals; complete
  committed internal checkpoint receipt is semantically identical to the
  actual archive receipt. Its retained file hash is4b28b173fd55608f4f6728e915b29c565ea2e75296857b18c0e13107f10cb246.
  Both committed gzip logs expand to exact actual raw log hashes; client log
  28daf23df81231ce508527fef3e71066ff543a725297480de98d20e9756cd12c.
  outcome.json agrees with all five file hashes/sizes,identities,phases and
  all58 actual compiler summaries. Working tree was clean at evidence commit.

The exact runtime attempt is SPENT/SUCCESS; never replay its immutable UNUSED
prelaunch manifest. Acceptance permits preparation/review of a NEW unified-0
at the same5aff/common230f with only accepted NEW native+runtime inputs.
It does not approve a future export or launch: require exact separate preflight,
fresh live admission/deadline/storage/input gates and independent acceptance of
the actual unified-0 result before compiler execution.

Separate declaration/unified/compiler/middle/sdk/tail/package,final artifact/
action/privilege/whole-seal/actual automatic-review and genuine ordered HQ595
gates remain open. No offload/test/build,installed/root/service/provider/
queue-state mutation,commit or push was performed by this independent review.
