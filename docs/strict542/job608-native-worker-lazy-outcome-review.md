# Independent combined native diagnostic outcome review608 — 2026-10-26

Accept the retained evidence as an incomplete FAILED diagnostic, not a passing
recipe, full typed package, admission promotion or application approval. The
actual source is `4ec0fa03d94d58e66630abe421670a9b64eeb0ca`, manifest
`22ac7df240fe89917b94686628bacbd02988d7ccfba337b7ae13cacec6a8a0c8`.
This review is independent of that diagnostic implementation/execution; later
selector-prerequisite source changes were not inputs to this run.

All eight copied result files below were compared byte-for-byte with the
recovered owned-slot `result598`; all nine evidence hashes were independently
recomputed. The broker copy also equals its unique original line in the retained
offload runs log:2026-10-26T16:39:09Z, remote rc1,2313s, exact native-worker-lazy
export. The recovered exit-code file contains1. The source/export identities
match the actual export manifest. No archive, compiler or diagnostic was rerun.

Exact files under `docs/strict542/`, prefixed `job608-native-worker-lazy-`:

| Suffix | SHA-256 |
| --- | --- |
| outcome.json | `ace3402eb7d5c8eec35a9e7d14ca4ecc0e41a526a7bbf1f960f8c5ccbea5f9c5` |
| broker.txt | `a858d245a23163d298ea753c662bd1b7613294247bff66a99e4bebe2bd109c99` |
| checks.json | `c5d2e13be0a6321a7280ad63d59f754ae7e81990eaf72fe22e609a64b38028cb` |
| tests.txt | `4d605b38125ed48ad96af1f0bf1da67cc5f53e5a72d04dffceef8417c3950c2b` |
| probe.txt | `ed7f84a715a4e647b4b50d7d015c3bb2ebe60cf2e768ef9f07eef849dfa398e8` |
| receipt.json | `936241691a52dbf73b53113e4159205597ec988cee08a3cfaf2f5808c12f1a01` |
| native-compile.txt | `bd0fb19319953fc655f9a5decf9a21960cbc933f78f1083abed425e2d4e78612` |
| native-receipt.json | `e210de64481feece6ae64ee192c0e14626cc112f2ef4c47c7fac526f7fc7faad` |
| parity.json | `3b01c8102d22f14548a1662efb4bb330b236f811cb36fca141f1e6fe4a486df0` |
| retention-negative.txt | `7635d542be80ec9763b56e1b02614c970dc4d1370c07c3b9218dc1b6f8731aa8` |

The recovered native compile receipt equals the original committed compile
receipt byte-for-byte, SHA256e210de64 above. Its four owner-source hashes match
their source bytes; the diagnostic's embedded native receipt equals that file.
The actual recovered24295760-byte addon hashes to
`f8b7634b1ccf713ec593f2a802373e16bffc92f1a63edd82704232c4960adcc6`,
matching the pinned receipt and parity evidence. The negative-retention fixture
records its intended two assertion failures. It is not a failed production
compiler test being hidden or reclassified.

The logs establish215 passing scoped checks (101+29 Node and85 Python), all3
typed-inventory tests, and9 real parity/lazy/minifier fixture tests:227 total.
The real parity test passed all8 ESM/CJS × maps × minification variants with
stock/patched byte equality. Both stock and native lazy/minifier fixture modes
passed. These passing checks do not make the subsequent compiler run complete.

The57-config census is retained. Results are exactly AI followed by main0..46:
AI and0..45 succeeded without reported scanner/error/timeout flags (47 successful
results). Config15 completed in184200.772444ms and has a closed record. Worker46
bundle ran99435.152952ms, reached build-end, then returned status null,
signal SIGKILL, timedOut false, error null and no reported import/scanner failure.
Its failed bundle prevented minifier admission under the unchanged phase owner;
no worker46 minifier ran, and main47..56 were not executed. The final child
record says parentSignal null, cleanup none, observedProcessState dead,
observationScope process-group. This records settlement, not compiler success.

Worker46's build-end sample records RSS1852047360 bytes and V8 heapUsed47288920;
later samples show RSS2003116032 then2010324992 while heapUsed is about15.7MB.
The final sampled cgroup charge is2145857536 bytes. This supports investigating
memory outside the reported V8 heap, including native compiler lifetime, but
does not identify a retaining object, exact post-build-end operation or killer.
The sampled oom/oom_kill counters remain zero. memory.peak2147864576 was already
present before worker46 (and before config15); it is cumulative and cannot be
presented as this worker's or diagnostic's measured peak.

This export is spent. No unchanged retry, floor reduction, resource increase,
bounded admission promotion or full-package run follows from these results.
The next gate is a concrete owning source correction with independent review
and a separately reviewed fresh source-only validation plan. A complete
accepted combined diagnostic must precede native bounded-package wiring; the
real complete typed build/frozen package and exact artifact, action, privilege,
seal and automatic queue reviews still remain. This reviewer performed only
bounded evidence/source reads and wrote this review; no offload, install,
service, config, provider, root or live application operation occurred.
