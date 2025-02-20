use std::collections::HashSet;

impl Solution {
    pub fn unique_morse_representations(words: Vec<String>) -> i32 {
        let morse = [
            ".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---",
            "-.-", ".-..", "--", "-.", "---", ".--.", "--.-", ".-.", "...", "-",
            "..-", "...-", ".--", "-..-", "-.--", "--.."
        ];
        
        let mut seen = HashSet::new();
        
        for word in words {
            let mut transformation = String::new();
            for c in word.chars() {
                transformation.push_str(morse[(c as usize) - ('a' as usize)]);
            }
            seen.insert(transformation);
        }
        
        seen.len() as i32
    }
}