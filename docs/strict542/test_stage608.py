import hashlib,json,sys,tempfile,unittest
from pathlib import Path

sys.path.insert(0,str(Path(__file__).resolve().parent))
import stage608

sha=lambda b:hashlib.sha256(b).hexdigest()


class Stage608Test(unittest.TestCase):
    def build(self,stage,tamper=None):
        root=Path(tempfile.mkdtemp());base=root/'stage608-inputs'
        addon=b'addon';compile_bytes=json.dumps({'addon_sha256':sha(addon)}).encode();libtests=b'{"lib":1}'
        files={'native/receipt.json':compile_bytes,'native/libtests-receipt.json':libtests,
               'native/'+stage608.ADDON:addon,'checks/tests.log':b'checks\n','checks/installed.json':b'{}',
               'compiler/tests.log':b'compiler\n'}
        needed=stage608.STAGES[stage];pins={}
        for n in needed:
            outs={o:sha(files[o]) for o in stage608.OUTPUTS[n]}
            receipt={'kind':'JOB608_STAGE_RECEIPT','stage':n,'exit_code':0,'source_commit':'c0ffee','outputs':outs}
            for o in stage608.OUTPUTS[n]:
                (base/o).parent.mkdir(parents=True,exist_ok=True);(base/o).write_bytes(files[o])
            rb=json.dumps(receipt).encode();(base/n/'stage-receipt.json').write_bytes(rb)
            pins.update(outs);pins[n+'/stage-receipt.json']=sha(rb)
        m={'stage':stage,'run_id':'r','source_commit':'c0ffee','stage_inputs':pins,
           'native_stage_outputs':{'compile/receipt.json':sha(compile_bytes),'libtests/receipt.json':sha(libtests)}}
        if tamper:tamper(root,m)
        (root/'export-manifest.json').write_text(json.dumps(m))
        return root

    def test_accepts_exact_inputs_for_every_stage(self):
        for stage in stage608.STAGES:
            stage608.verify_inputs(self.build(stage))

    def test_package_stages_native_and_merges_logs_in_order(self):
        root=self.build('package');stage608.verify_inputs(root);stage608.stage_native(root)
        self.assertEqual((root/'.native608'/stage608.ADDON).read_bytes(),b'addon')
        stage608.merge_logs(root,root/'merged.log')
        self.assertEqual((root/'merged.log').read_bytes(),b'checks\ncompiler\n')

    def test_refuses_unknown_stage(self):
        root=self.build('native',lambda r,m:m.update(stage='everything'))
        with self.assertRaisesRegex(ValueError,'no known stage'):stage608.verify_inputs(root)

    def test_refuses_extra_or_missing_inputs(self):
        root=self.build('compiler',lambda r,m:(r/'stage608-inputs/extra').write_bytes(b'x'))
        with self.assertRaisesRegex(ValueError,'exact required set'):stage608.verify_inputs(root)
        root=self.build('package',lambda r,m:(r/'stage608-inputs/compiler/tests.log').unlink())
        with self.assertRaisesRegex(ValueError,'exact required set'):stage608.verify_inputs(root)

    def test_refuses_digest_mismatch(self):
        root=self.build('package',lambda r,m:(r/'stage608-inputs/checks/tests.log').write_bytes(b'forged\n'))
        with self.assertRaisesRegex(ValueError,'digest mismatch'):stage608.verify_inputs(root)

    def test_refuses_failed_or_foreign_producing_receipt(self):
        def foreign(r,m):
            p=r/'stage608-inputs/checks/stage-receipt.json';v=json.loads(p.read_text());v['source_commit']='other'
            p.write_text(json.dumps(v));m['stage_inputs']['checks/stage-receipt.json']=sha(p.read_bytes())
        with self.assertRaisesRegex(ValueError,'producing stage receipt'):stage608.verify_inputs(self.build('package',foreign))

    def test_refuses_addon_not_matching_pinned_compile_receipt(self):
        def swap(r,m):
            p=r/'stage608-inputs/native'/stage608.ADDON;p.write_bytes(b'other');d=sha(b'other')
            m['stage_inputs']['native/'+stage608.ADDON]=d
            rp=r/'stage608-inputs/native/stage-receipt.json';v=json.loads(rp.read_text());v['outputs']['native/'+stage608.ADDON]=d
            rp.write_text(json.dumps(v));m['stage_inputs']['native/stage-receipt.json']=sha(rp.read_bytes())
        with self.assertRaisesRegex(ValueError,'independently pinned compile'):stage608.verify_inputs(self.build('compiler',swap))

    def test_receipt_pins_outputs(self):
        root=self.build('checks');res=root/'result608-checks';(res/'checks').mkdir(parents=True)
        (res/'checks/tests.log').write_bytes(b'checks\n');(res/'checks/installed.json').write_bytes(b'{}')
        stage608.receipt(root,res);v=json.loads((res/'checks/stage-receipt.json').read_text())
        self.assertEqual(v['outputs'],{'checks/tests.log':sha(b'checks\n'),'checks/installed.json':sha(b'{}')})
        self.assertEqual((v['stage'],v['exit_code'],v['source_commit']),('checks',0,'c0ffee'))


if __name__=='__main__':
    unittest.main()
