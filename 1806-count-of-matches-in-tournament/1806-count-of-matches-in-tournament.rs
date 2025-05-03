impl Solution {
    pub fn number_of_matches(mut n: i32) -> i32 {
        let mut matches = 0;
        while n > 1 {
            let played = n / 2;
            matches += played;
            n = if n % 2 == 0 { played } else { played + 1 };
        }
        matches
    }
}