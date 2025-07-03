impl Solution {
    pub fn kth_character(k: i32) -> char {
        let cnt = (k as u32 - 1).count_ones();
        (b'a' + cnt as u8) as char
    }
}