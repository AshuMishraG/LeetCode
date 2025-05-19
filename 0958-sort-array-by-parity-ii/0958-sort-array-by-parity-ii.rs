impl Solution {
    pub fn sort_array_by_parity_ii(mut nums: Vec<i32>) -> Vec<i32> {
        let (mut i, mut j) = (0, 1);
        let n = nums.len();
        while i < n && j < n {
            if nums[i] % 2 == 0 {
                i += 2;
                continue;
            }
            if nums[j] % 2 == 1 {
                j += 2;
                continue;
            }
            nums.swap(i, j);
        }
        nums
    }
}