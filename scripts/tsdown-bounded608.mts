// Full/package build compiler scheduling only. The build-all owner retains all other gates.
import {runWorkerPhases} from './lib/worker-phases608.mjs';
import { performance } from 'node:perf_hooks';
import { readProcessMemoryCapacity } from './lib/process-memory.mts';
import { BOUNDED_COMPILER_ENV, UNIFIED_GRAPH_THRASH_LIMIT_BYTES,
  typedConfigCensus, boundedConfigIndices, boundedResultSucceeded } from './lib/bounded-package608.mjs';
const stage=process.argv[2] ?? '';
if (process.argv.length !== 3 || !['ai','packages','unified'].includes(stage)) throw new Error('invalid bounded compiler stage');
for (const [key,value] of Object.entries(BOUNDED_COMPILER_ENV)) {
  if (process.env[key] !== value) throw new Error('bounded compiler policy not inherited: '+key);
}
function capacityAdmission() {
  const capacity=readProcessMemoryCapacity({});
  if (capacity.unresolved || !Number.isFinite(capacity.limitBytes) ||
      capacity.limitBytes! <= UNIFIED_GRAPH_THRASH_LIMIT_BYTES ||
      !Number.isFinite(capacity.capacityBytes) || capacity.capacityBytes! > 2*1024**3)
    throw new Error('bounded compiler capacity no longer admitted');
  return capacity;
}
capacityAdmission();
// Native allocator and pool controls must precede transitive native imports.
const { resolveTsdownBuildPlan, resolveTsdownBuildInvocation, runTsdownBuildInvocation, sanitizeTsdownBuildOutputRoots,
  cleanTsdownOutputRoots, resolveTsdownCleanOutputRoots, pruneUntrackedGeneratedSourceDeclarations,
  pruneStaleRuntimeSymlinks } = await import('./tsdown-build.mts');
const deadline=performance.now()+900_000;
const {default:configs}=await import('../tsdown.config.ts');
const census=typedConfigCensus(configs);
const indices=stage === 'ai' ? [] : boundedConfigIndices(census,stage);
// Preserve canonical cleanup ownership once per original group, never between configs.
const originalArgs=stage === 'ai' ? ['--config','tsdown.ai.config.ts'] :
  ['--config','tsdown.config.ts','--filter',stage === 'packages' ? 'openclaw-packages' : 'openclaw-unified'];
if (Object.hasOwn(process.env,'OPENCLAW_TSDOWN_MAX_OLD_SPACE_MB') ||
    Object.hasOwn(process.env,'OPENCLAW_DOCKER_BUILD_TSDOWN_MAX_OLD_SPACE_MB'))
  throw new Error('bounded compiler refuses heap override');
const admission=resolveTsdownBuildPlan({args:originalArgs,env:process.env});
if (admission.heapShortfall?.fatal) throw new Error(admission.heapShortfall.message);
sanitizeTsdownBuildOutputRoots(originalArgs);
pruneUntrackedGeneratedSourceDeclarations();
pruneStaleRuntimeSymlinks();
cleanTsdownOutputRoots({roots:resolveTsdownCleanOutputRoots(originalArgs),
  env:{...process.env,OPENCLAW_RUN_NODE_SKIP_DTS_BUILD:stage === 'unified' ? '1' : '0'}});
const plans=stage === 'ai' ? [{config:null,label:'ai',args:['--config','tsdown.ai.config.ts','--concurrency','1'],env:process.env}] :
  indices.map(index=>({config:configs[index],label:`main-config-${index}`,args:['--config','tsdown.bounded608.config.ts','--concurrency','1'],
    env:{...process.env,OPENCLAW_608_CONFIG_INDEX:String(index),OPENCLAW_608_CONFIG_CENSUS:JSON.stringify(census)}}));
for (const plan of plans) {
  const capacity=capacityAdmission();
  const remaining=Math.floor(deadline-performance.now());
  if (remaining <= 0) throw new Error('bounded compiler absolute deadline expired');
  const invocation=resolveTsdownBuildInvocation({args:plan.args,env:plan.env});
  const result=await runWorkerPhases({config:plan.config,invocation,remainingMs:()=>deadline-performance.now(),run:runTsdownBuildInvocation});
  console.log(JSON.stringify({kind:'BOUNDED_PACKAGE_COMPILER',stage,label:plan.label,capacity,result}));
  if (!boundedResultSucceeded(result)) {process.exitCode=result.timedOut ? 124 : result.status || 1;break;}
}
