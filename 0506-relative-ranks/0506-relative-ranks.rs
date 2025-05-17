impl Solution {
    pub fn find_relative_ranks(score: Vec<i32>) -> Vec<String> {
        let n = score.len();
        let mut pairs: Vec<(i32, usize)> = score.into_iter().zip(0..n).collect();
        pairs.sort_unstable_by(|a, b| b.0.cmp(&a.0));
        let mut ans = vec![String::new(); n];
        let medals = ["Gold Medal", "Silver Medal", "Bronze Medal"];
        for (rank, &(_sc, idx)) in pairs.iter().enumerate() {
            ans[idx] = if rank < 3 {
                medals[rank].to_string()
            } else {
                (rank + 1).to_string()
            };
        }
        ans
    }
}