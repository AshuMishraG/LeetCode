impl Solution {
    pub fn num_identical_pairs(nums: Vec<i32>) -> i32 {
        let mut freq = vec![0; 101];
        for num in nums {
            freq[num as usize] += 1;
        }
        freq.iter().map(|&f| f * (f - 1) / 2).sum()
    }
}