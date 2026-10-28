# Independent review: f1fe77e8 (finite build stage DAG, checkpoint transport, export preparer)

## Scope

Only commit f1fe77e8 (`git show f1fe77e8`), 10 files: `scripts/build-all.mts`,
`scripts/build-checkpoint608.mts`, `scripts/lib/bounded-build-checkpoint608.mjs`,
`docs/strict542/{stage608.py,prepare-finite608-export.py,run-stage608.sh,run-build-stage608.sh,build598.sh}`
and the two test files. I checked it against rules 1-6 of
`docs/strict542/job608-declaration-stage-continuation.md` (lines 36-100).
The previously reviewed `tsdown-declaration-writer.mts` and `declaration-checkpoint608.mjs` (9607b331/f1e0907a)
were read only for how this commit calls them. I ran no heavy builds or offloads. HEAD (01c7a18e) differs from
f1fe77e8 under docs/strict542 and scripts only in run-stage608.sh (+1 line), one new test file and the continuation
doc, so the focused tests run against the reviewed bytes.

## Checks run

- `cd docs/strict542 && python3 -m unittest test_stage608 -v`: 14/14 pass.
- `node --test docs/strict542/build-checkpoint608.test.mjs docs/strict542/declaration-checkpoint608.test.mjs`:
  10/10 pass (4 build-checkpoint + 6 declaration-checkpoint).
- Ad-hoc probes in /tmp (no source changes):
  - JS `writeBuildCheckpoint608` with output links `up -> ..` and `dist/up2 -> ../..`: ACCEPTED (F1).
  - Python `extract_checkpoint` with an out-of-order symlink chain (`f -> e/../../../..` before `e -> ../../..`):
    extracted, but Python 3.14.4's `data` filter normalized the link name so it stays inside data/. No escape on
    this interpreter (see F5).

## Verified as preserved or correct

- Admission and memory floor: `admitBoundedPackage` (4GiB cap, `UNIFIED_GRAPH_THRASH_LIMIT_BYTES` floor,
  inherited-control refusal) and the fresh-export check still run before any checkpoint work. The memory floor
  constant and native pin are unchanged. Cache stays off for boundedPackage, and the checkpoint requires
  `OPENCLAW_608_BOUNDED_PACKAGE=1` and `OPENCLAW_BUILD_CACHE=0`. The live-dist fence is unchanged.
- No caller-selected commands: boundedPackage now refuses `params.steps` (a tightening). The stage name comes from
  the manifest, is limited to a fixed allow-list in both shell and `buildStage608`, and runs under `env -i`.
  I found no privilege escalation.
- Phase partition: runtime, middle and tail together cover exactly the canonical label list. `complete` re-checks
  the full ordered list with every phase status `ran`. A checkpoint is written only when `exitCode === 0`, and a
  failing join throws before `finish`.
- Source drift: every producing receipt must match the consumer's `source_commit` and the common
  `source_export_sha256` (stage608.py:115), which is base archive + commit + successor archive and is not a
  per-stage manifest digest. JS receipts also bind the lock, workspace, package, toolchain, native receipts, addon,
  config census and fresh-source baseline inventory digest.
- Predecessors and partial output: middle needs runtime plus all 6 unified bindings, and tail needs middle plus
  both SDK bindings. Each binding is tied to the digest of the exact predecessor receipt and to the group inventory.
  A failed stage writes no `stage608.py receipt` and has `exit-code.txt != 0`, so `verify_inputs` and the preparer
  refuse it. A failed group or mismatch therefore cannot produce a join or a BUILT receipt.
- Tamper: archives and logs are pinned by the manifest and the producing receipt. JS restore re-verifies the receipt
  identity, the data inventory before mutation, and the restored inventory. Tar extraction refuses `..`, absolute,
  duplicate, hardlink, device and setuid/sgid entries, non-directory parents and collisions.
- Checkpoints live in `exportRoot/build608-checkpoints`, outside the extracted source (rule 3), and cleanup removes
  them.

## Findings

| # | Severity | Location | Finding |
|---|----------|----------|---------|
| F1 | Medium (blocking) | scripts/lib/bounded-build-checkpoint608.mjs:53 | The link-escape guard only rejects normalized targets that start with `'../'`. A target that normalizes to exactly `'..'` (top-level `x -> ..`, or `dist/y -> ../..`) passes. `writeBuildCheckpoint608` records it and `restoreBuildCheckpoint608`/`materialize608` would recreate a link to the parent of the source root (confirmed by probe). Today the Python transport check (stage608.py:55) refuses such links, so this is not reachable through a transported archive. But the JS restore guard is meant to refuse escapes on its own, and it does not. Fix: also reject `=== '..'` (and preferably resolve through already-recorded link entries), and add a test. |
| F2 | Medium (blocking, rule 5) | scripts/build-checkpoint608.mts:37-56, 64-71, 81-85 | The DAG validator (`validateChain`, `validateBinding`, join inventory recheck, `complete` ancestry) has no tests. Nothing tests a missing or extra unified/SDK group, a binding whose predecessor digest is foreign, a runtime receipt with ancestors, a mismatched `outputRoots`, source drift between a group and its predecessor, or `complete` without tail. Rule 5 requires predecessor, partial-output, tamper and source-drift tests before freezing new executable source. The existing tests cover only `buildStage608` partitioning and the low-level write/restore. |
| F3 | Low | scripts/build-all.mts:602-607, 671; build-checkpoint608.mts:75 | The group compile (`produce`) and the `join` now run in-process from `prepareBuildCheckpoint608` instead of as `runManagedCommand` children. They therefore no longer get `timeoutMs` from `BOUNDED_PACKAGE_DEADLINE_MS`, and the per-step deadline check is skipped for `produce`. The build stages in run-stage608.sh also have no inner `timeout`. Rule 3 only requires the outer finite offload deadline, so this is not blocking, but the inner deadline is weaker than before. |
| F4 | Low | scripts/build-all.mts:602 vs 637 | `prepareBuildCheckpoint608` (including a unified/SDK group compile) runs before the `heapShortfall.fatal` refusal. The result is still fail-closed (exit 1, no stage receipt), but a compile can run under a plan the original owner would refuse up front. Move the checkpoint preparation after the heap-shortfall check. |
| F5 | Info | docs/strict542/stage608.py:51-56, 65 | The Python link check is lexical, so an out-of-order symlink chain escape is caught only by the interpreter's `data` filter link normalization (present in 3.14.4). Pin or assert a Python version with that behavior, or validate links against already-accepted link entries. Not reachable without breaking the digest pins. |
| F6 | Info | docs/strict542/prepare-finite608-export.py:44 | The `.env`/`.db` name filter is weak (exact names only). It is acceptable because input comes from the committed git tree, but don't treat it as a secret control. Group names in `checkpoint_path` (stage608.py) are hardcoded copies of `tsdown-config-groups.mts`, with no test that checks them against each other. |
| F7 | Info | scripts/lib/bounded-build-checkpoint608.mjs:38 | `node_modules` is excluded from every checkpoint inventory. Any build output written under node_modules would not be carried between stages. A focused review can't verify this. The real package run must confirm that `complete` + deploy see identical outputs. |

## Verdict

CHANGES_REQUIRED. Fix F1 and add the rule 5 DAG refusal tests (F2); F3 and F4 are recommended. Apart from these,
the commit keeps admission, the memory floor, the 4GiB/1CPU/swap0 budget, cache-off, the native pin and the
canonical phase list. It enforces the common source identity, and I found no path where a failed or partial stage
yields a join or BUILT receipt.
