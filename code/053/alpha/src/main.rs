fn main() {
    let mut a: u128 = 1;
    let mut b: u128 = 1;
    let mut c: u128 = a + b;
    let mut count: u32 = 3;
    while count < 181 {
        println!("count = {count} > a = {a} - b = {b} - c = {c}");
        a = b;
        b = c;
        c = a + b;
        count += 1;
    }
}
