impl Solution {
    pub fn possible_string_count(word: String) -> i32 {
        let mut ans = 1;
        let b = word.as_bytes();
        for i in 1..b.len() {
            if b[i] == b[i - 1] {
                ans += 1;
            }
        }
        ans
    }
}