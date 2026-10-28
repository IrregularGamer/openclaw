# Independent corrected-freeze inventory and native preflight review608

**VERDICT: APPROVE SOURCE INVENTORY / PREFLIGHT EVIDENCE ONLY.**
No material finding in this scope. Reviewer: Rook
`/root/review_current_inventory`, 2026-10-28 UTC, independent of the preparer
and foreground offload operator.

Reviewed exact inventory commit `2001a386b2ac656a9bb53588c5700eda4bf7c49f`
and native launch record commit `dc4e4710bc788e9ed92833cef8863e1781620aa7`.
Each committed evidence blob equals its working file. Frozen build source is
`5f7d810b7f254e4f06dbf7761b557ba90bf1a2b0`; this review adds evidence and
must not change that source or relabel old frozen2b receipts.

Independent bounded Git/Python checks passed:

- Compared the exact sorted, duplicate-free inventory to
  `git diff --raw --no-abbrev --no-renames -z` from
  `877458d730d2455528fb639710ff3f9ba8aae5b2` to the freeze: 535 paths,
  518 additions and 17 modifications, no deletions. Streamed every present
  old/new Git blob through SHA256 using `git cat-file --batch`, with reads
  capped at 1 MiB: all 552 occurrences (537 distinct Git blob IDs), 11,550,835
  bytes, matched the recorded digests and Git modes. Modes are 551 occurrences
  of100644 and one100755. All518 old absences matched zero mode/OID and the
  exact `{state: absent}` representation; all535 new states are present.
  Inventory SHA256 is
  `093b7c0f13fec022cfd67530a1a501db741430368eb6e2c50306ab6feb4bf89f`.
- The current baseline proposal and retained whole original seal are identical
  at the freeze and current checkout, respectively SHA256
  `428ced690f0b3a3cb8a7a2a4fc38570ffa71fa98d7298423376a26fd3ee6a9c9`
  and `51170230064a8da20e074497eae6a6c968d293d262e9e31523dd7365a5c128d3`.
  Both match the inventory's references. Fresh application validation remains
  mandatory; neither reference may be silently refreshed. Package receipt,
  action and next-seal fields are null.
- Independently inspected the existing exact source correction review
  `5108bb4a8545829668d6764b24034a12e71d4720` for correction
  `00221e2d24c55e3bc00a3ca53c3f378c91b4a466`, and outcome review at the
  freeze for `60f3da408c690ca523829bccb184ea6d9f2c8482`. These, plus combined
  source review `3d178871afd0e759fdd0b4e0cc376a7cfc0b3df1`, are ancestors
  of the freeze. The inventory correctly describes their source-only scope.
  This review does not repeat their semantic review or eight correction tests.
- Export `/home/deploy/agentq/tmp/export608-stage-native-owned-next` has
  manifest SHA256
  `708a52c26402db1b4b030c0a0a64a91911fb6dd15d9798ade2e12b091c2f9e2e`,
  matching the committed launch record. Source commit, native stage, empty
  required stage-input set and common source-export identity all agree.
  Canonical JSON identity recomputes to
  `76b4b47a0e5c3e0a157f75ff1b76d60753c8acdbf5f76bc495668dd985d70f64`.
- Streamed the10,792,960-byte successor archive hash and independently streamed
  a fresh `git archive <freeze> -- <all535 successor_paths>` to SHA256; both
  equal `5f71a602a65342545551876133583c3127f37b2ae2954b0fbc89a35e9f68bfb7`.
  All535 regular member contents separately match frozen Git blobs. All archive
  members are regular files or directories with safe relative paths. Exact
  archive regeneration also proves Git archive mode/header representation;
  archive group-write bits are distinct from Git index modes.
- The source inventory and successor overlay have different scopes despite
  both containing535 paths. Overlay base is
  `c790ba44938bd90f75fb41f2f2eeaaff287df546`, whose full frozen diff has625
  paths. The90 omitted paths are all `docs/strict542/job608-*` historical
  evidence documents; no executable/source path from that diff is omitted.
  The inventory does not pretend to describe the overlay's selected path set.
- Export runner and stage helper bytes exactly match frozen source paths.
  Runner SHA256 is
  `728b162324c8241a2e6027de4e5f390adb8570efcdf1059678cdef92e1288f02`;
  helper SHA256 is
  `c162c5a15c9fc1392c5fbec06f543127f176031a162d99aaf4ea3b6b2c2a5d52`.
  `sh -n` and the helper's bounded `verify_inputs(export)` passed. Native
  stage correctly requires no prior stage receipt.
- Both small native receipt files match their manifest pins: compile
  `4a651254152b051476758d1a1a9156d87c535ce8242f30b7213f94862931ed9e`
  (2,117 bytes), libtests
  `2f81179f5d1bf14d1519cf446935a3cd783da0e28e79a69067c85e5f873dd946`
  (2,062 bytes). These are expected rebuild pins, not successful evidence for
  the new source's running native stage.

The manifest's inherited `runner_commit`, old test-correction review-pending
text, predecessor and UNUSED fields are historical descriptive metadata. Current
execution identity comes from the exact frozen source, current runner/helper
bytes, archive/export digests and existing00221e2d/5108bb4a plus60f3da40/5f7d810b
reviews. UNUSED in a committed preparation snapshot cannot prove current launch
state. The operator reports that the single foreground native offload has since
begun; this reviewer neither launched nor independently established its outcome.

The recorded finite command is
`offload run --timeout 2460 --mem 4g --cpus 1 --artifacts result608-native -- timeout -k 15s 2400s sh run608.sh`.
It retains normal admission, deadline and standing Decision618/S tg1825
4GiB/one-CPU authority. No budget, unit, broker, owner predicate or cancellation
exception is created by this record. Runtime admission and worker lifetime are
operator/controller facts, not proved by this review. The root operator must
preserve the admitted foreground run and settle it normally.

Limits: no giant retained source/native/upstream archive was rehashed here.
The preparer's streaming archive checks and the runner's mandatory pre-extraction
checks remain the basis for those raw pins; this review independently verifies
the small successor and current source/policy bytes, not a complete fresh
secret scan or the native toolchain. No full suite/build, offload launch, provider
call, installed/root/unit/sudoers/config/service/scheduler/seal operation ran in
this review. No new source export was created and the launched export was not
edited. No absence of live drift, completed compiler stage, artifact or
reproducibility result is inferred.

Reviewed587 fd3 transport remains required; obsolete586 request-time sudo and the
unapplied historical native-owner-read patch supply no authority. Exact final
artifact/tree, full required checks and realistic refusal/cancellation evidence,
action/privilege/original-and-next-seal reviews and automatic queue review remain
required. So do exact backups/rollback, finite foreground NONQUEUE HQ ownership
in a natural settled gap, unchanged native peer/cgroup/MainPID predicates and
fresh genuine post-restart owner binding AND accepted-run acknowledgements.
575/588/592 stay by reference,553 alone owns SAME510,497 alone later submits its
fresh reviewed scheduler request after all original gates. **595 MUST NOT APPLY.**
