# Job608 unified-5 retry (5r1) continuation — 595 MUST NOT APPLY

Unified-5 launch SPENT with exit 75 remote_lease_denied before any build output
(job608-unified-5-tsccwdf6a4-lease-revoked/). Retry uses a NEW stage path so a
stale remote rrsync lock on the old slug cannot refuse it:

P/stage-unified-5r1-tsccwdf6a4 = `cp -al` of the untouched spent stage (hardlinks,
0 new unique bytes; `diff -r` identical; export-manifest.json sha256
a63306a5afdfd7330d23c1cd27bbeea62edbfb9bacce261246668208fc1f81e4 = preflight
job608-unified1-5-tsccwdf6a4-preflight.json stages[4].manifest_sha256). Inputs are
only read by the runner (results go to ../result608-unified-5 on the remote), so
hardlinks do not couple the two stage trees.

Gates, all fresh, unchanged from job608-after-unified3-tsccwdf6a4-continuation.md:
health up and no competing run; root free >=1GB; storage608 check --stage unified-5
exit0; verify-inputs0, sh -n run608.sh 0, exact manifest above, result/log/rc absent
for 5r1; >=2655s left. Then ONCE:

```sh
cd /srv/encrypted/dev-move-98/agentq-source608-20261028-private/stage-unified-5r1-tsccwdf6a4
offload run --timeout 2460 --mem 14g --cpus 4 --artifacts result608-unified-5 -- timeout -k 15s 2400s sh run608.sh > ../unified-5r1-tsccwdf6a4-offload.log 2>&1
printf '%s\n' "$?" > ../unified-5r1-tsccwdf6a4-offload.rc
```

If 5r1 also exits 75, do not create 5r2 in the same worker: preserve, commit, and
let the queue retry remote_lease_denied. Capture evidence as for unified-4
(force-add ignored *.log copies with `git add -f`), then independent acceptance.
Accepted: unified-0..3, unified-4 pending re-acceptance of 5e70391f.
Afterwards remain: middle, sdk0/1, tail, package, final artifact/old-new inventory,
action/privilege/seal/reseal and automatic queue reviews, genuine ordered HQ595
handoff. 595 MUST NOT APPLY.
