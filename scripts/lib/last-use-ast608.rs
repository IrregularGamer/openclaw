// Compiled into the pinned disposable Rolldown compiler, never into the gateway.
// R cannot borrow the input: render returns an owned result before its AST drops.
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
    use super::LastUseAstTable;
    use std::{cell::RefCell, rc::Rc};

    struct Ast(usize, Rc<RefCell<Vec<usize>>>);
    impl Drop for Ast {
        fn drop(&mut self) { self.1.borrow_mut().push(self.0); }
    }
    fn ast(id: usize, drops: &Rc<RefCell<Vec<usize>>>) -> Option<Ast> {
        Some(Ast(id, drops.clone()))
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
