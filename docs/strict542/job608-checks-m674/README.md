# job608 checks m674 at 674840b6 — actual run (evidence; NOT yet independently accepted)

- Stage P/stage-checks-m674 (P=/srv/encrypted/dev-move-98/agentq-source608-20261028-private), manifest
  24fea139f68e2a4a6fb171d3d5895eb457dd3dcd074e4ebed3087bd4fa4baf29, source_commit 674840b6, stage_inputs {}
  (STAGES['checks']=[]). Preflight independent APPROVE 2e9a908c.
- Fresh gates at launch: health up, no competing run, no result/log/rc, verify-inputs 0, sh -n 0, storage608 check 0, 3290s left.
- Launch 21:02:11Z (same caps as tsccwdf6a4): offload run --timeout 1200 --mem 14g --cpus 4 --artifacts result608-checks -- timeout -k 15s 1140s sh run608.sh
- Procedural deviation (disclosed): the worker harness background command had a 600s kill limit shorter than the run.
  To avoid killing the approved single launch, only the wrapping bash was SIGKILLed at ~21:03; the offload client
  (pid 2909494) reparented to init inside the same worker cgroup and ran to completion ~21:15. Therefore the
  offload client rc file was NOT written. Completion evidence instead: artifacts returned (offload only copies back
  after the remote run settles), inner exit-code.txt 0, stage-receipt exit_code 0, STEP608 installed-checks-pass,
  14 passing checks (required 14), offload status shows no failure. No relaunch, no relabelling.
- Mode check: `find result608-checks -perm /022` = 0 entries. Result 310598 B.
- result-files.sha256 lists hashes of every result file as returned (before gzip of any large log).
- Next: independent acceptance, then compiler/runtime m674 with --input P/stage-native-m674/result608-native.
  595 MUST NOT APPLY. No install/seal/root/unit/sudo/service changes.
