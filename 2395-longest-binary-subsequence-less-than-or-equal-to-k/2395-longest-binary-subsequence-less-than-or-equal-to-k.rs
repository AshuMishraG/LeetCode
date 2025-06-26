impl Solution {
    pub fn longest_subsequence(s: String, k: i32) -> i32 {
        let (mut length, mut value) = (0, 0);
        for ch in s.bytes().rev() {
            if ch == b'0' {
                length += 1;
            } else {
                if length < 30 {
                    let bit = 1 << length;
                    if value + bit <= k {
                        value += bit;
                        length += 1;
                    }
                }
            }
        }
        length
    }
}