# Independent native last-use diagnostic input review608

Reviewer: Rook `/root/memory_review`, independent from implementation and export preparation.

Verdict: APPROVE_FOR_ONE_ADMITTED_CHANGED_SOURCE_DIAGNOSTIC_ONLY. Source review is `job608-native-last-use-source-review.md`, committed `a78be593`. This approves only the exact export below through normal offload admission at the unchanged default2GiB/1CPU cap. It supplies no execution success, full build/package, action, privilege, seal, automatic queue or application approval.

I independently compared all136 successor regular-file members byte-for-byte with `git show` of exact reviewed source `b6a438b9faffb1a3b43a398206e8ec501330cf13`. The member set equals both the manifest inventory and complete base-to-source Git diff. There are no omitted deletions/renames, duplicate files, links or special successor members. The external runner equals the committed `docs/strict542/run-native608.sh`. The repository manifest copy equals the export manifest bytes. I freshly hashed the delta, runner, native preparation archive, compiler source archive and manifest.

The658MiB retained base archive was not reread in this pass. I independently verified its device/inode/size match the previously independently reviewed `export608-bounded` archive. This review explicitly relies on that prior provenance and existing digest; the runner rechecks the raw base/native/delta digests before remote extraction. The native preparation archive also shares its retained inode and its fresh digest agrees. Its48 regular files remain within the scheduler preparation trees; the handoff `candidate/maintenance.py` digest is unchanged `bca40971a35d160ad87b5d18fd1cc7f7730a7f90d2bb5b8480f3d7d79d11c182`.

The5.7MiB compiler archive has18,406 entries under the exact immutable commit root. I checked its member paths/types and all five source pins. Its two upstream symlinks target files inside that source root: `CLAUDE.md` → `AGENTS.md` and the import-glob test fixture `linked/my-lib` → `../packages/my-lib`. Extraction uses Python's data filter. The compiler builder verifies this archive digest before extraction and pins the official Rust distribution separately. The source correction and native compiler identity remain separate from gateway-native587, owner predicates and sealed/runtime paths. No live auth/config/credential or provider input is introduced by the reviewed successor files. Normal secretless transfer-guard and resource admission checks remain mandatory.

Exact identities:

- Base source: `c790ba44938bd90f75fb41f2f2eeaaff287df546`
- Base archive SHA256: `e79a0e45a4eaea4afe325ca94ba201d5ae43d09d8c15dc07d0695c87ba743de3`
- Compiled source: `b6a438b9faffb1a3b43a398206e8ec501330cf13`
- Successor archive SHA256: `565c3c70b96fa99223bee9de02bb186c3048db55f4b694532d27254fb55c3499`
- Native preparation archive SHA256: `d73e4e35720ffcb71856ce8168e75fa3b4fd49251fd78c811e1abded8b2701de`
- Upstream compiler archive SHA256: `203aa4834d7a52522c758c81f6e493bea9fea828d4454fe2a25b9519d2d258ac`
- Runner SHA256: `34b7c4a1cb55a1e8cea35a15fce57c5b24c3a48e3524e8d7f1c01884b41748b1`
- Export manifest SHA256: `f6d8951e5c2bf139377e163ea139c08acc50e92b93a7812eb749637a65e05956`

Proceed only with the one reviewed changed-source native build, real lifetime/negative/library/parity/lazy-barrel checks and complete runtime config diagnostic. All those remote results and actual memory/settlement outcomes require subsequent independent evidence review. Failure/refusal authorizes no unchanged retry, larger budget, local heavy build or gate weakening. The canonical typed package and595's original application gates remain outstanding.
