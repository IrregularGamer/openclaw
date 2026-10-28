// Finite continuation of the canonical build owner. No installation authority.
import fs from 'node:fs';
import path from 'node:path';
import {createHash} from 'node:crypto';
import {isDeepStrictEqual as same} from 'node:util';
import {checkpointAncestry608} from './declaration-checkpoint608.mjs';
const require608=(ok,message)=>{if(!ok)throw new Error(message);};
export function shaFile608(file) {
 const fd=fs.openSync(file,fs.constants.O_RDONLY|fs.constants.O_NOFOLLOW),buffer=Buffer.allocUnsafe(1024*1024),hash=createHash('sha256');
 try {const before=fs.fstatSync(fd);require608(before.isFile(),'checkpoint requires regular file');for(let n;(n=fs.readSync(fd,buffer,0,buffer.length,null))>0;)hash.update(buffer.subarray(0,n));const after=fs.fstatSync(fd);require608(before.size===after.size&&before.mtimeMs===after.mtimeMs&&before.ctimeMs===after.ctimeMs,'checkpoint file changed during read');return hash.digest('hex');}finally{fs.closeSync(fd);}
}
export function portableBuildIdentity608(value,root) {
 if(typeof value==='string')return value===root?'$SOURCE':value.replaceAll(root+path.sep,'$SOURCE/');
 if(Array.isArray(value))return value.map(item=>portableBuildIdentity608(item,root));
 if(value&&typeof value==='object')return Object.fromEntries(Object.entries(value).map(([key,item])=>[portableBuildIdentity608(key,root),portableBuildIdentity608(item,root)]));
 return value;
}
export const digest608=value=>createHash('sha256').update(JSON.stringify(value)).digest('hex');
export function readJson608(file) {const stat=fs.lstatSync(file);require608(stat.isFile()&&!stat.isSymbolicLink()&&stat.nlink===1,'checkpoint JSON requires private regular file');return JSON.parse(fs.readFileSync(file,'utf8'));}
export function buildStage608(stage,labels,groups) {
 require608(Array.isArray(labels)&&new Set(labels).size===labels.length,'invalid canonical phases');
 const unified=labels.indexOf('write-unified-entry-dts'),sdk=labels.indexOf('write-plugin-sdk-entry-dts');
 require608(unified>0&&sdk>unified,'missing canonical declaration boundaries');
 if(stage==='runtime')return {labels:labels.slice(0,unified),predecessor:null};
 if(stage==='middle')return {labels:labels.slice(unified,sdk),predecessor:'runtime',join:'unified'};
 if(stage==='tail')return {labels:labels.slice(sdk),predecessor:'middle',join:'sdk'};
 if(stage==='complete')return {labels:[],predecessor:'tail'};
 const match=/^(unified|sdk)-(0|[1-9]\d*)$/.exec(stage);
 require608(match&&Number(match[2])<groups[match[1]].length,'unknown fixed build checkpoint stage');
 return {labels:[],kind:match[1],group:groups[match[1]][Number(match[2])],predecessor:match[1]==='unified'?'runtime':'middle'};
}
export function validatePhaseResults608(phases,labels) {
 require608(Array.isArray(phases)&&same(phases.map(item=>item.label),labels)&&phases.every(item=>item.status==='ran'&&Number.isFinite(item.durationMs)&&item.durationMs>=0),'checkpoint requires exact ordered successful original phases');
}
const safeName=name=>typeof name==='string'&&name&&!path.isAbsolute(name)&&!path.win32.isAbsolute(name)&&!name.split(/[\\/]/).some(part=>part==='..'||part==='.'||part==='');
const excluded=name=>['node_modules','.git','.artifacts','result598-build','strict542-checks'].includes(name)||name.startsWith('result608-');
export function workspaceInventory608(root,{data=false}={}) {
 checkpointAncestry608(root);const inventory={};
 function walk(directory,prefix='') {for(const name of fs.readdirSync(directory).sort()) {
  if(!data&&(name==='node_modules'||(!prefix&&excluded(name))))continue;
  const relative=prefix?`${prefix}/${name}`:name,file=path.join(directory,name),stat=fs.lstatSync(file);
  const mode=stat.mode&0o7777;
  if(stat.isDirectory()){inventory[relative]={kind:'directory',mode};walk(file,relative);}
  else if(stat.isSymbolicLink())inventory[relative]={kind:'link',mode,target:fs.readlinkSync(file)};
  else {require608(stat.isFile()&&(!data||stat.nlink===1),'unsupported or hardlinked checkpoint output');inventory[relative]={kind:'file',mode,sha256:shaFile608(file)};}
 }}walk(root);return inventory;
}
function validateInventory608(inventory) {
 require608(inventory&&typeof inventory==='object'&&!Array.isArray(inventory),'invalid checkpoint inventory');
 for(const [name,item]of Object.entries(inventory)) {
  require608(safeName(name)&&item&&['directory','file','link'].includes(item.kind)&&Number.isInteger(item.mode)&&item.mode>=0&&item.mode<=0o7777,'invalid checkpoint inventory entry');
  if(item.kind==='file')require608(/^[a-f0-9]{64}$/.test(item.sha256??''),'invalid checkpoint file digest');
  if(item.kind==='link')require608(typeof item.target==='string'&&!path.isAbsolute(item.target)&&!path.win32.isAbsolute(item.target)&&(resolved=>resolved!=='..'&&!resolved.startsWith('../'))(path.posix.normalize(path.posix.join(path.posix.dirname(name),item.target))),'checkpoint link escapes source');
  for(let parent=path.posix.dirname(name);parent!=='.';parent=path.posix.dirname(parent))require608(inventory[parent]?.kind==='directory','checkpoint output ancestor is not a directory');
 }
}
function materialize608(from,to,inventory) {
 validateInventory608(inventory);
 for(const [name,item]of Object.entries(inventory)) {
  const target=path.join(to,name),source=path.join(from,name);fs.mkdirSync(path.dirname(target),{recursive:true});
  if(item.kind==='directory'){fs.mkdirSync(target,{recursive:true});continue;}
  const existing=fs.lstatSync(target,{throwIfNoEntry:false});if(existing)fs.rmSync(target,{recursive:true,force:true});
  if(item.kind==='link')fs.symlinkSync(item.target,target);else fs.copyFileSync(source,target,fs.constants.COPYFILE_EXCL);
  if(item.kind!=='link')fs.chmodSync(target,item.mode);
 }
 for(const [name,item]of Object.entries(inventory).reverse())if(item.kind==='directory')fs.chmodSync(path.join(to,name),item.mode);
}
export function validateBuildReceipt608(receipt,{stage,identity,before,expectedLabels}) {
 require608(receipt.schema==='strict542-build-checkpoint608-v1'&&receipt.status==='CHECKPOINT_NOT_BUILT'&&receipt.stage===stage&&same(receipt.identity,identity),'checkpoint source/native/toolchain identity mismatch');
 require608(receipt.baselineSha256===digest608(before),'checkpoint fresh source inventory mismatch');
 validatePhaseResults608(receipt.phases,expectedLabels);validateInventory608(receipt.outputs);
 require608(Array.isArray(receipt.deleted)&&new Set(receipt.deleted).size===receipt.deleted.length&&receipt.deleted.every(name=>safeName(name)&&Object.hasOwn(before,name)&&!Object.hasOwn(receipt.outputs,name)),'invalid checkpoint deletion inventory');
 require608(Array.isArray(receipt.outputRoots)&&Array.isArray(receipt.ancestors),'missing checkpoint roots or ancestry');
}
export function writeBuildCheckpoint608({root,target,stage,identity,before,phases,expectedLabels,ancestors,outputRoots}) {
 validatePhaseResults608(phases,expectedLabels);require608(!fs.existsSync(target),'checkpoint already exists');
 const after=workspaceInventory608(root),outputs={};
 const selected=new Set(Object.keys(after).filter(name=>!same(after[name],before[name])||outputRoots.some(output=>name===output||name.startsWith(output+'/'))));
 for(const name of [...selected])for(let parent=path.posix.dirname(name);parent!=='.';parent=path.posix.dirname(parent))selected.add(parent);
 for(const name of Object.keys(after))if(selected.has(name))outputs[name]=after[name];
 validateInventory608(outputs);const deleted=Object.keys(before).filter(name=>!Object.hasOwn(after,name));
 const receipt={schema:'strict542-build-checkpoint608-v1',status:'CHECKPOINT_NOT_BUILT',stage,identity,baselineSha256:digest608(before),phases,ancestors,outputRoots,outputs,deleted};
 fs.mkdirSync(path.dirname(target),{recursive:true});checkpointAncestry608(path.dirname(target));const temporary=fs.mkdtempSync(path.join(path.dirname(target),'.build-checkpoint-'));
 try {fs.mkdirSync(path.join(temporary,'data'));materialize608(root,path.join(temporary,'data'),outputs);require608(same(workspaceInventory608(path.join(temporary,'data'),{data:true}),outputs),'checkpoint copy inventory mismatch');fs.writeFileSync(path.join(temporary,'receipt.json'),JSON.stringify(receipt)+'\n',{flag:'wx',mode:0o600});fs.renameSync(temporary,target);}finally{fs.rmSync(temporary,{recursive:true,force:true});}
 return receipt;
}
export function restoreBuildCheckpoint608({root,target,stage,identity,before,expectedLabels}) {
 checkpointAncestry608(target);require608(same(fs.readdirSync(target).sort(),['data','receipt.json']),'unexpected build checkpoint entries');
 const receipt=readJson608(path.join(target,'receipt.json'));validateBuildReceipt608(receipt,{stage,identity,before,expectedLabels});
 require608(same(workspaceInventory608(path.join(target,'data'),{data:true}),receipt.outputs),'checkpoint output inventory mismatch');
 // Verify everything before the first mutation; no traversing output symlink parents.
 for(const name of receipt.deleted.toSorted((a,b)=>b.length-a.length)){const parent=path.dirname(path.join(root,name));if(fs.existsSync(parent))checkpointAncestry608(parent);fs.rmSync(path.join(root,name),{recursive:true,force:true});}
 for(const name of Object.keys(receipt.outputs)){const parent=path.dirname(path.join(root,name));if(fs.existsSync(parent))checkpointAncestry608(parent);}
 materialize608(path.join(target,'data'),root,receipt.outputs);
 const restored=workspaceInventory608(root);for(const [name,item]of Object.entries(receipt.outputs))require608(same(restored[name],item),'restored checkpoint inventory mismatch');
 return receipt;
}

// Stage ancestry/group binding validators (moved unchanged from build-checkpoint608.mts so they are directly testable).
export function validateGroupBinding608(binding,{kind,group,predecessor,identity}) {
 require608(binding?.schema==='strict542-build-group-binding608-v1'&&binding.status==='COMPILED_GROUP_NOT_PUBLISHED'&&same(binding.identity,identity)&&binding.kind===kind&&binding.group===group&&binding.predecessorSha256===digest608(predecessor),'declaration predecessor workspace identity mismatch');
 require608(binding.receipt?.status==='COMPILED_GROUP_NOT_PUBLISHED'&&binding.receipt.group===group&&binding.receipt.source_commit===identity.sourceCommit&&binding.receipt.source_export_sha256===identity.sourceExportSha256,'missing successful canonical group receipt');
 require608(/^[a-f0-9]{64}$/.test(binding.inventorySha256??''),'missing complete group inventory binding');
}
export function validateBuildChain608(receipt,{identity,before,outputRoots,labels,groups}) {
 validateBuildReceipt608(receipt,{stage:receipt.stage,identity,before,expectedLabels:buildStage608(receipt.stage,labels,groups).labels});
 require608(['runtime','middle','tail'].includes(receipt.stage)&&same(receipt.outputRoots,outputRoots),'invalid canonical checkpoint stage or roots');
 if(receipt.stage==='runtime'){require608(receipt.ancestors.length===0,'runtime checkpoint has predecessors');return;}
 const kind=receipt.stage==='middle'?'unified':'sdk',predecessor=receipt.stage==='middle'?'runtime':'middle';
 require608(receipt.ancestors.length===groups[kind].length+1&&receipt.ancestors[0]?.stage===predecessor,'missing exact checkpoint ancestry');
 validateBuildChain608(receipt.ancestors[0],{identity,before,outputRoots,labels,groups});
 for(const [index,group]of groups[kind].entries())validateGroupBinding608(receipt.ancestors[index+1],{kind,group,predecessor:receipt.ancestors[0],identity});
}
export function validateCompleteCheckpoint608(predecessor,labels) {
 require608(predecessor?.stage==='tail','complete requires canonical tail');
 const middle=predecessor.ancestors[0],runtime=middle.ancestors[0];
 validatePhaseResults608([...runtime.phases,...middle.phases,...predecessor.phases],labels);
}
