impl Solution {
    pub fn shuffle(mut nums: Vec<i32>, n: i32) -> Vec<i32> {
        let n = n as usize;
        let base = 1001;
        for i in 0..(2 * n) {
            let new_val = if i % 2 == 0 {
                nums[i / 2] % base
            } else {
                nums[n + i / 2] % base
            };
            nums[i] += new_val * base;
        }
        for i in 0..(2 * n) {
            nums[i] /= base;
        }
        
        nums
    }
}