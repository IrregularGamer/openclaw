# Job608 native cmake-pinned admitted run: compile timeout, no measurement

Export `export608-native-cmake` (source 70dfe45e, successor 6e946be5…, runner
34b7c4a1…, manifest 763cd0dd…, independently approved in cc4b8fb6) ran once
through normal offload at default 2GiB/1CPU, 2026-10-26T06:30:51Z to 07:14:14Z,
rc=124. Raw tail: job608-native-cmake-offload.txt (full log runs/608/native-cmake-offload.log).

- Archive digests verified remotely; all pre-build policy checks shown passed (18/18 in tail).
- The cmake pin worked: libmimalloc-sys2 and the dependency graph compiled
  (no cmake error). The build reached `Compiling rolldown v1.2.9`; `rolldown_binding`
  did not start linking.
- The runner's own `timeout -k 15s 2400s` around build-native608.py fired (rc=124).
  No memory refusal or OOM appeared. Result artifacts are not returned on failure.
- No bundler, parity, lazy-barrel, config15 or memory result exists. This is a
  CPU-time limit of a from-source release compile on 1 CPU, not a source assertion.

Not authorized by this outcome: unchanged retry, larger CPU/RAM budget, a longer
timeout without review, a lower opt-level/LTO change without review, or local heavy build.

Next (needs its own source change + independent review): split the native compile
into its own admitted offload stage whose only output is the compiled addon plus a
receipt (rustc/cmake/source/compiler-archive digests and addon sha256), returned as
an artifact and pinned; then a second admitted stage consumes that pinned addon for
the lifetime/parity/lazy-barrel/config15 checks within the existing 2400s window.
