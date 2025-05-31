impl Solution {
    pub fn array_rank_transform(arr: Vec<i32>) -> Vec<i32> {
        let mut sorted = arr.clone();
        sorted.sort_unstable();
        sorted.dedup();
        let mut rank = std::collections::HashMap::new();
        for (i, &val) in sorted.iter().enumerate() {
            rank.insert(val, (i + 1) as i32);
        }
        arr.into_iter().map(|v| rank[&v]).collect()
    }
}