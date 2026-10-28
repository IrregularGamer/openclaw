// Private, non-published compiler checkpoints. The declaration writer owns admission.
import fs from 'node:fs';
import path from 'node:path';
import { createHash } from 'node:crypto';
import { isDeepStrictEqual } from 'node:util';

const same=isDeepStrictEqual;
const require608=(ok,message)=>{if(!ok)throw new Error(message);};
export function checkpointSelection608(options,groups,canonical) {
 require608(same(groups,canonical),'checkpoint requires the complete canonical writer selection');
 require608(options && ['produce','join'].includes(options.mode),'unknown declaration checkpoint mode');
 require608(/^[a-f0-9]{40}$/.test(options.sourceCommit ?? '') && /^[a-f0-9]{64}$/.test(options.sourceExportSha256 ?? ''),'missing exact checkpoint source/export identity');
 require608(typeof options.directory==='string' && path.isAbsolute(options.directory),'checkpoint directory must be absolute');
 require608(options.mode==='produce' ? groups.includes(options.group) : options.group===undefined,'invalid canonical checkpoint group');
 return options.mode==='produce' ? [options.group] : [...groups];
}
export function checkpointAncestry608(directory) {
 let current=path.parse(directory).root;
 for(const part of path.resolve(directory).slice(current.length).split(path.sep).filter(Boolean)) {
  current=path.join(current,part);const stat=fs.lstatSync(current);
  require608(stat.isDirectory() && !stat.isSymbolicLink(),'checkpoint ancestry must be real directories');
 }
}
export function checkpointInventory608(root) {
 checkpointAncestry608(root);const outputs={};
 function visit(directory) {
  for(const name of fs.readdirSync(directory).sort()) {
   const file=path.join(directory,name),stat=fs.lstatSync(file);
   require608(!stat.isSymbolicLink() && (stat.isDirectory() || (stat.isFile() && stat.nlink===1)),'checkpoint output must be private regular files or directories');
   if(stat.isDirectory())visit(file);
   else {
    const fd=fs.openSync(file,fs.constants.O_RDONLY|fs.constants.O_NOFOLLOW);
    try {
     const opened=fs.fstatSync(fd);require608(opened.ino===stat.ino && opened.dev===stat.dev && opened.nlink===1,'checkpoint file changed during read');
     const hash=createHash('sha256'),buffer=Buffer.allocUnsafe(1024*1024);
     for(let size;(size=fs.readSync(fd,buffer,0,buffer.length,null))>0;)hash.update(buffer.subarray(0,size));
     outputs[path.relative(root,file).split(path.sep).join('/')]=hash.digest('hex');
     const after=fs.fstatSync(fd);require608(opened.size===after.size && opened.mtimeMs===after.mtimeMs && opened.ctimeMs===after.ctimeMs && after.nlink===1,'checkpoint file changed during read');
    }
    finally {fs.closeSync(fd);}
   }
  }
 }
 visit(root);return outputs;
}
export function checkpointTopology608(root) {
 checkpointAncestry608(root);const topology=[];
 function visit(directory) {
  for(const name of fs.readdirSync(directory).sort()) {
   const file=path.join(directory,name),stat=fs.lstatSync(file);
   require608(!stat.isSymbolicLink() && (stat.isDirectory() || stat.isFile()),'checkpoint topology contains nonregular output');
   topology.push([path.relative(root,file).split(path.sep).join('/'),stat.isDirectory()?'directory':'file',stat.mode&0o7777]);
   if(stat.isDirectory())visit(file);
  }
 }
 visit(root);return topology;
}
export function validateCheckpoint608(receipt,wanted,root,validateInputs,artifactVersion) {
 const {record,topology,...identity}=receipt;
 require608(same(identity,wanted) && receipt.schema==='strict542-declaration-group608-v1' && receipt.status==='COMPILED_GROUP_NOT_PUBLISHED','checkpoint canonical/source identity mismatch');
 require608(Number.isSafeInteger(artifactVersion) && artifactVersion>0 && record && record.version===artifactVersion && /^[a-f0-9]{64}$/.test(record.signature ?? '') && Array.isArray(record.inputs) && record.inputs.every(x=>typeof x==='string') && record.outputs && Object.keys(record.outputs).length>0,'missing successful compiler seal');
 require608(new Set(record.inputs).size===record.inputs.length && record.inputs.every(name=>name && !path.isAbsolute(name) && !path.win32.isAbsolute(name) && !name.split(/[\\/]/).includes('..')),'invalid checkpoint compiler input membership');
 require608(Object.keys(record.outputs).every(name=>name && !path.isAbsolute(name) && !name.split(/[\\/]/).includes('..') && /^[a-f0-9]{64}$/.test(record.outputs[name])),'invalid checkpoint output identity');
 require608(same(record.outputs,checkpointInventory608(root)),'checkpoint output inventory changed');
 if(topology!==undefined)require608(same(topology,checkpointTopology608(root)),'checkpoint output topology changed');
 require608(validateInputs(record),'checkpoint compiler input identity changed');
 return record;
}
