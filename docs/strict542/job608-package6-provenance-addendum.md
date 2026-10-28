# Package6 provenance annotation correction

The original export manifest117f527b is immutable. It inherited descriptive `runner_commit=6648474b` and pending5ec111ba review wording from earlier base exports. These strings are stale and are not used by runner/stage receipt verification. They do not override the cryptographic input identities.

Primary and independent source reviewer each compared actual export0649 `run608.sh` and `stage608.py` byte-for-byte with `591158cfe4a569c9e857780e9cc185cb4590b9b7`. They match exactly:

- run608.sh SHA256d06e24a58bda1c787fc382d7e620758307ebd4a940869e4c045c794a553e83fb.
- stage608.py SHA256d86232c0506dd91a7e277fbc490ac0265d544b14f6c35d1d3056f06ba5858b59.

These are the committed source591158cf bytes, including reviewed runner corrections6ae72a29 and04a7b8ea. Source591158cf has independent census-digest review4a38e973; test race5ec111ba was independently approvedc5d5b84e. Matching native5/checks6/compiler5 receipts bind the same source and exact outputs. The independent review accepts an explicit annotation correction without unchanged rerun, conditional on all actual package/output gates succeeding. No manifest or result is rewritten. This addendum supplies no passing package/application receipt.
