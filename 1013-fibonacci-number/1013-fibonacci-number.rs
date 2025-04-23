impl Solution {
    pub fn fib(n: i32) -> i32 {
        if n < 2 {
            return n;
        }
        let (mut a, mut b) = (0, 1);
        for _ in 2..=n {
            let c = a + b;
            a = b;
            b = c;
        }
        b
    }
}