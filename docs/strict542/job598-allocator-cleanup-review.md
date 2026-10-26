# job598 allocator-slot cleanup successor: independent review receipt (2026-10-26)

- Reviewer: independent Claude reviewer (read-only; did not execute the script, ssh, or touch the remote/offload)
- Reviewed commit: 6bf701f26b5a4361b5b8bfbda2b3031777d2ad1f (branch strict542-source552)
- File: docs/strict542/reconcile-allocator-slot598.py
  sha256 51ee185ccc0653a59040418313bc79575395023449b626684b203f2377db8049
- Predecessor (approved once): reconcile-isolated-slot598.py
  sha256 5370a2b34f0edaa51ccf7c1de6afcfd51414e624249b628332ea63d1490a753c

Findings from `git diff --no-index` (only differences: docstring, OUT path, RECOVERED constants
plus local hash precheck, top-level set adds `source`, four new in-lock asserts, `.replace('RECOVERED',...)`):

1. Unchanged: same SLOT, same remote base path, same LeaseStore.runner_slot() held across
   READY / clean / VERIFY, lease digest must equal exactly [sha256(current worker lease)],
   zero DockerEngine containers before and after, nonsymlink slot, nonsymlink .pnpm-store,
   alarm(120), 60 s receive timeouts, and the sole mutation is the literal
   `ssh offload clean tmp-export598-config-isolation-98c59c32`. No other slug, path,
   privilege, scanner, budget or lock change.
2. `source` admission: requires result598 absent, source not a symlink,
   source/isolated-probe598.json absent, and source/result598-isolated == {probe.log},
   source/strict542-checks == {tests.log} (nonsymlink dirs) with sha256 equal to RECOVERED.
   This covers every output run598.sh (= run-isolated598.sh, 4ddaa154) can produce
   (exit-code.txt / copied probe json would make the set check fail). result598-probe is
   not an output of this runner. Local precheck: recovered files in
   runs/598/allocator-reconciliation/ hash to b91e20b8.../1b30cade... = RECOVERED;
   tests.log equals test_log_sha256 in job598-allocator-tests.json.
3. Substitution: EXPECTED and RECOVERED each occur once in the remote text (case-sensitive;
   'unrecovered' unaffected); reprs are valid literals and cannot introduce either token.
   Substituted remote code (dummy lease digest) and the script pass `python3 -I -m py_compile`.
4. Failure paths: local hash assert precedes ssh; any in-lock assert exits the remote
   before READY so receive() raises and clean is never invoked; clean failure/timeout
   raises before VERIFY; finally terminates the holder. Non-blocking note: exists()
   ignores dangling symlinks, which hold no data.

Verdict: APPROVE - execute exactly once, only under the existing mandatory ordered
execution conditions of job598-isolated-cleanup-review.md and the whole-slot rules of
job598-reconciliation-review.md. Any refusal or uncertain status means stop; no retry,
slot rotation or bypass.

This approval covers temporary workspace cleanup only. It grants no build, artifact,
release, native supervisor or application approval, and no allocator outcome is implied.

## Receipt: zero-lease predicate amendment (2026-10-26)

- Reviewer: independent Claude reviewer (read-only; did not execute the script, ssh, or run offload)
- Reviewed commit: f334807d726c3ca244609c7367a002d06303ec57 (branch strict542-source552)
- File: docs/strict542/reconcile-allocator-slot598.py
  sha256 69b1e08e25a4c67785c33d350e4adc9f2cd6eea559615b7feb9dfc0db95e46b3
  (base 8863e79f version verified = approved 51ee185c...8049)

Findings (`git diff 8863e79f f334807d`, script changes are exactly two lines plus a comment):
1. Pre-READY: `leases==[expected]` -> `leases in ([],[expected])`, evaluated inside the held
   `store.runner_slot()`. Any other/old lease, or more than one lease, still refuses.
   Zero leases is the original stricter rule of job598-reconciliation-review.md;
   [expected] is the job598-isolated-cleanup-review.md refinement. Nothing else is admitted.
2. Post-clean: `live()==[expected]` -> `live()==leases` (lease set unchanged from the in-lock
   snapshot) plus zero managed containers. A lease appearing, disappearing or changing in
   the window fails VERIFY (exit nonzero; no retry).
3. Unchanged: runner_slot lock, slot slug/path, `ssh offload clean <SLOT>`, container check,
   slot inventory, source/RECOVERED admission, local recovery hashes, substitution, timeouts,
   failure paths. Any in-lock assert exits before READY, so clean is never invoked.
4. Substituted remote code (dummy digest/RECOVERED; EXPECTED and RECOVERED each occur once)
   and the script pass `python3 -I` py_compile.
5. Exclusion: accepting zero leases does not weaken concurrent-run exclusion. The runner_slot
   lock is held from snapshot through VERIFY and offload run needs both a lease and that
   slot, so no run can start; no container may exist; any lease minted meanwhile is caught
   by the unchanged-set check. The local AGENTQ_LEASE_ID still binds which lease is admissible.

Verdict: APPROVE - execute exactly once, under the same mandatory ordered conditions as the
prior receipt. Any refusal or uncertain status means stop; no retry, slot rotation or bypass.
This approval covers temporary workspace cleanup only; it grants no build, artifact, release,
native supervisor or application approval.
