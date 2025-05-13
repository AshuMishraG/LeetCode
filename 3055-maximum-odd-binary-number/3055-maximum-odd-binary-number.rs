impl Solution {
    pub fn maximum_odd_binary_number(s: String) -> String {
        let ones = s.chars().filter(|&c| c == '1').count();
        let zeros = s.len() - ones;
        let mut result = String::with_capacity(s.len());
        for _ in 0..ones-1 {
            result.push('1');
        }
        for _ in 0..zeros {
            result.push('0');
        }
        result.push('1');
        result
    }
}