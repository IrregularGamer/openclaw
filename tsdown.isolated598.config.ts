// SOURCE ONLY diagnostic: one unchanged original graph, with telemetry only.
import fs from 'node:fs';
import configs from './tsdown.config.ts';
import { selectWholeConfig } from './scripts/lib/isolated-config.mjs';
const selected = selectWholeConfig(configs, process.env.OPENCLAW_598_CONFIG_INDEX,
  process.env.OPENCLAW_598_CONFIG_CENSUS);
let timer: ReturnType<typeof setInterval> | undefined;
function sample(phase: string) {
  let threads: number | null = null;
  try { threads=Number(/^Threads:\s+(\d+)$/m.exec(fs.readFileSync('/proc/self/status','utf8'))?.[1]) || null; } catch {}
  const nativePools=Object.fromEntries(['ROLLDOWN_WORKER_THREADS','ROLLDOWN_MAX_BLOCKING_THREADS','RAYON_NUM_THREADS','TOKIO_WORKER_THREADS'].map(key=>[key,process.env[key] ?? null]));
  const kernel: Record<string,string> = {};
  for (const name of ['memory.current','memory.peak','memory.events','cpu.stat']) {
    try { kernel[name] = fs.readFileSync('/sys/fs/cgroup/'+name,'utf8').trim(); }
    catch { kernel[name] = 'unavailable'; }
  }
  console.log(JSON.stringify({kind:'ISOLATED_CONFIG_DIAGNOSTIC',index:process.env.OPENCLAW_598_CONFIG_INDEX,
    phase,pid:process.pid,threads,nativePools,memory:process.memoryUsage(),kernel}));
}
// Add no transform/resolve/output hooks: these observations cannot change modules.
export default {...selected,plugins:[selected.plugins,{
  name:'openclaw:isolated-config-telemetry598',
  buildStart() { sample('begin'); timer=setInterval(()=>sample('running'),30_000).unref(); },
  buildEnd(error: unknown) { sample(error ? 'build-error' : 'build-end'); if (error) clearInterval(timer); },
  closeBundle() { sample('closed'); clearInterval(timer); },
}]};
