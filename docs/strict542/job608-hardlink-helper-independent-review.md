# Decision644 independent helper review

VERDICT: APPROVE

Reviewed exact source-only commit
`1a8b422d6e43897d5b8036585218e1585226b515` against base
`5555af58113e6b602802dc33e3baabb59b4c5e71` on 2026-10-28.
Scope: `prepare-stage608-export.py`, `test_prepare_stage608_export.py`,
and `job608-hardlink-helper-preparation.md` in this directory.

No material issues found. Accepted producing receipts and outputs now use
same-filesystem `os.link` rather than `shutil.copyfile`. The helper checks the
expected digest before linking, compares source device/inode/mode/size/mtime
before and after linking with the destination identity, then rechecks both
paths' digests. The shared hash helper still reads at most 1 MiB per iteration.
EXDEV explicitly fails with no copy fallback; existing destinations are not
overwritten. The helper neither writes nor chmods producer files.

Stage input paths reject traversal, direct symlinks, and symlink ancestors.
Required-stage completeness and duplicate refusal remain. Receipt kind, stage,
successful exit, exact source commit, common source/export identity, and exact
output digest mappings are checked. The top-level destination remains NEW and
the manifest remains UNUSED. The frozen consumer independently verifies the
exact input set, receipt identity, output digests, and native artifact pins.

This approval is for local preparation only. The build source remains
`2b543da30204b358d4b58a8fb52b060f405f3789`; invoke the reviewed helper with that
commit, not the helper or review commit. Hardlinked producer results and local
exports must remain immutable by procedure. Do not prepare during an offload
upload. This review authorizes no deletion, build-pin change, installed change,
or waiver of stage, budget, receipt, or consumer checks.

Independent validation:

- `PYTHONDONTWRITEBYTECODE=1 python3 -m unittest docs/strict542/test_prepare_stage608_export.py -v`
  passed all six tests, reporting 0.008 seconds. Coverage includes preserved
  producer bytes/mode/mtime and inode identity, bad-digest refusal, source and
  parent symlink refusal, existing destination and destination-parent symlink
  refusal, EXDEV refusal, and traversal refusal.
- `git diff --check 5555af58 1a8b422d` passed.
- Read the unchanged stage consumer and runner to confirm their verification
  contracts remain in place.

Only tiny local test fixtures ran. No export was prepared; no heavy test,
build, service, remote, installed, or producer mutation was performed.
