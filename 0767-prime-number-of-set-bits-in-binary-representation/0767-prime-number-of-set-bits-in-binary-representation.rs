use std::collections::HashSet;

impl Solution {
    pub fn count_prime_set_bits(left: i32, right: i32) -> i32 {
        let primes: HashSet<i32> = [2, 3, 5, 7, 11, 13, 17, 19].iter().cloned().collect();

        (left..=right)
            .filter(|&x| primes.contains(&(x.count_ones() as i32)))
            .count() as i32
    }
}