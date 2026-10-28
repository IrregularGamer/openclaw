#!/usr/bin/env node
// Source-only fixed continuation. Outer runner owns admitted execution provenance.
import fs from 'node:fs';
import path from 'node:path';
import {pathToFileURL} from 'node:url';
import {execFileSync} from 'node:child_process';
import {isDeepStrictEqual as same} from 'node:util';
import {isDirectRunUrl} from './lib/direct-run.mjs';
import {typedConfigCensus,typedConfigCensusDigest} from './lib/bounded-package608.mjs';
import {TSDOWN_NON_SDK_DTS_CONFIG_GROUPS,TSDOWN_PLUGIN_SDK_DTS_CONFIG_GROUPS} from './lib/tsdown-config-groups.mts';
import {writeBoundedDeclarationCheckpoint608} from './lib/tsdown-declaration-writer.mts';
import {buildStage608,portableBuildIdentity608,digest608,shaFile608,readJson608,workspaceInventory608,writeBuildCheckpoint608,restoreBuildCheckpoint608,validateBuildReceipt608,validatePhaseResults608} from './lib/bounded-build-checkpoint608.mjs';
const groups={unified:[...TSDOWN_NON_SDK_DTS_CONFIG_GROUPS],sdk:[...TSDOWN_PLUGIN_SDK_DTS_CONFIG_GROUPS]};
const require608=(ok:unknown,message:string)=>{if(!ok)throw new Error(message);};
export function resolveBuildCheckpointStage608(stage:string,labels:string[]) {return buildStage608(stage,labels,groups);}

/** Called only after fresh bounded/native admission, preflight and live-dist fence. */
export async function prepareBuildCheckpoint608({stage,root,env,labels,outputRoots}:{stage:string;root:string;env:NodeJS.ProcessEnv;labels:string[];outputRoots:string[]}) {
 const selection=resolveBuildCheckpointStage608(stage,labels);
 require608(/^[a-f0-9]{40}$/.test(env.STRICT542_SOURCE_COMMIT??'')&&/^[a-f0-9]{64}$/.test(env.STRICT542_SOURCE_EXPORT_SHA256??''),'checkpoint requires verified common source archive');
 require608(env.OPENCLAW_608_BOUNDED_PACKAGE==='1'&&env.OPENCLAW_BUILD_CACHE==='0','checkpoint requires admitted native no-cache build');
 const directory=path.resolve(root,'../build608-checkpoints');
 fs.mkdirSync(directory,{recursive:true});
 const originalEnv={...process.env};Object.assign(process.env,env);
 let configs;try {({default:configs}=await import(pathToFileURL(path.join(root,'tsdown.config.ts')).href));}
 finally {for(const key of Object.keys(process.env))if(!Object.hasOwn(originalEnv,key))delete process.env[key];Object.assign(process.env,originalEnv);}
 const identity={sourceCommit:env.STRICT542_SOURCE_COMMIT,sourceExportSha256:env.STRICT542_SOURCE_EXPORT_SHA256,
  lockSha256:shaFile608(path.join(root,'pnpm-lock.yaml')),workspaceSha256:shaFile608(path.join(root,'pnpm-workspace.yaml')),
  packageSha256:shaFile608(path.join(root,'package.json')),node:process.version,pnpm:execFileSync('pnpm',['--version'],{encoding:'utf8'}).trim(),
  nativeCompileSha256:shaFile608(path.resolve(root,'../.native608/receipt.json')),
  nativeLibtestsSha256:shaFile608(path.resolve(root,'../.native608/libtests-receipt.json')),
  nativeAddonSha256:shaFile608(path.resolve(root,'../.native608/rolldown-binding.linux-x64-gnu.node')),
  configCensusSha256:typedConfigCensusDigest(portableBuildIdentity608(typedConfigCensus(configs),root)),
  environment:Object.fromEntries(['GIT_COMMIT','OPENCLAW_BUILD_TIMESTAMP','SOURCE_DATE_EPOCH','TZ','LANG','LC_ALL','CI'].map(name=>[name,env[name]??'']))};
 const before=workspaceInventory608(root);
 const expected=(name:string)=>resolveBuildCheckpointStage608(name,labels).labels;
 const validateChain=(receipt:any):void=>{
  validateBuildReceipt608(receipt,{stage:receipt.stage,identity,before,expectedLabels:expected(receipt.stage)});
  require608(['runtime','middle','tail'].includes(receipt.stage)&&same(receipt.outputRoots,outputRoots),'invalid canonical checkpoint stage or roots');
  if(receipt.stage==='runtime'){require608(receipt.ancestors.length===0,'runtime checkpoint has predecessors');return;}
  const kind=receipt.stage==='middle'?'unified':'sdk',predecessor=receipt.stage==='middle'?'runtime':'middle';
  require608(receipt.ancestors.length===groups[kind].length+1&&receipt.ancestors[0]?.stage===predecessor,'missing exact checkpoint ancestry');
  validateChain(receipt.ancestors[0]);
  for(const [index,group]of groups[kind].entries())validateBinding(receipt.ancestors[index+1],kind,group,receipt.ancestors[0]);
 };
 const validateBinding=(binding:any,kind:'unified'|'sdk',group:string,predecessor:any)=>{
  require608(binding?.schema==='strict542-build-group-binding608-v1'&&binding.status==='COMPILED_GROUP_NOT_PUBLISHED'&&same(binding.identity,identity)&&binding.kind===kind&&binding.group===group&&binding.predecessorSha256===digest608(predecessor),'declaration predecessor workspace identity mismatch');
  require608(binding.receipt?.status==='COMPILED_GROUP_NOT_PUBLISHED'&&binding.receipt.group===group&&binding.receipt.source_commit===identity.sourceCommit&&binding.receipt.source_export_sha256===identity.sourceExportSha256,'missing successful canonical group receipt');
  require608(/^[a-f0-9]{64}$/.test(binding.inventorySha256??''),'missing complete group inventory binding');
 };
 let predecessor:any=null;
 if(selection.predecessor) {
  const target=path.join(directory,selection.predecessor);
  predecessor=readJson608(path.join(target,'receipt.json'));validateChain(predecessor);
  restoreBuildCheckpoint608({root,target,stage:selection.predecessor,identity,before,expectedLabels:expected(selection.predecessor)});
 }
 const ancestors=predecessor?[predecessor]:[];
 if(selection.join) {
  for(const group of groups[selection.join as 'unified'|'sdk']) {
   const stored=path.join(directory,selection.join,group),binding=readJson608(stored+'.build608.json');
   validateBinding(binding,selection.join as 'unified'|'sdk',group,predecessor);
   require608(same(binding.receipt,readJson608(path.join(stored,'receipt.json')))&&binding.inventorySha256===digest608(workspaceInventory608(stored,{data:true})),'declaration group output inventory changed');
   ancestors.push(binding);
  }
 }
 const declaration=async(kind:'unified'|'sdk',mode:'produce'|'join',group?:string)=>{
  const original={...process.env};Object.assign(process.env,env);
  try {await writeBoundedDeclarationCheckpoint608(kind,{mode,group,directory:path.join(directory,kind),sourceCommit:identity.sourceCommit!,sourceExportSha256:identity.sourceExportSha256!});}
  finally {for(const key of Object.keys(process.env))if(!Object.hasOwn(original,key))delete process.env[key];Object.assign(process.env,original);}
 };
 if(selection.kind) {
  const kind=selection.kind as 'unified'|'sdk';fs.mkdirSync(path.join(directory,kind),{recursive:true});
  const stored=path.join(directory,kind,selection.group);
  require608(!fs.existsSync(stored+'.build608.json'),'group predecessor binding already exists');
  await declaration(kind,'produce',selection.group);
  const receipt=readJson608(path.join(stored,'receipt.json'));
  const binding={schema:'strict542-build-group-binding608-v1',status:'COMPILED_GROUP_NOT_PUBLISHED',kind,group:selection.group,identity,predecessorSha256:digest608(predecessor),receipt,inventorySha256:digest608(workspaceInventory608(stored,{data:true}))};
  validateBinding(binding,kind,selection.group,predecessor);
  fs.writeFileSync(stored+'.build608.json',JSON.stringify(binding)+'\n',{flag:'wx',mode:0o600});
 }
 if(stage==='complete') {
  require608(predecessor?.stage==='tail','complete requires canonical tail');
  const middle=predecessor.ancestors[0],runtime=middle.ancestors[0];
  validatePhaseResults608([...runtime.phases,...middle.phases,...predecessor.phases],labels);
 }
 return {labels:selection.labels,
  join:selection.join?()=>declaration(selection.join as 'unified'|'sdk','join'):null,
  finish:(phases:any[])=>{
   validatePhaseResults608(phases,selection.labels);
   if(['runtime','middle','tail'].includes(stage))writeBuildCheckpoint608({root,target:path.join(directory,stage),stage,identity,before,phases,expectedLabels:selection.labels,ancestors,outputRoots});
  }};
}
if(isDirectRunUrl(process.argv[1],import.meta.url)) {
 const args=process.argv.slice(2);if(args.length!==1)throw new Error('Usage: scripts/build-checkpoint608.mts <runtime|unified-0..5|middle|sdk-0..1|tail|complete>');
 const {runBuildAllSteps}=await import('./build-all.mts');
 const {withDistArtifactOwnership}=await import('./lib/dist-artifact-ownership.mts');
 const result=await withDistArtifactOwnership(process.cwd(),()=>runBuildAllSteps('boundedPackage',{boundedCheckpointStage:args[0]}));
 process.exitCode=result.exitCode;
}
