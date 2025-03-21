impl Solution {
    pub fn freq_alphabets(s: String) -> String {
        let bytes = s.as_bytes();
        let mut i = s.len() as i32 - 1;
        let mut res = String::with_capacity(s.len());
        while i >= 0 {
            if bytes[i as usize] == b'#' {
                // Convert two digits before '#' to number
                let num = (bytes[(i - 2) as usize] - b'0') * 10 
                        + (bytes[(i - 1) as usize] - b'0');
                res.push((b'a' + num - 1) as char);
                i -= 3;
            } else {
                let num = bytes[i as usize] - b'0';
                res.push((b'a' + num - 1) as char);
                i -= 1;
            }
        }
        res.chars().rev().collect()
    }
}