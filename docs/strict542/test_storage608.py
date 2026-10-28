"""Small source-staging storage checks; no actual encrypted-volume writes."""
import importlib.util,json,tempfile,unittest
from pathlib import Path
from unittest.mock import patch
P=Path(__file__).with_name('storage608.py')
spec=importlib.util.spec_from_file_location('storage608',P) if P.exists() else None
storage=importlib.util.module_from_spec(spec) if spec else None
if spec:spec.loader.exec_module(storage)

class Storage608Test(unittest.TestCase):
 def setUp(self):
  self.assertIsNotNone(storage,'missing executable bounded source-staging owner')
  self.tmp=tempfile.TemporaryDirectory();self.addCleanup(self.tmp.cleanup);self.root=Path(self.tmp.name)
 def test_forecast_includes_all_fifteen_stage_returns_and_base_overlays(self):
  plan=storage.forecast(696548381)
  self.assertEqual(len(storage.CAPS),15);self.assertEqual(plan['return_caps_bytes'],2784*storage.MIB)
  self.assertEqual(plan['overlay_bytes'],16*16*storage.MIB)
  self.assertLessEqual(plan['total_bytes'],storage.MAX_STORE)
 def test_oversized_forecast_refuses(self):
  with self.assertRaisesRegex(ValueError,'forecast'):storage.forecast(storage.MAX_STORE)
 def test_logical_return_count_charges_each_hardlink_but_store_counts_inode_once(self):
  p=self.root/'a';p.write_bytes(b'abc');(self.root/'b').hardlink_to(p)
  self.assertEqual(storage.bytes_used(self.root,unique=False),6)
  self.assertEqual(storage.bytes_used(self.root,unique=True),3)
 def test_escaping_symlink_is_refused_without_following_it(self):
  (self.root/'bad').symlink_to('../escape')
  with self.assertRaisesRegex(ValueError,'link'):storage.bytes_used(self.root)
 def test_return_cap_and_free_reserve_refuse(self):
  result=self.root/'result';result.mkdir();(result/'payload').write_bytes(b'abcd')
  with patch.dict(storage.CAPS,{'native':3}):
   with self.assertRaisesRegex(ValueError,'return cap'):storage.check_result(result,'native')
  with self.assertRaisesRegex(ValueError,'free reserve'):storage.check_room(self.root,'native',free=storage.FREE_RESERVE)
 def test_verified_copy_preserves_original_and_refuses_digest_drift(self):
  base=self.root/'base';base.mkdir();m={'native_stage_outputs':{}}
  for name,key in storage.ARCHIVES.items():
   (base/name).write_bytes(name.encode());m[key]=storage.sha(base/name)
  for name in storage.SMALL_FILES:(base/name).write_bytes(b'fixture')
  (base/'native608-stages').mkdir();dest=self.root/'dest';dest.mkdir()
  storage.copy_base(base,dest,m)
  for name in [*storage.ARCHIVES,*storage.SMALL_FILES]:
   self.assertEqual((base/name).read_bytes(),(dest/name).read_bytes())
   self.assertNotEqual((base/name).stat().st_ino,(dest/name).stat().st_ino)
  m['base_source_archive_sha256']='0'*64;other=self.root/'other';other.mkdir()
  with self.assertRaisesRegex(ValueError,'digest'):storage.copy_base(base,other,m)
 def test_unknown_stage_refuses(self):
  with self.assertRaisesRegex(ValueError,'stage'):storage.check_result(self.root,'arbitrary')

if __name__=='__main__':unittest.main()
