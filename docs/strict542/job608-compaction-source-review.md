# Independent compaction source review — APPROVE preparation only

Reviewer: Rook independent source-analysis lane. Exact maintained source
2f6788455aea5051cdc5b748cd06554f3ab039a1, implementation0114091e plus
sparse-owner6307bf80; current manifest-only3bfc1085 does not change this source.

The correction belongs to the existing native AST and scan-to-link owners.
LinkStage::new replaces present ASTs serially before linker metadata allocation;
assignment drops each previous arena before cloning the next. The existing
cache clone retains its capacity policy. Both clone methods use one private
implementation and canonical clone_in_with_semantic_ids, keeping source ArcStr,
source_type, spans and semantic identity. No graph/module/export is removed,
no semantic pass repeats, and no cancellation/owner/privilege check changes.
Upstream internal-docs/ast-mutation/implementation.md explicitly states that
cross-pass references use IDs rather than pointers and that cache clones use
this same identity-preserving primitive. Exact native context pins fail closed.

- `crates/rolldown_ecmascript/src/ecma_ast/mod.rs`: old `cbe7294b949f84ac1df482296f7fb023edd7e895a19dfe0c519f70fef6c09245`, prepared `dfb684bce6712f574fb73195ec33b1a6c66b427bed63be01313464a373e9605c`.
- `crates/rolldown/src/stages/link_stage/mod.rs`: old `66b52c2db0ffe0792907275993abd5f0bf935144cf21f8f6a21290f2221fa99e`, prepared `18853d0aa7697d4c7dd38d03e1ec9c92520de179e7ea650302e7cf4efc29ac80`.

Independently fetched official locked crates and verified their Cargo.lock hashes:
oxc_allocator0.150.0 8c5deaaa43f0813b6d4a18dcc5f41bea1996f193f0a55d0242831d7f29bfa16d;
oxc_ast0.150.0 7ef5ff9b1d70a32b100145065aec1c6c455c58b19c4681d092bd88c24c53972d;
oxc_ast_visit0.150.0 f0cf0a82e610e199a916833a98b6fac20aebd18a5a98a5ac0ec93c23dd600a74.
Confirmed capacity() reports allocated bytes, used_bytes() reports used bytes,
all candidate node_id methods are inherent, and VisitJs signatures match.
The real embedded regression compares code and scope/symbol/reference/node
identities for imports, require, dynamic import and new URL; it measures both
used bytes and capacity, checks the old retained-capacity policy, and rechecks
after dropping the original. The runner requires full ecmascript libsuite exit0
AND the exact named regression acceptance before completing compile/libtest
receipts. Consumers reject missing/failed compaction proof and changed owners.

Independently reran lightweight checks:2 patch-policy,3 native-receipt and3
consumer tests PASS. Real Rust execution, deterministic new addon equality,
config46 resource fit and the full package remain UNRUN. Serial compaction adds
one module's new arena transiently; default2GiB fit is an empirical gate.
Recovered238-check phase outcome is failed diagnostic evidence, not package proof.
No application/action/privilege/seal/automatic-review or595 gate is waived.
This approval permits only the separately reviewed fresh source export stage.
