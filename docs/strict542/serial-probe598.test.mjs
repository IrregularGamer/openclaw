import assert from 'node:assert/strict';
import {test} from 'node:test';
import {admitProbe, admitUnifiedGraphCapacity, UNIFIED_GRAPH_THRASH_LIMIT_BYTES, probeSucceeded} from './serial-probe598-policy.mjs';
const capacity = {unresolved:false, capacityBytes:2*1024**3, limitBytes:1600*1024**2};
test('admits fixed serial diagnostic only with observed bounded capacity',()=>{
  assert.doesNotThrow(()=>admitProbe(capacity,{},false));
});
test('refuses unknown or oversized capacity and existing output',()=>{
  for(const value of [null,NaN,Infinity,0,2*1024**3+1])
    assert.throws(()=>admitProbe({...capacity,capacityBytes:value},{},false));
  assert.throws(()=>admitProbe({...capacity,unresolved:true},{},false));
  assert.throws(()=>admitProbe(capacity,{},true));
});
test('refuses caller-controlled compiler budget, selection, preload or plugin exclusions',()=>{
  for(const key of ['NODE_OPTIONS','OPENCLAW_TSDOWN_MAX_OLD_SPACE_MB','OPENCLAW_DOCKER_BUILD_TSDOWN_MAX_OLD_SPACE_MB','OPENCLAW_INTERNAL_DOCKER_BUILD_PLUGIN_IDS','OPENCLAW_BUILD_PRIVATE_QA','OPENCLAW_RUN_NODE_SKIP_DTS_BUILD'])
    assert.throws(()=>admitProbe(capacity,{[key]:'1'},false));
});
test('compiler warnings, unresolved imports and unsettled/failed runs refuse success',()=>{
 const good={status:0,timedOut:false,error:null,fatalUnresolvedImport:null,hasIneffectiveDynamicImport:false};
 assert.equal(probeSucceeded(good),true);
 for(const changed of [{status:1},{status:null},{timedOut:true},{error:new Error('spawn')},{fatalUnresolvedImport:'missing'},{hasIneffectiveDynamicImport:true}])
   assert.equal(probeSucceeded({...good,...changed}),false);
});
test('accepts only the owning tsx launcher cache-disabled value',()=>{
 assert.doesNotThrow(()=>admitProbe(capacity,{TSX_DISABLE_CACHE:'1'},false));
 for(const value of ['', '0', 'true']) assert.throws(()=>admitProbe(capacity,{TSX_DISABLE_CACHE:value},false));
});

test('refuses inherited output and native thread scheduling controls even when empty',()=>{
 for(const key of ['OUTPUT_SOURCE_MAPS','RAYON_NUM_THREADS','UV_THREADPOOL_SIZE'])
  for(const value of ['', '0', '1', '8']) assert.throws(()=>admitProbe(capacity,{[key]:value},false));
});


import {fixedOneCpuCompilerEnv,BOUNDED_NATIVE_ALLOCATOR} from './serial-probe598-policy.mjs';
test('refuses inherited allocator controls even when empty or matching generated policy',()=>{
 for(const key of ['MIMALLOC_ALLOW_THP','MIMALLOC_PURGE_DELAY','MIMALLOC_RESERVE_HUGE_OS_PAGES','mimalloc_allow_thp'])
  for(const value of ['', '0', '1']) assert.throws(()=>admitProbe(capacity,{[key]:value},false));
});
test('fixed allocator policy preserves caller and pool bounds without raising any budget',()=>{
 const caller={PATH:'/fixture'}; const env=fixedOneCpuCompilerEnv(caller);
 assert.deepEqual(caller,{PATH:'/fixture'});
 assert.deepEqual(BOUNDED_NATIVE_ALLOCATOR,{MIMALLOC_ALLOW_THP:'0'});
 assert.equal(Object.isFrozen(BOUNDED_NATIVE_ALLOCATOR),true);
 assert.equal(env.MIMALLOC_ALLOW_THP,'0');
 assert.equal(env.ROLLDOWN_WORKER_THREADS,'1');
 assert.equal(env.ROLLDOWN_MAX_BLOCKING_THREADS,'1');
 assert.equal(env.NODE_OPTIONS,undefined);
 assert.equal(env.OPENCLAW_TSDOWN_MAX_OLD_SPACE_MB,undefined);
});
test('refuses the unified graph at or below the observed reclaim-thrash limit',()=>{
  for (const limitBytes of [UNIFIED_GRAPH_THRASH_LIMIT_BYTES, 1024**3, NaN, undefined])
    assert.throws(()=>admitUnifiedGraphCapacity({...capacity,limitBytes}),/reclaim-thrash/);
  assert.throws(()=>admitUnifiedGraphCapacity({...capacity,limitBytes:UNIFIED_GRAPH_THRASH_LIMIT_BYTES}),
    /capacityBytes=2147483648, limitBytes=1625784320,.*floorBytes=1625784320/);
  assert.doesNotThrow(()=>admitUnifiedGraphCapacity({...capacity,limitBytes:UNIFIED_GRAPH_THRASH_LIMIT_BYTES+1}));
});
