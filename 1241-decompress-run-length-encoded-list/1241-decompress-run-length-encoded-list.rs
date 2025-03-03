impl Solution {
    pub fn decompress_rl_elist(nums: Vec<i32>) -> Vec<i32> {
        nums.chunks(2)
            .flat_map(|chunk| std::iter::repeat(chunk[1]).take(chunk[0] as usize))
            .collect()
    }
}