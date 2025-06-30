impl Solution {
    pub fn num_subseq(mut nums: Vec<i32>, target: i32) -> i32 {
        const MOD: i32 = 1_000_000_007;  
        nums.sort_unstable();
        let n = nums.len();  

        let mut pow2 = vec![1; n];
        for i in 1..n {
            pow2[i] = (pow2[i - 1] * 2) % MOD;
        }

        let (mut l, mut r) = (0, n - 1);
        let mut ans = 0;
        while l <= r {
            if nums[l] + nums[r] <= target {
                ans = (ans + pow2[r - l]) % MOD;
                l += 1;
            } else {
                if r == 0 { break; } 
                r -= 1;
            }
        }
        ans
    }
}
