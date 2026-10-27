"""Scan-to-link memory contract. Real native execution remains admitted offload."""
import importlib.util
from pathlib import Path
import unittest

spec = importlib.util.spec_from_file_location('prepare608', 'scripts/lib/prepare-native608.py')
p = importlib.util.module_from_spec(spec)
spec.loader.exec_module(p)


class CompactPatch(unittest.TestCase):
    def test_serial_replacement_precedes_link_metadata_without_changing_other_bytes(self):
        self.assertTrue(callable(getattr(p, 'patched_link_compaction', None)))
        original = 'prefix\n  pub fn new(mut scan_stage_output: NormalizedScanStageOutput, options: &\'a SharedOptions) -> Self {\n    // since constant export is spared in most of time, aggregate them would make searching more efficient\nsuffix'
        patched = p.patched_link_compaction(original)
        start = patched.index('    // Reclaim abandoned preprocessing arena allocations')
        end = patched.index('    // since constant export', start)
        self.assertEqual(patched[:start] + patched[end:], original)
        insertion = patched[start:end]
        self.assertIn('scan_stage_output.index_ecma_ast.iter_mut().flatten()', insertion)
        self.assertIn('*ast = ast.clone_with_compact_arena();', insertion)
        self.assertNotIn('collect', insertion)
        self.assertNotIn('par_iter', insertion)

    def test_changed_context_refuses_before_writing(self):
        self.assertTrue(callable(getattr(p, 'patched_link_compaction', None)))
        self.assertTrue(callable(getattr(p, 'patched_compact_ast', None)))
        for fn in [p.patched_link_compaction, p.patched_compact_ast]:
            with self.assertRaises(ValueError):
                fn('unreviewed source')


if __name__ == '__main__':
    unittest.main()
