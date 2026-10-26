# 608 consumer slot refusal (2026-10-26T12:29Z), reconciled

Fresh worker (started 12:24Z) verified the unused local export
tmp/export608-native-consumer-unitfast: run608.sh 39d26e32, successor598.tar
91ffa313, export-manifest.json a09747e3 (all match
job608-native-consumer-unitfast-export.json). ONE `offload run --artifacts
result598 -- timeout -k 15s 3000s sh run608.sh` was started at 12:27Z.

Outcome: exit 75 within ~2 minutes, before run608.sh executed:

    [offload-agent] refusing: secret-like file in tree: .native608/cmake-tool/cmake/data/share/cmake-3.31/Templates/Windows/Windows_TemporaryKey.pfx
    {"offload_status": "remote_environment_blocked", "local_execution": false, "retry_requires_reconciliation": true}

No consumer stage ran: no native equality, parity, config15, build or package
result exists from this attempt. Raw log: job608-consumer-slot-refusal.log.

## Reconciliation

- The local export contains no `.native608` (only the five manifest inputs plus
  native608-stages receipts). The file is a stock CMake 3.31 template, not a
  credential; nothing secret was sent.
- `offload` derives the remote slot from the export path (no git root), so the
  slot is private to this path. `.native608/` is created only remotely by
  prepare-native-consumer608.py. Its presence means an earlier attempt already
  started this exact export remotely and was cut off before run608.sh's EXIT
  trap ran (the 12:13Z worker ended "exit None"; blocked/unknown runs are not
  written to runs.log). That lost attempt produced no recoverable result.
- push_tree uses `rsync --delete --exclude-from=offload.exclude`; `*.pfx` is
  excluded, so rsync never deletes the remote leftover and every later run of
  this path is refused. This is infrastructure state, not a source failure.
- `offload status` 12:30Z: friend VPS up, load 0.28, so nothing is still running.
- offload, its exclude list and the remote agent were not modified, and nothing
  was retried in this worker.

## Corrected continuation (supersedes the export path in job608-resume-after-unitfast.md)

1. In a FRESH worker with >=55 minutes left, create a NEW never-used export
   directory (for example tmp/export608-native-consumer-unitfast-b) with
   byte-identical contents: hard-link the four archives and copy run608.sh,
   export-manifest.json and native608-stages/*/receipt.json. Re-verify all
   digests against the committed manifest before launching. Source, runner and
   manifest identities are unchanged, so review 11b14be3 still applies.
2. Launch immediately, never late in a worker. A run killed by the worker or
   timeout skips the EXIT trap and dirties its slot again, so treat any cut-off
   path as spent and do not reuse it.
3. The stale slot for tmp/export608-native-consumer-unitfast holds only a public
   CMake template. Cleaning it needs a remote-agent operator action; it is not
   needed for step 1.

All later gates in job608-resume-after-unitfast.md stay as written.
