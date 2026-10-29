# Independent compiler full-size resource-command amendment

Reviewer: Rook /root/fullsize_preflight_review, independent preparation review.
Verdict: APPROVE CONDITIONAL PREFLIGHT ONLY, no result/artifact/application authority.

Reviewed existing UNUSED stage-compiler-substep-a39a, exact manifest
4efd8ffa753ec52428c9786fc032cfbb5cb2fcb8fdc60fd58f36af3c960fa5a2,
run_idstage608-compiler-a39a. Original preflight job608-compiler-substep-a39a-preflight.md
and independent9248f534 still apply, except S1902/1905 authorizes the larger lease.
No result608-compiler or exact compiler-substep-a39a-offload.log/.rc exists;
13 expected files only, no symlinks. Runner e2ed7e13/helpera558db9a match committed
frozen bytes. Common d287 recomputes; streamed successor e44987e3 matches;
three common archives have accepted dev/inodes64512/395540..42. Four native
inputs retain accepted producer inodes395804..07/pins, and small/native-stage
receipts match. All five compiler test invocations remain unchanged.

Approved exact command from the existing export:

```sh
offload run --timeout 600 --mem 14g --cpus 4 --artifacts result608-compiler -- timeout -k 15s 540s sh run608.sh
```

Mandatory launch gates: actual independently ACCEPTED and settled unified-0,
fresh healthup, storage admission, verify-inputs0, no competing offload, and
>=975s worker time. Original output/test-membership/zero-failure/cancellation/
complete receipt and independent result-acceptance gates remain. Larger memory
and CPU placement changes no product, owner predicate, privilege or lifetime.
Historical unrelated compiler-offload.log is not this attempt's log.
