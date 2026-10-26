import {test} from 'node:test';
import assert from 'node:assert/strict';
import {admitBoundedPackage, boundedConfigIndices, typedConfigCensus,
 selectTypedWholeConfig, boundedResultSucceeded, UNIFIED_GRAPH_THRASH_LIMIT_BYTES,
 boundedCompilerStep, BOUNDED_COMPILER_ENV} from '../../scripts/lib/bounded-package608.mjs';
const admitted={unresolved:false,capacityBytes:2*1024**3,limitBytes:1800*1024**2};
test('bounded package preserves observed capacity floor and refuses compiler overrides',()=>{
 assert.doesNotThrow(()=>admitBoundedPackage(admitted,{}));
 for (const change of [{unresolved:true},{capacityBytes:3*1024**3},{limitBytes:UNIFIED_GRAPH_THRASH_LIMIT_BYTES},{limitBytes:null}])
   assert.throws(()=>admitBoundedPackage({...admitted,...change},{}));
 for (const key of ['NODE_OPTIONS','OPENCLAW_TSDOWN_MAX_OLD_SPACE_MB','OPENCLAW_RUN_NODE_SKIP_DTS_BUILD','OPENCLAW_BUILD_PRIVATE_QA','ROLLDOWN_WORKER_THREADS','MIMALLOC_ALLOW_THP','NAPI_RS_NATIVE_LIBRARY_PATH'])
   assert.throws(()=>admitBoundedPackage(admitted,{[key]:'1'}));
});
test('bounded package refuses verbose control that disables reviewed lazy barrels',()=>{
 for(const value of ['', '0', '1'])
   assert.throws(()=>admitBoundedPackage(admitted,{OPENCLAW_BUILD_VERBOSE:value}),/compiler control/u);
});
test('bounded package refuses every bundled plugin selector by presence',()=>{
 const accepted=[];
 for(const key of ['OPENCLAW_BUNDLED_PLUGIN_BUILD_IDS','OPENCLAW_INTERNAL_DOCKER_BUILD_PLUGIN_IDS','OPENCLAW_INCLUDE_OPTIONAL_BUNDLED']) {
   for(const value of ['', '0', '1']) {
     try {admitBoundedPackage(admitted,{[key]:value});accepted.push({key,value});}
     catch(error) {assert.match(error.message,/compiler control/u);}
   }
 }
 assert.deepEqual(accepted,[]);
});
test('whole config selection retains object identity and exact typed inventory',()=>{
 const configs=[{name:'openclaw-packages',entry:{x:'x.ts'},dts:true},
   {name:'openclaw-unified',entry:{a:'a.ts',b:'b.ts'},dts:false},
   {name:'openclaw-dts-base',entry:{a:'a.ts',b:'b.ts'},dts:{emitDtsOnly:true,entry:['a.ts']}}];
 const census=typedConfigCensus(configs);
 assert.deepEqual(boundedConfigIndices(census,'packages'),[0]);
 assert.deepEqual(boundedConfigIndices(census,'unified'),[1]);
 assert.equal(selectTypedWholeConfig(configs,'1',JSON.stringify(census)),configs[1]);
 assert.throws(()=>selectTypedWholeConfig(configs,'1','[]'));
 assert.throws(()=>selectTypedWholeConfig(configs,'3',JSON.stringify(census)));
 assert.throws(()=>boundedConfigIndices([{...census[0],dts:false}],'packages'));
 assert.throws(()=>boundedConfigIndices([{...census[1],dts:true}],'unified'));
});
test('bounded compiler stages cannot skip canonical typed gates',()=>{
 const step={label:'tsdown-packages',args:['original'],cache:{inputs:['x']}};
 assert.deepEqual(boundedCompilerStep(step).env, {...BOUNDED_COMPILER_ENV,OPENCLAW_PRESERVE_CLI_STARTUP_METADATA:'1'});
 for (const label of ['write-unified-entry-dts','write-plugin-sdk-entry-dts','ui:build','check-plugin-sdk-exports','runtime-postbuild']) {
   const canonical={label,args:['canonical']};
   assert.deepEqual(boundedCompilerStep(canonical),{...canonical,cache:undefined});
 }
});
test('compiler scanner failures and timeout cannot become package evidence',()=>{
 assert.equal(boundedResultSucceeded({status:0}),true);
 for (const change of [{status:1},{status:null},{timedOut:true},{error:'failure'},
   {fatalUnresolvedImport:'dependency'},{hasIneffectiveDynamicImport:true}])
   assert.equal(boundedResultSucceeded({status:0,...change}),false);
});
