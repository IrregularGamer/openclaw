# Independent native cmake-pinned diagnostic input review608

Reviewer: independent Claude reviewer subagent (Opus 5.5), independent from implementation, the cmake pin change and export preparation.

Verdict: APPROVE_FOR_ONE_ADMITTED_CHANGED_SOURCE_DIAGNOSTIC_ONLY. This approves only the exact export below through normal offload admission at the unchanged default2GiB/1CPU cap. It supplies no execution success, full build/package, action, privilege, seal, automatic queue or application approval.

Recipe change (`70dfe45e`, `docs/strict542/build-native608.py`, +22/-1): adds one digest-pinned official PyPI wheel `cmake-3.31.6-py3-none-manylinux_2_17_x86_64.manylinux2014_x86_64.whl`, fetched only from its exact `files.pythonhosted.org/packages/59/e8/096984b8.../` URL, sha256-checked before use, unpacked with `zipfile` as data (no pip, no wheel install, no setup code), its `cmake/data/bin` tools chmod 0755 and appended to PATH after the pinned Rust toolchain, the wheel digest recorded in the receipt, and `cmake --version` asserted to equal `cmake version 3.31.6`. No allocator, cargo feature, budget, floor, check, cargo policy, inherited-env refusal or test change; no secret, credential or provider input; no network beyond the single pinned URL (the existing Rust distribution fetch is unchanged). The other two changed files are evidence/outcome documents.

I independently verified:

- PyPI JSON `https://pypi.org/pypi/cmake/3.31.6/json` lists that exact filename at that exact URL with sha256 `1c8b05df0602365da91ee6a3336fe57525b137706c4ab5675498f662ae1dbcec` (size 27,800,904). A fresh download into an empty `/tmp` directory hashes to the same digest.
- The wheel has 3,875 entries, including `cmake/data/bin/cmake` (plus `ctest`, `cpack`) and 3,815 files under `cmake/data/share/cmake-3.31/` (the runtime module root). No absolute or `..` member paths and no symlink members, so `extractall` on this digest-pinned archive is acceptable. An extracted copy outside the repo reports `cmake version 3.31.6`; nothing else from it was executed.
- `export-manifest.json` is byte-equal to committed `docs/strict542/job608-native-cmake-export.json` (`a8c8af1a`); its sha256 is the manifest identity below.
- `successor598.tar` sha256 equals the manifest `successor_archive_sha256` and equals a fresh `git archive 70dfe45e` of the sorted `git diff --name-only --no-renames c790ba44 70dfe45e` paths. Its 141 regular-file members equal both the manifest `successor_paths` set and the full base-to-source diff (131 added, 10 modified, no deletions/renames).
- `run608.sh` is byte-equal to committed `docs/strict542/run-native608.sh` and its sha256 equals `runner_sha256` (unchanged from the prior approval).
- `source598.tar`, `native598.tar` and `rolldown608-source.tar.gz` share device inode with those in the previously independently reviewed `export608-native-last-use` (inodes 1583918, 1583919, 308931). The 658MiB base archive was not reread in this pass; this review relies on that prior provenance, and the runner rechecks the raw base/native/delta digests before remote extraction. `native598.tar` and the compiler tarball were freshly hashed and match the manifest and `rolldown-source-pin608.json` pins.
- No `.env`, key, credential or database files are present in the export directory or the successor members.

Exact identities:

- Base source: `c790ba44938bd90f75fb41f2f2eeaaff287df546`
- Base archive SHA256: `e79a0e45a4eaea4afe325ca94ba201d5ae43d09d8c15dc07d0695c87ba743de3`
- Compiled source: `70dfe45eb66d1237b353f67625afa44b20cd8ed6`
- Successor archive SHA256: `6e946be5c954239de7e8f8ec6164a44474065b13a061fd23af0f38881e3d01ba`
- Native preparation archive SHA256: `d73e4e35720ffcb71856ce8168e75fa3b4fd49251fd78c811e1abded8b2701de`
- Upstream compiler archive SHA256: `203aa4834d7a52522c758c81f6e493bea9fea828d4454fe2a25b9519d2d258ac`
- cmake 3.31.6 wheel SHA256: `1c8b05df0602365da91ee6a3336fe57525b137706c4ab5675498f662ae1dbcec`
- Runner SHA256: `34b7c4a1cb55a1e8cea35a15fce57c5b24c3a48e3524e8d7f1c01884b41748b1`
- Export manifest SHA256: `763cd0dd9225f16b920483e3b1b96edcc44d30678c7ec47001e532dd2f97bb39`

Notes: the cmake pin lives inline in the builder rather than in `rolldown-source-pin608.json`; it is still covered by the builder's `owner_inputs` digest and the receipt. The remote run needs egress to `files.pythonhosted.org`; if offload egress refuses it, that is a refusal, not grounds to relax the pin.

Proceed only with the one reviewed changed-source native build, real lifetime/negative/library/parity/lazy-barrel checks and complete runtime config diagnostic. All those remote results and actual memory/settlement outcomes require subsequent independent evidence review. Failure/refusal authorizes no unchanged retry, larger budget, local heavy build or gate weakening. The canonical typed package and 595's original application gates remain outstanding.
