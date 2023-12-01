use std::collections;
use std::hash::Hash;

struct Cacher<T, Z>
where T: Fn(Z) -> Z,
      Z: Copy + Eq + Hash {
    calculation: T,
    value: collections::HashMap<Z, Z>
}

impl<T, Z> Cacher<T, Z>
where T: Fn(Z) -> Z,
      Z: Copy + Eq + Hash {
    fn new(f: T) -> Cacher<T, Z> {
        Cacher {
            calculation: f,
            value: collections::HashMap::new()
        }
    }

    fn get_value(&mut self, arg: Z) -> &Z {
        if self.value.contains_key(&arg) {
            return self.value.get(&arg).unwrap()
        } else {
            let v = (self.calculation)(arg);
            self.value.insert(arg, v);
            self.value.get(&arg).unwrap()
        }
    }
}

fn ex_2(x: &str) -> &str {
    x
}

fn main() {
    println!("Cacher main!");

    let mut expensive_function = Cacher::new(|x: i32| -> i32 {
        println!("Computing expensive value for {}", x);
        x + 1
    });

    let mut expensive_function_2 = Cacher::new(ex_2);

    expensive_function_2.get_value("foo");
    expensive_function.get_value(1);
    expensive_function.get_value(2);
    expensive_function.get_value(1);

}
