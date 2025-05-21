impl Solution {
    pub fn self_dividing_numbers(left: i32, right: i32) -> Vec<i32> {
        fn is_self_dividing(mut num: i32) -> bool {
            let original = num;
            while num > 0 {
                let digit = num % 10;
                if digit == 0 || original % digit != 0 {
                    return false;
                }
                num /= 10;
            }
            true
        }

        (left..=right).filter(|&x| is_self_dividing(x)).collect()
    }
}