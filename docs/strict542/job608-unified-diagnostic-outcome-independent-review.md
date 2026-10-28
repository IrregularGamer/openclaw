# Independent review: actual finite unified diagnostic evidence608

Verdict: APPROVE EVIDENCE ONLY, exact evidence commit
a71d150f4292cadb292be76d45b6a7c76067d49a. Reviewer: independently delegated Rook
source-analysis lane. This review does not accept a build checkpoint, final
artifact/package, source fix, application, privilege change, seal or installation.
595 MUST NOT APPLY. The subsequently committed41ee9e9f scratch correction is
outside this outcome review.

I streamed every regular member of the262482byte evidence tar.gz and checked its
SHA2561d56021edf5b01a95105b8d8de9bcd3bd917af1b4ec89e00e9b01d3283dbbc46.
All16 regular members matched the actual local files:12 diagnostic raw files plus
offload.log/offload.rc/export-manifest.json/diagnostic-manifest.json. There were
no unexpected regular files, duplicate names, unsafe paths or link members.
Every raw size/hash equals the committed outcome inventory. Regenerating the
analysis from actual raw files with the committed analyzer reproduced the entire
committed decompressed analysis JSON exactly, including6 profile descriptors,
68 process/cgroup samples and672.234047seconds sample span.

Small provenance checks passed: exact export-manifest SHA2563d5634ac91c09e0129a58285f90f1df1bcd7cc733f4284784f74a10b3c727435,
manifest-pinned runner and stage-helper hashes, common source5f7d810b and export
76b4b47a. The actually exported diagnostic matches reviewed857ca783 and SHA256
7ffb4a1b8e813034e2c742f485072c4975136230448c545f1d8859230f2e6288.
That source has the original same-thread observer;06d042e2's corrected Worker
observer remains prepared and unused. The ready/manifest UNUSED fields are
preserved prelaunch descriptions; actual outcome/logs establish that this first
export was consumed. They must never authorize replay. No second diagnostic run
is represented or required by these records.

The actual client return was0, while actual diagnostic command/build return was
124. The returned JSON explicitly identifies diagnostic evidence only and records
682.2506108284seconds total elapsed. The compiler/install window was600seconds;
the log shows the compiler invocation received168.4seconds before parent SIGTERM,
then process-group cleanup observed it dead. A successful client return here
means the finite diagnostic completed its evidence collection, not build success.

Independent raw-profile aggregation confirms the first295.487second outer profile
contains191.162seconds inclusive workspace inventory and170.721seconds inclusive
file hashing, with60.931seconds GC and26.361seconds unsafe-buffer allocation.
These are sampled wall-duration weights; inclusive frames overlap and must not
be added or described as exclusive CPU totals. The source's per-file1MiB scratch
allocation is a concrete optimization target. Inner Node profiles also capture
filesystem/read/boundary callback work. Native tsc CPU counters advance; the data
does not establish a permanent native wait/deadlock. No sampled memory.max/OOM/
OOM-kill counter increment occurred in the observed admitted cgroup. This is not
a claim about ancestors or historical runs.

The short diagnostic does not reproduce the complete2400second failed build and
does not prove that allocation changes solve the historical timeout, that native
semantic checking finishes, or that package/install gates passed. Source fixes
still require exact independent review, relevant/full checks and new affected
receipts under the original ownership and budget rules. All original final
source/action/privilege/seal/automatic-queue/HQ and post-restart genuine owner/ack
gates remain. No offload, build, source mutation or runtime action was performed
by this review; verification used bounded local evidence reads and analysis only.
