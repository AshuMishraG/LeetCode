impl Solution {
    pub fn max_diff(num: i32) -> i32 {
        let s = num.to_string();
        let chars: Vec<char> = s.chars().collect();

        let mut max_chars = chars.clone();
        if let Some(&c) = chars.iter().find(|&&c| c != '9') {
            for ch in &mut max_chars {
                if *ch == c {
                    *ch = '9';
                }
            }
        }
        let a = max_chars.iter().collect::<String>().parse::<i32>().unwrap();

        let mut min_chars = chars.clone();
        let first = chars[0];
        if first != '1' {
            for ch in &mut min_chars {
                if *ch == first {
                    *ch = '1';
                }
            }
        } else {
            if let Some(&c) = chars.iter().skip(1).find(|&&c| c != '0' && c != first) {
                for ch in &mut min_chars {
                    if *ch == c {
                        *ch = '0';
                    }
                }
            }
        }
        let b = min_chars.iter().collect::<String>().parse::<i32>().unwrap();

        a - b
    }
}