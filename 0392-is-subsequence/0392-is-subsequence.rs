impl Solution {
    pub fn is_subsequence(s: String, t: String) -> bool {
        let (mut i, mut j) = (0, 0);
        let s_bytes = s.as_bytes();
        let t_bytes = t.as_bytes();
        while i < s_bytes.len() && j < t_bytes.len() {
            if s_bytes[i] == t_bytes[j] {
                i += 1;
            }
            j += 1;
        }
        i == s_bytes.len()
    }

    pub fn builder(t: String) -> Vec<Vec<usize>> {
        let mut next_pos = vec![Vec::new(); 26];
        for (idx, &b) in t.as_bytes().iter().enumerate() {
            next_pos[(b - b'a') as usize].push(idx);
        }
        next_pos
    }

    pub fn is_subsequence_with_map(
        s: String,
        next_pos: &Vec<Vec<usize>>,
    ) -> bool {
        use std::cmp::Ordering;
        let mut prev_idx = 0usize;
        for &b in s.as_bytes() {
            let vec = &next_pos[(b - b'a') as usize];
            match vec.binary_search(&prev_idx) {
                Ok(found) => prev_idx = found + 1,
                Err(insert) => {
                    if insert == vec.len() {
                        return false;
                    }
                    prev_idx = vec[insert] + 1;
                }
            }
        }
        true
    }
}