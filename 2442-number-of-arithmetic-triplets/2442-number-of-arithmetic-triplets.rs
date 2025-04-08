use std::collections::HashSet;

impl Solution {
    pub fn arithmetic_triplets(nums: Vec<i32>, diff: i32) -> i32 {
        let set: HashSet<i32> = nums.iter().copied().collect();
        nums.iter()
            .filter(|&&x| set.contains(&(x + diff)) && set.contains(&(x + 2 * diff)))
            .count() as i32
    }
}
