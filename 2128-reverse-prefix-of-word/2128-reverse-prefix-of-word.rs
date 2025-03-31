impl Solution {
    pub fn reverse_prefix(word: String, ch: char) -> String {
        if let Some(idx) = word.find(ch) {
            let (prefix, suffix) = word.split_at(idx + 1);
            let reversed_prefix: String = prefix.chars().rev().collect();
            format!("{}{}", reversed_prefix, suffix)
        } else {
            word
        }
    }
}