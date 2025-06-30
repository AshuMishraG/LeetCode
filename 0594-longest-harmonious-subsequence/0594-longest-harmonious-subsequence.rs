use std::collections::HashMap;

impl Solution {
    pub fn find_lhs(nums: Vec<i32>) -> i32 {
        let mut freq = HashMap::new();
        for &x in &nums {
            *freq.entry(x).or_insert(0) += 1;
        }
        let mut ans = 0;
        for (&x, &cnt) in &freq {
            if let Some(&cnt_next) = freq.get(&(x + 1)) {
                ans = ans.max(cnt + cnt_next);
            }
        }
        ans
    }
}
