# Current runtime read-only observation

SOURCE ONLY;595 MUST NOT APPLY. The admitted runtime run remains active, with no
accepted completion receipt. One read-only `ps` snapshot and a two-second read-only
cgroup sample on friend-vps were captured using the existing SSH host alias.
No Docker command, service operation, signal, cgroup change or root mutation ran.

The sample showed 2018287 microseconds of aggregate slice CPU usage in
two wall seconds (approximately one CPU). Memory moved from2010157056 to2016960512
bytes under MemoryHigh=MemoryMax=4294967296; cpu.max stayed100000/100000.
All memory.events counters were unchanged across this sample. These counters
are cumulative: their nonzero historical OOM totals are NOT attributed to this
run. This sample establishes active CPU work at observation time, not whole-run
resource history, compiler success, absence of any earlier pressure, or the cause
of any eventual timeout. Detailed build log and actual client/result receipt are
still required. The process list showed one MainThread and esbuild in the admitted
slice. No argv, environment, auth/config/credentials or provider data were read.
