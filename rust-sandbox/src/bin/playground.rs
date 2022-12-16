fn main() {
    let a = Box::new(5);
    let b = vec![1,2,3,4];
    let c = &b[0..3];
    let d = c.into_iter().map(|v| *v)
    let e = c.into_iter().map(|v| *v)
    println!("{:#?}", c.into_iter().map(|v| *v).zip(d));
}

