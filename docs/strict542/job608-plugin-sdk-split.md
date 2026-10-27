# Job608: finite plugin-SDK canonical partition cases (Decision637 rule)

Installed637dr (source 6eeeee81, 4g/1CPU, maxConcurrency=1) passed 194/195;
the sole failure was the 120000 ms timeout of the cumulative base case
`write-plugin-sdk-entry-dts > publishes fresh canonical partitions with stable
bytes and public nominal identity` (four writer runs plus a consumer typecheck
in one case on 1 CPU). Per Decision637 (assertion-preserving bounded split, never
a timeout acceptance), the owning test now runs that body as four sequential
cases under one suite-owned fixture lifetime: initial production build; private
QA build; changed-input build; relocated cache restore plus consumer typecheck.

Every original statement and `expect` is moved verbatim in order (43 -> 44
`expect` calls; the extra one is the stage guard that fails each successor if
any predecessor did not complete). Only the history root moves from the
per-case command to the suite lifetime; the relocated fixture and every writer
command stay owned by the running case's abort signal. Per-case timeout stays
`WRITER_TEST_TIMEOUT_MS` (120000 ms, 360000 ms on Windows). No fixture, cache
rule, compiler, budget, floor, swap or deadline changes. The runner is
unchanged; the successor overlay gains this path. Independent review of this
split and the regenerated export is required before the full package receipt.
