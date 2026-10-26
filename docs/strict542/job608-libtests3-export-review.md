# Independent exact libtests3 export review608

VERDICT: APPROVE ONE future libtests-stage offload, conditional on compile4 settlement, normal controller/lease admission and at least 51 minutes of foreground worker lifetime remaining at launch. No run was launched by this reviewer. Compiler fit, combined diagnostic, package, action, privilege, seal and automatic queue acceptance remain unproven.

Reviewed fresh `/home/deploy/agentq/tmp/export608-native-libtests3` against committed `job608-native-libtests3-export.json`. Manifest SHA256 is `3047f378a219497f392994bbe6ef36d7ffe6e23b5aaaf1e51681b8136076fb94`; its bytes equal the committed manifest. Source is `b1416481c38ba1480d8c881ca36e96785512fc47`. Recreating `git archive --format=tar` at that commit with all 174 manifest paths reproduces `successor598.tar` byte for byte.

Independently recomputed hashes equal the manifest and the approved compile4 export:

- Successor: `29c3853b9715326cd7323547058d3b7fd448a9ca8a653682fad92da98eff65e6`.
- Pinned upstream: `203aa4834d7a52522c758c81f6e493bea9fea828d4454fe2a25b9519d2d258ac`.
- Stage runner: `2c6e313a9aa7dddfbbdfe36986325bed7f46346d6e05822d4c032ca344290e57`.

Parsed compile4/libtests3 manifests differ only in `purpose` and `stage` (`compile` to `libtests`). The runner also equals committed `run-native608-stage.sh`. The export contains exactly four regular files: manifest, runner, successor archive and upstream archive; no source/output directories, dependency tree, addon, Cargo cache/target, toolchain, runtime/config/auth files or large base archive are supplied. The successor has 174 regular members and six directories, no links. Both archives have unique, safe relative member paths. Upstream has two symlinks: `CLAUDE.md -> AGENTS.md` and the existing import-glob fixture `linked/my-lib -> ../packages/my-lib`; both resolve inside its single root. No escaping link or special member was found.

Fresh private-key/token-pattern and sensitive-filename scans across both archives, runner and manifest found no credentials or sensitive filenames. The assignment-pattern scan's sole upstream hit was Rust `Token::` match syntax in `crates/rolldown_utils/src/filter_expression.rs`, inspected as a false positive. All six pinned upstream file hashes match `rolldown-source-pin608.json`.

The four compiler owner inputs in the archive equal both source commit and current checkout:

- `scripts/lib/prepare-native608.py`: `cd172e32b7376e89300ee794c3e85ee6740a557951c81f72e8f8fb9a82e649be`.
- `scripts/lib/last-use-ast608.rs`: `8d293f921d754f3ffca6f60eaec8b61fc577ebef779d9c5714db5f46c4cf2da4`.
- `docs/strict542/rolldown-source-pin608.json`: `644d4ab9b970df0aaa34070cd8db96add012fb82db9f72bce7878571549988ca`.
- `docs/strict542/build-native608.py`: `f213797ea4b8eb45bb2b93564734714b41d3a3b8d2b2b2a20c3b3b8c531f269c`.

These are compile4's post-metadata release owners, including the changed prepare owner already independently reviewed in `job608-post-metadata-source-review.md`. Earlier native receipts for the old prepare hash cannot satisfy them. Personally inspected the stage runner, build owner, prepare transformation, unchanged helper and `native-compiler608.mjs`: receipt admission requires the exact four current owner hashes, matching complete compile/libtests receipts, toolchain/patched-source agreement, lifetime success, negative-control detection and matching addon bytes.

The fixed libtests branch runs `cargo test --locked --release --jobs 1 -p rolldown --lib`, after the shared seven lifetime tests and retention negative control. It does not build the addon. It rejects inherited compiler controls; digest-pinned Rust 1.98.1 and cmake 3.31.6 are installed only under disposable `.native608`, with Cargo jobs 1, release codegen units 64, LTO false and opt level 3. It changes no installed files, services, privileges, seal, provider settings or production state. No RAM/CPU override is supplied: normal admitted offload remains 2 GiB/1 CPU.

ONE future command, after the sole active compile4 run launched at 21:12:57Z in the worker that started at 21:12:00Z has settled and its outcome has been reconciled (launch recorded in `/home/deploy/agentq/runs/608/NOTES.md`):

```sh
offload run --artifacts result-native608-libtests -- timeout -k 15s 2700s sh run608.sh libtests
```

The outer 2700-second deadline plus 15-second kill grace caps the unchanged 5400-second inner deadline. Require at least 51 minutes foreground lifetime at launch for execution, grace and collection/settlement reserve. This approval does not authorize concurrent work, a duplicate compile4, an unchanged retry, local fallback, budget increase or standalone lifetime-only retry. Preserve and reconcile refusal, failure, timeout or uncertain transport outcomes. Fresh accepted compile4 and matching libtests3 receipts must precede any separately reviewed combined source-native diagnostic; complete compiler fit and later package/action/privilege/seal/queue gates remain outstanding. This review used read-only source/archive/hash inspection only; no tests, offload, runtime or installed changes were performed.
