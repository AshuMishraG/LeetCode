impl Solution {
    pub fn smaller_numbers_than_current(nums: Vec<i32>) -> Vec<i32> {
        let mut freq = vec![0; 101];
        // Count frequency for each number (0 to 100)
        for &num in &nums {
            freq[num as usize] += 1;
        }
        // Build prefix sum: for each number, freq[i] becomes count of numbers ≤ i.
        for i in 1..101 {
            freq[i] += freq[i - 1];
        }
        // For each number, the answer is the count of numbers strictly less than it.
        nums.into_iter()
            .map(|num| if num == 0 { 0 } else { freq[num as usize - 1] })
            .collect()
    }
}
