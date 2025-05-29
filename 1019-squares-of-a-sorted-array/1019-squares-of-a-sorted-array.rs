impl Solution {
    pub fn sorted_squares(nums: Vec<i32>) -> Vec<i32> {
        let mut res = vec![0; nums.len()];
        let (mut left, mut right, mut pos) = (0, nums.len() - 1, nums.len() - 1);
        while left <= right {
            let left_sq = nums[left] * nums[left];
            let right_sq = nums[right] * nums[right];
            if left_sq > right_sq {
                res[pos] = left_sq;
                left += 1;
            } else {
                res[pos] = right_sq;
                if right == 0 { break; }
                right -= 1;
            }
            if pos == 0 { break; }
            pos -= 1;
        }
        res
    }
}