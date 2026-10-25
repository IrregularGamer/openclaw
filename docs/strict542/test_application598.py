"""Source-only release preparation; fixtures contain no runtime credentials."""
import hashlib
import importlib.util
import json
from pathlib import Path
import tempfile
import unittest

spec = importlib.util.spec_from_file_location('application598', Path(__file__).with_name('application598.py'))
a = importlib.util.module_from_spec(spec)
spec.loader.exec_module(a)

class PreparationTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory(); self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name); self.runtime = self.root/'runtime'; self.runtime.mkdir()
        for name in ('dist/index.js', 'node_modules/example/package.json', 'package.json'):
            path=self.runtime/name;path.parent.mkdir(parents=True,exist_ok=True);path.write_text('{}')
        self.lock=self.root/'pnpm-lock.yaml';self.lock.write_text('lockfileVersion: 9')
        self.evidence=self.root/'evidence.json'
        self.build=self.root/'build.log';self.build.write_text('build completed')
        self.tests=self.root/'tests.log';self.tests.write_text('tests completed')
        self.proof={'source_commit':'a'*40,'source_export_sha256':'b'*64,'lockfile_sha256':a.sha(self.lock.read_bytes()),'toolchain':{'node':'v26.1.0','pnpm':'12.5.1','python':'3.14.0'},'build_exit':0,'test_exit':0,'build_log_sha256':a.sha(self.build.read_bytes()),'test_log_sha256':a.sha(self.tests.read_bytes()),'execution':'admitted-offload','remote_run_id':'fixture-only','fixture':True}
        self.evidence.write_text(json.dumps(self.proof))
    def tree(self):return a.make_tree(self.runtime,self.lock,self.evidence,self.build,self.tests,allow_fixture=True)
    def test_deterministic_tree(self):
        first=self.tree();second=self.tree();self.assertEqual(first,second)
        self.assertEqual(first['status'],'FIXTURE_ONLY');self.assertEqual(first['tree_sha256'],a.digest(first['entries']))
    def test_missing_dependency_or_dist_refuses(self):
        (self.runtime/'dist/index.js').unlink()
        with self.assertRaises(ValueError):self.tree()
    def test_escaping_and_absolute_symlinks_refuse(self):
        for target in ('/etc/passwd','../../outside'):
            link=self.runtime/'link';link.symlink_to(target)
            with self.assertRaises(ValueError):self.tree()
            link.unlink()
    def test_internal_symlink_is_recorded(self):
        (self.runtime/'node_modules/example/link').symlink_to('package.json')
        item=next(x for x in self.tree()['entries'] if x['path'].endswith('/link'))
        self.assertEqual(item['target'],'package.json')
    def test_secret_names_refuse(self):
        for name in ('.env','auth-profiles.json','credentials.json','state.sqlite','private.key'):
            p=self.runtime/name;p.write_text('synthetic')
            with self.assertRaises(ValueError):self.tree()
            p.unlink()
    def test_nonzero_build_and_tampered_log_refuse(self):
        self.proof['build_exit']=1;self.evidence.write_text(json.dumps(self.proof))
        with self.assertRaises(ValueError):self.tree()
        self.proof['build_exit']=0;self.evidence.write_text(json.dumps(self.proof));self.build.write_text('changed')
        with self.assertRaises(ValueError):self.tree()
    def test_fixture_cannot_claim_built(self):
        with self.assertRaises(ValueError):a.make_tree(self.runtime,self.lock,self.evidence,self.build,self.tests)
    def test_tree_rejects_setuid(self):
        (self.runtime/'package.json').chmod(0o4755)
        with self.assertRaises(ValueError):self.tree()
    def test_runtime_mutation_refuses_validation(self):
        receipt=self.tree();(self.runtime/'dist/index.js').write_text('changed')
        with self.assertRaises(ValueError):a.check_tree(receipt,self.runtime,allow_fixture=True)

    def staged(self):
        stage=self.root/'stage';stage.mkdir();self.runtime.rename(stage/'runtime')
        self.runtime=stage/'runtime'
        for name in ('apply598.py','application598.py'):(stage/name).write_text('synthetic '+name)
        for name in a.TARGETS:
            if name != 'runtime':(stage/name).write_text('synthetic '+name)
        return stage
    def baseline(self):
        meta={'mode':0o600,'uid':0,'gid':0,'mtime_ns':1,'ctime_ns':1,'xattrs_sha256':'e'*64}
        return {'targets':{target:{'state':'absent'} for target in a.TARGETS.values()},'seal_sha256':'c'*64,'seal_metadata':meta,'boot_id':'fixture-boot','observed_guards':{path:{'sha256':'f'*64,'metadata':meta} for path in a.GUARDS}}
    def action(self,stage):
        # Fixture proof is never accepted by production preparation. Patch only
        # the native hash and fixture BUILT classification in this isolated test.
        tree=self.tree()
        return tree,a.make_action(tree,stage,self.baseline())
    def test_action_native_hash_refuses_without_patch(self):
        stage=self.staged()
        with self.assertRaises(ValueError):self.action(stage)
    def test_action_binding_and_independent_reviews(self):
        from unittest.mock import patch
        stage=self.staged()
        actual=a.check_tree
        with patch.object(a,'NATIVE_SHA',a.file_hash(stage/'maintenance.py')), patch.object(a,'check_tree',side_effect=lambda receipt,runtime,**kw:actual(receipt,runtime,allow_fixture=True)):
            tree,action=self.action(stage)
            reviews=[{'scope':scope,'verdict':'APPROVE','action_sha256':action['action_sha256'],'tree_receipt_sha256':a.digest(tree),'source_commit':'a'*40,'author':'author','reviewer':'independent','review_receipt_sha256':'d'*64} for scope in ('source','action','privilege-policy')]
            self.assertEqual(a.validate_action(action,tree,stage,reviews)['status'],'PREPARED_REVIEWED_NOT_APPLIED')
            reviews[0]['reviewer']='author'
            with self.assertRaises(ValueError):a.validate_action(action,tree,stage,reviews)
    def test_action_stage_tamper_refuses(self):
        from unittest.mock import patch
        stage=self.staged()
        actual=a.check_tree
        with patch.object(a,'NATIVE_SHA',a.file_hash(stage/'maintenance.py')), patch.object(a,'check_tree',side_effect=lambda receipt,runtime,**kw:actual(receipt,runtime,allow_fixture=True)):
            tree,action=self.action(stage)
            (stage/'native_owner_server542.py').write_text('changed')
            with self.assertRaises(ValueError):a.validate_action(action,tree,stage,[])
    def test_unknown_target_or_missing_seal_refuses(self):
        baseline=self.baseline();baseline['targets']['/etc/sudoers']={'state':'absent'}
        with self.assertRaises(ValueError):a.baseline_inventory(baseline)
        baseline=self.baseline();del baseline['seal_sha256']
        with self.assertRaises(ValueError):a.baseline_inventory(baseline)
    def test_receipt_output_cannot_overwrite(self):
        path=self.root/'output.json';a.emit(path,{'a':1})
        with self.assertRaises(FileExistsError):a.emit(path,{'a':2})

    def test_fixture_receipt_cannot_be_promoted(self):
        tree=self.tree();tree['status']='BUILT'
        with self.assertRaises(ValueError):a.check_tree(tree,self.runtime)

    def test_check_tree_revalidates_all_evidence_shape(self):
        for key,value in (('build_exit',False),('test_exit',2),('execution','local'),('toolchain',{'node':'v26.1.0','pnpm':'other','python':'3.14'})):
            tree=self.tree();tree['execution_evidence'][key]=value;tree['execution_evidence_sha256']=a.digest(tree['execution_evidence'])
            with self.assertRaises(ValueError):a.check_tree(tree,self.runtime,allow_fixture=True)

    def test_runtime_root_mode_refuses(self):
        self.runtime.chmod(0o777)
        with self.assertRaises(ValueError):self.tree()
    def test_special_file_fifo_refuses(self):
        import os
        os.mkfifo(self.runtime/'pipe')
        with self.assertRaises(ValueError):self.tree()
    def test_source_reference_and_lock_drift_refuse(self):
        self.lock.write_text('changed')
        with self.assertRaises(ValueError):self.tree()
