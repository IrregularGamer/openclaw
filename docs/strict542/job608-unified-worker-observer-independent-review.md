# Independent review: worker-owned diagnostic observer608

Verdict: APPROVE CORRECTED DIAGNOSTIC OBSERVER ONLY, exact source commit
06d042e2fa178ada7d487777edebc7f61a32ed3c and diagnose-unified608.py SHA256
e9054f13c3b94e0813c825d3318e3da5e14beb40a37947be0cfd7ae6b22d7aa8.
Reviewer: separately delegated independent Rook source-analysis lane.
This supersedes the observer implementation portion of the857ca783 diagnostic
review; that earlier review and first run remain historical evidence. It grants
no source application, package, install, restart, release or final-review authority.
The current diagnostic was neither changed nor relaunched by this reviewer.

The correction addresses an observed diagnostic limitation: the original observer
runs its flush timer on the same Node main thread as synchronous source work.
The builder reports sustained main-thread CPU with no profile flush. A tiny
fixture using the exact857ca783 PROFILER, changing only its interval60000 to50ms,
confirmed zero profile files before yielding after350ms of synchronous main work.
Absence of its profiles therefore establishes neither native compilation nor a
native transport deadlock. The existing admitted run must finish and its actual
files be inspected before any further execution is selected.

The corrected external preload leaves the source checkout and its native owner
checks pristine. It starts a Worker with execArgv:[], connects that inspector
session to the main thread, waits for readiness and unreferences the Worker.
The Worker independently flushes main-thread CPU profiles every60seconds. Its
parentPort listener keeps initial inspector commands alive. The main beforeExit
handler references the Worker for a final stop; the serialized promise chain
orders interval capture and shutdown. Setting stopping before queueing the final
capture prevents queued interval work from restarting the profiler. Errors close
the session/port and set the parent diagnostic exit status to failure.

Tiny independent fixtures ran only under /var/tmp, with no dependencies, compiler,
installation, source mutation or admitted-run changes:

- Exact current PROFILER/PROFILE_WORKER, changing only fixture interval60000 to50ms:
  six valid main-thread profiles existed before yielding after350ms synchronous
  main work. RSS was77381632bytes. Normal parent and observed child shutdown
  completed successfully;39 profiles from3 genuine Node process IDs parsed.
- Real Node array/options-only/null/undefined spawn overloads passed. Synthetic
  environment/argv and original options objects remained unchanged. Nullish args
  preserved third options and their expected synthetic-cwd ENOENT refusal.
  A real non-Node /bin/sh child retained argv/options and synthetic output.
- Replacing the fixture profile directory with a regular file forced ENOTDIR.
  The Worker reported DIAGNOSTIC_PROFILE_ERROR608; the parent exited1 without
  hanging. No fixture changed worker/source behavior to suppress that error.
- Mocked outer execution generated the external worker artifact and shell
  adapters. Executing only their PRISTINE generation block preserved every
  inventoried fixture source byte. All three generated adapters passed sh -n;
  archive-build and stage-receipt invocations remained absent.
- Python AST parse and git diff --check passed. The production60second cadence
  was inspected; tests accelerated only the disposable fixture timer.

The existing fixed source5f/stage/runner pins, original package/input/native
admission, predecessor validation, genuine artifact ownership and cancellation/
settlement entry points remain. The4GiB/1CPU/swap0 and1080/1020/600second outer/
inner plan is unchanged; observer threads remain inside that same admitted
budget. This amendment is a reviewed response to timer starvation, not evidence
of a product fix or authority for an unchanged long retry. Every subsequent
export must pin this exact diagnostic and record its own actual outcome. No
instrumented output can become an accepted checkpoint/package receipt; the
original source/action/privilege/seal/automatic-queue/HQ gates remain outstanding.
