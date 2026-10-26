# Job608 compile3 export review (independent; diagnostic only)

Verdict: APPROVE ONE compile-stage offload of /home/deploy/agentq/tmp/export608-native-compile3.

## (1) Commits ddc789b1 + 40947f38 (HEAD 40947f38830cd19e75ac6925bb2590d9f7d34a28)
- E0282 root cause confirmed: the untyped `|idx|` closure's first use is `module_table[idx]` (a generic Index impl), so rustc cannot infer the type of `idx`. The fix changes one line: `|idx: rolldown_common::ModuleIdx|`.
- Annotation correct against pinned upstream 5b4746e4: ModuleIdx is `define_index_type! { pub struct ModuleIdx = u32; }`, re-exported from the rolldown_common root (lib.rs `pub use crate::{ecmascript::{module_idx::ModuleIdx}}`). The rolldown crate already uses rolldown_common. `ChunkGraph::module_is_in_live_chunk(&self, module_idx: ModuleIdx)` takes it by value. `IndexEcmaAst = IndexVec<ModuleIdx, Option<EcmaAst>>`, so `iter_enumerated()` yields the same ModuleIdx (Copy).
- Predicate unchanged: I diffed the generated finalizer against upstream. The only changes inside the predicate are the closure header and `*idx` -> `idx` (2 sites). The included/runtime/strict-liveness terms are byte-identical. The par filter is now `should_finalize(*idx)`. Nothing is weakened.
- Masked-error sweep (borrowck runs after typeck), by reasoning only, no rustc:
  - should_finalize captures only shared places: self.link_output.{module_table,metas,runtime}, strict, has_required_order_runtime, *chunk_graph. The original filter closure captured the same set and lived alongside filter_map, so it is borrow-compatible and Sync.
  - Its last use is inside `finalized`. The later `&mut chunk_graph.chunk_table` and the `self.link_output` mutations are fine under NLL (closures have no Drop).
  - `release_unneeded(ast_table.iter_mut(), ..)` takes a slice IterMut (ExactSizeIterator). It does not overlap should_finalize, which never captures ast_table.
  - `.raw()` exists: upstream already calls `ChunkIdx::raw`. ChunkTable derefs to IndexVec, so `.iter()` is fine.
  - Renderer: the closure returns an owned ModuleRenderOutput (no lifetime). The nested `.map` FnMut reborrows `&mut asts`. The removed rayon import has no other users in the file. No lint levels are set to deny for rustc (workspace lints are clippy only; RUSTFLAGS only remaps paths).
  - compile2 reported exactly 1 error, so every other body in the patched files already passed typeck.
  - Residual risk: rustc has not borrow-checked any of this yet. The offload is that check.
- Tests: `python3 -m unittest -v docs/strict542/test_native_finalizer608.py` with ROLLDOWN608_SOURCE_ARCHIVE set to the compile3 archive ran 3 tests, OK. RED reproduced: the ddc789b1 tree (test updated, script not) gives FAILED (failures=1), matching job608-finalizer-type-red.txt.

## (2) Export
- successor598.tar 5eb5a44e1e3ec2b6c506c128aff0f18ce1cc5ee5b62a7c407f6fbf6f575ef2e5 = manifest
- rolldown608-source.tar.gz 203aa4834d7a52522c758c81f6e493bea9fea828d4454fe2a25b9519d2d258ac = manifest = pin source_archive_sha256 (upstream 5b4746e442989d770c606ce08d2737e6aafbd25d)
- run608.sh 2c6e313a9aa7dddfbbdfe36986325bed7f46346d6e05822d4c032ca344290e57 = manifest, byte-equal to HEAD:docs/strict542/run-native608-stage.sh
- source_commit is the full HEAD and stage is compile. The 145 successor_paths are identical to job608-native-compile2-export.json and include prepare-native608.py, last-use-ast608.rs, build-native608.py and the pin.
- `git archive --format=tar HEAD -- <paths>` reproduces the tar sha exactly. A secret-pattern scan of the tar contents, runner and manifest found nothing.
- Note: the outer `timeout 2700s` caps the runner's inner 5400s. The compile2 run reached crate rolldown inside this budget, so this is accepted.

ONE run (next worker, >=35 min left): `offload run --artifacts result-native608-compile -- timeout -k 15s 2700s sh run608.sh compile`
