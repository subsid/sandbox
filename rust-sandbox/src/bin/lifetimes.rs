fn fn_lifetimes<'a, 'b>(x: &'a str, y: &'a str) -> &'a str {
    if x.len() > y.len() {
        x
    } else {
        y
    }
}

#[derive(Debug)]
struct SinglePart<'a> {
    part: &'a str
}

impl<'a> SinglePart<'a> {
    fn yoyo(&'a self, boo: &'a str) -> &'a str {
        boo
    }
}

fn single_part() {
    let s = String::from("Foobar barfoo");
    let p1 = SinglePart {
        part: &s[..3]
    };

    {
        let boo = "booo";
        println!("{}", p1.yoyo(boo));
    }

    println!("p1: {:?}", p1);
    println!("p1.yoyo(): {:?}", p1.yoyo("bar"));
}

fn main() {
    // println!("{}", fn_lifetimes("abc", "abcd"));

    single_part();

}
