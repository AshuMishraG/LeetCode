use std::collections::HashMap;

impl Solution {
    const MOD: i64 = 1_000_000_007;
    const MAXN: usize = 100_000;

    fn mod_exp(mut base: i64, mut exp: i64, mod_: i64) -> i64 {
        let mut result = 1;
        while exp > 0 {
            if exp & 1 == 1 {
                result = (result * base) % mod_;
            }
            base = (base * base) % mod_;
            exp >>= 1;
        }
        result
    }

    fn ncr(n: usize, r: usize, fact: &Vec<i64>, inv_fact: &Vec<i64>) -> i64 {
        if r > n {
            return 0;
        }
        (fact[n] * inv_fact[r] % Solution::MOD * inv_fact[n - r] % Solution::MOD) % Solution::MOD
    }

    pub fn count_good_arrays(n: i32, m: i32, k: i32) -> i32 {
        if n == 1 {
            return if k == 0 { m as i32 } else { 0 };
        }

        let n = n as usize;
        let k = k as usize;
        let m = m as i64;

        let mut fact = vec![1; Solution::MAXN + 1];
        let mut inv_fact = vec![1; Solution::MAXN + 1];

        for i in 1..=Solution::MAXN {
            fact[i] = (fact[i - 1] * i as i64) % Solution::MOD;
        }

        inv_fact[Solution::MAXN] = Solution::mod_exp(fact[Solution::MAXN], Solution::MOD - 2, Solution::MOD);

        for i in (0..Solution::MAXN).rev() {
            inv_fact[i] = (inv_fact[i + 1] * (i + 1) as i64) % Solution::MOD;
        }

        let choose = Solution::ncr(n - 1, k, &fact, &inv_fact);
        let ways = (choose * m) % Solution::MOD;
        let ways = (ways * Solution::mod_exp(m - 1, (n - k - 1) as i64, Solution::MOD)) % Solution::MOD;

        ways as i32
    }
}