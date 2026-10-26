// Synthetic local input only. A new process initializes the existing release tracer.
import {createRequire} from 'node:module';
import {pathToFileURL} from 'node:url';
import path from 'node:path';
import assert from 'node:assert/strict';
const require=createRequire(import.meta.url);
const {rolldown}=await import(pathToFileURL(require.resolve('rolldown',{paths:[path.dirname(require.resolve('tsdown'))]})).href);
assert.equal(process.argv.length,3);
const bundle=await rolldown({cwd:process.argv[2],input:'entry.ts',logLevel:'silent',experimental:{lazyBarrel:true}});
try {
 const result=await bundle.generate({format:'es'});
 assert.equal(result.output.length,1);
 assert.match(result.output[0].code,/42/);
} finally {await bundle.close();}
