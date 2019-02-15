fn main() {
    let s_imm = String::from(" s_imm: main");
    let mut s_mut = String::from(" s_mut: main");
    let mut s_mut2 = String::from(" s_mut2: main");

    // Move semantics
    // Move s to function, it can read/write value, it has control.
    // The function argument is a new stack variable, pointing to the struct.
    // This can be mutable or immutable.
    // change_move(s_imm, s_mut);
    // This won't work, as main does not have access to s_imm after the first arg is passed.
    // change_move(s_imm, s_imm);
    // This won't work, as main no longer has access to s_imm
    // println!("{}", s_imm);

    // Borrow semantics
    // Give reference of s_mut to function, it can read value, but does not own it.
    // It cannot write to s_mut.
    // change_borrow(&s_mut, &s_mut);
    // This works, as the func just borrows the value, hence is not killed at end of its scope
    // println!("{}", s_mut);

    // Mutable borrow semantics
    // Give mutable reference of s to function, it can read/write value, but does not own it.
    // change_borrow_mut(&mut s_mut, &s_imm);
    // This does not work, as after the mutable borrow arg, main loses access to it, till the
    // function is done.
    // change_borrow_mut(&mut s_mut, &s_mut);
    // This works, as the func just borrows the value. It has also been changed!
    // println!("{}", s_mut);
}

fn change_move(mut s1: String, s2: String) {
    println!("change_move start");
    s1.push_str(&s2);
    println!("s1 = {}", s1);
    println!("change_move end");
}

fn change_borrow(s1: &String, s2: &String) {
    println!("change_borrow start");
    // s1.push_str(s2);
    println!("s1 = {}", s1);
    println!("s2 = {}", s2);
    println!("change_borrow end");
}

fn change_borrow_mut(s1: &mut String, s2: &String) {
    println!("change_borrow_mut start");
    s1.push_str(s2);
    println!("s1 = {}", s1);
    println!("s2 = {}", s2);
    println!("change_borrow_mut end");
}
