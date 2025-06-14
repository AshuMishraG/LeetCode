impl Solution {
    pub fn min_max_difference(mut num: i32) -> i32 {
        let s = num.to_string();
        
        let mut max_s = s.clone().into_bytes();
        if let Some(&b) = max_s.iter().find(|&&b| b != b'9') {
            for c in &mut max_s {
                if *c == b { *c = b'9'; }
            }
        }
        
        let mut min_s = s.into_bytes();
        if let Some(&b) = min_s.iter().find(|&&b| b != b'0') {
            for c in &mut min_s {
                if *c == b { *c = b'0'; }
            }
        }
        
        let max_val = String::from_utf8(max_s).unwrap().parse::<i32>().unwrap();
        let min_val = String::from_utf8(min_s).unwrap().parse::<i32>().unwrap();
        max_val - min_val
    }
}
