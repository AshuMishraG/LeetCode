impl Solution {
    pub fn divide_string(s: String, k: i32, fill: char) -> Vec<String> {
        let k = k as usize;
        let mut res = Vec::new();
        let bytes = s.as_bytes();
        let n = bytes.len();
        let mut i = 0;
        while i < n {
            let end = usize::min(i + k, n);
            let mut group = bytes[i..end]
                .iter()
                .map(|&b| b as char)
                .collect::<String>();
            if end - i < k {
                group.extend(std::iter::repeat(fill).take(k - (end - i)));
            }
            res.push(group);
            i += k;
        }
        res
    }
}