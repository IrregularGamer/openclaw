// SOURCE ONLY diagnostic: one unchanged original graph, with telemetry only.
import fs from 'node:fs';
import configs from '../../tsdown.config.ts';
import { selectWholeConfig } from '../../scripts/lib/isolated-config.mjs';
const selected = selectWholeConfig(configs, process.env.OPENCLAW_598_CONFIG_INDEX,
  process.env.OPENCLAW_598_CONFIG_CENSUS);
let timer: ReturnType<typeof setInterval> | undefined;
function sample(phase: string) {
  const kernel: Record<string,string> = {};
  for (const name of ['memory.current','memory.peak','memory.events','cpu.stat']) {
    try { kernel[name] = fs.readFileSync('/sys/fs/cgroup/'+name,'utf8').trim(); }
    catch { kernel[name] = 'unavailable'; }
  }
  console.log(JSON.stringify({kind:'ISOLATED_CONFIG_DIAGNOSTIC',index:process.env.OPENCLAW_598_CONFIG_INDEX,
    phase,pid:process.pid,memory:process.memoryUsage(),kernel}));
}
// Add no transform/resolve/output hooks: these observations cannot change modules.
export default {...selected,plugins:[selected.plugins,{
  name:'openclaw:isolated-config-telemetry598',
  buildStart() { sample('begin'); timer=setInterval(()=>sample('running'),30_000).unref(); },
  buildEnd(error: unknown) { sample(error ? 'build-error' : 'build-end'); clearInterval(timer); },
  closeBundle() { sample('closed'); clearInterval(timer); },
}]};
