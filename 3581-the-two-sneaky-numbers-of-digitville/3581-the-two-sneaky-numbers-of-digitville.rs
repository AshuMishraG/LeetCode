impl Solution {
    pub fn get_sneaky_numbers(nums: Vec<i32>) -> Vec<i32> {
        let n = nums.len() - 2;
        let mut freq = vec![0; n];
        for &num in &nums {
            freq[num as usize] += 1;
        }
        let mut result = Vec::with_capacity(2);
        for (i, &count) in freq.iter().enumerate() {
            if count == 2 {
                result.push(i as i32);
            }
        }
        result
    }
}