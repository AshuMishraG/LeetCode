impl Solution {
    pub fn minimum_sum(num: i32) -> i32 {
        let mut digits = [
            num / 1000,
            (num / 100) % 10,
            (num / 10) % 10,
            num % 10,
        ];
        digits.sort_unstable();                                              // 
        let new1 = digits[0] * 10 + digits[2];
        let new2 = digits[1] * 10 + digits[3];
        new1 + new2
    }
}