impl Solution {
    pub fn max_distance(s: String, k: i32) -> i32 {
        let s = s.as_bytes();
        let k = k as i32;
        let mut ans = 0;
        for &(c1, c2) in &[ (b'N', b'E'), (b'N', b'W'), (b'S', b'E'), (b'S', b'W') ] {
            let mut curr = 0;
            let mut rem = k;
            for &c in s {
                if c == c1 || c == c2 {
                    if rem > 0 {
                        rem -= 1;
                        curr += 1;
                    } else {
                        curr -= 1;
                    }
                } else {
                    curr += 1;
                }
                ans = ans.max(curr);
            }
        }
        ans
    }
}