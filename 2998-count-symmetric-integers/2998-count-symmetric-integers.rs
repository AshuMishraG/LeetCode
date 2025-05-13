impl Solution {
    pub fn count_symmetric_integers(low: i32, high: i32) -> i32 {
        let mut count = 0;
        for x in low..=high {
            if x < 10 {
                continue;
            } else if x < 100 {
                let a = x / 10;
                let b = x % 10;
                if a == b {
                    count += 1;
                }
            } else if x < 1000 {
                continue;
            } else {
                let a = x / 1000;
                let b = (x / 100) % 10;
                let c = (x / 10) % 10;
                let d = x % 10;
                if a + b == c + d {
                    count += 1;
                }
            }
        }
        count
    }
}