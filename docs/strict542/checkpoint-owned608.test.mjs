import {test} from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs';
import path from 'node:path';
import {pathToFileURL} from 'node:url';
import {stripTypeScriptTypes} from 'node:module';
const data=s=>'data:text/javascript;base64,'+Buffer.from(s).toString('base64');
test('checkpoint uses supported inherited owner and retains unjoined fencing',async()=>{
 const root=fs.mkdtempSync('/var/tmp/checkpoint-owned608-'),cwd=process.cwd(),argv=process.argv;
 try {
  const state=path.join(root,'state.mjs');
  fs.writeFileSync(state,`export const state={held:false,acquires:0};export async function acquireFileLock(){state.acquires++;if(state.held)throw new Error('SELF_WAIT');state.held=true;return {release:async()=>{state.held=false}}}`);
  const stateUrl=pathToFileURL(state).href;
  const ownerPath=process.env.DIST_OWNER_FIXTURE608??path.resolve('scripts/lib/dist-artifact-lock.mts');
  let owner=stripTypeScriptTypes(fs.readFileSync(ownerPath,'utf8'));
  const replacements={
   '@openclaw/fs-safe/file-lock':stateUrl,
   '@openclaw/fs-safe/root':data('export const root=async()=>({});'),
   './managed-child-process.mts':data('export const hasUnjoinedWork=e=>e?.unjoined===true;'),
   './record-shared.mjs':data('export const isRecord=x=>x!==null&&typeof x==="object";'),
   './repo-root.mjs':data('export const findRepoRoot=()=>null;'),
  };
  for(const [specifier,url] of Object.entries(replacements))owner=owner.replaceAll(JSON.stringify(specifier),JSON.stringify(url));
  const ownerUrl=data(owner),api=await import(ownerUrl),{state:s}=await import(stateUrl);
  process.chdir(root);
  await assert.rejects(api.withDistArtifactOwnership(root,()=>api.withDistArtifactOwnership(root,async()=>{})),/SELF_WAIT|Could not acquire/);
  assert.equal(s.acquires,2);assert.equal(s.held,false);
  const entry=path.join(root,'entry.mjs');
  fs.writeFileSync(entry,`import {withDistArtifactOwnership} from ${JSON.stringify(ownerUrl)};await withDistArtifactOwnership(process.cwd(),async()=>{if(process.argv[2]==='sdk-0')throw Object.assign(new Error('unjoined'),{unjoined:true});});`);
  let launcher=fs.readFileSync(path.join(cwd,'scripts/build-checkpoint608-owned.mjs'),'utf8');
  launcher=launcher.replaceAll('"./lib/dist-artifact-ownership.mts"',JSON.stringify(ownerUrl)).replaceAll('"./lib/dist-artifact-lock.mts"',JSON.stringify(ownerUrl)).replaceAll('"./lib/direct-run.mjs"',JSON.stringify(data('export const isDirectRunUrl=()=>false;')));
  const load=href=>import(data(launcher.replace('new URL("./build-checkpoint608.mts", import.meta.url).href',JSON.stringify(href))));
  const {runCheckpoint608}=await load(pathToFileURL(entry).href);
  s.acquires=0;await runCheckpoint608(['unified-0']);assert.equal(s.acquires,1);assert.equal(s.held,false);
  assert.deepEqual(fs.readdirSync(path.join(root,'.artifacts/dist-artifacts.lock')),[]);
  s.acquires=0;const failed=await load(pathToFileURL(entry).href+'?unjoined');await assert.rejects(failed.runCheckpoint608(['sdk-0']),/unjoined/);assert.equal(s.acquires,1);assert.equal(s.held,true);
  assert.equal(fs.existsSync(path.join(root,'.artifacts/dist-artifacts.lock/unjoined')),true);
 } finally {process.chdir(cwd);process.argv=argv;fs.rmSync(root,{recursive:true,force:true});}
});
