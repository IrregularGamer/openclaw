// Source-owned lifetime scheduling for the four portable self-contained workers.
export const WORKER_ENTRIES608=Object.freeze({
 'worker/worker':'src/worker/worker-deploy-entry.ts',
 'worker/file-tool-planning.worker':'src/worker/worker-deploy-file-tool-planning.ts',
 'worker/image-processor.worker':'src/worker/worker-deploy-image-processor.ts',
 'worker/sqlite-store.worker':'src/worker/worker-deploy-sqlite-store.ts',
});
export function workerEntry608(config) {
 const entries=Object.entries(config.entry ?? {});
 const candidate=entries.some(([key])=>Object.hasOwn(WORKER_ENTRIES608,key));
 if (!candidate) {
  if(config.define?.WORKER_DEPLOY_BUILD==='true' && config.minify?.compress===true)throw new Error('unsupported portable worker inventory');
  return null;
 }
 const [key,source]=entries[0];
 if(entries.length!==1 || WORKER_ENTRIES608[key]!==source || config.dts!==false ||
    config.outDir!=='dist' || config.define?.WORKER_DEPLOY_BUILD!=='true' ||
    config.define?.SEALED_RUNTIME_BUILD!=='true' || config.outputOptions?.codeSplitting!==false ||
    JSON.stringify(config.minify)!==JSON.stringify({codegen:true,compress:true,mangle:{keepNames:true}}) ||
    ![false,true].includes(config.sourcemap))throw new Error('portable worker packaging policy changed');
 return key;
}
export function workerBundleConfig(config) {
 return workerEntry608(config) ? {...config,minify:false} : config;
}
function succeeded(result) {
 return result.status===0 && !result.timedOut && !result.error &&
  !result.fatalUnresolvedImport && !result.hasIneffectiveDynamicImport;
}
export async function runWorkerPhases({config,invocation,remainingMs,run}) {
 const key=config ? workerEntry608(config) : null;
 async function execute(value) {
  const remaining=Math.floor(remainingMs());
  if(remaining<=0)throw new Error('worker phases shared deadline expired');
  return run(value,{env:{...value.options?.env,OPENCLAW_TSDOWN_TIMEOUT_MS:String(remaining)}});
 }
 const result=await execute(invocation);
 // run() is the existing process-group settlement owner. Never overlap phases.
 if(!key || !succeeded(result))return result;
 const next={...invocation,args:['scripts/minify-worker608.mjs',key,String(config.sourcemap)]};
 return execute(next);
}
