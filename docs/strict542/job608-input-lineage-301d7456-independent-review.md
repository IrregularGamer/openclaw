# Independent source review: job608 input lineage 301d7456 (Decision662 Option B)

Verdict: **APPROVE** (no required changes; two non-blocking hardening notes below).

Commands run (in /home/deploy/agentq/tmp/source552, read-only apart from this file):
- `git show 301d7456` (stage608.py +39, prepare-stage608-export.py +21, test_prepare_stage608_export.py +91)
- `git merge-base --is-ancestor 674840b6 301d7456` -> 0 (ancestor)
- `git diff --name-only 674840b6 301d7456` piped through `stage608.lineage_path_allowed` -> 0 disallowed paths
  (non-evidence paths: build598.sh, frozen-package608.py, test_frozen_package608.py, stage608.py, prepare-stage608-export.py, test_prepare_stage608_export.py)
- `cd docs/strict542 && python3 -m unittest test_prepare_stage608_export test_stage608 test_frozen_package608` -> Ran 39 tests, OK; worktree clean after

Findings:
1. Default path unchanged. Without `--lineage-ancestor`, `lin=None` and the else-branch is the original exact assertion (exit 0, source_commit==C, source_export==C export). Remote: `check_lineage` returns None when the key is absent, so commit/export stay the manifest's. `receipt()` adds `input_lineage` only if present in the manifest; with sort_keys the default receipt bytes are identical. Test `test_default_binding_still_refuses_ancestor_receipts` covers it.
2. Opt-in and package-only: prepare asserts stage=='package', resolves ancestor via rev-parse, refuses anc==C, and requires `git merge-base --is-ancestor`. Remote refuses any record on a non-package manifest or with ancestor==source_commit.
3. Allowlist: the real 674840b6..301d7456 diff passes. Native/compiler/tail outputs are byte-pinned by digest (plus native independently pinned to native_stage_outputs/addon) and were accepted at the ancestor. The allowlisted scripts run at C only as package-side code, and each one is source-reviewed at C. checks at C runs test_stage608/test_prepare/test_frozen_package608. In the actual diff, frozen-package608.py only adds `materialize` (package path; preflight unchanged) and stage608.py only adds lineage verification. Acceptable. Caveat (non-blocking, process): frozen-package608.py `preflight` and stage608.py `archive_build`/`stage-native` also run inside producing stages (run-build-stage608.sh:13,16; tail archive). A future A..C change to those producer-side functions would still pass the static allowlist. So every package preflight that uses lineage must state that the recorded changed_paths diff of stage608.py/frozen-package608.py touches no producer-side logic. A source change is not required for this use.
4. Remote verify_inputs enforces the record: the exact key set; stages non-empty and a subset of {native, compiler, tail}; receipt_sha256 keys == stages; every changed_path allowed. Per lineage stage, the pinned receipt digest must equal the recorded digest, and receipt commit/export must equal the single recorded ancestor commit/export. Every listed stage must actually be used (`used==stages`). Non-lineage stages still require C/C-export. All prior pin, exact-set, output and native checks are unchanged.
5. Bypass analysis: checks cannot use lineage (refused in prepare as not in LINEAGE_STAGES; remote forces checks to C). Commits cannot mix: one ancestor commit/export, and prepare refuses differing ancestor exports. A receipt at any third commit falls to the exact-C branch. A tampered manifest is pinned by manifest_sha256 and preflight review. changed_paths is self-declared (remote has no git), which is the same trust level as source_commit. build598.sh:52 still binds checks evidence to exact C.

Non-blocking hardening (optional, future source change):
- `check_lineage` does not type-check `ancestor_source_export_sha256`/`ancestor_commit` (None is accepted). This is not exploitable because receipt digests are pinned and real receipts always carry a string export. A 64-hex/40-hex check would be cleaner.
- Consider narrowing the allowlist to function-level review or excluding producer-side changes in a later revision.
