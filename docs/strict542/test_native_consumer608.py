"""Refusal boundaries for source-only native consumer; no real compiler runs."""
import hashlib
import importlib.util
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

spec=importlib.util.spec_from_file_location('consumer608',Path(__file__).with_name('prepare-native-consumer608.py'))
c=importlib.util.module_from_spec(spec);spec.loader.exec_module(c)


class SourceOnlyConsumer(unittest.TestCase):
    def fixture(self,root):
        owner=Path(root)/'source';owner.mkdir()
        inputs=owner.parent/'native608-stages'
        common={key:{} for key in ['owner_inputs','patched_sources','cargo_policy','rustc','cmake',
            'cmake_wheel_sha256','upstream_commit','source_archive_sha256','rust_archive_sha256',
            'lifetime_tests_exit','retention_negative_detected']}
        common['compaction_tests_exit']=0
        compile_receipt={**common,'kind':'NATIVE_COMPILER608_COMPILE_STAGE','stage':'compile',
            'complete':True,'addon_sha256':hashlib.sha256(b'compiled fixture').hexdigest()}
        tests={**common,'kind':'NATIVE_COMPILER608_LIBTEST_STAGE','stage':'libtests','complete':True,'native_lib_tests_exit':0}
        expected={}
        for stage,receipt in [('compile',compile_receipt),('libtests',tests)]:
            p=inputs/stage/'receipt.json';p.parent.mkdir(parents=True);p.write_text(json.dumps(receipt))
            expected[stage+'/receipt.json']=hashlib.sha256(p.read_bytes()).hexdigest()
        manifest=owner.parent/'export-manifest.json';manifest.write_text(json.dumps({'native_stage_outputs':expected}))
        return owner,inputs,manifest,compile_receipt

    def test_uploaded_binary_or_redirected_receipt_refuses_before_compilation(self):
        for mutation in ['binary','symlink','digest','unfinished']:
            with self.subTest(mutation=mutation),tempfile.TemporaryDirectory() as root:
                owner,inputs,manifest,receipt=self.fixture(root)
                p=inputs/'libtests/receipt.json'
                if mutation=='binary':(inputs/'compile/uploaded.node').write_bytes(b'binary')
                elif mutation=='symlink':p.rename(p.with_name('saved'));p.symlink_to('saved')
                elif mutation=='digest':p.write_text('{}')
                else:
                    value=json.loads(p.read_text());value['complete']=False;p.write_text(json.dumps(value))
                    value=json.loads(manifest.read_text());value['native_stage_outputs']['libtests/receipt.json']=hashlib.sha256(p.read_bytes()).hexdigest();manifest.write_text(json.dumps(value))
                with patch.object(c.subprocess,'run') as compiler:
                    with self.assertRaises(ValueError):c.prepare(owner)
                    compiler.assert_not_called()

    def test_rebuilt_addon_or_receipt_drift_never_publishes_native_directory(self):
        for mutation in ['addon','receipt','formatting']:
            with self.subTest(mutation=mutation),tempfile.TemporaryDirectory() as root:
                owner,inputs,manifest,receipt=self.fixture(root)
                def compile_fixture(*args,**kwargs):
                    out=owner/'result598-native';out.mkdir()
                    value={**receipt}
                    if mutation=='receipt':value['rustc']='changed'
                    (out/'receipt.json').write_text(json.dumps(value,indent=2) if mutation=='formatting' else json.dumps(value))
                    (out/'rolldown-binding.linux-x64-gnu.node').write_bytes(b'wrong' if mutation=='addon' else b'compiled fixture')
                with patch.object(c.subprocess,'run',side_effect=compile_fixture):
                    with self.assertRaisesRegex(ValueError,'source rebuild differs'):c.prepare(owner)
                self.assertFalse((owner.parent/'.native608').exists())

    def test_exact_rebuilt_receipt_and_addon_publish_only_verified_bytes(self):
        with tempfile.TemporaryDirectory() as root:
            owner,inputs,manifest,receipt=self.fixture(root)
            def compile_fixture(*args,**kwargs):
                out=owner/'result598-native';out.mkdir()
                (out/'receipt.json').write_bytes((inputs/'compile/receipt.json').read_bytes())
                (out/'rolldown-binding.linux-x64-gnu.node').write_bytes(b'compiled fixture')
            with patch.object(c.subprocess,'run',side_effect=compile_fixture):c.prepare(owner)
            target=owner.parent/'.native608'
            self.assertEqual((target/'receipt.json').read_bytes(),(inputs/'compile/receipt.json').read_bytes())
            self.assertEqual((target/'rolldown-binding.linux-x64-gnu.node').read_bytes(),b'compiled fixture')


if __name__=='__main__':unittest.main()
