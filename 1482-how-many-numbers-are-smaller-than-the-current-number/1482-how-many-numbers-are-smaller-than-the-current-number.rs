impl Solution {
    pub fn smaller_numbers_than_current(nums: Vec<i32>) -> Vec<i32> {
        let mut count = [0; 101];
        let mut result = Vec::with_capacity(nums.len());

        // Count the occurrences of each number in nums
        for &num in &nums {
            count[num as usize] += 1;
        }

        // Compute the prefix sums to determine how many numbers are smaller than each value
        for i in 1..101 {
            count[i] += count[i - 1];
        }

        // Construct the result array
        for &num in &nums {
            if num == 0 {
                result.push(0);
            } else {
                result.push(count[(num - 1) as usize]);
            }
        }

        result
    }
}
