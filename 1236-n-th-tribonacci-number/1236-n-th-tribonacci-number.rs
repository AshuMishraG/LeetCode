impl Solution {
    pub fn tribonacci(n: i32) -> i32 {
        if n == 0 { return 0; }
        if n <= 2 { return 1; }

        let (mut t0, mut t1, mut t2) = (0, 1, 1);
        let mut t3 = 0;

        for _ in 3..=n {
            t3 = t0 + t1 + t2;
            t0 = t1;
            t1 = t2;
            t2 = t3;
        }
        t3
    }
}
