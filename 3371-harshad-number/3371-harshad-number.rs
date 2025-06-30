impl Solution {
    pub fn sum_of_digits(num: i32) -> i32 {
        let mut n = num;
        let mut s = 0;
        while n > 0 {
            s += n % 10;
            n /= 10;
        }
        s
    }

    pub fn sum_of_the_digits_of_harshad_number(x: i32) -> i32 {
        let s = Self::sum_of_digits(x);
        if x % s == 0 { s } else { -1 }
    }
}
