impl Solution {
    pub fn kth_distinct(arr: Vec<String>, k: i32) -> String {
        use std::collections::HashMap;
        let mut freq = HashMap::new();
        for s in &arr {
            *freq.entry(s).or_insert(0) += 1;
        }
        let mut count = 0;
        for s in &arr {
            if freq[s] == 1 {
                count += 1;
                if count == k {
                    return s.clone();
                }
            }
        }
        "".to_string()
    }
}
