// SOURCE ONLY. Run once from a reviewed admitted disposable secretless export.
// Does not create accepted build evidence or bypass the normal build preflight.
import fs from 'node:fs';
import { performance } from 'node:perf_hooks';
import { readProcessMemoryCapacity } from '../../scripts/lib/process-memory.mts';
import { resolveTsdownBuildInvocation, runTsdownBuildInvocation } from '../../scripts/tsdown-build.mts';
import { configCensus } from '../../scripts/lib/isolated-config.mjs';
import { admitProbe, probeSucceeded } from './serial-probe598-policy.mjs';
const capacity=readProcessMemoryCapacity({});
admitProbe(capacity,process.env,['.git','dist','dist-runtime','isolated-probe598.json'].some(p=>fs.existsSync(p)));
if (process.argv.length !== 2) throw new Error('probe accepts no caller arguments');
const env={...process.env,OPENCLAW_RUN_NODE_SKIP_DTS_BUILD:'1'};
// Config evaluation must see the same runtime-only policy as the compiler child.
process.env.OPENCLAW_RUN_NODE_SKIP_DTS_BUILD='1';
const deadline=performance.now()+900_000;
const {default:configs}=await import('../../tsdown.config.ts');
const census=configCensus(configs);
const receipt={kind:'DIAGNOSTIC_ONLY_NOT_BUILD_EVIDENCE',capacity,deadlineMs:900_000,census,
  inheritedOutputAndThreadControls:'ABSENT_VERIFIED_BY_ADMISSION',
  results:[] as unknown[]};
function save() {fs.writeFileSync('isolated-probe598.json',JSON.stringify(receipt)+'\n');}
fs.writeFileSync('isolated-probe598.json',JSON.stringify(receipt)+'\n',{flag:'wx'});
const plans=[{label:'ai',args:['--config','tsdown.ai.config.ts','--concurrency','1'],env},
  ...census.map(c=>({label:`main-config-${c.index}`,args:['--config','docs/strict542/isolated-config598.mts','--concurrency','1'],
    env:{...env,OPENCLAW_598_CONFIG_INDEX:String(c.index),OPENCLAW_598_CONFIG_CENSUS:JSON.stringify(census)}}))];
for (const plan of plans) {
  const remaining=Math.floor(deadline-performance.now());
  if (remaining<=0) throw new Error('absolute isolated probe deadline expired');
  const invocation=resolveTsdownBuildInvocation({args:plan.args,env:plan.env});
  console.log(JSON.stringify({kind:receipt.kind,label:plan.label,args:invocation.args,remaining}));
  const started=performance.now();
  const result=await runTsdownBuildInvocation(invocation,{env:{...env,OPENCLAW_TSDOWN_TIMEOUT_MS:String(remaining)}});
  receipt.results.push({label:plan.label,elapsedMs:performance.now()-started,result});
  save();
  if (!probeSucceeded(result)) {process.exitCode=1;break;}
}
