use std::collections::HashMap;

impl Solution {
    pub fn frequency_sort(mut nums: Vec<i32>) -> Vec<i32> {
        let mut freq = HashMap::new();
        for &num in &nums {
            *freq.entry(num).or_insert(0) += 1;
        }
        nums.sort_by(|&a, &b| {
            let fa = freq.get(&a).unwrap();
            let fb = freq.get(&b).unwrap();
            if fa != fb {
                fa.cmp(fb)
            } else {
                b.cmp(&a)
            }
        });
        nums
    }
}