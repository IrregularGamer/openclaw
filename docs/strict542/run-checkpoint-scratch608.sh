#!/bin/sh
# Focused source regression only, inside an admitted committed secretless export.
set -eu
mkdir result608-scratch
node --version >result608-scratch/node-version.txt
sha256sum scripts/lib/bounded-build-checkpoint608.mjs scripts/lib/declaration-checkpoint608.mjs docs/strict542/checkpoint-scratch608.test.mjs docs/strict542/build-checkpoint608.test.mjs docs/strict542/declaration-checkpoint608.test.mjs scripts/build-checkpoint608.mts scripts/build-all.mts scripts/lib/build-artifact-cache.mts scripts/lib/tsdown-declaration-writer.mts >result608-scratch/source-sha256.txt
node --test --test-concurrency=1 --test-reporter=tap docs/strict542/checkpoint-scratch608.test.mjs docs/strict542/build-checkpoint608.test.mjs docs/strict542/declaration-checkpoint608.test.mjs >result608-scratch/tests.log 2>&1 || {
 status=$?; tail -50 result608-scratch/tests.log; exit "$status";
}
tail -9 result608-scratch/tests.log
printf '0\n' >result608-scratch/exit-code.txt
