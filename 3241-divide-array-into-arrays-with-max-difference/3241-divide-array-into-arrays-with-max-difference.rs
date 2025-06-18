impl Solution {
    pub fn divide_array(nums: Vec<i32>, k: i32) -> Vec<Vec<i32>> {
        let mut nums = nums;
        nums.sort();

        let mut result = Vec::new();

        for i in (0..nums.len()).step_by(3) {
            let group = &nums[i..i + 3];

            if group[2] - group[0] > k {
                return vec![];
            }

            result.push(group.to_vec());
        }

        result
    }
}