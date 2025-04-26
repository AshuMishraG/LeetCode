impl Solution {
    pub fn get_longest_subsequence(words: Vec<String>, groups: Vec<i32>) -> Vec<String> {
        let mut result = Vec::new();
        if words.is_empty() { return result; }
        result.push(words[0].clone());
        for i in 1..words.len() {
            if groups[i] != groups[i - 1] {
                result.push(words[i].clone());
            }
        }
        result
    }
}
