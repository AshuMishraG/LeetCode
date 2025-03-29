impl Solution {
    pub fn sort_sentence(s: String) -> String {
        let mut words: Vec<&str> = s.split_whitespace().collect();
        words.sort_unstable_by_key(|word| word.chars().last().unwrap());
        words.into_iter()
             .map(|word| &word[..word.len()-1])
             .collect::<Vec<&str>>()
             .join(" ")
    }
}