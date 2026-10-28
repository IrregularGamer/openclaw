# Independent review: frozen9fb inventory and unused native preflight

Verdict: APPROVE SOURCE INVENTORY / UNUSED NATIVE PREFLIGHT ONLY, exact committed
preparation20343a54d8aab106db4871ec99f14c6bf58d585b. Reviewer: separately delegated
independent Rook source-analysis lane. Frozen executable source remains
9fb3d43951f4f2e2b84388b0ad6d1eb994de4dae; this review commit does not move it.
No source-native build, full482 checks, package, artifact/action/privilege/seal,
automatic queue approval, install or release is accepted.595 MUST NOT APPLY.

I independently compared the complete no-renames Git diff from old source
877458d730d2455528fb639710ff3f9ba8aae5b2 to frozen9fb against the committed inventory:
615exact paths,632present old/new descriptors and598absence descriptors. All modes,
SHA256 values, and presence/absence states match.613distinct Git blobs totaling
13854691bytes were streamed in64KiB chunks; no giant build archive was reread.
The source inventory retains null build/package receipt, application action and
next-seal fields. It is not the final installed-target or artifact inventory.

Final source_export_sha256 equals the native-ready descriptor and actual manifest:
fbeed48cc8ecc375257396e34ff4bfaf1708a141ffa21af979ff2efc49dbbfc8.
I recomputed it from the canonical sorted compact JSON formula containing exact
base archive digest, frozen source commit and successor archive digest. The small
13MiB successor archive streamed SHA256 matches
3dc6dc27db3dc589a2717451b6fe692e5e563463341d3cef590f4e6fa409d187.
The actual manifest SHA256 matches
f99a16bd9ee223d4814f473925d4fe6a059400c9f99d8a536f29a6987e7a13cf.

Actual native export runner/helper bytes match both manifest/ready pins and their
exact frozen9fb Git source blobs. Runner SHA2562604fe3410a452951c4214ae37de0762935914443a9fc3456e5b5c041e9bb21c;
helper SHA256c162c5a15c9fc1392c5fbec06f543127f176031a162d99aaf4ea3b6b2c2a5d52.
The exact native compile/libtests JSON pins match their actual staged files;
base/native external archive identity fields agree across descriptors. The
canonical preparer reports its earlier full raw archive checks and actual0;
this review did not independently rehash those giant archives or relabel old
native receipts as new producing-stage acceptance. Actual stage is native,
manifest is UNUSED, stage_inputs is empty, no native result directory exists.
The actual fixed stage608.py verify-inputs command returned0 independently.
No build/test/offload was launched by this review.

The recorded64MiB native return reserve fits the recorded288092160free bytes,
but the previous313378134byte runtime checkpoint alone exceeds that free space.
This preflight does not approve an expensive rebuild while its end-to-end return
storage/source-carrier gate remains unresolved. The continuation explicitly
requires storage reconciliation or an independently reviewed correction in the
existing stage owner before affected launches; no deletion or hash/receipt waiver
is authorized. Recheck actual space, worker deadline, source binding and complete
return reserve before any later finite admitted execution. A carrier source
change requires a declared reviewed freeze rather than silently modifying9fb.

All historical5f receipts remain historical. Subsequent native/compiler/checks/
runtime/declaration/package stages need exact new-source producing receipts,
independent acceptance, complete original checks and final artifact/action/
privilege/seal/automatic review. The original finite natural-gap nonqueue HQ
ownership procedure and genuine fresh post-restart owner/accepted-run ACKs remain
mandatory; queued ops ownership supplies none of that authority. No runtime,
root/unit/sudoers/service/gateway/provider/scheduler or seal mutation occurred.
