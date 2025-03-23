impl Solution {
    pub fn count_consistent_strings(allowed: String, words: Vec<String>) -> i32 {
        let mut allowed_mask = 0;
        for c in allowed.chars() {
            allowed_mask |= 1 << (c as u8 - b'a');
        }
        
        words.iter().filter(|word| {
            let mut word_mask = 0;
            for c in word.chars() {
                word_mask |= 1 << (c as u8 - b'a');
            }
            word_mask & !allowed_mask == 0
        }).count() as i32
    }
}