impl Solution {
    pub fn find_k_distant_indices(nums: Vec<i32>, key: i32, k: i32) -> Vec<i32> {
        let n = nums.len();
        let mut result = Vec::new();
        let k = k as usize;

        for i in 0..n {
            let start = i.saturating_sub(k);
            let end = usize::min(n - 1, i + k);
            for j in start..=end {
                if nums[j] == key {
                    result.push(i as i32);
                    break;
                }
            }
        }

        result
    }
}