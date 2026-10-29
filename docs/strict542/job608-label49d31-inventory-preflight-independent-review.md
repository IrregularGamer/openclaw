# Independent label49d31 source inventory and preflight review

Reviewer: Rook `/root/unified_type_review`, independent of preparation.
Reviewed exact HEAD `09689a6f6953567b702b72a5dbc6b266a9385144`, including
inventory/checks preparation `4a1f915239e930175c0e2a02196154ae285d7c5a`,
actual private checks/native exports, and executable source freeze
`49d3fe3348215314582acf7be3872f403f7f6af4`.

**VERDICT: APPROVE exact SOURCE INVENTORY and CHECKS LAUNCH PREFLIGHT,
conditional on fresh live admission/deadline/storage checks at launch.
APPROVE NATIVE PREPARATION ONLY, conditional on independently accepted actual
NEW checks and the next fresh worker. 595 MUST NOT APPLY.**

## Exact full source inventory

Current inventory bytes equal the committed 4a1f9152 and 09689a6f bytes, SHA-256
`8cc2a377f0efcbb321ae7166adf7e90ba27eb413046597d75132c21dda859804`.
I independently recomputed the no-renames diff from original605 source
`877458d730d2455528fb639710ff3f9ba8aae5b2` through 49d3fe33: exactly 858
unique sorted paths, comprising 838 additions and 20 modifications, with no
deletions, missing entries or extra entries. Every old/new presence/absence,
Git mode and SHA-256 matches. I streamed all 841 distinct Git blobs in chunks
of at most 1 MiB: 18144943 total bytes, largest blob 1587906 bytes. All 878
present sides have recorded modes: 877 at 100644 and one at 100755.
application_action, build_package_receipt and next_seal remain null.

Source-only correction approval 386f7231 remains applicable to the exact
49d3fe33 parser/test/runner bytes and narrow actual RED/complete GREEN2
evidence. I independently confirmed that deterministic gzip carriers added
by ae00a7a3 decompress to the exact four raw install/typecheck log blobs in
386f7231. This preserves the prior recorded 36-test narrow evidence without
claiming a fresh test execution or independently attesting installed compiler
version. The incomplete intermediate GREEN remains failed/NOT acceptance.

## Actual prepared exports

Both exports are under the existing private encrypted staging root:
stage-checks-label49d31 and stage-native-label49d31. Current preflight and
continuation files equal their committed 09689a6f bytes. Preflight SHA-256:
checks `9cc7194ea7e4915beb39e10aa2db3042276e81f2a271d6b3878dd5184c366fd8`;
native `8f86b79ffe04e273d1377e22ba7fc0f2ef420d9d429691ca062ae519f2518d7c`.

Actual exact manifest SHA-256:

- Checks: `1bcc330f8c64591398c960c1303b35ff633b1b7b7bee012b0a8965688b34eade`.
- Native: `61c98062564508324da33f5f9c54ef0eb8954630aa97fedb4100a379c2d68401`.

Each selects its correct stage/run_id, source/runner commit 49d3fe33,
required_checks 14, execution_state UNUSED, launch_history
`none (fresh finite export)`, and exact empty stage_inputs. Neither export
has a result directory, extra file, symlink, special entry or stage-input
directory. Neither unique sibling offload log nor rc exists.

Each complete nine-file inventory consists of manifest, runner, helper,
source598.tar, native598.tar, rolldown608-source.tar.gz, successor598.tar, and
the two native608-stages receipt JSON files. All small-file digests match
actual manifest/preflight pins; runner and helper bytes equal their exact
committed source paths at 49d3fe33:

- Runner: `715e53bd43979434f317807973d9712bc58d6ecbeec357561f92053b8aa3cd6a`.
- Helper: `a558db9afacd22111fb5c2590fe902298b12ea06910eac6efab43f4aa27c0de4`.
- Native compile receipt: `4a651254152b051476758d1a1a9156d87c535ce8242f30b7213f94862931ed9e`.
- Native libtests receipt: `2f81179f5d1bf14d1519cf446935a3cd783da0e28e79a69067c85e5f873dd946`.

I freshly streamed both 17664000-byte successor archives; both hash to
`ae36bfdf844917b226f4f98d358894b00268696316f6fa71eee0a38adf207e75`.
I inspected every tar member without extracting: exactly the declared 858
file paths, all committed source bytes match 49d3fe33, executable bits match
Git, and no symlink/special member exists. Tar modes 0664/0775 retain the
Git archive encoding of nonexecutable/executable files.

Canonical JSON identity independently recomputes common export
`0bb56af5f6e205bf03be00ff446a7a5fe884162becad239d153ff0f6b913737e`
from the exact base source digest, source commit and successor digest.
The three unchanged common archives match the manifest/preflight digest pins
and retain the same device 64512, inodes, size and mtime as the reviewed
stage-unified-0-fullsize5aff1 archives: source598 inode 395540/689664000 bytes,
native598 inode 395541/921600 bytes, compiler source inode 395542/5962781 bytes.
Those large previously reviewed bytes were not redundantly rehashed here.
The maintained preparer is unchanged SHA-256
`1e701de05d9ccdfccee532cfef8bcc93ba0fc8f9937caf86d689cfc3eda216f2`;
its preparation path streams all common archive hashes before linking.
The remote runner will verify archive digests again before extraction.

Inherited manifest descriptive purpose/budget/source-correction-review text
does not override the actual stage, exact 49d3 source/runner, new common
identity, approval 386f7231 or explicit current preflight launch gates.

## Fresh bounded verification and launch conditions

Fresh independent `python3 -I -B stage608.py verify-inputs` and `sh -n run608.sh`
exit 0 in BOTH actual exports. Fresh storage608.py check exits 0 for checks
and native: current unique bytes 1641777846, free bytes 5682520064, reserve
2147483648, aggregate cap 4294967296; return caps are respectively 16777216
and 67108864 bytes. These are observations, not substitutes for live checks
immediately before launch.

Exact checks command is
`offload run --timeout 1200 --mem 14g --cpus 4 --artifacts result608-checks -- timeout -k 15s 1140s sh run608.sh`.
Require this exact independent review, source approval, UNUSED/no result/log/rc,
inputs/storage 0, fresh health up, no competing remote run and at least 1575
worker seconds remaining AFTER preflight, including transfer/settlement margin.
After execution require actual client/result 0, exact manifest/source/common/
run/input/output/producing receipt pins, complete tests.log and installed JSON
with every required case, real supervisor IPC refusal/cancellation/settlement
coverage, storage-result 0 within 16 MiB, committed complete evidence and
independent acceptance. This preflight does not grant checks acceptance.

Exact native command remains
`offload run --timeout 2460 --mem 14g --cpus 4 --artifacts result608-native -- timeout -k 15s 2400s sh run608.sh`.
Native is permitted ONLY as the FIRST heavy action in the NEXT FRESH worker,
after actual independently ACCEPTED NEW 49d3/common0bb5 checks, with exact
review, fresh health/no competitor, UNUSED/no outputs/log/rc, inputs/storage 0,
and at least 2655 seconds AFTER preflight (prefer 2895 including observed
transfer). The current worker cannot fit it. No native launch is authorized
before those conditions. Acceptance must inspect actual newly produced native
receipts/addon/result and storage bound; inherited original native libtests
remain inherited evidence, never a newly executed libtest run.

Fresh `git diff --check 5aff81fe 49d3fe33` exits 0. The optional full
original605..49d3 whitespace check reports existing whitespace in retained raw
historical log artifacts; that is not a new executable-source defect or a
reason to rewrite historical evidence. No full checks/build was run here.

## Authority and remaining work

Historical 5aff/common230f checks/native/runtime remain historical evidence
for their exact producer identities. The failed unified-0-fullsize5aff1 remains
SPENT_FAILURE_NO_REPLAY; no checkpoint returned and no compiler successor was
unlocked. Prepared compiler668db7e1 and old-source future exports are superseded
for this correction. No historical receipt may be relabelled as 49d3/common0bb5.
An admitted failure is spent: preserve evidence and diagnose before a changed
reviewed attempt; preadmission refusals and uncertain settlement retain RUNBOOK
rules. No broker, budget, owner, privilege, lifetime or settlement gate changes.

Fresh runtime/unified/compiler/package stages and their exact source/input/
preflight/result/storage/independent-acceptance gates remain open. Actual NEW
unified-0 must pass and be independently accepted before compiler execution.
There is no final package/artifact/action/privilege/whole-seal/actual automatic
review or genuine ordered HQ595 application approval. This document authorizes
no automatic later-stage launch, application, installed-state mutation or
production deployment. **595 MUST NOT APPLY.**

Only this requested review document was written. No commit/push, offload,
heavy test/build, provider, root, service, queue or installed-state action.
