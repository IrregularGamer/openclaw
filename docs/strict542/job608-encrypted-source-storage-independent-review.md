# Independent bounded source-storage placement/action review608

**VERDICT: APPROVE EXACT SOURCE-STAGING INITIALIZATION ONLY.** No material
source or namespace finding for the new unprivileged placement below. Reviewer:
Rook `/root/carrier_review`,2026-10-28 UTC. Reviewed exact supplemental owner
`ec3b1b4dd3d5b2436ef8482c07ee4266cf2b0ad3`, base `f0c85278`, two files
`storage608.py` and `test_storage608.py`.

Approved initialization scope is ONLY the new private directory
`/srv/encrypted/dev-move-98/agentq-source608-20261028-private`, using exact
reviewed base `/home/deploy/agentq/tmp/export608-stage-checks-carrier-next`.
No existing archive contents, retained source/results, backup/DB directories,
mounts, root files, installed runtime, configuration, services, units, budgets
or policy may be changed. This is reversible new source staging under the
existing deploy-owned private namespace, within authorized source preparation.
It supplies no native/build/package launch or final installation approval.

Fresh independent evidence:

- `namei` confirms real directory ancestry and existing parent `deploy:deploy`
  mode0700. The exact new directory is absent. `findmnt` identifies existing
  `/srv/encrypted` as rw ext4 on `/dev/mapper/encdb`. No existing archive contents
  were opened. Available unprivileged filesystem bytes are7,324,835,840, above
  the helper's initial4GiB+2GiB floor6,442,450,944. The current root filesystem's
  shortage does not authorize final `/opt` installation;595 must separately
  reconcile that later capacity obligation.
- Actual base manifest hashes to
  `20111ce5f68e7764e7176a670df6e9097deafa51d02291810bf65dd41c8c7c2d`.
  Source1bed/common5d7e and empty stage inputs match the owner's fixed pins;
  actual small runner/helper files match their manifest hashes. The source
  freeze remains `1bed4d1bb53eff145f724cc6a448dc73b3609015`, common export
  `5d7e9d57fb660e2b54f5595e81ddf332027e21b303937c2cd6bc7f718f311263`.
- Three original raw archive sizes sum696,548,381 bytes. Forecast includes
  268,435,456 bytes for16 overlays,2,919,235,584 bytes for all15 stage return
  caps and134,217,728 bytes for metadata/filesystem allowance: total
  **4,018,437,149 bytes**,276,530,147 below4GiB. The actual base overlay is below
  its16MiB allowance. The package return ceiling is2GiB and includes its full
  returned uncompressed runtime tree; that obligation is not omitted.
- Before writes, initialization requires the exact pinned manifest, frozen
  identity, no predecessor inputs, exact runner/helper pins, new fixed-namespace
  destination and full free floor. The copy owner validates its entire exact
  archive/runner/helper/manifest/native-receipt allowlist first, rejects path
  redirects and digest drift, streams copies in64KiB chunks with exclusive new
  output files, and verifies each copied digest. It does not recursively copy
  the source directory, move/delete history or mutate original files. Raw base
  digests are rechecked by initialization; this reviewer did not reread those
  giant archives or invoke initialization.
- Future local storage checks count unique regular-file inodes for immutable
  same-filesystem hardlinks; returned result checks count every logical path
  because current `rsync -az` omits `-H`. Escaping symlinks, special files,
  unknown stages, excess result size and insufficient capacity refuse. A failed
  initialization may leave its new partial private directory; it cannot be
  silently reused because initialization requires a new destination.
- Inspected the installed offload client's artifact boundary: `cmd_run` calls
  `pull_artifacts` only when the remote command exits zero. Therefore running
  the exact supplemental `result` guard as the final remote command, preserving
  its nonzero status, can prevent an over-cap return from being pulled. A size
  guard run only after transfer cannot provide that protection. This review
  changes no broker or installed offload bytes.
- Independently ran all7 focused tests:PASS,0.011s, under256MiB address-space,
  30s CPU and60s outer wall limits, with cleaned `/var/tmp` scratch. Coverage
  includes forecast overflow, logical-vs-inode accounting, redirects, caps/free
  reserve, unknown stage and copied-byte/original preservation. Both files equal
  exact committed source and `git diff --check f0c85278..ec3b1b4d` passes.
  Owner SHA256 is
  `2cf48a3bb643051e7ccfa719cb7e7cfda96da7d77ba1ecbe66bb1695657d1c04`;
  test SHA256 is
  `74cdb873fab2d1ae150b3c92635040ee8cf8d6b3f67ebe338122e45cf902e0df`.

Limits and next action boundaries: the caps are executable refusal ceilings,
not measured guarantees that future stages complete within them. Capacity checks
are point-in-time checks plus a conservative logical-size/metadata forecast,
not a filesystem quota or a guarantee against unrelated volume growth. Preserve
the2GiB free reserve, recheck before later staging/returns, account for every new
path, and refuse on drift. Never bypass an oversized or uncertain return with an
unguarded transfer. A refused result remains a remote reconciliation obligation,
not permission to repeat an expensive stage unchanged.

Initialization does not prepare or launch a native stage. Each future finite
export still needs exact source/predecessor/receipt preflight and an actual
admitted foreground run fitting the worker's remaining lifetime. Supplemental
guard bytes copied for remote return checking must match the exact reviewed
owner digest and run after stage settlement but before artifact pull. The guard
checks size/redirects only; original stage owners retain every success, digest,
source/export, mode/link, native and receipt acceptance check.

This host copy/return wrapper is outside the gateway build overlay and has its
own exact source/action review. It supplies no altered gateway source or stage
receipt, so it does not move the1bed build freeze or relabel the current491-check
attempt. Any actual build/source correction still requires a new reviewed freeze
and valid new producing evidence. Final package/artifact/action/privilege/seal,
genuine foreground NONQUEUE ownership/accepted ACKs and REAL automatic queue
gates remain unchanged. **595 MUST NOT APPLY.**

No encrypted-volume file was created or modified by this reviewer. No heavy
build/test, offload launch, root/unit/config/service/runtime/scheduler mutation
occurred. Only this independent review document was authored.
