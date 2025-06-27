impl Solution {
    pub fn longest_subsequence_repeated_k(s: String, k: i32) -> String {
        let k = k as usize;
        let s_chars: Vec<char> = s.chars().collect();
        let mut freq = [0; 26];
        for &c in &s_chars {
            freq[(c as u8 - b'a') as usize] += 1;
        }

        let hot: Vec<char> = (0..26)
            .filter_map(|i| if freq[i] >= k { Some((b'a' + i as u8) as char) } else { None })
            .collect();

        let mut queue = std::collections::VecDeque::new();
        queue.push_back(String::new());

        let mut answer = String::new();
        while let Some(curr) = queue.pop_front() {
            if curr.len() * k > s_chars.len() {
                break;
            }
            for &ch in &hot {
                let next = format!("{}{}", curr, ch);
                if Self::is_k_subsequence(&s_chars, &next, k) {
                    answer = next.clone();
                    queue.push_back(next);
                }
            }
        }

        answer
    }

    fn is_k_subsequence(s: &[char], sub: &str, k: usize) -> bool {
        let sub_chars: Vec<char> = sub.chars().collect();
        let m = sub_chars.len();
        if m == 0 { return true; }

        let mut count = 0;
        let mut idx = 0;
        for &c in s {
            if c == sub_chars[idx] {
                idx += 1;
                if idx == m {
                    count += 1;
                    if count == k { return true; }
                    idx = 0;
                }
            }
        }
        false
    }
}