impl Solution {
    pub fn number_of_steps(num: i32) -> i32 {
        let mut n = num;
        let mut steps = 0;
        while n > 0 {
            if n & 1 == 0 {
                n >>= 1;
            } else {
                n -= 1;
            }
            steps += 1;
        }
        steps
    }
}
