"""Exact patch contract; real Rust/compiler validation remains admitted offload."""
import importlib.util
from pathlib import Path
import unittest
import hashlib,json,os,tarfile

spec=importlib.util.spec_from_file_location('prepare_finalizer608',Path('scripts/lib/prepare-native608.py'))
p=importlib.util.module_from_spec(spec);spec.loader.exec_module(p)


class FinalizerPatch(unittest.TestCase):
    def test_patch_preserves_original_finalizer_predicate_and_all_other_bytes(self):
        self.assertTrue(callable(getattr(p,'patched_finalizer',None)), 'early finalizer patch is absent')
        archive=Path(os.environ.get('ROLLDOWN608_SOURCE_ARCHIVE',str(Path.cwd().parent/'rolldown608-source.tar.gz')))
        pin=json.loads(Path('docs/strict542/rolldown-source-pin608.json').read_text())
        self.assertEqual(hashlib.sha256(archive.read_bytes()).hexdigest(),pin['source_archive_sha256'])
        with tarfile.open(archive,'r:gz') as tf:
            member=next(m for m in tf.getmembers() if m.name.endswith('/'+p.FINALIZE))
            original=tf.extractfile(member).read().decode()
        patched=p.patched_finalizer(original)
        predicate=original[original.index('        .filter(|(idx, _ast)| {'):original.index('        .filter_map(|(idx, ast)| {')]
        self.assertIn(predicate.replace('        .filter(|(idx, _ast)| {','    let should_finalize = |idx: rolldown_common::ModuleIdx| {').replace('*idx','idx').removesuffix('        })\n')+'    };',patched)
        self.assertLess(patched.index('release_unneeded'),patched.index('let finalized ='))
        self.assertIn('for chunk in chunk_graph.chunk_table.iter()',patched)
        self.assertIn('required_asts[module.idx.raw() as usize] = true;',patched)
        self.assertIn('.filter(|(idx, _ast)| should_finalize(*idx))',patched)
        self.assertEqual(patched.count('ctx.finalize_normal_module(ast, ast_scope)'),1)
        prefix=patched[:patched.index('    let should_finalize = ')]
        remaining=patched[patched.index('    let finalized = '):].replace('        .filter(|(idx, _ast)| should_finalize(*idx))\n',predicate)
        self.assertEqual(prefix+remaining,original)

    def test_changed_filter_refuses(self):
        self.assertTrue(callable(getattr(p,'patched_finalizer',None)), 'early finalizer patch is absent')
        with self.assertRaises(ValueError):p.patched_finalizer('unreviewed source')

class RetentionNegativeControl(unittest.TestCase):
    def test_old_retention_mutation_keeps_rust_delimiters(self):
        # Mirrors build-native608.py; rustc itself runs only in admitted offload.
        src=Path('docs/strict542/build-native608.py').read_text()
        expr=src[src.index("old=helper.replace("):src.index("\nassert old != helper")]
        helper=Path('scripts/lib/last-use-ast608.rs').read_text()
        scope={'helper':helper};exec(expr,{},scope);old=scope['old']
        self.assertNotEqual(old,helper)
        self.assertNotIn('take());',old.replace('values.iter_mut()',''))
        code=[]
        for line in old.splitlines():
            line=line.split('//',1)[0];code.append(line)
        text='\n'.join(code)
        for a,b in ['{}','()','[]']:self.assertEqual(text.count(a),text.count(b),a+b)


if __name__=='__main__':unittest.main()
