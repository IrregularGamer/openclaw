#!/bin/sh
# Diagnostic observer only. No source edits, checkpoint fabrication or authority.
set -u
started=$(date +%s)
sampler() {
  sleep_pid=
  trap 'if [ -n "$sleep_pid" ]; then kill "$sleep_pid" 2>/dev/null || :; wait "$sleep_pid" 2>/dev/null || :; fi; exit 0' TERM INT
  while :; do
    sleep 120 & sleep_pid=$!
    wait "$sleep_pid" || :
    sleep_pid=
    echo "SAMPLE608 elapsed=$(( $(date +%s)-started ))s"
    ps -eo pid,ppid,etimes,time,rss,args --sort=-time 2>/dev/null | head -8 | cut -c1-220
    tail -20 result608-unified-0/unified-0/build.log 2>/dev/null || :
  done
}
sampler & sampler_pid=$!
timeout -k 15s 2300s sh run608.sh
status=$?
kill "$sampler_pid" 2>/dev/null || :
wait "$sampler_pid" 2>/dev/null || :
echo "SAMPLE608 end rc=$status elapsed=$(( $(date +%s)-started ))s"
tail -80 result608-unified-0/unified-0/build.log 2>/dev/null || :
exit "$status"
