impl Solution {
    pub fn merge_alternately(word1: String, word2: String) -> String {
        let mut result = String::with_capacity(word1.len() + word2.len());
        let mut it1 = word1.chars();
        let mut it2 = word2.chars();

        loop {
            match (it1.next(), it2.next()) {
                (Some(c1), Some(c2)) => {
                    result.push(c1);
                    result.push(c2);
                },
                (Some(c1), None) => {
                    result.push(c1);
                    result.extend(it1);
                    break;
                },
                (None, Some(c2)) => {
                    result.push(c2);
                    result.extend(it2);
                    break;
                },
                (None, None) => break,
            }
        }
        result
    }
}