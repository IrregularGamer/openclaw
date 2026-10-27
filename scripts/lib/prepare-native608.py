"""Exact source-only compiler patch. No runtime or privileged paths are accepted."""
from pathlib import Path
import hashlib
import json

RENDER = 'crates/rolldown/src/stages/generate_stage/render_chunk_to_assets.rs'
MOD = 'crates/rolldown/src/stages/generate_stage/mod.rs'
FINALIZE = 'crates/rolldown/src/stages/generate_stage/finalize_modules.rs'
COMPACT_TESTS = r'''
#[cfg(test)]
mod compact_arena_tests {
  use super::EcmaAst;
  use crate::{EcmaCompiler, PrintOptions};
  use oxc::{
    ast::ast,
    ast_visit::{VisitJs, walk_js},
    semantic::{ScopeFlags, ScopeId},
    span::SourceType,
  };
  use std::cell::Cell;

  #[derive(Default)]
  struct Identity(Vec<String>);
  impl<'ast> VisitJs<'ast> for Identity {
    fn enter_scope(&mut self, flags: ScopeFlags, scope: &Cell<Option<ScopeId>>) {
      self.0.push(format!("scope:{flags:?}:{:?}", scope.get()));
    }
    fn visit_binding_identifier(&mut self, it: &ast::BindingIdentifier<'ast>) {
      self.0.push(format!("binding:{}:{:?}:{:?}", it.name, it.node_id(), it.symbol_id.get()));
    }
    fn visit_identifier_reference(&mut self, it: &ast::IdentifierReference<'ast>) {
      self.0.push(format!("reference:{}:{:?}:{:?}", it.name, it.node_id(), it.reference_id.get()));
    }
    fn visit_import_declaration(&mut self, it: &ast::ImportDeclaration<'ast>) {
      self.0.push(format!("import:{:?}", it.node_id()));
      walk_js::walk_import_declaration(self, it);
    }
    fn visit_import_expression(&mut self, it: &ast::ImportExpression<'ast>) {
      self.0.push(format!("dynamic:{:?}", it.node_id()));
      walk_js::walk_import_expression(self, it);
    }
    fn visit_call_expression(&mut self, it: &ast::CallExpression<'ast>) {
      self.0.push(format!("call:{:?}", it.node_id()));
      walk_js::walk_call_expression(self, it);
    }
    fn visit_new_expression(&mut self, it: &ast::NewExpression<'ast>) {
      self.0.push(format!("new:{:?}", it.node_id()));
      walk_js::walk_new_expression(self, it);
    }
  }
  fn identities(ast: &EcmaAst) -> Vec<String> {
    let mut result=Identity::default();
    result.visit_program(ast.program());
    result.0
  }

  #[test]
  fn compact_clone_reclaims_abandoned_arena_and_preserves_scan_identity() {
    let source=r#"import { x as imported } from 'dep';
      export function f(parameter) {
        const target = new URL('asset', import.meta.url);
        return imported(parameter) + require('dep').value + import('lazy') + target.href;
      }"#;
    let mut ast=EcmaCompiler::parse("compact.mjs", source, SourceType::mjs()).unwrap();
    // Matches scan's post-semantic boundary; never rebuild semantic after cloning.
    let _scoping=ast.make_scoping();
    let before_ids=identities(&ast);
    assert!(before_ids.iter().any(|v| v.starts_with("dynamic:")));
    assert!(before_ids.iter().any(|v| v.starts_with("new:")));
    assert!(before_ids.iter().any(|v| v.starts_with("binding:")));
    let before_code=EcmaCompiler::print_with(&ast, PrintOptions::default()).code;
    ast.program.with_mut(|fields| {
      // Preprocessing uses a bump allocator; replaced nodes leave unreachable bytes.
      let _abandoned=fields.allocator.alloc([0_u8; 65536]);
    });
    let old_used=ast.program.borrow_owner().allocator.used_bytes();
    let old_capacity=ast.program.borrow_owner().allocator.capacity();
    // Exercise the previous allocation policy as a negative control.
    let retained=ast.clone_with_another_arena();
    assert!(retained.program.borrow_owner().allocator.capacity() >= old_used);
    drop(retained);
    let compact=ast.clone_with_compact_arena();
    assert_eq!(compact.source_type, ast.source_type);
    assert_eq!(compact.source(), ast.source());
    assert_eq!(compact.program().span, ast.program().span);
    assert_eq!(identities(&compact), before_ids);
    assert_eq!(EcmaCompiler::print_with(&compact, PrintOptions::default()).code, before_code);
    assert!(compact.program.borrow_owner().allocator.used_bytes() + 32768 < old_used);
    // Detects preallocating old.used_bytes(): used bytes alone misses reserved waste.
    assert!(compact.program.borrow_owner().allocator.capacity() + 32768 < old_capacity);
    drop(ast);
    assert_eq!(identities(&compact), before_ids);
    assert_eq!(EcmaCompiler::print_with(&compact, PrintOptions::default()).code, before_code);
  }
}
'''

AST = 'crates/rolldown_ecmascript/src/ecma_ast/mod.rs'
LINK = 'crates/rolldown/src/stages/link_stage/mod.rs'


def patched_link_compaction(text):
    boundary = '''  pub fn new(mut scan_stage_output: NormalizedScanStageOutput, options: &'a SharedOptions) -> Self {
    // since constant export is spared in most of time, aggregate them would make searching more efficient'''
    if text.count(boundary) != 1:
        raise ValueError('unreviewed scan-to-link ownership boundary')
    insertion = '''    // Reclaim abandoned preprocessing arena allocations before link metadata.
    // Each assignment drops the old arena before the next module is cloned.
    // The canonical clone preserves every semantic ID and source allocation.
    for ast in scan_stage_output.index_ecma_ast.iter_mut().flatten() {
      *ast = ast.clone_with_compact_arena();
    }

'''
    return text.replace(boundary, boundary.replace('    // since constant export', insertion + '    // since constant export'), 1)


def patched_compact_ast(text):
    boundary = '''  pub fn clone_with_another_arena(&self) -> EcmaAst {
    let program = ProgramCell::new('''
    allocator = '        allocator: Allocator::with_capacity(self.program.borrow_owner().allocator.used_bytes()),'
    if text.count(boundary) != 1 or text.count(allocator) != 1:
        raise ValueError('unreviewed canonical semantic-ID clone')
    replacement = '''  pub fn clone_with_another_arena(&self) -> EcmaAst {
    self.clone_in_arena(Allocator::with_capacity(self.program.borrow_owner().allocator.used_bytes()))
  }

  /// Compact a completed preprocessing pass without retaining its dead arena nodes.
  /// Between passes all external AST references are semantic IDs, not pointers.
  #[must_use]
  pub fn clone_with_compact_arena(&self) -> EcmaAst {
    self.clone_in_arena(Allocator::default())
  }

  fn clone_in_arena(&self, allocator: Allocator) -> EcmaAst {
    let program = ProgramCell::new('''
    return text.replace(boundary, replacement, 1).replace(allocator, '        allocator,', 1) + COMPACT_TESTS


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
        '        .filter(|(idx, _ast)| {','    let should_finalize = |idx: rolldown_common::ModuleIdx| {',1).replace('*idx','idx')+'    };\n'
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


def patched_generate_stage(text):
    boundary = '''    let final_esm_init_metadata =
      self.compute_wrapped_esm_init_metadata(&ast_table, &chunk_graph, &order_state);

    self.compute_cross_chunk_links('''
    if text.count(boundary) != 1:
        raise ValueError('unreviewed post-metadata AST reader boundary')
    insertion = '''    // Last metadata AST reader has completed. Conservatively retain every
    // possible later finalizer and every renderer, before cross-link allocations.
    let has_required_order_runtime = !order_state.required_runtime_helpers().is_empty();
    let mut required_asts = ast_table
      .iter_enumerated()
      .map(|(idx, _)| {
        self.link_output.module_table[idx].as_normal().is_some_and(|m| {
          self.link_output.metas[m.idx].is_included
            || (m.idx == self.link_output.runtime.id() && has_required_order_runtime)
        })
      })
      .collect::<Vec<_>>();
    for chunk in chunk_graph.chunk_table.iter() {
      for &module_idx in &chunk.modules {
        if let Some(module) = self.link_output.module_table[module_idx].as_normal() {
          assert_eq!(module.idx, module_idx, "canonical AST index mismatch");
          required_asts[module.idx.raw() as usize] = true;
        }
      }
    }
    last_use_ast_table::release_unneeded(ast_table.iter_mut(), &required_asts);
    drop(required_asts);

'''
    return text.replace(boundary, boundary.replace('    self.compute_cross_chunk_links(',
        insertion+'    self.compute_cross_chunk_links('), 1)


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
    mod.write_text(patched_generate_stage(text).replace('mod render_chunk_to_assets;', 'mod last_use_ast_table;\nmod render_chunk_to_assets;'))
    ast = source / AST
    ast.write_text(patched_compact_ast(ast.read_text()))
    link = source / LINK
    link.write_text(patched_link_compaction(link.read_text()))
    helper = source / 'crates/rolldown/src/stages/generate_stage/last_use_ast_table.rs'
    helper.write_bytes((owner / 'scripts/lib/last-use-ast608.rs').read_bytes())
    return {name: hashlib.sha256((source / name).read_bytes()).hexdigest() for name in [RENDER, MOD, FINALIZE, AST, LINK, str(helper.relative_to(source))]}


if __name__ == '__main__':
    print(json.dumps(prepare(Path('../.native608/source'), Path.cwd()), sort_keys=True))
