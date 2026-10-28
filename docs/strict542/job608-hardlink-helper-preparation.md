# Decision644 local export helper correction

The build source and all accepted native7/compiler7/runtime7 inputs remain frozen
at 2b543da30204b358d4b58a8fb52b060f405f3789. This is a local export-preparation
helper correction only. Invoke the corrected helper with --commit 2b543da3;
do not advance the build pin to this preparation/evidence commit.

The interrupted uncommitted main() wrapper and six filesystem regression tests
were present on entry; the tests failed because link_input was absent. Implemented
same-filesystem hardlinks for accepted stage receipts and output files, with
1MiB streaming hashes before/after, original producer identity/mode/mtime checks,
source and destination ancestor symlink refusal, traversal refusal, new destination
requirement and explicit EXDEV refusal. No copy fallback, chmod or producer write.
Receipt kind, stage, source commit/export identity and output digests remain
required; frozen stage608.py independently verifies every consumer input remotely.

Validation: python3 -m unittest docs/strict542/test_prepare_stage608_export.py -v
passed all six focused local filesystem checks. These tests allocate tiny files;
no build or full suite ran locally. Raw red/green logs are in runs/608.

All producing results and these linked local exports must remain immutable.
Do not run a preparer during offload upload. Use a NEW destination. Before each
stage, record df and projected return-artifact size plus reserve; preserve inputs
and report any shortfall. Decision644 authorizes no deletion. Rsync copies inputs
to remote storage; there is no shared producer inode on the friend VPS. No source
build/test check, receipt pin, cancellation, owner predicate or budget is waived.

Next: exact independent helper review, then synchronize the reviewed helper to
runs/608/prepare-stage608-export.py and prepare unified-0 from native7/runtime7.
The current checks8 offload remains the only active remote run. Read-only seal
inventory confirms neither helper path is sealed. No installed, root, unit,
sudoers, service, credential or provider change occurred.
