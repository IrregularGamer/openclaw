// SOURCE ONLY. Run once from a reviewed admitted disposable secretless export.
// Does not create accepted build evidence or bypass the normal build preflight.
import fs from 'node:fs';
import { performance } from 'node:perf_hooks';
import { readProcessMemoryCapacity } from '../../scripts/lib/process-memory.mts';
import { configCensus } from '../../scripts/lib/isolated-config.mjs';
import { admitProbe, admitUnifiedGraphCapacity, probeSucceeded, fixedOneCpuCompilerEnv, ONE_CPU_NATIVE_POOLS, BOUNDED_NATIVE_ALLOCATOR } from './serial-probe598-policy.mjs';
const capacity=readProcessMemoryCapacity({});
admitUnifiedGraphCapacity(capacity);
admitProbe(capacity,process.env,['.git','dist','dist-runtime','isolated-probe598.json'].some(p=>fs.existsSync(p)));
if (process.argv.length !== 2) throw new Error('probe accepts no caller arguments');
const env=fixedOneCpuCompilerEnv(process.env);
// Config evaluation must see the same runtime-only policy as the compiler child.
Object.assign(process.env,ONE_CPU_NATIVE_POOLS,BOUNDED_NATIVE_ALLOCATOR,{OPENCLAW_RUN_NODE_SKIP_DTS_BUILD:'1'});
// Initialize allocator policy before loading the build owner's transitive native imports.
const {resolveTsdownBuildInvocation,runTsdownBuildInvocation}=await import('../../scripts/tsdown-build.mts');
const deadline=performance.now()+900_000;
const {default:configs}=await import('../../tsdown.config.ts');
const census=configCensus(configs);
const receipt={kind:'DIAGNOSTIC_ONLY_NOT_BUILD_EVIDENCE',capacity,deadlineMs:900_000,census,
  inheritedOutputAndThreadControls:'ABSENT_VERIFIED_BY_ADMISSION',nativePools:ONE_CPU_NATIVE_POOLS,allocator:BOUNDED_NATIVE_ALLOCATOR,
  results:[] as unknown[]};
function save() {fs.writeFileSync('isolated-probe598.json',JSON.stringify(receipt)+'\n');}
fs.writeFileSync('isolated-probe598.json',JSON.stringify(receipt)+'\n',{flag:'wx'});
const plans=[{label:'ai',args:['--config','tsdown.ai.config.ts','--concurrency','1'],env},
  ...census.map(c=>({label:`main-config-${c.index}`,args:['--config','tsdown.isolated598.config.ts','--concurrency','1'],
    env:{...env,OPENCLAW_598_CONFIG_INDEX:String(c.index),OPENCLAW_598_CONFIG_CENSUS:JSON.stringify(census)}}))];
for (const plan of plans) {
  const remaining=Math.floor(deadline-performance.now());
  if (remaining<=0) throw new Error('absolute isolated probe deadline expired');
  const invocation=resolveTsdownBuildInvocation({args:plan.args,env:plan.env});
  for (const [key,value] of Object.entries({...ONE_CPU_NATIVE_POOLS,...BOUNDED_NATIVE_ALLOCATOR})) {
    if (invocation.options.env[key]!==value) throw new Error('native pool limit did not propagate: '+key);
  }
  console.log(JSON.stringify({kind:receipt.kind,label:plan.label,args:invocation.args,nativePools:ONE_CPU_NATIVE_POOLS,allocator:BOUNDED_NATIVE_ALLOCATOR,nodeOptions:invocation.options.env.NODE_OPTIONS,remaining}));
  const started=performance.now();
  const result=await runTsdownBuildInvocation(invocation,{env:{...env,OPENCLAW_TSDOWN_TIMEOUT_MS:String(remaining)}});
  receipt.results.push({label:plan.label,elapsedMs:performance.now()-started,result});
  save();
  if (!probeSucceeded(result)) {process.exitCode=1;break;}
}
