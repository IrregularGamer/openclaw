# Worker output lifetime split implementation plan608

Goal: remove portable-worker graph/minifier memory overlap without changing its single-file packaging, bundling policy, owner predicates or any budget.

Spec: job608 changes round2; recovered consumer-b evidence/review1226f122.
Source diagnosis: config46 is worker/worker, dts=false. workerDeployBuildConfig always bundles nonbuiltins, embeds WASM/base64 and invokes compress+mangle. Pinned Rolldown render_chunk_to_assets retains link_output/chunk metadata while minify_chunks parses the whole rendered worker. Existing AST-last-use correction drops module ASTs, not that linked graph. The observed native RSS growth after buildEnd is consistent with this overlap; no declaration claim is supported. Source establishes lifetime overlap; the new measured run must establish fit.

Existing solution: use the SAME pinned Rolldown1.2.9 public rolldown/utils minify API (packages/rolldown/src/utils/minify.ts). It supports inputMap composition, compression and mangle.keepNames. No dependency, native patch or lease increase. Worker no-sidecar generateBundle refusal stays in the bundle phase. Normal canonical non-bounded configs remain unchanged.

- [x] Add regression tests: only the four exact portable workers may split, preserve config except required deferred minify; compiler failure/timeout/scanner refusal must prevent minify; successful bundle must be settled before minify; second failure never succeeds; remaining shared deadline required.
- [x] Add shared config selector/orchestrator and fixed worker minifier; wire isolated and bounded owning drivers. Output maps compose; source/legal/name/dynamic-import behavior checked on actual bundler fixture. Symlink/redirection and parse failures refuse. No runtime worker code runs in the real build diagnostic.
- [ ] Independently review exact committed source/export. Run ONE fresh secretless focused worker diagnostic with frozen dependencies, all209 scoped checks, typed3, split fixtures and all4 real worker configs,2GiB1CPU. No native binary input. Existing native/parity/config15 evidence remains at the old exact source; focused stock compiler is identified honestly, not claimed as full patched consumer/package evidence.
- [ ] Reconcile actual outcome, then complete separately admitted full typed build/frozen package with exact native binding and real deterministic receipt, original/new hashes, source/action/privilege/seal and automatic queue reviews. Those gates cannot be satisfied by the focused diagnostic.

Limits unchanged: 1625784320-byte admission floor, 2GiB1CPU lease, absolute900s compiler window and existing process-group cancellation/settlement owner. No live mutation, services, credentials or provider calls. Ordered595 handoff remains job608-to595.md; fresh post-restart genuine owner binding AND accepted-run acknowledgements mandatory.575/588 by reference,553 sole SAME510 owner.
