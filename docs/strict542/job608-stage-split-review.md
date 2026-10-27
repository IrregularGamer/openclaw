VERDICT: APPROVE

Independent review of 6648474b ("INC-261027-18 finite stage split") against parent 37d44c9b.
Reviewer did not author the change. Local checks only: `python3 -I -m unittest` of
docs/strict542/test_stage608.py passed (8 tests), `sh -n run-stage608.sh` passed, and the
command blocks were diffed line by line against run-package608.sh.

## 1. Check/deadline coverage (each command in exactly one stage, unchanged)
- VERIFY_ARCHIVES (4 archive digests + native_stage_outputs exact set) and ORDINARY_ENV: byte-identical, run in every stage (they are guards, not checks).
- Scoped node/python test block (orig L58-69): identical, `checks` only.
- Installed vitest tooling checks (orig L77, 1 worker, no file parallelism, json output): identical, `checks` only.
- 2400s native rebuild `timeout -k 15s 2400s prepare-native-consumer608.py` (orig L84): identical, `native` only.
- Compiler checks block (orig L91-96, incl. NAPI_RS_NATIVE_LIBRARY_PATH runs): identical, `compiler` only.
- CHECK_EVIDENCE heredoc: body identical (indentation of the opening line only), `package` only.
- BUILDER_IDENTITIES, pnpm physical/version checks, and `env -i ... sh docs/strict542/build598.sh`: identical, `package` only.
No check, deadline, worker or concurrency flag was dropped or altered.

## 2. Deliberate deviations
(a) Acceptable. Package stage omits the outer `pnpm install --frozen-lockfile`. build598.sh L19 does its own frozen install
    inside the clean env, followed by its own guarded releaseDisposableStore. frozen-package608.py preflight only checks env
    and PINS digests, so it does not need node_modules. The resolved pnpm path is still re-verified as 12.5.1.
(b) Acceptable. Compiler stage frozen install + releaseDisposableStore puts it in the same state the single run had
    before its compiler block (node_modules installed, store released, .native608 present).
(c) Acceptable. prepare-native-consumer608.py / build-native608.py use only python, rustc/cargo and pinned downloads.
    There is no node/pnpm/node_modules dependency. The rebuild still refuses CARGO_/RUST/NAPI_RS_ env and an existing .native608.
(d) Acceptable. stage608.py verify_inputs checks the staged compile receipt against the independently pinned
    native_stage_outputs['compile/receipt.json'], libtests against its pin, and the addon against
    compile receipt addon_sha256. These are the same identities prepare-native-consumer608.py enforces and nativeCompiler608 /
    build598 BUILD_EVIDENCE re-read from ../.native608. stage_native reproduces exactly the 3-file .native608 the rebuild writes.
(e) Acceptable. The single run wrote scoped output, appended installed.log, then appended the compiler block; nothing else
    went to tests.log in between, and native-rebuild.log is separate. checks tests.log + compiler tests.log (compiler stage writes it fresh with `>`)
    is the same sequence. evidence.json hashes the merged file, so build598's `sha(test)==proof['test_log_sha256']` holds.

## 3. stage608.py refusal logic
Sound. The stage comes only from manifest `stage` in a fixed set. Both the pinned set and the on-disk set (files and symlinks) must
equal exactly {required receipts + required outputs}. Every pinned file must be a non-symlink regular file with a matching digest.
Each producing receipt must have kind JOB608_STAGE_RECEIPT, the matching stage, exit_code 0, the same source_commit, and outputs equal to the pins.
The native pins are checked as described in (d). The CLI accepts only fixed subcommands, and the shell `case` has fixed branches. merge-logs/receipt
take only a path from the script itself. No caller-chosen command path exists. A receipt is written only after `set -e` success.

## 4. Fit within 40 min (findings are non-blocking)
- checks, compiler and package each hold a subset of the remaining ~53 min minus the rebuild, plus one frozen install. They plausibly fit.
- Native: the inner deadline (2400s + 15s kill) is not shorter than the 40 min admission, and archive hashing,
  extraction and release come before it. A rebuild that nears its cap is therefore killed by the outer offload first, which returns no
  artifacts and no tail, instead of the reviewed 2400s timeout. The required "deadline unchanged" rule forbids lowering 2400s, so this is
  accepted. Operators should treat an outer kill of the native stage as "rebuild exceeded budget", not as a new failure class. If the observed
  rebuild runs in the high 30s of minutes, the split does not reliably fit and S/Pinch needs a decision.

## Minor notes (no change required)
- The single run's `rm -rf ../native608-stages` after the rebuild was dropped. No later consumer reads native608-stages
  (grep), and the cleanup trap never removed it either, so this has no effect on checks.
- stage608-inputs/ (including the staged addon) and native608-stages/ are left at the export root after the run. The cleanup trap does
  not remove them, unlike .pnpm-store/.native608. This is harmless for result artifacts, but should be noted if export roots are ever reused.
- result598-native/ now appears in result608-native, not result608-package. No in-repo consumer depends on the old location.
- The package stage receipt pins no outputs (OUTPUTS has no 'package' entry). It is terminal, and its evidence is in result598-build/evidence.json.
- Producing-receipt checks do not compare run_id/manifest_sha256. Trust rests on the manifest stage_inputs pins, which is sufficient.
