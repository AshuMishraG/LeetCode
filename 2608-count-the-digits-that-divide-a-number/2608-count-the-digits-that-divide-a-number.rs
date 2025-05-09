impl Solution {
    pub fn count_digits(num: i32) -> i32 {
        let mut count = 0;
        let mut x = num;
        while x > 0 {
            let d = x % 10;
            if num % d == 0 {
                count += 1;
            }
            x /= 10;
        }
        count
    }
}