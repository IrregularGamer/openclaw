# Independent actual candidate95 focused composition outcome608

Verdict: APPROVE ACTUAL FOCUSED COMPOSITION EVIDENCE ONLY at evidence commit
47736353a8d671798ec20e05f63f2fd00f13ee34. Executed source is frozen
95e62f8b6c7af341b2dfc21163627aa8a533649d. Preflightca447412 and conditional
prelaunch review80e7c4cf remain the source/command boundary. This review does
not establish actual native compilation, snapshot sealing, full required checks,
package/build completion, timeout resolution, speedup or application authority.
595 MUST NOT APPLY.

I independently compared the committed outcome, source-manifest and compressed
raw logs with actual retained files in
`/home/deploy/agentq/tmp/export608-admission95-focused.n_rr23g0` and
`/home/deploy/agentq/runs/608/admission95-focused-offload.{log,rc}`.
The source manifest SHA256 is
62f8ce637fce562f34d4c3de1bcd314976b80a2b0a6d8f7851952dfd131fc5bd;
its exact bytes match the export's focused-source-manifest.json. Its fields
equal the committed preflight with only command/launch_gate omitted. All five
source file pins agree among manifest, preflight and outcome, and every actual
exported file is byte-identical to its exact95 git blob:

* native-admission608.fixture.mjs: e1c4200c64ebd527c2f543978f0d55bf4d62d779dd9130de4ad417dc0ac737e4.
* native-admission608.test.mjs: 4fad11c1c7783b599152a3b837d1db736c1e78e9e4d37191838bfe18e8742c10.
* local-check-runtime.mts: 0677859daa8187b8a5b6a1653a6ba559539f9111d85f440e6716dc4582bcc1e5.
* native-declaration-emitter.mts: 2f8a05d0b713daf4d60d4e0359efe677b8f2710b05b1fd594e401adf1a3a2431.
* native-declaration-filesystem.mts: b45a6a8d34945f612a1edbb7dc755bd77efb91e5f87aea5ef455745abb6cdacf.

The five source files total35,759bytes. The current export has exactly these
five files, its one metadata file and the two expected returned result files;
there are no symlinks or extra regular files. The archive hash0a1f4dbf is a
retained preflight/manifest identity, not a newly rehashed archive in this review;
actual extracted source-byte equivalence was independently verified instead.

Both committed gzip logs decompress to their actual retained raw files and
match the entire outcome size/hash inventory. offload.log and tests.log are
identical1,207byte TAP streams, SHA256
1845d81d0871e56e91cfde54b1418c1a0b2bdcbe71ccdb6138f9e89df4d984da.
Actual offload.rc and result608-admission/exit-code.txt are both exact bytes
`0\n`, SHA256
9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa.
Thus actual client and returned inner result statuses are both0; these are
separate verified files, not an inference from a successful transport alone.

I parsed and reconciled all numbered TAP results with the frozen test source.
The plan is1..7 with exactly seven successful cases in order: lookups,
identity-escape, policy, retarget, missing-retarget, pinned-read and
lexical-outside. Final totals are7tests/7pass/0fail/0cancelled/0skipped/0todo;
no not-ok, SKIP or TODO result appears. Reported total duration is3008.528857ms,
not a compiler or full-build timing measurement. Every retained_raw_pins entry
matches its committed raw/decompressed bytes, including the source manifest.

The fixture invokes the REAL candidate95 emitter/filesystem/checkout boundary,
while tiny API/compiler, diagnostics, toolchain and snapshot/seal doubles isolate
composition. These results support repeated per-callback policy, identity-policy
containment, custom denial, symlink/negative-lookup retarget checks, supplied
pinned-read wiring, virtual-config membership and lexical outside-path refusal.
They do not test the real native transport, semantic graph/diagnostics, actual
snapshot identity/seal correctness, native emission or the historical long query.
The actual compiler/snapshot/tsdown suites and complete candidate stage/package
evidence remain required under the existing admitted owner and budgets.

No tests, compiler, build, offload or runtime mutation was rerun for this review;
verification was bounded source/evidence reads and deterministic comparison.
No change-request findings. All final source/artifact/action/privilege/seal/
actual automatic queue/HQ and fresh post-restart genuine owner plus accepted-run
acknowledgement gates remain. Neither this evidence nor the separate1bed
diagnostic supplies candidate95 build acceptance or permission for595 to apply.
