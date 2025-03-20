impl Solution {
    pub fn balanced_string_split(s: String) -> i32 {
        let mut count = 0;
        let mut ans = 0;
        for c in s.chars() {
            if c == 'R' {
                count += 1;
            } else {
                count -= 1;
            }
            if count == 0 {
                ans += 1;
            }
        }
        ans
    }
}