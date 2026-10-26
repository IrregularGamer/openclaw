# Independent worker lazy-barrel evidence/source/export review608 — 2026-10-26

**Verdict: APPROVE ONE changed-source focused diagnostic of exact source `4ec4bde8610a69cc81e843a9062bdf1658165f7c` from fresh `/home/deploy/agentq/tmp/export608-worker-phases-b`, subject to normal controller/lease admission and the foreground deadline below. This is source/input approval; fit and full package/application acceptance remain unproved.**

Approved command: `offload run --artifacts result608-workers -- timeout -k 15s 1500s sh run608.sh`, default 2 GiB/1 CPU, unchanged shared 900000 ms compiler deadline across all four workers and both phases. Before launch verify the foreground worker still expires at or after 2026-10-26 15:34:53 UTC and at least 27 minutes remain; launch by 15:07 UTC. Clock check during this review was 15:05:20 UTC. If that condition fails, this review does not authorize starting this run in the remaining worker lifetime. The narrowed 1500-second outer bound plus kill grace preserves settlement margin. All checks are fatal. Neither an unchanged retry nor a larger budget is approved.

## Accepted prior evidence

Independently recomputed the recovered a evidence hashes and compared tests, typed result and probe bytes to retained `/home/deploy/agentq/tmp/export608-worker-phases-a/result608-workers` originals:

| File suffix (`job608-worker-phases-a-`) | SHA-256 |
| --- | --- |
| `tests.txt` | `aaf2c676c40e1f0d3bd50ba597881af018d47b021f4b7212019ca85329b41466` |
| `vitest.json` | `21325a55f1fb14645b2ae20489310ba2e8338818f91db42f03cf6ee2853516a7` |
| `probe.json` | `1c54eca5d84df9c0c68df989206fbfea3ebc5eaf68b9365e87c982424056609b` |

The offload text is empty (SHA-256 `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`), so it is not independent execution proof. The recovered tests record 101 Node + 84 Python + 28 policy tests = 213 scoped/policy passes; typed JSON confirms all 3 tests passed; the real minifier fixture records 2 passes: 218 recorded passes total. Those fixtures establish the actual pinned minifier API/maps/names/legal/dynamic/parse/redirection behavior on the fixture.

The diagnostic probe at source38cd394a records only config46 worker/worker, one bundle phase, elapsed 163426.565316 ms, status null, SIGKILL, timedOut false. No minifier phase or later worker ran. Captured samples reached RSS2034434048 and cgroup2145935360, with no closed event. The retained tests log records process-group dead settlement. Accept overall refusal rc1; the broker metadata records 495 seconds, not a passing package. Pre-kill memory.events samples do not independently establish kernel OOM attribution. This falsifies minification overlap as the sole stock-build explanation and justifies diagnosing the bundle frontier. The spent a export cannot be retried unchanged.

## Source delta and gates

Compared owning change4ec4bde8 to its parent and reviewed existing split source. Only the four exact bounded/isolated portable-worker config copies receive `experimental.lazyBarrel: true`; ordinary configs and unminified sealed helpers retain identity. The wrapper invokes the original input-options factory with every argument, preserves its returned dependency/external/platform settings and merges all existing experimental values. No sideEffects/purity annotation, dependency externalization, entry removal, ownership predicate, output split, no-sidecar refusal, compression or name-preservation policy changes. Required minification remains a settled second child. Source claims fit only after the measured run.

The new regression checks factory argument/result preservation and experimental merge; fresh tiny local `node --test docs/strict542/worker-phases608.test.mjs` passed 5/5. The focused runner now requires the existing two real lazy-barrel tests (unannotated side effects, pure unused reexports, singleton identity and dynamic exports) before the two real minifier fixtures and complete four-worker diagnostic. It retains frozen dependencies, all 209 pre-existing scoped tests, now five new phase tests and three typed inventory tests: 221 required recorded tests total if successful. Existing process-group cancellation/settlement, fatal scanner checks, recomputed remaining deadline, fixed one-CPU pools and 1625784320-byte capacity floor are unchanged. No compiled native binding or compile-stage receipt is input; this is explicitly stock Rolldown1.2.9 focused evidence.

Source-only review of af5be03af7aed1384e1d438493702156523b3276 confirms the full native consumer now requires the phase tests and real split/minifier fixtures in stock and rebuilt-patched modes. NAPI_RS_NATIVE_LIBRARY_PATH passes through the fixture process and its minifier child for the patched mode. Existing native parity and lazy-barrel stock/patched checks remain fatal. No execution of that full consumer is approved or claimed here.

## Exact b input verification

| Identity | SHA-256 |
| --- | --- |
| Manifest | `3e9bce05245b5d373110fb3e71268f5b82751a77d930278a2c88bf3ec56739ac` |
| `run608.sh` | `093333b9f5c939b97eab91ae8de107be331cd117ef5120789a455ad12a2eab10` |
| `successor598.tar` | `2c2567f1b6aa2b917af9e16a30a39924f83d846e77067b789bf9aed0e4e0f99a` |
| Native source fixture archive | `d73e4e35720ffcb71856ce8168e75fa3b4fd49251fd78c811e1abded8b2701de` |
| Retained base archive pin | `e79a0e45a4eaea4afe325ca94ba201d5ae43d09d8c15dc07d0695c87ba743de3` |

Recomputed the first four hashes and matched all 180 successor regular-file bytes against exact commit4ec4bde8, with only safe directory/file member types and paths. The runner equals committed run-workers608.sh. Base/native archives share device+inode with the previously reviewed retained consumer-b originals; the base raw digest was not reread locally. The runner verifies all archive digests before extraction. The fresh export contained only manifest, runner and three archives, with no prior output.

No blocking issue found for this changed-source diagnostic. Prior native parity/config15 evidence remains bound to exact old source0041793a. Full typed build/frozen package, rebuilt exact native receipt, deterministic original/new hashes, action/privilege/seal, automatic queue reviews and ordered595 genuine owner binding plus accepted-run acknowledgements remain required. This review grants no installation, service mutation or release approval. Reviewer performed evidence/source inspection, hash comparisons and the five tiny policy tests only; no heavy tests, dependency install or offload.
