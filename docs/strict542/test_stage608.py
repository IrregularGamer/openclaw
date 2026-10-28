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
        for n in getattr(stage608,'BUILD_STAGES',[]):
            files.update({n+'/checkpoint.tar':b'archive',n+'/build.log':b'build\n'})
        needed=stage608.STAGES[stage];pins={}
        for n in needed:
            outs={o:sha(files[o]) for o in stage608.OUTPUTS[n]}
            receipt={'kind':'JOB608_STAGE_RECEIPT','stage':n,'exit_code':0,'source_commit':'c0ffee',
                     'source_export_sha256':'b'*64,'outputs':outs}
            for o in stage608.OUTPUTS[n]:
                (base/o).parent.mkdir(parents=True,exist_ok=True);(base/o).write_bytes(files[o])
            rb=json.dumps(receipt).encode();(base/n/'stage-receipt.json').write_bytes(rb)
            pins.update(outs);pins[n+'/stage-receipt.json']=sha(rb)
        m={'stage':stage,'run_id':'r','source_commit':'c0ffee','source_export_sha256':'b'*64,'stage_inputs':pins,
           'native_stage_outputs':{'compile/receipt.json':sha(compile_bytes),'libtests/receipt.json':sha(libtests)}}
        if tamper:tamper(root,m)
        (root/'export-manifest.json').write_text(json.dumps(m))
        return root

    def test_accepts_exact_inputs_for_every_stage(self):
        for stage in stage608.STAGES:
            stage608.verify_inputs(self.build(stage))

    def test_finite_build_dependencies_require_every_canonical_group(self):
        self.assertEqual(stage608.STAGES['runtime'],['native'])
        self.assertEqual(stage608.STAGES['middle'],['native','runtime']+['unified-'+str(i) for i in range(6)])
        self.assertEqual(stage608.STAGES['tail'],['native','middle','sdk-0','sdk-1'])
        self.assertIn('tail',stage608.STAGES['package'])

    def test_foreign_common_export_identity_is_refused(self):
        def foreign(r,m):
            p=r/'stage608-inputs/native/stage-receipt.json';v=json.loads(p.read_text());v['source_export_sha256']='d'*64
            p.write_text(json.dumps(v));m['stage_inputs']['native/stage-receipt.json']=sha(p.read_bytes())
        with self.assertRaisesRegex(ValueError,'producing stage receipt'):stage608.verify_inputs(self.build('compiler',foreign))

    def test_build_archive_refuses_escape_links_and_duplicate_entries(self):
        import io,tarfile
        for name,link in [('../escape',''),('runtime/escape','../../escape'),('runtime/data/file','')]:
            root=Path(tempfile.mkdtemp());archive=root/'bad.tar'
            with tarfile.open(archive,'w') as t:
                entry=tarfile.TarInfo(name)
                if link:entry.type=tarfile.SYMTYPE;entry.linkname=link;t.addfile(entry)
                else:
                    entry.size=1;t.addfile(entry,io.BytesIO(b'x'))
                    if name=='runtime/data/file':t.addfile(entry,io.BytesIO(b'x'))
            with self.assertRaises(ValueError):stage608.extract_checkpoint(archive,root/'checkpoints','runtime')

    def test_build_archive_roundtrip_preserves_exact_modes_and_owned_links(self):
        import tarfile
        root=Path(tempfile.mkdtemp());data=root/'owned/runtime/data/dist';data.mkdir(parents=True)
        (data/'entry').write_bytes(b'output');(data/'entry').chmod(0o664)
        (data/'alias').symlink_to('entry');data.chmod(0o775)
        with tarfile.open(root/'checkpoint.tar','w') as t:t.add(root/'owned/runtime',arcname='runtime')
        stage608.extract_checkpoint(root/'checkpoint.tar',root/'checkpoints','runtime')
        restored=root/'checkpoints/runtime/data/dist'
        self.assertEqual((restored/'entry').read_bytes(),b'output')
        self.assertEqual((restored/'entry').stat().st_mode&0o777,0o664)
        self.assertEqual(restored.stat().st_mode&0o777,0o775)
        self.assertTrue((restored/'alias').is_symlink())

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

    def test_compiler_stage_creates_every_evidence_dir_its_tests_write(self):
        here=Path(__file__).resolve().parent;runner=(here/'run-stage608.sh').read_text()
        branch=runner.split('\ncompiler)\n',1)[1].split('\n  ;;\n',1)[0]
        import re
        for test in re.findall(r'docs/strict542/(\S+\.test\.mjs)',branch):
            for d in set(re.findall(r"writeFile\('([^'/]+)/",(here/test).read_text())):
                self.assertIn('mkdir '+d+'\n',branch.split(test,1)[0],test+' writes '+d)

    def test_package_builder_failure_surfaces_log_tail_and_keeps_status(self):
        import re,subprocess
        branch=(Path(__file__).resolve().parent/'run-stage608.sh').read_text().split('\npackage)\n',1)[1]
        block=re.search(r'\n  env -i [^\n]*build598\.sh checkpoint608( \|\| \{\n.*?\n  \}\n)',branch,re.S)
        self.assertIsNotNone(block,'builder failure must not be silent')
        d=Path(tempfile.mkdtemp());(d/'result598-build').mkdir()
        (d/'fake.sh').write_text('echo hidden-build-error >result598-build/build.log; exit 7\n')
        r=subprocess.run(['sh','-c','set -eu\nsh fake.sh'+block.group(1)+'echo reached\n'],cwd=d,capture_output=True,text=True)
        self.assertEqual(r.returncode,7);self.assertIn('STEP608 builder-fail 7',r.stdout)
        self.assertIn('hidden-build-error',r.stdout);self.assertNotIn('reached',r.stdout)

    def test_receipt_pins_outputs(self):
        root=self.build('checks');res=root/'result608-checks';(res/'checks').mkdir(parents=True)
        (res/'checks/tests.log').write_bytes(b'checks\n');(res/'checks/installed.json').write_bytes(b'{}')
        stage608.receipt(root,res);v=json.loads((res/'checks/stage-receipt.json').read_text())
        self.assertEqual(v['outputs'],{'checks/tests.log':sha(b'checks\n'),'checks/installed.json':sha(b'{}')})
        self.assertEqual((v['stage'],v['exit_code'],v['source_commit']),('checks',0,'c0ffee'))


if __name__=='__main__':
    unittest.main()
