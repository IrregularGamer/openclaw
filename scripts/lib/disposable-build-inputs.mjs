// Own only verified consumed inputs of a disposable secretless build export.
import fs from 'node:fs';
import path from 'node:path';

export function releaseConsumedArchives(root) {
  root = fs.realpathSync(root);
  const names = ['source598.tar', 'successor598.tar', 'native598.tar'];
  // Caller verifies digests and finishes extraction before invoking this operation.
  for (const name of names) {
    const p = path.join(root, name);
    if (!fs.lstatSync(p).isFile() || fs.lstatSync(p).isSymbolicLink())
      throw new Error('consumed archive must be a regular file');
  }
  for (const name of names) fs.unlinkSync(path.join(root, name));
}

export function releaseDisposableStore(root) {
  root = fs.realpathSync(root);
  const source = path.join(root, 'source');
  const store = path.join(root, '.pnpm-store');
  for (const directory of [source, path.join(source, 'node_modules')]) {
    if (!fs.lstatSync(directory).isDirectory() || fs.lstatSync(directory).isSymbolicLink())
      throw new Error('disposable source and node_modules must be real directories');
  }
  if (!fs.lstatSync(store).isDirectory() || fs.lstatSync(store).isSymbolicLink())
    throw new Error('disposable store must be a real directory');
  const policy = fs.readFileSync(path.join(source, 'pnpm-workspace.yaml'), 'utf8');
  if (!/^nodeLinker: isolated$/m.test(policy) || !/^packageImportMethod: clone-or-copy$/m.test(policy))
    throw new Error('store cleanup requires private installed inodes');
  // Check every installed link before deleting anything; no surviving dependency
  // may point into the store or outside the disposable source tree.
  function walk(directory) {
    for (const item of fs.readdirSync(directory, {withFileTypes:true})) {
      const p = path.join(directory, item.name);
      if (item.isSymbolicLink()) {
        const resolved = fs.realpathSync(p);
        if (!resolved.startsWith(source + path.sep)) throw new Error('installed link escapes source: ' + p);
      } else if (item.isDirectory()) walk(p);
    }
  }
  walk(path.join(source, 'node_modules'));
  fs.rmSync(store, {recursive:true});
}
