impl Solution {
    pub fn replace_digits(s: String) -> String {
        let mut chars: Vec<char> = s.chars().collect();
        for i in (1..chars.len()).step_by(2) {
            if let Some(digit) = chars[i].to_digit(10) {
                chars[i] = ((chars[i - 1] as u8) + (digit as u8)) as char;
            }
        }
        chars.iter().collect()
    }
}