# Independent compressed checkpoint carrier source review608

**VERDICT: APPROVE SOURCE PREPARATION ONLY.** No unresolved material source
finding in the reviewed correction. Reviewer: Rook `/root/carrier_review`,
2026-10-28 UTC, independent of the implementation lane.

Reviewed exact cumulative diff `eef3064c97beddc92f06ea191eb8a9cd269d2742` through
`1bed4d1bb53eff145f724cc6a448dc73b3609015`: the carrier implementation at
`2888b2bd7743a33ad776ff14febdf26ad5486207` and the canonical preparer metadata
correction at `1bed4d1b`. The affected owners are `stage608.py`,
`prepare-stage608-export.py`, `run-stage608.sh` and their two focused Python
test files. This review does not declare or change the build source freeze.

- The existing stage owner writes exclusively to a new `checkpoint.tar.gz`
  using streaming PAX tar output through level-1 gzip. It creates neither a
  complete raw tar file nor a payload-sized in-memory buffer. Empty gzip
  filename and `mtime=0` remove run filename/time from the gzip header. Tar
  contents retain their existing metadata and stage ownership.
- Every build stage's exact `OUTPUTS`, receipt digests and restore filename use
  the compressed carrier. Both existing preparers load the committed helper's
  output contract dynamically. Producer source/common-export identity,
  successful receipt status, exact output/input sets, regular-file checks and
  independent native receipt/addon pins remain enforced. Historical raw-tar
  receipts cannot be relabelled as successful compressed-carrier receipts.
- Restore keeps its complete member validation before creating the destination:
  fixed stage ownership, duplicate/traversal/type/special-mode refusals,
  non-directory-parent rejection, confined relative symlinks, required sidecars
  and collision refusal are retained. Python's data extraction filter remains
  active, followed by restoration of already-validated ordinary mode bits.
  `r:*` deliberately reads both raw and compressed archives; receipt/input
  acceptance still requires the exact new carrier filename and digest.
- The canonical preparer now refreshes both `runner_commit` and
  `stage_helper_sha256` alongside the existing runner digest. This resolves the
  inherited metadata inconsistency when exporting the changed helper. The
  sibling finite preparer already records these fields from the current bytes.
  The added regression exercises canonical preparation with tiny local files
  and mocked Git/archive production, checking actual generated manifest pins.
- The existing full checks runner now executes all seven preparer tests.
  Together with the two new carrier tests this adds nine cases to the prior
  planned 482, giving 491 expected cases (158 Node, 135 Python, 198 installed).
  This arithmetic is a planned count, not a complete-suite result.

Fresh independent verification on the final reviewed source:

- Both focused files passed: **23 tests, 0 failures/errors, 0.149 seconds**
  (16 stage helper tests and seven canonical preparer tests). The process had
  a 256 MiB address-space limit, 30-second CPU limit and 60-second outer wall
  timeout. Default scratch was a cleaned temporary directory under `/var/tmp`;
  the preparer fixture's tiny repository-local temporary directory also cleaned
  itself. No full source archive or real checkpoint was read by these tests.
- The carrier regression demonstrates gzip bytes, strong compression of its
  approximately 1.1 MiB repetitive synthetic payload, equal repeat hashes, exact
  restored bytes and file/directory modes, and readable owned symlink contents.
  Compressed and raw malformed fixtures both refuse before restore-directory
  creation. Existing tests retain exact-input, foreign-source/export, digest,
  native pin, mode/link and receipt coverage.
- `sh -n docs/strict542/run-stage608.sh` and
  `git diff --check eef3064c..1bed4d1b` passed.

Limits: repeat hashes prove the same unchanged input metadata under the tested
Python/zlib environment; the code does not normalize tar metadata or promise
cross-version gzip byte identity. Streaming avoids payload-sized buffering but
tar member metadata and recursive directory lists still consume memory.
Compression of the synthetic fixture does not establish the real checkpoints'
compression ratio, peak working set, end-to-end scratch/storage fit or admitted
remote runtime. No fresh production-size export or complete 491-case suite,
native/compiler/build/package run, final artifact/tree inventory or restore of
real stage results was performed here. The fixture's mocked archive production
does not substitute for fresh exact-export preflight.

End-to-end capacity remains unresolved. The coordinator reports a historical
runtime compression estimate of 313,313,280 raw bytes to 88,505,333 gzip bytes;
this reviewer did not reproduce that measurement. It cannot prove capacity for
all retained runtime/middle/tail carriers, final package, native copies and peak
scratch/return reserve together. Source acceptance supplies no approval to
launch the expensive native stage while that capacity gate remains unresolved.
Keep the prepared export UNUSED pending that reconciliation; deleting retained
artifacts is not authorized by this review.

The executable correction requires a separately declared reviewed freeze,
fresh source/export bindings and newly valid producing stage evidence before
use. Historical stage evidence retains its historical identity. Exact final
artifact, action, privilege, original-and-next-seal, owner/acknowledgement and
REAL automatic queue gates remain required as previously specified.

No offload launch, heavy test/build, installed/sealed/root/unit/sudoers/runtime,
service, scheduler or policy change was made in this review. The only authored
deliverable is this review document. **595 MUST NOT APPLY from this review.**
