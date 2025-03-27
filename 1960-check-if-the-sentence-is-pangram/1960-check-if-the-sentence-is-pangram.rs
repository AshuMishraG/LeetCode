impl Solution {
    pub fn check_if_pangram(sentence: String) -> bool {
        let mut mask = 0;
        for b in sentence.bytes() {
            mask |= 1 << (b - b'a');
            if mask == (1 << 26) - 1 {
                return true;
            }
        }
        mask == (1 << 26) - 1
    }
}