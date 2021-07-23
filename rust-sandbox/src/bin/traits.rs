use std::collections::HashMap;

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

fn main() {
    println!("Hello playground!");

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


