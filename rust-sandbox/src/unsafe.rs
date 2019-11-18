fn main() {
    let mut num = 5;

    // Can create raw pointers anywhere, but can't dereference them outside unsafe.
    let r1 = &num as *const i32;
    let r2 = &mut num as *mut i32;

    let address = 0x012345usize;
    let r = address as *const i32;

    unsafe {
        println!("r1 is {}", *r1);
        println!("r2 is {}", *r2);
        println!("r is {}", *r);
    }
}
