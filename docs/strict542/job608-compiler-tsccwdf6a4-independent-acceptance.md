# Job 608 compiler tsccwdf6a4: independent acceptance

Independent review dated 2026-10-29. Reviewed actual compiler evidence `5212bbb0`
and exact phase-trace carrier correction `ad057e66`, following preflight `83709e90`
and launch `917f1206`. Actual unified-0 acceptance `ffc14e61` and preflight `83709e90`
are both Git ancestors of the launch. P denotes
`/srv/encrypted/dev-move-98/agentq-source608-20261028-private`.

VERDICT: ACCEPT compiler tsccwdf6a4 at f6a4de2e. No findings.
595 MUST NOT APPLY.

## Exact returned evidence and receipt

- Private sibling `compiler-tsccwdf6a4-offload.rc`, committed `compiler-offload.rc`,
  and actual result `exit-code.txt` all contain 0. The deterministic gzip outer-log
  carrier decompresses byte-for-byte to the private original, ending with
  `STEP608 compiler-checks-pass`. No real failure, timeout, OOM, kill or signal
  failure line is present. The only warning-related text is the package-manager
  preinstall-warning script name.
- Actual result is exactly the six files named in `result-files.sha256`; every
  raw SHA256 matches. All five direct committed result copies are byte-identical
  to their private originals. The deterministic gzip phase-trace carrier
  decompresses byte-for-byte to the sixth original, preserving its trailing
  blank line. Both gzip carriers have fixed zero mtime. The raw result totals
  26748 bytes.
- Receipt SHA256:
  `e5b96beb97e88aee7465bd95322f8f187896f1b270455fe317b196c3918251c1`.
  Kind `JOB608_STAGE_RECEIPT`, stage compiler, exit_code 0, run_id
  `stage608-compiler-tsccwdf6a4`. Its manifest binding equals actual manifest SHA256
  `39dbe8f21e6e6e5cb7d250900607fb88b7ddaf96192461a6fe15db62df6bf3e8`.
  Source and runner remain `f6a4de2ebc6924d16fe559f9858bf8c50dce1eba`; common export
  is `e81e07d2770ad597bb11de77e1dbf899d5f5286b8d3d52e8c5616faa74458145`.
- Receipt stage_inputs exactly equal the manifest's four pins. Fresh streaming
  hashes of actual staged inputs and corresponding accepted native `57742314`
  files match: addon `0b6607e7...e042`, compile receipt `4a651254...ed9e`, libtests
  receipt `2f81179f...d946`, and producing stage receipt `10474857...6d3`.
- Receipt outputs exactly bind `compiler/tests.log` to
  `c83027888cc1664d2f1b529adf50660cad143f8725ac86d0efe11ca24cc8af24`;
  actual log bytes match. Returned `strict542-checks/tests.log` is the same log.
  Supplemental parity and phase files are included in the exact six-file inventory.
- Fresh `storage608.py result --result P/stage-compiler-tsccwdf6a4/result608-compiler
  --stage compiler` exits 0: 26748 logical bytes <16777216-byte return cap.

## Complete actual compiler membership

Actual runner bytes match the manifest pin and frozen f6a4 Git source. The complete
compiler log has five ordered Node summaries, each reporting tests2/pass2/fail0/
cancelled0/skipped0/todo0. All ten successful testcase records match the exact
ordered pairs declared in the frozen source, with six unique names across the
five invocations. The frozen runner establishes these modes and order:

1. Stock worker-minify: `real split worker retains side effects, names, dynamic
   imports, maps and legal text`; `real minifier rejects parse failure and
   redirected output without replacing bytes`.
2. Native-codegen: `native last-use codegen is byte-equal to stock for shared
   graphs, ESM/CJS, maps and minification`; `release native addon emits existing
   link and generation phase spans to stdout`.
3. Stock lazy-barrel: `owning config enables lazy barrels only for the complete
   shared runtime graph`; `lazy barrels preserve side effects, live singleton
   identity and dynamic exports`.
4. Native lazy-barrel: the same two lazy-barrel cases, with
   `NAPI_RS_NATIVE_LIBRARY_PATH` resolved through the required native compiler owner.
5. Native worker-minify: the same two worker/minifier cases with that native path.

Inspection of the exact frozen test bodies confirms that success includes real
worker execution, retained function/class names, side effects, dynamic imports,
source-map lookups and legal text; refusal of syntax-error and redirected output
without replacing bytes; stock/native byte equality; and lazy-barrel singleton,
side-effect, dynamic-export and dead-code semantics. No testcase or invocation
was substituted by a summary count. Installed-check metadata `required_checks14`
is not compiler membership and is not used as proof here.

## Retained native evidence

`stock-patched-equality.json` hashes to
`56682414120f0dd5b29f15aef8feb24143a2619f888b92a33987f40487d24418` and binds the
accepted native addon. It contains all eight combinations of ES/CJS, maps on/off,
and minify on/off, with 44 complete output records: four per no-map variant and
seven per map variant. Names are unique within each variant, output kinds and
SHA256 shapes are valid. The passing frozen test asserts deep equality of the
actual stock and patched result arrays before writing this evidence.

Raw phase trace hashes to
`b08a22d8c31b97828ec87bbf077adc3d58b8d78e2692808aaeeeb4c317fdc1db`.
It includes native `rolldown::stages::link_stage` and
`rolldown::stages::generate_stage`, 30 enter and 25 close records, and no disabled
tracing message. The passing test verifies child exit0/no signal and the required
spans before retaining stdout. This proves the fixture's selected native span
output; it does not claim config15 phase attribution or a later package result.

## Scope and limits

This actual compiler attempt is SPENT and must not replay. Immutable manifest
UNUSED text remains prelaunch metadata. This accepts the compiler result only;
remaining unified1..5/middle/sdk/tail/package and final artifact/action/privilege/
installed-target/whole-seal/automatic-review/HQ595 gates remain open. It grants
no application, installation, sealing or deployment authority.

Review ran only read-only evidence/hash/storage checks. No heavy test/build,
offload, live provider, installed/root/service/queue state change was made. Only
this requested review document and its Git publication change.

595 MUST NOT APPLY.
