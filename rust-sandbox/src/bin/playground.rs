fn main() {
    let a = "foo";
    let z = String::from("bar");

    let foo = |z| { z == a };

    println!("{:#?}", a);
    println!("{}", foo(&z));
    println!("{}", foo(&z));

    println!("Hello playground!");
}

#[cfg(test)]
mod tests {
    #[test]
    fn it_works() {
        assert_eq!(2 + 2, 4);
    }

}


