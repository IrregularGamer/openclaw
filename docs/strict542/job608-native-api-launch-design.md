# Finite native API phase diagnostic, source only

This external launcher observes the unchanged reviewed source
`1bed4d1bb53eff145f724cc6a448dc73b3609015`, common export
`5d7e9d57fb660e2b54f5595e81ddf332027e21b303937c2cd6bc7f718f311263`.
The native and runtime inputs remain the exact accepted inputs verified by
the pinned original runner/helper. This is one diagnostic, not a rebuild retry,
checkpoint acceptance, package receipt, or application authorization.

Prepare a NEW committed secretless export using the reviewed stage preparer,
then copy the committed `diagnose-native-api608.py`,
`native-api-phases608.mjs`, and `install-native-api-phases608.mjs` to its root.
Record and independently review the exact export/pins before admission.
Run only through admitted offload, with explicit `--timeout 1740`, artifacts
`native-api608`, one CPU, zero swap, and the already justified 4 GiB cap.
Do not launch unless 1740 seconds plus the mandated settlement allowance fit.
The fixed remote entry is `python3 diagnose-native-api608.py`; no command,
stage, budget, environment, or binary override is supported by the launcher.

The launcher verifies source/common/runner/helper/observer pins. It writes
external copies only. The runner still validates all inputs and restores the
accepted native/runtime inputs. The build shell still performs its frozen
install and both preflights. Immediately before the original owned checkpoint
entry it runs the real installed async API preload (30 seconds), so native
prototype/import refusal stops the probe. It then runs that same owned entry
once, adding the reviewed observer preload, bounded to 900 seconds. All owner
predicates, memory admission, build identity, cancellation and settlement remain
unchanged. The external runner suppresses archive-build and receipt operations.
No inventoried source bytes are changed and no checkpoint can be accepted.

The full setup/probe tree has an additional 1500-second timeout and 15-second
kill grace. SIGTERM/SIGINT are forwarded to the process group, boundedly waited
for, and reported as cancellation. Live process-group members are checked after
the timeout leader exits; remaining members receive KILL and a five-second
live-process settlement check (zombies cannot execute). Escaped process groups
remain subject to the unchanged offload container lifecycle. Process grouping does not change cgroups or
budgets. The original runner cleanup and logs are retained when available;
the external collector always retains its runner log and actual inner exit.
An inner exit 124 has collection exit zero solely to retrieve diagnostic
artifacts; its actual 124 remains in `diagnostic.json` and `exit-code.txt`.
Other failures and cancellation remain failures. No live auth, provider calls,
root/unit/sudoers/service changes, runtime install, or release authority follow.

Focused validation: `python3 -m unittest discover -s docs/strict542 -p
test_diagnose_native_api608.py -v`. Installed preload acceptance and actual
phase observations require the admitted diagnostic and must not be inferred
from these local synthetic process tests. Review actual output before choosing
any source correction or bounded compiler split. Job595 must not apply.
