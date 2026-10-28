import test from 'node:test';
import assert from 'node:assert/strict';
import {observeNativeApi608,propagateNativeObserver608} from './native-api-phases608.mjs';

function fixture(){
 class API {#value='private';async parseConfigFile(...args){return [this.#value,...args];}async createSnapshot(){}async close(){}}
 class Program {#value='program';async getSemanticDiagnostics(...args){return [this.#value,...args];}}
 for(const name of ['getConfigFileParsingDiagnostics','getProgramDiagnostics','getGlobalDiagnostics','getSyntacticDiagnostics','getBindDiagnostics','emitToString','getSourceFileNames'])Program.prototype[name]=async function(){return [];};
 return {API,Program};
}
test('observes exact receiver, arguments and result without logging arguments',async()=>{
 const api=fixture(),events=[];observeNativeApi608(api,event=>events.push(event),()=>12);
 const result=await new api.API().parseConfigFile('secret-test-only');
 assert.deepEqual(result,['private','secret-test-only']);
 assert.deepEqual(events.map(e=>e.phase),['start','end']);
 assert.ok(!JSON.stringify(events).includes('secret-test-only'));
 assert.deepEqual(await new api.Program().getSemanticDiagnostics(['a.ts']),['program',['a.ts']]);
});
test('preserves rejection identity and emits failure',async()=>{
 const api=fixture(),expected=new Error('original'),events=[];
 api.Program.prototype.getBindDiagnostics=async()=>{throw expected;};
 observeNativeApi608(api,event=>events.push(event));
 await assert.rejects(new api.Program().getBindDiagnostics(),error=>error===expected);
 assert.equal(events.at(-1).status,'failed');
});
test('does not complete or serialize pending requests',async()=>{
 const api=fixture(),events=[];let release;
 api.API.prototype.createSnapshot=()=>new Promise(resolve=>{release=resolve;});
 observeNativeApi608(api,event=>events.push(event));
 const value=new api.API(),pending=value.createSnapshot();
 await value.parseConfigFile();assert.equal(events.filter(e=>e.phase==='end').length,1);
 release(42);assert.equal(await pending,42);assert.equal(events.at(-1).method,'API.createSnapshot');
});
test('refuses unsupported APIs before modifying any method',()=>{
 const api=fixture(),original=api.API.prototype.parseConfigFile;delete api.Program.prototype.emitToString;
 assert.throws(()=>observeNativeApi608(api),/unsupported native API/);
 assert.equal(api.API.prototype.parseConfigFile,original);
});
test('refuses a duplicate installation',()=>{
 const api=fixture();observeNativeApi608(api,()=>{});assert.throws(()=>observeNativeApi608(api),/already observed/);
});
test('propagates only to exact Node children and preserves options and results',()=>{
 const calls=[],result={child:true},cp={spawn(...args){calls.push(args);return result;}},options={cwd:'/source',env:{TEST_ONLY:'value'}};
 propagateNativeObserver608(cp,'/observer.mjs','/fixed/node');
 assert.equal(cp.spawn('/fixed/node',['entry.mjs'],options),result);
 assert.deepEqual(calls[0],['/fixed/node',['--import','/observer.mjs','entry.mjs'],options]);
 cp.spawn('/other/node',['entry.mjs'],options);assert.deepEqual(calls[1],['/other/node',['entry.mjs'],options]);
 cp.spawn('/fixed/node',['--import','/observer.mjs','entry.mjs'],options);assert.equal(calls[2][1].length,3);
 cp.spawn('/fixed/node',options);assert.deepEqual(calls[3],['/fixed/node',['--import','/observer.mjs'],options]);
});
test('preserves original spawn errors',()=>{
 const expected=new Error('spawn failure'),cp={spawn(){throw expected;}};
 propagateNativeObserver608(cp,'/observer.mjs','/fixed/node');assert.throws(()=>cp.spawn('/fixed/node',[]),error=>error===expected);
});
