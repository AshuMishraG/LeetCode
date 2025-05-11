impl Solution {
    pub fn sum_of_multiples(n: i32) -> i32 {
        fn sum_d(n: i32, d: i32) -> i32 {
            let m = n / d;
            d * m * (m + 1) / 2
        }

        let s3  = sum_d(n,  3);
        let s5  = sum_d(n,  5);
        let s7  = sum_d(n,  7);
        let s15 = sum_d(n, 15);
        let s21 = sum_d(n, 21);
        let s35 = sum_d(n, 35);
        let s105= sum_d(n,105);

        s3 + s5 + s7 - s15 - s21 - s35 + s105
    }
}