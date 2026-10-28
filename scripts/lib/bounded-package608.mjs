import { createHash } from 'node:crypto';
// Whole-config scheduling for a complete typed package under an admitted 4 GiB lease.
export const BOUNDED_PACKAGE_DEADLINE_MS = 2_700_000;
export const UNIFIED_GRAPH_THRASH_LIMIT_BYTES = 1625784320;
export const BOUNDED_COMPILER_ENV = Object.freeze({
  ROLLDOWN_WORKER_THREADS: '1', ROLLDOWN_MAX_BLOCKING_THREADS: '1',
  RAYON_NUM_THREADS: '1', TOKIO_WORKER_THREADS: '1', MIMALLOC_ALLOW_THP: '0',
  OPENCLAW_RUN_NODE_SKIP_DTS_BUILD: '0',
});
export function admitBoundedCapacity608(capacity) {
  if (capacity.unresolved || !Number.isFinite(capacity.capacityBytes) ||
      capacity.capacityBytes <= 0 || capacity.capacityBytes > 4 * 1024 ** 3 ||
      !Number.isFinite(capacity.limitBytes) || capacity.limitBytes > capacity.capacityBytes ||
      capacity.limitBytes <= UNIFIED_GRAPH_THRASH_LIMIT_BYTES)
    throw new Error('boundedPackage requires observed admitted capacity above the unchanged config15 floor and at most 4GiB');
}
export function admitBoundedPackage(capacity, env) {
  admitBoundedCapacity608(capacity);
  for (const key of Object.keys(env)) {
    if (key === 'TSX_DISABLE_CACHE' && env[key] === '1') continue;
    if (['OPENCLAW_608_BOUNDED_PACKAGE','NODE_OPTIONS','NODE_PATH','OUTPUT_SOURCE_MAPS','RAYON_NUM_THREADS','RAYON_RS_NUM_CPUS','UV_THREADPOOL_SIZE','OPENCLAW_BUILD_VERBOSE','OPENCLAW_BUNDLED_PLUGIN_BUILD_IDS','OPENCLAW_INCLUDE_OPTIONAL_BUNDLED'].includes(key) ||
        /^(TSDOWN_|TSX_|ROLLDOWN_|TOKIO_|MIMALLOC_|NAPI_RS_|OPENCLAW_(RUN_NODE_SKIP_DTS_BUILD|TSDOWN_|BUILD_PRIVATE_QA|INTERNAL_DOCKER_))/u.test(key))
      throw new Error(`boundedPackage refuses inherited compiler control: ${key}`);
  }
}
export function boundedCompilerStep(step) {
  const stage = {'tsdown-ai':'ai','tsdown-packages':'packages','tsdown-unified':'unified'}[step.label];
  if (!stage) return {...step, cache: undefined};
  return {...step, cache: undefined,
    args: ['--import','tsx','scripts/tsdown-bounded608.mts',stage],
    env: {...step.env, ...BOUNDED_COMPILER_ENV, OPENCLAW_PRESERVE_CLI_STARTUP_METADATA:'1'}};
}
export function typedConfigCensus(configs) {
  if (!Array.isArray(configs) || configs.length === 0) throw new Error('missing typed config inventory');
  return configs.map((config,index) => {
    if (!config || !config.entry || Array.isArray(config.entry) || typeof config.entry !== 'object' ||
        Object.keys(config.entry).length === 0 || Object.values(config.entry).some(source => typeof source !== 'string'))
      throw new Error('unsupported config entry inventory');
    return {index,name:config.name ?? null,entry:config.entry,outDir:config.outDir ?? 'dist',dts:config.dts};
  });
}
// The full census exceeds the kernel's 128 KiB per-environment-string limit
// (spawn E2BIG), so children receive its sha256 and recompute it exactly.
export function typedConfigCensusDigest(census) {
  return createHash('sha256').update(JSON.stringify(census)).digest('hex');
}
export function selectTypedWholeConfig(configs,indexText,expectedCensusSha256) {
  if (!/^[0-9a-f]{64}$/u.test(expectedCensusSha256 ?? '')) throw new Error('invalid typed config census digest');
  if (typedConfigCensusDigest(typedConfigCensus(configs)) !== expectedCensusSha256) throw new Error('typed config census changed');
  if (!/^(0|[1-9]\d*)$/u.test(indexText ?? '')) throw new Error('invalid config index');
  const index = Number(indexText);
  if (!Number.isSafeInteger(index) || index >= configs.length) throw new Error('config index out of range');
  return configs[index];
}
export function boundedConfigIndices(census,stage) {
  const name = {packages:'openclaw-packages',unified:'openclaw-unified'}[stage];
  if (!name) throw new Error('invalid whole-config stage');
  const selected = census.filter(config => config.name === name);
  if (!selected.length || selected.some(config => stage === 'packages' ? !config.dts : config.dts !== false))
    throw new Error('typed/runtime config inventory mismatch');
  return selected.map(config => config.index);
}
export function boundedResultSucceeded(result) {
  return result.status === 0 && !result.timedOut && !result.error &&
    !result.fatalUnresolvedImport && !result.hasIneffectiveDynamicImport;
}
