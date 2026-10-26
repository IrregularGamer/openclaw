# Independent native last-use source review608

Reviewer: Rook `/root/memory_review`, independent from implementation and export preparation.
Reviewed exact twelve-file source delta: `b14ca0d04f897b0d944c956ab8eb6276dda3d98a` → `b6a438b9faffb1a3b43a398206e8ec501330cf13`.

Verdict: APPROVE_SOURCE_FOR_ONE_REVIEWED_ADMITTED_CHANGED_SOURCE_RUN_ONLY. This is not native compilation, measured memory fit, completed build/package, runtime installation, action, privilege, seal or automatic queue approval. The exact secretless export still needs independent review before execution.

I independently checked all five pinned upstream file digests against immutable Rolldown commit `5b4746e442989d770c606ce08d2737e6aafbd25d`, applied the actual Python patch to those bytes, and verified that a second application refuses. Resulting SHA256 values:

| Patched upstream file | SHA256 |
| --- | --- |
| `crates/rolldown/src/stages/generate_stage/render_chunk_to_assets.rs` | `ea7fa82fd638d526104f4ae2eea0bfddf297e2082b6026c8bcc828466e81abc7` |
| `crates/rolldown/src/stages/generate_stage/mod.rs` | `7a20ac29a8222be770c442f85b8c33d8cd1d4a30c8c2a6738b826af4fdeb7fdd` |
| `crates/rolldown/src/stages/generate_stage/last_use_ast_table.rs` | `7df17000aa7fda8f144064a57babe34717bc907515b29e7708fce1807414ef84` |

The owning correction counts every normal-module occurrence, including chunks filtered only after code generation. It asserts the canonical table/module index identity, preserves external `None` positions, original indentation and ordered output vectors, releases unused arenas before rendering, and releases each used arena only after its final render returns. Repeated occurrences remain readable until then. `ModuleRenderOutput` owns its String/map; the generic callback cannot return a borrow of its AST. The patch retains the complete linked graph, singleton identity, plugin hooks, existing purity annotations and externalization policy. Sequential generation is consistent with the fixed one-CPU run. Source establishes reduced AST/output overlap, not the location or complete cause of the prior failure or a successful 2GiB fit.

I inspected upstream `rolldown_binding/Cargo.toml`, `build.rs`, allocator initialization, `.cargo/config.toml`, and the generated JS binding loader. The crate supplies a cdylib through napi-build and supports the selected `NAPI_RS_NATIVE_LIBRARY_PATH` override. Cargo keeps the locked dependency graph, jobs1, explicit reviewed release profile and private toolchain/cache paths. Receipt validation binds the owner sources and resulting addon bytes; caller-selected NAPI controls are refused before owner selection. The runner executes real helper lifetime tests, the retained-lifetime negative mutation, native library tests, stock/patched output equality, singleton/effect/dynamic-import and eight ESM/CJS/map/minification variants, plus stock and patched lazy-barrel checks before the complete diagnostic config sequence. Failures stop the sequence. The native artifact remains separate from the unchanged owner-native587/generator pins.

I independently ran the22 small Node policy/inventory/disposable tests:22 passed, zero skipped or failed. Shell/Python syntax and `git diff --check` passed. Rust is unavailable locally; actual Rust tests, negative mutation, native compilation, API/parity fixtures and the changed-source compiler diagnostic remain unrun and must succeed in the reviewed admitted remote run. The2400-second native build and900-second diagnostic deadlines remain finite; hard memory/CPU caps, canonical4352MiB full-build guard and1625784320-byte diagnostic floor are unchanged. No runtime, sealed tree, unit, service, scheduler, privilege, owner/cancellation predicate or live application changed.

Primary source: [pinned renderer](https://github.com/rolldown/rolldown/blob/5b4746e442989d770c606ce08d2737e6aafbd25d/crates/rolldown/src/stages/generate_stage/render_chunk_to_assets.rs), [owned module render result](https://github.com/rolldown/rolldown/blob/5b4746e442989d770c606ce08d2737e6aafbd25d/crates/rolldown_common/src/types/module_render_output.rs), [native crate](https://github.com/rolldown/rolldown/blob/5b4746e442989d770c606ce08d2737e6aafbd25d/crates/rolldown_binding/Cargo.toml), [binding loader](https://github.com/rolldown/rolldown/blob/5b4746e442989d770c606ce08d2737e6aafbd25d/packages/rolldown/src/binding.cjs).
