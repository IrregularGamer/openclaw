import {test} from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs';
import path from 'node:path';
import {createHash} from 'node:crypto';
import {shaFile608,workspaceInventory608} from '../../scripts/lib/bounded-build-checkpoint608.mjs';
const digest=bytes=>createHash('sha256').update(bytes).digest('hex');
function fixture(t){const root=fs.mkdtempSync('/var/tmp/scratch608-');t.after(()=>fs.rmSync(root,{recursive:true,force:true}));return root;}

test('inventory hashing keeps scratch allocation bounded across many small files and repeated traversals',t=>{
 const root=fixture(t),expected={};
 for(let i=0;i<32;i++){const name=`file-${String(i).padStart(2,'0')}`,bytes=Buffer.from(`source ${i}\n`);fs.writeFileSync(path.join(root,name),bytes);expected[name]={kind:'file',mode:fs.statSync(path.join(root,name)).mode&0o7777,sha256:digest(bytes)};}
 const original=Buffer.allocUnsafe;let scratchBytes=0;
 Buffer.allocUnsafe=function(size){if(size===1024*1024)scratchBytes+=size;return original(size);};
 try {assert.deepEqual(workspaceInventory608(root),expected);assert.deepEqual(workspaceInventory608(root),expected);}
 finally {Buffer.allocUnsafe=original;}
 assert.ok(scratchBytes<=2*1024*1024,`two inventories allocated ${scratchBytes} scratch bytes, budget is 2MiB`);
});

test('shared traversal scratch preserves exact multi-chunk, short, empty, mode and link inventory',t=>{
 const root=fixture(t),large=Buffer.alloc(2*1024*1024+17,0x61),small=Buffer.from('short');
 fs.writeFileSync(path.join(root,'a-large'),large);fs.writeFileSync(path.join(root,'b-short'),small);fs.writeFileSync(path.join(root,'c-empty'),'');
 fs.chmodSync(path.join(root,'b-short'),0o640);fs.symlinkSync('b-short',path.join(root,'d-link'));
 const inventory=workspaceInventory608(root);
 assert.equal(inventory['a-large'].sha256,digest(large));assert.equal(inventory['b-short'].sha256,digest(small));assert.equal(inventory['c-empty'].sha256,digest(''));
 assert.equal(inventory['b-short'].mode,0o640);assert.deepEqual(inventory['d-link'],{kind:'link',mode:0o777,target:'b-short'});
 assert.equal(shaFile608(path.join(root,'a-large')),digest(large));
 assert.throws(()=>shaFile608(path.join(root,'d-link')),/ELOOP/);
});

test('nested inventory and standalone reads cannot overwrite another traversal scratch',t=>{
 const outer=fixture(t),inner=fixture(t),a=Buffer.alloc(1024*1024+5,0x61),b=Buffer.alloc(1024*1024+9,0x62);
 fs.writeFileSync(path.join(outer,'a'),a);fs.writeFileSync(path.join(inner,'b'),b);
 const original=fs.readSync;let nested=false,inside,standalone;
 fs.readSync=function(...args){const count=original(...args);if(!nested){nested=true;inside=workspaceInventory608(inner);standalone=shaFile608(path.join(inner,'b'));}return count;};
 let inventory;try {inventory=workspaceInventory608(outer);}finally {fs.readSync=original;}
 assert.equal(inventory.a.sha256,digest(a));assert.equal(inside.b.sha256,digest(b));assert.equal(standalone,digest(b));
});

test('source mutation, hardlinked output and read-error refusal remain fail-closed with fd cleanup',t=>{
 const root=fixture(t),file=path.join(root,'file');fs.writeFileSync(file,'first');
 const original=fs.readSync;let changed=false;
 fs.readSync=function(...args){const count=original(...args);if(!changed){changed=true;fs.appendFileSync(file,'changed');}return count;};
 try {assert.throws(()=>workspaceInventory608(root),/changed during read/);}finally {fs.readSync=original;}
 fs.linkSync(file,path.join(root,'alias'));assert.throws(()=>workspaceInventory608(root,{data:true}),/hardlinked checkpoint output/);
 let descriptor;
 fs.readSync=function(fd){descriptor=fd;throw new Error('injected read failure');};
 try {assert.throws(()=>shaFile608(file),/injected read failure/);}finally {fs.readSync=original;}
 assert.throws(()=>fs.fstatSync(descriptor),{code:'EBADF'});
});
