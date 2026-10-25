import assert from 'node:assert/strict';
import { test } from 'node:test';
import { configCensus, selectWholeConfig } from '../../scripts/lib/isolated-config.mjs';
const configs = [
 {name:'packages',entry:{a:'packages/a.ts'},outDir:'packages/a/dist',dts:false},
 {name:'unified',entry:{gateway:'src/gateway.ts',sdk:'src/sdk.ts'},dts:false,plugins:[{}]},
 {name:'unified',entry:{worker:'src/worker.ts'},dts:false},
];
test('census preserves every ordered config and alias/source pair including duplicate group names',()=>{
 const census=configCensus(configs);
 assert.equal(census.length,3);
 assert.deepEqual(census[1],{index:1,name:'unified',entry:configs[1].entry,outDir:'dist',dts:false});
 assert.deepEqual(census.map(c=>c.index),[0,1,2]);
});
test('selection returns the entire original graph by identity',()=>{
 const census=JSON.stringify(configCensus(configs));
 for(let i=0;i<configs.length;i++) assert.equal(selectWholeConfig(configs,String(i),census),configs[i]);
 assert.equal(Object.keys(selectWholeConfig(configs,'1',census).entry).length,2);
});
test('refuses invalid indices, declaration graphs and drifted inventory',()=>{
 const census=JSON.stringify(configCensus(configs));
 for(const value of [undefined,'','-1','01','1.0','1x','3','9007199254740992'])
  assert.throws(()=>selectWholeConfig(configs,value,census));
 assert.throws(()=>selectWholeConfig([...configs].reverse(),'1',census));
 assert.throws(()=>selectWholeConfig(configs,'1',census.replace('sdk.ts','changed.ts')));
 assert.throws(()=>configCensus([{...configs[0],dts:true}]));
 assert.throws(()=>configCensus([]));
 assert.throws(()=>configCensus([{...configs[0],entry:['src/a.ts']}]));
});

import * as poolPolicy from './serial-probe598-policy.mjs';
test('one-CPU diagnostic owns fixed native pools without changing caller environment',()=>{
 assert.equal(typeof poolPolicy.fixedOneCpuCompilerEnv,'function');
 const input={PATH:'/fixture',TSX_DISABLE_CACHE:'1'};
 const before={...input};const env=poolPolicy.fixedOneCpuCompilerEnv(input);
 for(const key of ['ROLLDOWN_WORKER_THREADS','ROLLDOWN_MAX_BLOCKING_THREADS','RAYON_NUM_THREADS','TOKIO_WORKER_THREADS']) assert.equal(env[key],'1');
 assert.equal(env.OPENCLAW_RUN_NODE_SKIP_DTS_BUILD,'1');
 assert.deepEqual(input,before); assert.equal(env.PATH,input.PATH);
});
test('refuses inherited native worker controls before owner generates limits',()=>{
 for(const key of ['ROLLDOWN_WORKER_THREADS','ROLLDOWN_MAX_BLOCKING_THREADS','TOKIO_WORKER_THREADS','RAYON_RS_NUM_CPUS'])
  for(const value of ['', '0', '1', '100']) assert.throws(()=>poolPolicy.admitProbe({unresolved:false,capacityBytes:2*1024**3,limitBytes:1600*1024**2},{[key]:value},false));
});
