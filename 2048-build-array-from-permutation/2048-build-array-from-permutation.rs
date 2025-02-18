impl Solution {
    pub fn build_array(nums: Vec<i32>) -> Vec<i32> {
        let n = nums.len();
        let mut ans = Vec::with_capacity(n);
        for i in 0..n {
            ans.push(nums[nums[i] as usize]);
        }
        ans
    }
}
