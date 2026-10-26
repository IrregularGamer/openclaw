import assert from 'node:assert/strict';
import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';
import {test} from 'node:test';
import {releaseConsumedArchives, releaseDisposableStore} from '../../scripts/lib/disposable-build-inputs.mjs';

function fixture(t) {
  const root = fs.mkdtempSync(path.join(os.tmpdir(), 'disposable608-'));
  t.after(() => fs.rmSync(root, {recursive:true,force:true}));
  fs.mkdirSync(path.join(root,'source/node_modules/.pnpm/a'), {recursive:true});
  fs.mkdirSync(path.join(root,'.pnpm-store'));
  fs.writeFileSync(path.join(root,'source/pnpm-workspace.yaml'), 'nodeLinker: isolated\npackageImportMethod: clone-or-copy\n');
  fs.writeFileSync(path.join(root,'source/node_modules/.pnpm/a/index.js'), 'private copy');
  fs.symlinkSync('.pnpm/a',path.join(root,'source/node_modules/a'));
  for (const name of ['source598.tar','successor598.tar','native598.tar']) fs.writeFileSync(path.join(root,name),'consumed');
  return root;
}
test('consumed archives and private store release preserves installed bytes and links',t=>{
  const root=fixture(t); releaseConsumedArchives(root); releaseDisposableStore(root);
  assert.equal(fs.existsSync(path.join(root,'source598.tar')),false);
  assert.equal(fs.existsSync(path.join(root,'.pnpm-store')),false);
  assert.equal(fs.readFileSync(path.join(root,'source/node_modules/a/index.js'),'utf8'),'private copy');
});
test('escaping installed link refuses before deleting store',t=>{
  const root=fixture(t); fs.symlinkSync('../../.pnpm-store',path.join(root,'source/node_modules/escape'));
  assert.throws(()=>releaseDisposableStore(root),/escapes/);
  assert.equal(fs.existsSync(path.join(root,'.pnpm-store')),true);
});
test('unsupported install policy and archive symlinks refuse',t=>{
  const root=fixture(t);fs.writeFileSync(path.join(root,'source/pnpm-workspace.yaml'),'packageImportMethod: hardlink\n');
  assert.throws(()=>releaseDisposableStore(root),/private installed inodes/);
  fs.unlinkSync(path.join(root,'native598.tar'));fs.symlinkSync('source598.tar',path.join(root,'native598.tar'));
  assert.throws(()=>releaseConsumedArchives(root),/regular file/);
  assert.equal(fs.existsSync(path.join(root,'source598.tar')),true);
});
