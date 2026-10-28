import test from 'node:test';
import assert from 'node:assert/strict';
import {execFileSync} from 'node:child_process';
import {fileURLToPath} from 'node:url';

for(const name of ['lookups','identity-escape','policy','retarget','missing-retarget','pinned-read','lexical-outside','scheduling-default','scheduling-override']) {
  test(`native admission composition: ${name}`,()=>{
    const output=execFileSync(process.execPath,[fileURLToPath(new URL('./native-admission608.fixture.mjs',import.meta.url)),name],
      {encoding:'utf8',timeout:15000,maxBuffer:1024*1024});
    assert.equal(JSON.parse(output.trim()).status,'PASS');
  });
}
