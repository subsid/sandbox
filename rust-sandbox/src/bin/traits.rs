#[allow(unused)]
mod trait_basics {
    struct Tweet {
        username: String,
        content: String,
        reply: bool,
        retweet: bool
    }

    impl Summarize for Tweet {
        fn summarize(&self) -> String {
            String::from(format!("{} {}", self.username, self.content))
        }
    }

    struct Article {
        author: String,
        headline: String,
        content: String
    }

    impl Summarize for Article {
        fn summarize(&self) -> String {
            String::from(format!("{} {} {}", self.author, self.headline, self.content))
        }
    }

    trait Summarize {
        fn summarize(&self) -> String;
    }

    fn notify<T>(t: &T)
        where T: Summarize {
        print!("{}", t.summarize());
    }

    pub fn run() {
        let tweet = Tweet {
            username: String::from("elonmusk"),
            content: String::from("To Mars we will go!"),
            reply: false,
            retweet: false
        };

        let article = Article {
            author: String::from("rowling"),
            headline: String::from("Must says"),
            content: String::from("Lets go to Mars")
        };

        notify(&article);
        notify(&tweet);
    }
}

mod assoc_types {
    struct Counter {
        count: i32
    }

    trait MyIter {
        type Out;

        fn my_next(&mut self) -> Option<Self::Out>;
    }

    trait MyIter2<T> {
        fn my_next_2(&mut self) -> Option<T>;
    }

    impl MyIter for Counter {
        type Out = i32;

        fn my_next(&mut self) -> Option<i32> {
            let c = self.count;

            self.count += 1;

            Some(c)
        }
    }

    impl MyIter2<i32> for Counter {
        fn my_next_2(&mut self) -> Option<i32> {
            let c = self.count;

            self.count += 1;

            Some(c)
        }

    }

    impl MyIter2<String> for Counter {
        fn my_next_2(&mut self) -> Option<String> {
            let c = self.count;

            self.count += 1;

            Some(c.to_string())
        }
    }

    pub fn run() {
        let mut _c = Counter{count: 0};
        let mut c2 = Counter{count: 0};

        println!("Assoc Iter {:?}", MyIter2::<i32>::my_next_2(&mut c2));
        println!("Assoc Iter {:?}", c2.my_next());
        // println!("Assoc Iter {:?}", c2.my_next_2());
        // println!("Assoc Iter {:?}", c2.my_next_2());
        // println!("Assoc Iter {:?}", c2.my_next_2());
        // println!("Assoc Iter {:?}", c2.my_next_2());
    }
}

fn main() {
    // trait_basics::run();
    assoc_types::run();
}


