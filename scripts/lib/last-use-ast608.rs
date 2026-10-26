// Compiled into the pinned disposable Rolldown compiler, never into the gateway.
// R cannot borrow the input: render returns an owned result before its AST drops.
// Release only slots outside the union of every remaining AST reader.
pub(super) fn release_unneeded<'a, T: 'a>(
    values: impl ExactSizeIterator<Item = &'a mut Option<T>>,
    required: &[bool],
) {
    assert_eq!(values.len(), required.len(), "AST reader census length mismatch");
    for (value, required) in values.zip(required) {
        if !*required { drop(value.take()); }
    }
}

pub(super) struct LastUseAstTable<T> {
    values: Vec<Option<T>>,
    remaining: Vec<usize>,
}

impl<T> LastUseAstTable<T> {
    pub(super) fn new(mut values: Vec<Option<T>>, remaining: Vec<usize>) -> Self {
        assert_eq!(values.len(), remaining.len(), "AST census length mismatch");
        for (value, count) in values.iter_mut().zip(&remaining) {
            if *count == 0 {
                drop(value.take());
            }
        }
        Self { values, remaining }
    }

    pub(super) fn render<R>(&mut self, index: usize, render: impl FnOnce(&T) -> R) -> R {
        assert!(self.remaining[index] > 0, "AST census exhausted");
        let result = render(self.values[index].as_ref().expect("should have ast"));
        self.remaining[index] -= 1;
        if self.remaining[index] == 0 {
            drop(self.values[index].take());
        }
        result
    }
}

#[cfg(test)]
mod tests {
    use super::{LastUseAstTable, release_unneeded};
    use std::{cell::RefCell, rc::Rc};

    struct Ast(usize, Rc<RefCell<Vec<usize>>>);
    impl Drop for Ast {
        fn drop(&mut self) { self.1.borrow_mut().push(self.0); }
    }
    fn ast(id: usize, drops: &Rc<RefCell<Vec<usize>>>) -> Option<Ast> {
        Some(Ast(id, drops.clone()))
    }

    #[test]
    fn early_reader_union_retains_finalizer_only_renderer_only_and_both() {
        let drops = Rc::new(RefCell::new(vec![]));
        let mut values = vec![ast(0,&drops), ast(1,&drops), ast(2,&drops), ast(3,&drops), None];
        // Finalizer-only1, renderer-only2, both3; unused0 may drop now.
        release_unneeded(values.iter_mut(), &[false,true,true,true,false]);
        assert_eq!(*drops.borrow(), vec![0]);
        assert!(values[0].is_none());
        for idx in 1..4 { assert_eq!(values[idx].as_ref().unwrap().0, idx); }
    }

    #[test]
    #[should_panic(expected="AST reader census length mismatch")]
    fn early_release_refuses_incomplete_reader_census() {
        release_unneeded([Some(1)].iter_mut(), &[]);
    }

    #[test]
    fn unused_is_released_before_first_render() {
        let drops = Rc::new(RefCell::new(vec![]));
        let mut table = LastUseAstTable::new(vec![ast(0,&drops),ast(1,&drops),None], vec![0,1,0]);
        assert_eq!(*drops.borrow(), vec![0]);
        let result = table.render(1, |value| {
            assert_eq!(*drops.borrow(), vec![0]);
            format!("owned:{}",value.0)
        });
        assert_eq!(result,"owned:1");
        assert_eq!(*drops.borrow(),vec![0,1]);
    }

    #[test]
    fn repeated_module_survives_until_last_render_then_drops_before_next_module() {
        let drops = Rc::new(RefCell::new(vec![]));
        let mut table = LastUseAstTable::new(vec![ast(0,&drops),ast(1,&drops)], vec![2,1]);
        assert_eq!(table.render(0, |v| v.0),0);
        assert!(drops.borrow().is_empty());
        assert_eq!(table.render(0, |v| {assert!(drops.borrow().is_empty());v.0}),0);
        assert_eq!(*drops.borrow(),vec![0]);
        table.render(1, |_| assert_eq!(*drops.borrow(),vec![0]));
        assert_eq!(*drops.borrow(),vec![0,1]);
    }

    #[test]
    #[should_panic(expected="should have ast")]
    fn referenced_missing_ast_still_refuses() {
        LastUseAstTable::<Ast>::new(vec![None],vec![1]).render(0, |_| ());
    }

    #[test]
    #[should_panic(expected="AST census exhausted")]
    fn extra_read_cannot_reuse_released_ast() {
        let mut table=LastUseAstTable::new(vec![Some(42)],vec![1]);
        assert_eq!(table.render(0,|v| *v),42);
        table.render(0,|v| *v);
    }

    #[test]
    #[should_panic(expected="AST census length mismatch")]
    fn incomplete_census_refuses() { LastUseAstTable::<Ast>::new(vec![None],vec![]); }
}
