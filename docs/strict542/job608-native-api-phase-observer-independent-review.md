# Independent exact native API observer review608

Verdict: CHANGES for source4a52e82814b0bd197cf8b5bbeae986e82d119740.
This is an external, UNLAUNCHED diagnostic observer review only. Candidate95
executable freeze is unchanged. No diagnostic launcher/export is prepared or
approved by this review, and595 MUST NOT APPLY.

Two focused corrections are required before approving the stated forwarding
contract:

1. In native-api-phases608.mjs, start `now`/`emit` run before the forwarding try,
   and end `now`/`emit` run in its finally without isolation. A synchronous sink
   or clock failure can prevent the original API call entirely or replace its
   result/original rejection. I independently reproduced both with tiny class
   fixtures: a throwing start sink left original-called=false; a throwing end
   sink replaced the exact original compiler Error with the sink Error. Isolate
   observer timing/logging failures so original dispatch and settlement remain
   intact, and add start/end failure regressions. This is not an actual compiler
   failure and must never be interpreted as such in future diagnostics.
2. `argv.includes(observer)` does not establish that Node preloads the observer.
   I independently reproduced `node app.mjs /observer.mjs` suppressing --import
   merely because the observer path is an application argument. Detect actual
   Node preload option syntax before the application/-- boundary; preserve
   original application arguments and options. Add an application-argument
   collision regression alongside real preload duplicate avoidance.

I independently ran the seven committed focused tests on exact4a52e828 working
bytes:7 passed,0 failed/skipped,195.394663ms under Node24.21.0. These verify
private receiver/arguments, awaited values, original rejection, pending and
concurrent calls, preflight method-shape refusal before patching, duplicate
installation refusal, spawn options/receiver/result/error forwarding and the
currently covered preload form. They did not cover the failures above.
`node --check` passed for observer and preload. No actual installed API preload,
native transport, offload, compiler or build was invoked.

The raw RED log compressed SHA256 is
76fcb97bfc842a2391e61a1a16f42c8009da8815514024454978c2aa7f2fa71e;
it contains expected module-not-found before the helper existed. The GREEN log
compressed SHA256 is
efac9c7aa79b3e3364b814635112de888df3abecb09686455c7ce92bbca2de32;
it contains seven passing focused cases. I independently decompressed/read both;
the RED log is an absent-module baseline, not a targeted red test of all
forwarding behaviors or actual API loading.

I verified the captured primary source references under
`/home/deploy/agentq/runs/608/unified0-owned-diag`. All four documented hashes
match: async API c22d23de, async client ae0813c4, options.js6459db5d and
options.d.ts851f6431. The actual async API source directly exports API and
Program, and all11 observed methods are async class prototype methods: API
parseConfigFile/createSnapshot/close and Program's six diagnostic queries,
emitToString and getSourceFileNames. Their class-method form supports the
writable value descriptors checked before patching. The captured package is
TypeScript7.1.0-dev.20260920.1 and exports unstable/async as
./dist/api/async/api.js.

Preload resolution uses createRequire at physical cwd/package.json, resolves
the captured async package export, rejects lexical and realpath escapes, then
imports that file URL. The source emitter imports the same package specifier
from inside that checkout, so standard Node package resolution supports the
intended module identity. This is static resolution evidence, not an actual
installed preload smoke test. Such an admitted integration smoke remains
required before interpreting future phase logs, including confirmation that
the observed methods are the ones used by the owned emitter process.

Outside the two findings, source inspection confirms Reflect.apply preserves
the API receiver/arguments; no API options/results, filesystem membership,
diagnostics or inventoried source are directly changed. Log fields contain
method/phase/status/timing/PID rather than arguments/native data. Node child
propagation patches spawn, synchronizes builtin ESM exports, passes the same
options object and restricts injection to exact process.execPath; native Go
children are not injected. Async wrapping still changes scheduling and no
observer output may supply build/checkpoint or source acceptance.

The documentation requires a separately reviewed NEW external launcher/export,
source-pristine installation, no stage/checkpoint receipt publication, explicit
inner/outer status separation, finite admitted deadlines and cancellation/
settlement evidence. It preserves full owner/input/diagnostic/publication gates
and does not implement or authorize a native diagnostic split/checkpoint.
The existing1bed diagnostic cannot accept changed candidate95; its actual
outcome must be independently reviewed separately. All final source/artifact/
action/privilege/seal/automatic-queue/HQ and post-restart genuine owner plus
accepted-run acknowledgement gates remain. No launch or application authority
is granted by this review.
