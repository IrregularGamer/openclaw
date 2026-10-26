// Diagnostic scheduling policy only; never an application/build receipt.
export function admitProbe(capacity, env, existingOutput) {
  if (capacity.unresolved || !Number.isFinite(capacity.capacityBytes) ||
      capacity.capacityBytes <= 0 || capacity.capacityBytes > 2*1024**3 ||
      !Number.isFinite(capacity.limitBytes) || capacity.limitBytes <= 0 ||
      capacity.limitBytes > capacity.capacityBytes)
    throw new Error('probe requires observed capacity no larger than admitted2GiB');
  if (existingOutput) throw new Error('probe requires a fresh disposable source export');
  for (const key of Object.keys(env)) {
    // scripts/lib/tsx-cli-shim.mjs owns this fixed cache-disabled setting.
    if (key === 'TSX_DISABLE_CACHE' && env[key] === '1') continue;
    if (['NODE_OPTIONS','NODE_PATH','OUTPUT_SOURCE_MAPS','RAYON_NUM_THREADS','RAYON_RS_NUM_CPUS','UV_THREADPOOL_SIZE'].includes(key) || /^(OPENCLAW_|TSDOWN_|TSX_|ROLLDOWN_|TOKIO_|MIMALLOC_)/iu.test(key))
      throw new Error(`probe refuses compiler environment control: ${key}`);
  }
}
// Job605 evidence: unified config15 thrashes in memory.high reclaim (user CPU ~5%,
// system CPU ~95%) and peaked at this cgroup charge. A limit not above it cannot
// complete the probe, so refuse the whole probe instead of burning the deadline;
// this never lowers a check or splits the singleton-owning unified graph.
export const UNIFIED_GRAPH_THRASH_LIMIT_BYTES = 1625784320;
export function admitUnifiedGraphCapacity(capacity) {
  if (!Number.isFinite(capacity.limitBytes) || capacity.limitBytes <= UNIFIED_GRAPH_THRASH_LIMIT_BYTES)
    throw new Error('probe refused: observed memory limit is not above the job605 config15 reclaim-thrash peak');
}
export function probeSucceeded(result) {
  return result.status === 0 && !result.timedOut && !result.error &&
    !result.fatalUnresolvedImport && !result.hasIneffectiveDynamicImport;
}

// Generated only after fixed diagnostic admission; no caller-selected pool size.
export const ONE_CPU_NATIVE_POOLS = Object.freeze({
 ROLLDOWN_WORKER_THREADS:'1', ROLLDOWN_MAX_BLOCKING_THREADS:'1',
 RAYON_NUM_THREADS:'1', TOKIO_WORKER_THREADS:'1',
});
// Process-local allocator policy; never changes kernel/cgroup limits.
export const BOUNDED_NATIVE_ALLOCATOR = Object.freeze({MIMALLOC_ALLOW_THP:'0'});
export function fixedOneCpuCompilerEnv(env) {
 return {...env, ...ONE_CPU_NATIVE_POOLS, ...BOUNDED_NATIVE_ALLOCATOR, OPENCLAW_RUN_NODE_SKIP_DTS_BUILD:'1'};
}
