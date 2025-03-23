impl Solution {
    pub fn count_consistent_strings(allowed: String, words: Vec<String>) -> i32 {
        let allowed_mask: u32 = allowed.bytes().fold(0, |acc, b| acc | (1 << (b - b'a')));
        
        words.into_iter().fold(0, |count, word| {
            let word_mask: u32 = word.bytes().fold(0, |acc, b| acc | (1 << (b - b'a')));
            if word_mask & !allowed_mask == 0 { count + 1 } else { count }
        })
    }
}
