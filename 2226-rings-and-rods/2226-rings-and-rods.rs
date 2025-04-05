impl Solution {
    pub fn count_points(rings: String) -> i32 {
        let mut rods = [0u8; 10];
        let bytes = rings.as_bytes();
        for i in (0..rings.len()).step_by(2) {
            let color = bytes[i] as char;
            let rod = (bytes[i + 1] - b'0') as usize;
            let mask = match color {
                'R' => 1,
                'G' => 2,
                'B' => 4,
                _   => 0,
            };
            rods[rod] |= mask;
        }
        rods.iter().filter(|&&m| m == 7).count() as i32
    }
}