impl Solution {
    pub fn maximum69_number(num: i32) -> i32 {
        let mut chars: Vec<char> = num.to_string().chars().collect();
        for c in chars.iter_mut() {
            if *c == '6' {
                *c = '9';
                break;
            }
        }
        chars.into_iter().collect::<String>().parse().unwrap()
    }
}
