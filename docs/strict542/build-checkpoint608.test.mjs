import {test} from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs';
import path from 'node:path';
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
