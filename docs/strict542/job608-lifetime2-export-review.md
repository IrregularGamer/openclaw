# Job608 native608 lifetime-stage export 2: independent review (2026-10-26)

Verdict: **APPROVE** (diagnostic run only). This is NOT compiler, package or
application acceptance. A lifetime receipt grants no addon, lib-test or install authority.

## 1. Source (33335af7 vs 74d93ffa)
- The only executable change is `build-native608.py` (+3/-2). The old-retention mutation now
  replaces `drop(value.take());` and `drop(self.values[index].take());` with `/* ... */`
  instead of `// ...`. Under `//`, the one-line `if !*required { drop(value.take()); }` (helper
  line 10) lost its `}` (28 `{` vs 27 `}`). That matches the first run's "unclosed delimiter" rc=1
  (job608-native-lifetime-offload.txt). With the block comments the count is 28/28, with () 106/106 and [] 43/43.
- The 3 replaced statements (lines 10, 24, 35) are all in non-test code. Test bodies, expected
  values and assertions are untouched, and the required FAILED names
  (`unused_is_released_before_first_render`, `repeated_module_..._before_next_module`) still fail
  under retention by inspection. The `extra_read` and `missing_ast` should_panic tests are unaffected.
  The unused `value` binding only triggers a warning: there is no deny/-D warnings.
- New test `RetentionNegativeControl` execs the build script's exact replace expression on the real
  helper. It asserts the mutation changed the helper, removed every `take());` drop and kept the delimiters balanced. It is
  meaningful: run against the old `//` mutation it reports {} 28 vs 27, so it would be RED.
- `python3 -m unittest -v docs/strict542/test_native_finalizer608.py`: 3 tests OK.

## 2. Export (/home/deploy/agentq/tmp/export608-native-lifetime2), recomputed sha256
- successor598.tar          495c6c70f1ead4a86b29b7ac6abfef5da6490035ff19f8dba032a6fb95ba649a (= manifest)
- run608.sh                 2c6e313a9aa7dddfbbdfe36986325bed7f46346d6e05822d4c032ca344290e57
  (= manifest; byte-equal to `git show 33335af7:docs/strict542/run-native608-stage.sh`)
- rolldown608-source.tar.gz 203aa4834d7a52522c758c81f6e493bea9fea828d4454fe2a25b9519d2d258ac
  (= manifest = rolldown-source-pin608.json source_archive_sha256)
- source_commit = 33335af79e38272dd2ef6d377407b5749f73d9e0. The 145 successor_paths are identical
  to the first export's. The only manifest diffs are source_commit and successor sha. `git archive --format=tar
  33335af7 <paths>` reproduces the tar sha exactly. No .env/key/pem/db/credential members
  in either archive. The export is fresh: there is no result-*, source or .native608 dir.

## 3. Command
`offload run --artifacts result-native608-lifetime -- timeout -k 15s 1500s sh run608.sh lifetime`
(default 2g/1CPU) is unchanged and finite. Run it once. Accept only rc0 with receipt
`complete: true` and `retention_negative_detected: true`. On refusal or timeout, record the outcome
and do not rerun in this export.
