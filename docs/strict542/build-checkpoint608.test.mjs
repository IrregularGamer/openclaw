import {test} from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs';
import path from 'node:path';
import {spawnSync} from 'node:child_process';
import {buildStage608, workspaceInventory608, writeBuildCheckpoint608, restoreBuildCheckpoint608, validatePhaseResults608} from '../../scripts/lib/bounded-build-checkpoint608.mjs';
const labels=['clean:dist','plugins:assets:build','tsdown-ai','tsdown-packages','tsdown-unified','write-unified-entry-dts','external-plugins:local-dist','check-cli-bootstrap-imports','plugins:assets:copy','runtime-postbuild','build-stamp','runtime-postbuild-stamp','write-plugin-sdk-entry-dts','check-plugin-sdk-exports','ui:build','write-build-info','write-cli-startup-metadata'];
const groups={unified:['base','e1','e2','e3','e4','e5'],sdk:['s1','s2']};
test('fixed stages partition precisely the complete original bounded package phases',()=>{
 assert.deepEqual(['runtime','middle','tail'].flatMap(stage=>buildStage608(stage,labels,groups).labels),labels);
 assert.equal(buildStage608('unified-5',labels,groups).group,'e5');
 for(const stage of ['unified-6','sdk-2','caller','runtime-0'])assert.throws(()=>buildStage608(stage,labels,groups));
 for(const status of ['cached','reused','failed'])assert.throws(()=>validatePhaseResults608([{label:'a',status,durationMs:1}],['a']));
 assert.throws(()=>validatePhaseResults608([{label:'b',status:'ran',durationMs:1}],['a']));
 assert.throws(()=>validatePhaseResults608([{label:'a',status:'ran',durationMs:1},{label:'a',status:'ran',durationMs:1}],['a']));
});
test('workspace checkpoint retains every generated root, file/link modes and deletions and refuses tampered output or source',()=>{
 const parent=fs.mkdtempSync('/var/tmp/build-checkpoint608-'),root=path.join(parent,'source');fs.mkdirSync(root);
 try {
  fs.writeFileSync(path.join(root,'source.ts'),'source');fs.writeFileSync(path.join(root,'deleted'),'old');
  const before=workspaceInventory608(root),identity={sourceCommit:'a'.repeat(40),sourceExportSha256:'b'.repeat(64)};
  fs.mkdirSync(path.join(root,'assets'));fs.writeFileSync(path.join(root,'assets/new'),'bytes',{mode:0o700});fs.symlinkSync('new',path.join(root,'assets/link'));fs.unlinkSync(path.join(root,'deleted'));
  const target=path.join(parent,'checkpoint');
  const receipt=writeBuildCheckpoint608({root,target,stage:'runtime',identity,before,phases:[{label:'a',status:'ran',durationMs:1}],expectedLabels:['a'],ancestors:[],outputRoots:['assets']});
  assert.equal(receipt.status,'CHECKPOINT_NOT_BUILT');
  fs.rmSync(path.join(root,'assets'),{recursive:true});fs.writeFileSync(path.join(root,'deleted'),'old');
  restoreBuildCheckpoint608({root,target,stage:'runtime',identity,before,expectedLabels:['a']});
  assert.equal(fs.readlinkSync(path.join(root,'assets/link')),'new');assert.equal(fs.statSync(path.join(root,'assets/new')).mode&0o777,0o700);assert.equal(fs.existsSync(path.join(root,'deleted')),false);
  fs.writeFileSync(path.join(target,'data/assets/new'),'tampered');
  assert.throws(()=>restoreBuildCheckpoint608({root,target,stage:'runtime',identity,before,expectedLabels:['a']}),/inventory/);
  assert.throws(()=>restoreBuildCheckpoint608({root,target,stage:'runtime',identity:{...identity,sourceCommit:'c'.repeat(40)},before,expectedLabels:['a']}),/identity/);
 }finally{fs.rmSync(parent,{recursive:true,force:true});}
});
test('failed and incomplete phases never publish a checkpoint',()=>{
 const parent=fs.mkdtempSync('/var/tmp/build-checkpoint608-');
 try {const root=path.join(parent,'source');fs.mkdirSync(root);const before=workspaceInventory608(root),target=path.join(parent,'checkpoint');
  assert.throws(()=>writeBuildCheckpoint608({root,target,stage:'runtime',identity:{},before,phases:[],expectedLabels:['a'],ancestors:[],outputRoots:[]}));assert.equal(fs.existsSync(target),false);
 }finally{fs.rmSync(parent,{recursive:true,force:true});}
});
test('portable source census is identical across fresh export roots',async()=>{
 const {portableBuildIdentity608,digest608}=await import('../../scripts/lib/bounded-build-checkpoint608.mjs');
 assert.equal(digest608(portableBuildIdentity608({entry:{base:'/export/A/src/base.ts'},outDir:'/export/A/dist'},'/export/A')),digest608(portableBuildIdentity608({entry:{base:'/export/B/src/base.ts'},outDir:'/export/B/dist'},'/export/B')));
});

test('stage ancestry/group bindings refuse missing, extra, foreign, drifted, reordered and incomplete chains',async()=>{
 const {validateBuildChain608,validateCompleteCheckpoint608,digest608}=await import('../../scripts/lib/bounded-build-checkpoint608.mjs');
 const identity={sourceCommit:'a'.repeat(40),sourceExportSha256:'b'.repeat(64)},before={'source.ts':{kind:'file',mode:0o644,sha256:'c'.repeat(64)}},outputRoots=['dist'];
 const phases=stage=>buildStage608(stage,labels,groups).labels.map(label=>({label,status:'ran',durationMs:1}));
 const checkpoint=(stage,ancestors)=>({schema:'strict542-build-checkpoint608-v1',status:'CHECKPOINT_NOT_BUILT',stage,identity,baselineSha256:digest608(before),phases:phases(stage),ancestors,outputRoots,outputs:{},deleted:[]});
 const binding=(kind,group,predecessor)=>({schema:'strict542-build-group-binding608-v1',status:'COMPILED_GROUP_NOT_PUBLISHED',kind,group,identity,predecessorSha256:digest608(predecessor),
  receipt:{status:'COMPILED_GROUP_NOT_PUBLISHED',group,source_commit:identity.sourceCommit,source_export_sha256:identity.sourceExportSha256},inventorySha256:'d'.repeat(64)});
 const runtime=checkpoint('runtime',[]);
 const middle=checkpoint('middle',[runtime,...groups.unified.map(g=>binding('unified',g,runtime))]);
 const tail=checkpoint('tail',[middle,...groups.sdk.map(g=>binding('sdk',g,middle))]);
 const options={identity,before,outputRoots,labels,groups};
 assert.doesNotThrow(()=>validateBuildChain608(tail,options));assert.doesNotThrow(()=>validateCompleteCheckpoint608(tail,labels));
 const clone=value=>structuredClone(value);
 const mutated=[
  [t=>{t.ancestors[0].ancestors.pop();},/ancestry/],                                   // missing unified group
  [t=>{t.ancestors.push(binding('sdk','s3',t.ancestors[0]));},/ancestry/],            // extra sdk group
  [t=>{[t.ancestors[1],t.ancestors[2]]=[t.ancestors[2],t.ancestors[1]];},/predecessor/],// reordered groups
  [t=>{t.ancestors[1].predecessorSha256='0'.repeat(64);},/predecessor/],              // foreign predecessor digest
  [t=>{t.ancestors[0].ancestors[3].identity={...identity,sourceCommit:'e'.repeat(40)};},/predecessor/],// group source drift
  [t=>{t.ancestors[2].receipt.source_export_sha256='f'.repeat(64);},/group receipt/],  // group receipt drift
  [t=>{t.ancestors[1].receipt.status='BUILT';},/group receipt/],
  [t=>{delete t.ancestors[1].inventorySha256;},/inventory/],
  [t=>{t.outputRoots=['dist','extra'];},/roots/],
  [t=>{t.ancestors[0].ancestors[0].ancestors=[clone(runtime)];},/predecessors/],
  [t=>{t.ancestors[0]=clone(tail);},/ancestry/],                                        // wrong predecessor stage order
  [t=>{t.identity={...identity,sourceCommit:'e'.repeat(40)};},/identity/],
  [t=>{t.phases.pop();},/./],
 ];
 for(const [change,error] of mutated){const t=clone(tail);change(t);assert.throws(()=>validateBuildChain608(t,options),error);}
 for(const predecessor of [null,middle,runtime])assert.throws(()=>validateCompleteCheckpoint608(predecessor,labels),/canonical tail/);
 const short=clone(tail);short.phases.pop();assert.throws(()=>validateCompleteCheckpoint608(short,labels));
});
test('checkpoint links resolving to exactly the parent or above are refused (F1)',async()=>{
 const {validateBuildReceipt608,digest608}=await import('../../scripts/lib/bounded-build-checkpoint608.mjs');
 const identity={sourceCommit:'a'.repeat(40)},before={};
 const receipt=outputs=>({schema:'strict542-build-checkpoint608-v1',status:'CHECKPOINT_NOT_BUILT',stage:'runtime',identity,baselineSha256:digest608(before),phases:[{label:'a',status:'ran',durationMs:1}],ancestors:[],outputRoots:[],outputs,deleted:[]});
 const check=outputs=>validateBuildReceipt608(receipt(outputs),{stage:'runtime',identity,before,expectedLabels:['a']});
 assert.doesNotThrow(()=>check({dist:{kind:'directory',mode:0o755},'dist/same':{kind:'link',mode:0o777,target:'.'},'dist/up':{kind:'link',mode:0o777,target:'..'}}));
 for(const outputs of [{up:{kind:'link',mode:0o777,target:'..'}},{dist:{kind:'directory',mode:0o755},'dist/up2':{kind:'link',mode:0o777,target:'../..'}},{up3:{kind:'link',mode:0o777,target:'a/../../b'}}])
  assert.throws(()=>check(outputs),/escapes source/);
});

test('job608 checkpoint entry injects its preparer instead of a top-level-await self-import cycle', () => {
 // Runtime stage exit 13 (2026-10-28): build-all dynamically imported build-checkpoint608.mts while that
 // module was the entry still awaiting runBuildAllSteps, so neither promise could settle.
 const entry=fs.readFileSync(new URL('../../scripts/build-checkpoint608.mts',import.meta.url),'utf8');
 const all=fs.readFileSync(new URL('../../scripts/build-all.mts',import.meta.url),'utf8');
 assert.match(entry,/runBuildAllSteps\('boundedPackage',\{boundedCheckpointStage:args\[0\],prepareCheckpoint:prepareBuildCheckpoint608\}\)/);
 assert.match(all,/params\.prepareCheckpoint \?\? \(await import\("\.\/build-checkpoint608\.mts"\)\)\.prepareBuildCheckpoint608/);
 const dir=fs.mkdtempSync('/var/tmp/tla608-');
 fs.writeFileSync(path.join(dir,'main.mjs'),"export function prep(){return 'ok'}\nconst {run}=await import('./lib.mjs');\nconsole.log(await run(process.argv[2]==='inject'?prep:null));\n");
 fs.writeFileSync(path.join(dir,'lib.mjs'),"export async function run(p){return (p ?? (await import('./main.mjs')).prep)();}\n");
 const run=mode=>spawnSync(process.execPath,[path.join(dir,'main.mjs'),mode],{encoding:'utf8'});
 assert.equal(run('import').status,13);
 const injected=run('inject');assert.equal(injected.status,0);assert.equal(injected.stdout.trim(),'ok');
 fs.rmSync(dir,{recursive:true,force:true});
});
