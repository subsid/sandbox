mod box_basics {
    use std::ops::Deref;

    #[derive(Debug)]
    enum List<T> {
        Cons(T, Box<List<T>>),
        Nil
    }

    struct MyBox<T>(T);

    impl<T> Deref for MyBox<T> {
        type Target = T;

        fn deref(&self) -> &Self::Target {
            println!("Derefing");

            &self.0
        }
    }

    impl<T> Drop for MyBox<T> {
        fn drop(&mut self) {
            println!("Dropping box value");
        }
    }


    pub fn run() {
        // println!("Box basics");
        // let a = List::Cons(1, Box::new(List::Cons(2, Box::new(List::Nil))));
        // println!("{:?}", a);
        let v = 10;
        let w = MyBox(10);

        assert_eq!(v, *w);
    }
}

mod ref_counting {
    use std::rc::Rc;

    #[derive(Debug)]
    pub enum List<T> {
        Cons(T, Rc<List<T>>),
        Nil
    }

    pub fn run() {
        let a = Rc::new(List::Cons("my dear ", Rc::new(List::Cons("world", Rc::new(List::Nil)))));
        println!("RC count of a: {}", Rc::strong_count(&a));

        let b = List::Cons("hello ", Rc::clone(&a));

        {
            println!("RC count of a: {}", Rc::strong_count(&a));
            let c = List::Cons("yolo ", Rc::clone(&a));
            println!("RC count of a: {}", Rc::strong_count(&a));
            println!("c: {:?}", c);
        }

        println!("RC count of a: {}", Rc::strong_count(&a));
        println!("b: {:?}", b);
    }
}

mod interior_mut_pattern {
    use std::cell::RefCell;
    use std::rc::Rc;

    #[derive(Debug)]
    enum List<T> {
        Cons(Rc<RefCell<T>>, Rc<List<T>>),
        Nil
    }

    pub fn run() {
        // mutable ref to immutable data is a nono.
        // let a = String::from("abc");
        // let b = &mut a;

        // immutable ref to mutable data is a nono.
        // let mut c = String::from("abc");
        // let d = &mut c;
        // (*d).push_str("100");

        // Thus borrow checker rules prevent us from mutating some underlying data with immutable
        // ref. We can make d mutable, but that would mean only 1 ref.

        // Refcell smart pointer to the rescue!
        let v = Rc::new(RefCell::new(String::from("world")));
        let a = Rc::new(List::Cons(Rc::clone(&v), Rc::new(List::Nil)));
        let b = List::Cons(Rc::new(RefCell::new(String::from("hello "))), Rc::clone(&a));
        let c = List::Cons(Rc::new(RefCell::new(String::from("howdy "))), Rc::clone(&a));

        (*v).borrow_mut().push_str("y");

        println!("a: {:?}", a);
        println!("b: {:?}", b);
        println!("c: {:?}", c);


    }

}

fn main() {
    box_basics::run();
    // ref_counting::run();
    // interior_mut_pattern::run();
}

