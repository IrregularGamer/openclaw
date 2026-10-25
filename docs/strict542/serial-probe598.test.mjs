import assert from 'node:assert/strict';
import {test} from 'node:test';
import {admitProbe, probeSucceeded} from './serial-probe598-policy.mjs';
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
