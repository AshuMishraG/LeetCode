impl Solution {
    pub fn pivot_integer(n: i32) -> i32 {
        let s = n as i64 * (n as i64 + 1) / 2;
        let x = (s as f64).sqrt().floor() as i64;
        if x * x == s { x as i32 } else { -1 }
    }
}
