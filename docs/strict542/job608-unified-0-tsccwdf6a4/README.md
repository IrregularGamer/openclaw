# Job608 unified-0 tsccwdf6a4 — actual run evidence (595 MUST NOT APPLY)

- Frozen source f6a4de2ebc6924d16fe559f9858bf8c50dce1eba; common export e81e07d2770ad597bb11de77e1dbf899d5f5286b8d3d52e8c5616faa74458145.
- Stage P/stage-unified-0-tsccwdf6a4, manifest 3a1b42d1b104c977b258a82b82fedd85a02e15c7d2fdaaff754caad4e455708a;
  independent preflight ad22814a, launch 577ba15e. P is
  /srv/encrypted/dev-move-98/agentq-source608-20261028-private.
- ONE admitted offload: `offload run --timeout 2460 --mem 14g --cpus 4 --artifacts result608-unified-0 -- timeout -k 15s 2400s sh run608.sh`.
- Actual client rc 0; result exit-code.txt 0; STEP608 unified-0-build-done +422s,
  unified-0-pass. Storage result check exit 0, 647069 bytes <33554432 cap.
- Receipt SHA256 1ac0a79838bd11407b95f46f1a4f239f7d2e41873118c918acb102a4ea9c1563.
- Output checkpoint SHA256 1583290f01734085ea0a5f64ab08eac32855b43116df426103da4080b7740897,
  636339 bytes; kept in the private result directory (not committed).
- Full five-file inventory in result-files.sha256; other four files are committed
  byte-for-byte, plus deterministic gzip of the complete outer log and actual rc.
- Inputs are the exact 7 native/runtime pins accepted by 57742314/5824b14b.
- Stage SPENT. Never replay; immutable manifest UNUSED is prelaunch metadata.
- Pending independent acceptance before compiler launch. No package, artifact,
  action, privilege, seal or automatic queue approval is established here.
