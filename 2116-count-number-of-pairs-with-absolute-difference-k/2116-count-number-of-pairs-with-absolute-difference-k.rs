impl Solution {
    pub fn count_k_difference(nums: Vec<i32>, k: i32) -> i32 {
        let mut freq = vec![0; 101];
        for num in nums {
            freq[num as usize] += 1;
        }
        
        let mut count = 0;
        for x in 1..=100 {
            if x + k as usize <= 100 {
                count += freq[x] * freq[x + k as usize];
            }
        }
        count as i32
    }
}