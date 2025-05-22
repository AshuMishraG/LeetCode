impl Solution {
    pub fn count_prime_set_bits(left: i32, right: i32) -> i32 {
        fn is_prime(n: u32) -> bool {
            matches!(n, 2 | 3 | 5 | 7 | 11 | 13 | 17 | 19)
        }

        (left..=right)
            .filter(|&n| is_prime(n.count_ones()))
            .count() as i32
    }
}