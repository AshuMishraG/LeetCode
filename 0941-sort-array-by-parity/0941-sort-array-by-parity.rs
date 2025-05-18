impl Solution {
    pub fn sort_array_by_parity(mut nums: Vec<i32>) -> Vec<i32> {
        let (mut i, mut j) = (0, nums.len() - 1);
        while i < j {
            if nums[i] % 2 == 1 {
                nums.swap(i, j);
                j -= 1;
            } else {
                i += 1;
            }
        }
        nums
    }
}