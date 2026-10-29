**VERDICT: APPROVE**

# Independent review: job608 runtime preflight at singleThreaded freeze a46c

SOURCE ONLY; 595 MUST NOT APPLY; no launch performed. This review read the
preflight (de398b3a, 726f9c8a) and the UNUSED export
`/srv/encrypted/dev-move-98/agentq-source608-20261028-private/stage-runtime-singlethreaded-a46c`.
It compared them with the approved 1bed runtime preflight (and its independent
review) and the approved native a46c preflight. It ran no offload, did not run
run608.sh, and installed nothing.

Checks (all pass):

1. `export-manifest.json` sha256 f9ed6da9cc5529981b164327a3ef06ea0ab6a291f6c0838b8049b84d940713b4.
   Fields: stage runtime, execution_state UNUSED, run_id stage608-runtime-a46c,
   source_commit/runner_commit a46cd5765702f3b019d5a433b82d19ac57821a8d,
   source_export_sha256 88279fe17ba6263f5e982c8bb7bad16a13e8f5ad8cf367eebb1921caded20d9e
   (same as the native a46c export), required_checks 14.
2. manifest `stage_inputs` holds exactly 4 entries: native/stage-receipt.json 7d1573ac…,
   native/receipt.json 4a651254…, native/libtests-receipt.json 2f81179f…,
   native/rolldown-binding.linux-x64-gnu.node 0b6607e7…. These are the
   outputs of the accepted native a46c run (acceptance 35dbdbf6). The repo copy
   `job608-native-singlethreaded-a46c/stage-receipt.json` hashes to 7d1573ac…
   and is byte-identical (`cmp`) to the private result's stage-receipt.
3. `stage608-inputs/native/*` are hard links: link count 2, and the inodes
   395721-395724 are the same as `stage-native-singlethreaded-a46c/result608-native/native/*`.
   The on-disk hashes match the manifest.
4. Pinned on-disk sha256: run608.sh eb662d81…, stage608.py a558db9a…,
   native598.tar d73e4e35…, rolldown608-source.tar.gz 203aa483…,
   source598.tar e79a0e45…, successor598.tar dcc959c7…. All are identical to
   the native a46c export. run608.sh and stage608.py match
   `git show a46cd576:docs/strict542/{run-stage608.sh,stage608.py}`.
5. `python3 -I -B stage608.py verify-inputs`, run inside the export dir, exits 0.
   It creates no `__pycache__`.
6. There is no `result608-runtime/` and no `../runtime-singlethreaded-a46c-offload.*`.
   There are no .env, .db, key or pem files and no `__pycache__`.
7. Launch bound: `offload run --timeout 2460 --mem 4g --cpus 1 --artifacts result608-runtime -- timeout -k 15s 2400s sh run608.sh`.
   It requires `offload deadline` >= 2655 s. This is the same as the approved 1bed
   runtime launch (cf8907d3 bound). It differs from the approved native a46c
   launch only in the artifact name and the log/rc names. 2400 s + 15 s is
   below 2460 s, which is below 2655 s.
8. The preparer `docs/strict542/prepare-stage608-export.py` is committed and
   unmodified, sha256 1e701de05d9ccdfccee532cfef8bcc93ba0fc8f9937caf86d689cfc3eda216f2.

Non-blocking: the manifest `purpose` text says "build stage native". This
wording comes from the preparer template and is the same in the approved
stage-runtime-1bed manifest. `stage` is correctly `runtime`.

The approval is limited to one bounded runtime offload of this UNUSED export.
The launch must be the first step of a fresh worker. It grants no application,
install, package or reseal authority. On timeout or failure, do not rerun
unchanged.
