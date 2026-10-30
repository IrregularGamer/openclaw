# job608 package 301d — ONE launch, rc 1 (identity mismatch), 595 MUST NOT APPLY

Launch: preflight 77350895, independent APPROVE 1fe9cdbc, fresh gates OK, ~05:33Z, 14g/4CPU/2460s, cwd P/stage-package-301d
(manifest 025654bd, lineage ancestor 674840b6). rc 1 after pnpm install (~60s); no result608-package returned.
Log: package-offload.log.gz. Failing line:
`Error: checkpoint source/native/toolchain identity mismatch` at validateBuildReceipt608
(scripts/lib/bounded-build-checkpoint608.mjs:72) <- validateBuildChain608 <- prepareBuildCheckpoint608 (build-all.mts:605).

## Diagnosis (source analysis, no rerun)
- Gateway checkpoint identity = {sourceCommit, sourceExportSha256, toolchain} (scripts/build-checkpoint608.mts:27),
  taken from STRICT542_SOURCE_COMMIT/STRICT542_SOURCE_EXPORT_SHA256, which run-package608.sh:120 sets from the
  package manifest (301d7456 / 301d export). The restored tail-m674 checkpoint (and its whole chain native..tail)
  carries identity 674840b6 / e1a6de35. validateBuildReceipt608 requires exact equality -> refusal. Correct refusal.
- Option B (301d7456, APPROVE 7beaf342) admits lineage only at the outer stage608 input binding; the inner gateway
  checkpoint identity remains exact-commit. That is by design and must NOT be relaxed: feeding the ancestor identity
  to a 301d tree, or accepting lineage inside validateBuildReceipt608, would forge/weaken source identity.

## Decision for continuation (no S question needed: it keeps every existing check)
Rebuild the identity-bound chain at ONE exact commit (current reviewed HEAD of docs/strict542 tooling, >= 301d7456),
same-commit binding, no --lineage-ancestor: native, compiler, sdk-0, sdk-1, unified-0..5, runtime, middle, tail,
(checks 301d already at 301d7456 and accepted: reuse only if the chosen commit is exactly 301d7456), then package.
Use 301d7456 as the chain commit so checks-301d (ACCEPT 788c76fc) is reusable; m674 caps/launch argv per stage
unchanged; one launch per stage with its own preflight + independent review + acceptance; fit each --timeout to
`offload deadline`. Storage: delete only own spent m674 stages after pinning manifests (as done here); never lower
the reserve. Option B lineage code stays (harmless, reviewed) but is not used for package.
