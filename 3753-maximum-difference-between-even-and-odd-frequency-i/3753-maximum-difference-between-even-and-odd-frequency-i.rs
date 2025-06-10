impl Solution {
    pub fn max_difference(s: String) -> i32 {
        let mut freq = [0; 26];
        for b in s.bytes() {
            freq[(b - b'a') as usize] += 1;
        }
        let max_odd = freq.iter().filter(|&&c| c % 2 == 1).max().unwrap();
        let min_even = freq.iter().filter(|&&c| c % 2 == 0 && c > 0).min().unwrap();
        max_odd - min_even
    }
}