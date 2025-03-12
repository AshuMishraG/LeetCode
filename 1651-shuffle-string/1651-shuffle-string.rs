impl Solution {
    pub fn restore_string(s: String, indices: Vec<i32>) -> String {
        let n = s.len();
        let mut res = vec![' '; n];
        for (i, ch) in s.chars().enumerate() {
            res[indices[i] as usize] = ch;
        }
        res.into_iter().collect()
    }
}