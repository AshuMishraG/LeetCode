impl Solution {
    pub fn maximum_number_of_string_pairs(words: Vec<String>) -> i32 {
        // Fixed-size array for possible two-letter words, mapped into indices 0..=675.
        let mut present = [false; 26 * 26];
        // Mark each word's presence.
        for word in &words {
            let bytes = word.as_bytes();
            // Each word is exactly 2 characters: xy => index = (x - 'a')*26 + (y - 'a')
            let index = ((bytes[0] - b'a') as usize) * 26 + ((bytes[1] - b'a') as usize);
            present[index] = true;
        }
        let mut count = 0;
        // For each word that is present, check if its reverse exists.
        for i in 0..(26 * 26) {
            if present[i] {
                // Convert index back to two letters:
                let first = i / 26;
                let second = i % 26;
                // Reverse: from (first, second) to (second, first)
                let rev = second * 26 + first;
                // To avoid double-counting, only count when i < rev.
                if i < rev && present[rev] {
                    count += 1;
                }
            }
        }
        count
    }
}
