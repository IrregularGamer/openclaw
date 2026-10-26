import assert from 'node:assert/strict';
import {test} from 'node:test';
import * as owner from '../../scripts/lib/worker-phases608.mjs';
const config={entry:{'worker/worker':'src/worker/worker-deploy-entry.ts'},dts:false,outDir:'dist',define:{WORKER_DEPLOY_BUILD:'true',SEALED_RUNTIME_BUILD:'true'},outputOptions:{codeSplitting:false},minify:{codegen:true,compress:true,mangle:{keepNames:true}},sourcemap:false,plugins:[{}]};
const ok={status:0,timedOut:false,error:null,hasIneffectiveDynamicImport:false,fatalUnresolvedImport:null};
test('only exact self-contained workers defer required minification',()=>{
 const selected=owner.workerBundleConfig(config);assert.equal(selected.minify,false);
 assert.deepEqual({...selected,minify:config.minify},config);
 const ordinary={entry:{x:'src/x.ts'},dts:false};assert.equal(owner.workerBundleConfig(ordinary),ordinary);
});
test('changed worker packaging/minify policy refuses instead of omitting a phase',()=>{
 for(const change of [{minify:false},{dts:true},{outputOptions:{codeSplitting:true}},{entry:{'worker/worker':'other.ts'}}])assert.throws(()=>owner.workerBundleConfig({...config,...change}));
});
test('each compiler refusal prevents minifier and second phase failure propagates',async()=>{
 for(const failure of [{...ok,status:1},{...ok,timedOut:true},{...ok,fatalUnresolvedImport:'missing'},{...ok,hasIneffectiveDynamicImport:true}]){
  let calls=0;const result=await owner.runWorkerPhases({config,invocation:{},remainingMs:()=>1000,run:async()=>{calls++;return failure;}});assert.equal(calls,1);assert.equal(result,failure);
 }
 let calls=0;const failure={...ok,status:1};const result=await owner.runWorkerPhases({config,invocation:{command:process.execPath,options:{env:{},stdio:['ignore','pipe','pipe']}},remainingMs:()=>1000,run:async()=>++calls===1?ok:failure});assert.equal(calls,2);assert.equal(result,failure);
});
test('settled bundle precedes fixed minifier and expired deadline refuses',async()=>{
 const order=[];let settled=false;
 await owner.runWorkerPhases({config,invocation:{command:process.execPath,options:{env:{},stdio:['ignore','pipe','pipe']}},remainingMs:()=>500,run:async invocation=>{if(!settled){order.push('bundle');await Promise.resolve();settled=true;}else{order.push('minify');assert.deepEqual(invocation.args,['scripts/minify-worker608.mjs','worker/worker','false']);}return ok;}});
 assert.deepEqual(order,['bundle','minify']);let calls=0;
 await assert.rejects(owner.runWorkerPhases({config,invocation:{},remainingMs:()=>0,run:async()=>{calls++;return ok;}}),/deadline/);assert.equal(calls,0);
});
