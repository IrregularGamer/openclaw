VERDICT: APPROVE

Independent review (reviewer did not author the change) of 6ae72a29 against 5fd299c1:
run-stage608.sh compiler branch `mkdir result598-native` + test_stage608.py regression test.

1. Minimal and correct: 3 lines after stage-native, before install and compiler checks; no check,
   deadline, order or set -e/+e handling changed. Log cause matches (native-codegen608.test.mjs
   L35/L59 ENOENT inside fs.writeFile after computation); build-native608.py out.mkdir() created it
   in the single run.
2. mkdir without -p is right: a pre-existing source/result598-native aborts under set -eu instead of
   mixing stale evidence (same refusal as build-native608.py).
3. Cleanup trap still moves source/result598-native into result608-compiler/.
4. No other stage/test writes into a relative dir the split stage does not create (compiler tests use
   mkdtemp except L35/L59; checks tests use tmp fixtures; build598.sh creates result598-build and
   strict542-checks itself).
5. Regression test meaningful (red/green recorded). Limit: matches only single-quoted literal
   writeFile('dir/...) in the compiler branch; acceptable, no other forms exist today.
6. Note (pre-existing, unchanged): returned result598-native/* evidence is not in OUTPUTS['compiler'],
   so the compiler stage receipt pins only compiler/tests.log.
7. Local checks: discover test_stage608.py 9 tests OK; sh -n run-stage608.sh OK. Nothing heavy run.
