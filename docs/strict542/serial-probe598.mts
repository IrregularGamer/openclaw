// SOURCE ONLY diagnostic. Run only in an admitted offload disposable export.
// Does not call build-all, package runtime, or create accepted build evidence.
import fs from 'node:fs';
import { performance } from 'node:perf_hooks';
import { readProcessMemoryCapacity } from '../../scripts/lib/process-memory.mts';
import { resolveTsdownBuildInvocations, runTsdownBuildInvocation } from '../../scripts/tsdown-build.mts';
import { admitProbe, probeSucceeded } from './serial-probe598-policy.mjs';

const capacity = readProcessMemoryCapacity({});
admitProbe(capacity, process.env, ['.git', 'dist', 'dist-runtime', 'serial-probe598.json'].some(p=>fs.existsSync(p)));
if (process.argv.length !== 2) throw new Error('probe accepts no caller arguments');
const env = {...process.env, OPENCLAW_RUN_NODE_SKIP_DTS_BUILD:'1'};
const invocations = resolveTsdownBuildInvocations({args:['--concurrency','1'], env});
const deadline = performance.now()+900_000;
const receipt = {kind:'DIAGNOSTIC_ONLY_NOT_BUILD_EVIDENCE', capacity, concurrency:1, declarations:false,
  invocations:invocations.map(i=>({command:i.command,args:i.args})), results:[] as unknown[]};
fs.writeFileSync('serial-probe598.json', JSON.stringify(receipt)+'\n', {flag:'wx'});
for (const invocation of invocations) {
  const remaining = Math.floor(deadline-performance.now());
  if (remaining <= 0) throw new Error('absolute probe deadline expired');
  console.log(JSON.stringify({kind:receipt.kind,capacity,args:invocation.args}));
  const result = await runTsdownBuildInvocation(invocation,{env:{...env,OPENCLAW_TSDOWN_TIMEOUT_MS:String(remaining)}});
  receipt.results.push(result);
  fs.writeFileSync('serial-probe598.json', JSON.stringify(receipt)+'\n');
  if (!probeSucceeded(result)) {
    process.exitCode=1;
    break;
  }
}
