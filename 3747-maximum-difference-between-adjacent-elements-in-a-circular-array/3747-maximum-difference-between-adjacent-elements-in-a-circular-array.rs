impl Solution {
    pub fn max_adjacent_distance(nums: Vec<i32>) -> i32 {
        let n = nums.len();
        let mut ans = 0;
        for i in 0..n {
            let j = (i + 1) % n;
            let diff = (nums[i] - nums[j]).abs();
            if diff > ans {
                ans = diff;
            }
        }
        ans
    }
}