impl Solution {
    pub fn find_permutation_difference(s: String, t: String) -> i32 {
        let mut pos_t = [0; 26];
        for (i, &c) in t.as_bytes().iter().enumerate() {
            pos_t[(c - b'a') as usize] = i as i32;
        }
        
        let mut result = 0;
        for (i, &c) in s.as_bytes().iter().enumerate() {
            let pos_in_t = pos_t[(c - b'a') as usize];
            result += (i as i32 - pos_in_t).abs();
        }
        result
    }
}
