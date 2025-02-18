impl Solution {
    pub fn build_array(mut nums: Vec<i32>) -> Vec<i32> {
        let n = nums.len() as i32;
        for i in 0..nums.len() {
            let original_value = nums[nums[i] as usize];
            let new_val = original_value % n;
            nums[i] += new_val * n;
        }
        for i in 0..nums.len() {
            nums[i] /= n; 
        }
        nums 
    }
}
