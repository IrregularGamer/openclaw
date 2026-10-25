# Job587 independent exact source review

Verdict: APPROVE_SOURCE_ONLY. Reviewer: separate independent agent
/root/transport_review, not the implementer. Exact source reviewed from
5a5536e4 through 556d4f46bb9d63bc0f25659df83c7075827f0a54.

The initial review rejected leader-only cancellation acknowledgement. The
corrected endpoint retains its leader unreaped until group signaling finishes,
then reaps adopted descendants with kernel child checks and pidfds, including
escaped sessions. No settled receipt is sent without proved settlement before
the shared deadline. Existing pinned Native510.owner_check and Preservation.owner
remain authoritative with caller=True. No Controller or competing owner exists.
The gateway requires operator.read, live authority and combined request and
connection cancellation. Session memory lease and preflight invalidation remain.

Final review found no unresolved findings. The reviewer inspected actual remote
log /home/deploy/agentq/runs/587/remote-tests-3.log, SHA256
b40ff75522fe109e6044755e0b78d950d89e811b0f99478f8df283dc30b5121a. All 101 Node, 15 native transport
and 18 native preparation tests passed, exit 0, from a fresh secretless git archive
under approved offload placement. The receipt JSON pins reviewed source hashes.

Fixture startup failures were not acceptance evidence. The external module's
self-hash reads __file__; test-only source-path substitution now points only at
the pinned source archive. Production keeps its fixed external path. No runtime
path was created to satisfy tests. This review approves source and synthetic
evidence only, never installation, deployment or native/provider availability.
