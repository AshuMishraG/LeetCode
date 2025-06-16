impl Solution {
    pub fn maximum_difference(nums: Vec<i32>) -> i32 {
        let mut min_val = nums[0];
        let mut ans = -1;
        for &x in nums.iter().skip(1) {
            if x > min_val {
                ans = ans.max(x - min_val);
            } else if x < min_val {
                min_val = x;
            }
        }
        ans
    }
}