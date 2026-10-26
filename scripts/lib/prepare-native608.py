"""Exact source-only compiler patch. No runtime or privileged paths are accepted."""
from pathlib import Path
import hashlib
import json

RENDER = 'crates/rolldown/src/stages/generate_stage/render_chunk_to_assets.rs'
MOD = 'crates/rolldown/src/stages/generate_stage/mod.rs'
FINALIZE = 'crates/rolldown/src/stages/generate_stage/finalize_modules.rs'


def patched_renderer(text):
    start = text.index('    chunk_graph\n      .chunk_table\n      .par_iter()\n', text.index('  fn create_chunk_to_codegen_ret_map('))
    end = text.index('\n  }', start)
    replacement = '''    // Count every occurrence, including chunks filtered only AFTER codegen.
    // The complete linked graph and output order remain unchanged.
    let mut remaining = vec![0_usize; ast_table.len()];
    for chunk in chunk_graph.chunk_table.iter() {
      for &module_idx in &chunk.modules {
        if let Some(module) = self.link_output.module_table[module_idx].as_normal() {
          assert_eq!(module.idx, module_idx, "canonical AST index mismatch");
          remaining[module.idx.raw() as usize] += 1;
        }
      }
    }
    let mut asts = super::last_use_ast_table::LastUseAstTable::new(
      ast_table.into_iter().collect(), remaining,
    );
    chunk_graph
      .chunk_table
      .iter()
      .map(|item| {
        item
          .modules
          .iter()
          .map(|&module_idx| match self.link_output.module_table[module_idx].as_normal() {
            Some(module) => {
              let initial_indent = if needs_extra_indent
                || !matches!(
                  self.link_output.metas[module_idx].concatenated_wrapped_module_kind,
                  ConcatenateWrappedModuleKind::None
                ) {
                1
              } else {
                0
              };
              Some(asts.render(module.idx.raw() as usize, |ast| {
                module.render(self.options, &ModuleRenderArgs::Ecma { ast }, initial_indent)
              }))
            }
            _ => None,
          })
          .collect::<Vec<_>>()
      })
      .collect::<Vec<_>>()'''
    # This function has no other parallel iteration after this change.
    return (text[:start] + replacement + text[end:]).replace(
        '  rayon::{IntoParallelRefIterator, ParallelIterator},\n', '')


def patched_finalizer(text):
    start_marker = '        .filter(|(idx, _ast)| {\n'
    end_marker = '        .filter_map(|(idx, ast)| {\n'
    if text.count(start_marker) != 1 or text.count(end_marker) != 1 or text.count('    let finalized = ') != 1:
        raise ValueError('unreviewed finalizer source context')
    start=text.index(start_marker);end=text.index(end_marker,start)
    original=text[start:end]
    if not original.endswith('        })\n'):
        raise ValueError('unreviewed finalizer predicate boundary')
    # Derive the exact old predicate once; the old finalizer consumes it too.
    predicate=original.removesuffix('        })\n').replace(
        '        .filter(|(idx, _ast)| {','    let should_finalize = |idx| {',1).replace('*idx','idx')+'    };\n'
    insertion=predicate+"""    let mut required_asts = ast_table
      .iter_enumerated()
      .map(|(idx, _)| should_finalize(idx))
      .collect::<Vec<_>>();
    // Rendering enumerates all chunks before later optimization filtering.
    for chunk in chunk_graph.chunk_table.iter() {
      for &module_idx in &chunk.modules {
        if let Some(module) = self.link_output.module_table[module_idx].as_normal() {
          assert_eq!(module.idx, module_idx, "canonical AST index mismatch");
          required_asts[module.idx.raw() as usize] = true;
        }
      }
    }
    super::last_use_ast_table::release_unneeded(ast_table.iter_mut(), &required_asts);

"""
    text=text[:start]+'        .filter(|(idx, _ast)| should_finalize(*idx))\n'+text[end:]
    return text.replace('    let finalized = ',insertion+'    let finalized = ',1)


def prepare(source, owner):
    pin = json.loads((owner / 'docs/strict542/rolldown-source-pin608.json').read_text())
    for name, expected in pin['files'].items():
        path = source / name
        if not path.is_file() or path.is_symlink() or hashlib.sha256(path.read_bytes()).hexdigest() != expected:
            raise ValueError('upstream source pin mismatch: ' + name)
    renderer = source / RENDER
    renderer.write_text(patched_renderer(renderer.read_text()))
    finalizer = source / FINALIZE
    finalizer.write_text(patched_finalizer(finalizer.read_text()))
    mod = source / MOD
    text = mod.read_text()
    assert text.count('mod render_chunk_to_assets;') == 1
    mod.write_text(text.replace('mod render_chunk_to_assets;', 'mod last_use_ast_table;\nmod render_chunk_to_assets;'))
    helper = source / 'crates/rolldown/src/stages/generate_stage/last_use_ast_table.rs'
    helper.write_bytes((owner / 'scripts/lib/last-use-ast608.rs').read_bytes())
    return {name: hashlib.sha256((source / name).read_bytes()).hexdigest() for name in [RENDER, MOD, FINALIZE, str(helper.relative_to(source))]}


if __name__ == '__main__':
    print(json.dumps(prepare(Path('../.native608/source'), Path.cwd()), sort_keys=True))
