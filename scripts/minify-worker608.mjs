// Fixed unprivileged build child. Never accepts a path, command or arbitrary options.
import fs from 'node:fs';
import path from 'node:path';
import {createRequire} from 'node:module';
import {pathToFileURL} from 'node:url';
import {createHash} from 'node:crypto';
import {WORKER_ENTRIES608} from './lib/worker-phases608.mjs';
const [key,maps]=process.argv.slice(2);
if(process.argv.length!==4 || !Object.hasOwn(WORKER_ENTRIES608,key) || !['true','false'].includes(maps))throw new Error('invalid fixed worker minifier selection');
for(const [name,value] of Object.entries({ROLLDOWN_WORKER_THREADS:'1',ROLLDOWN_MAX_BLOCKING_THREADS:'1',RAYON_NUM_THREADS:'1',TOKIO_WORKER_THREADS:'1',MIMALLOC_ALLOW_THP:'0'}))if(process.env[name]!==value)throw new Error('missing worker compiler budget policy: '+name);
const filename='dist/'+key+'.mjs';const mapname=filename+'.map';
function regular(name) {
 const parts=name.split('/');let current='';
 for(let i=0;i<parts.length;i++) {
  current=path.join(current,parts[i]);const stat=fs.lstatSync(current);
  if(stat.isSymbolicLink() || (i===parts.length-1 ? !stat.isFile() || stat.nlink!==1 : !stat.isDirectory()))throw new Error('redirected worker output');
 }
 return fs.readFileSync(name,'utf8');
}
const input=regular(filename);
let inputMap;
if(maps==='true') {
 inputMap=JSON.parse(regular(mapname));
 if(!input.trimEnd().endsWith('//# sourceMappingURL='+path.basename(mapname)))throw new Error('worker source-map reference changed');
} else if(fs.existsSync(mapname) || /^\/\/[#@] sourceMappingURL=.*$/mu.test(input))throw new Error('unexpected worker source-map');
const require=createRequire(import.meta.url);
const packagePath=require.resolve('rolldown/package.json',{paths:[path.dirname(require.resolve('tsdown'))]});
if(JSON.parse(fs.readFileSync(packagePath,'utf8')).version!=='1.2.9')throw new Error('worker minifier pin changed');
const {minifySync}=await import(pathToFileURL(path.join(path.dirname(packagePath),'dist/utils-index.mjs')).href);
const before=process.memoryUsage();
console.log(JSON.stringify({kind:'WORKER_MINIFY608_BEGIN',key,memory:before}));
const result=minifySync(path.basename(filename),input,{module:true,compress:true,mangle:{keepNames:true},codegen:{removeWhitespace:true,legalComments:'inline'},sourcemap:maps==='true',...(inputMap ? {inputMap}: {})});
if(result.errors.length || !result.code || (maps==='true' && !result.map))throw new Error('worker minification failed: '+JSON.stringify(result.errors));
const code=result.code+(maps==='true' ? '\n//# sourceMappingURL='+path.basename(mapname)+'\n' : '\n');
// Exclusive temporary siblings, no output accepted until this child exits successfully.
const temps=[];
try {
 for(const [name,bytes] of [...(maps==='true' ? [[mapname,JSON.stringify({...result.map,file:path.basename(filename)})]] : []),[filename,code]]) {
  const temp=name+'.pending608';fs.writeFileSync(temp,bytes,{flag:'wx',mode:0o644});temps.push([temp,name]);
 }
 for(const [temp,name] of temps)fs.renameSync(temp,name);
} finally {for(const [temp] of temps)if(fs.existsSync(temp))fs.unlinkSync(temp);}
console.log(JSON.stringify({kind:'WORKER_MINIFY608',key,inputSha256:createHash('sha256').update(input).digest('hex'),outputSha256:createHash('sha256').update(code).digest('hex'),before,after:process.memoryUsage()}));
