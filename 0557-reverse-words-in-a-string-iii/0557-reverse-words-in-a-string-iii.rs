impl Solution {
    pub fn reverse_words(s: String) -> String {
        let mut bytes = s.into_bytes();
        let n = bytes.len();
        let mut i = 0;
        while i < n {
            if bytes[i] == b' ' {
                i += 1;
            } else {
                let start = i;
                while i < n && bytes[i] != b' ' {
                    i += 1;
                }
                bytes[start..i].reverse();
            }
        }
        String::from_utf8(bytes).unwrap()
    }
}
