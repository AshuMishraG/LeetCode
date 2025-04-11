use std::collections::HashSet;

impl Solution {
    pub fn maximum_number_of_string_pairs(words: Vec<String>) -> i32 {
        let mut set: HashSet<String> = words.into_iter().collect();
        let mut count = 0;
        for word in set.clone() {
            let rev: String = word.chars().rev().collect();
            if word != rev && set.contains(&rev) {
                count += 1;
                set.remove(&word);
                set.remove(&rev);
            }
        }
        count
    }
}