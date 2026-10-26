// ONE source-only portable-worker diagnostic. No accepted full build evidence.
import fs from 'node:fs';
import {performance} from 'node:perf_hooks';
import {readProcessMemoryCapacity} from '../../scripts/lib/process-memory.mts';
import {admitProbe,admitUnifiedGraphCapacity,fixedOneCpuCompilerEnv} from './serial-probe598-policy.mjs';
import {configCensus} from '../../scripts/lib/isolated-config.mjs';
import {workerEntry608,runWorkerPhases,WORKER_ENTRIES608} from '../../scripts/lib/worker-phases608.mjs';
if(process.argv.length!==2)throw new Error('worker probe accepts no arguments');
const capacity=readProcessMemoryCapacity({});
admitUnifiedGraphCapacity(capacity);admitProbe(capacity,process.env,fs.existsSync('dist'));
const env=fixedOneCpuCompilerEnv(process.env);Object.assign(process.env,env);
const {resolveTsdownBuildInvocation,runTsdownBuildInvocation}=await import('../../scripts/tsdown-build.mts');
const {default:configs}=await import('../../tsdown.config.ts');
const census=configCensus(configs);const selected=configs.map((config,index)=>({config,index,key:workerEntry608(config)})).filter(p=>p.key);
if(JSON.stringify(selected.map(p=>p.key))!==JSON.stringify(Object.keys(WORKER_ENTRIES608)))throw new Error('complete worker inventory changed');
const deadline=performance.now()+900_000;
const receipt={kind:'WORKER_PHASE_DIAGNOSTIC_ONLY_NOT_PACKAGE',compiler:'stock-rolldown1.2.9',capacity,results:[] as unknown[]};
const save=()=>fs.writeFileSync('worker-probe608.json',JSON.stringify(receipt)+'\n');save();
for(const plan of selected) {
 const invocation=resolveTsdownBuildInvocation({args:['--config','tsdown.isolated598.config.ts','--concurrency','1'],env:{...env,OPENCLAW_598_CONFIG_INDEX:String(plan.index),OPENCLAW_598_CONFIG_CENSUS:JSON.stringify(census)}});
 const phases=[] as unknown[];const start=performance.now();
 const result=await runWorkerPhases({config:plan.config,invocation,remainingMs:()=>deadline-performance.now(),run:async (child,options)=>{
  const result=await runTsdownBuildInvocation(child,options);phases.push({args:child.args,result});return result;
 }});
 receipt.results.push({key:plan.key,index:plan.index,elapsedMs:performance.now()-start,phases,result});save();
 if(result.status!==0 || result.timedOut || result.error || result.fatalUnresolvedImport || result.hasIneffectiveDynamicImport){process.exitCode=1;break;}
}
if(receipt.results.length!==4)process.exitCode=1;
