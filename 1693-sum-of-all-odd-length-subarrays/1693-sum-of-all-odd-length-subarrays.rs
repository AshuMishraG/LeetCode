impl Solution {
    pub fn sum_odd_length_subarrays(arr: Vec<i32>) -> i32 {
        let n = arr.len();
        arr.into_iter().enumerate()
            .map(|(i, num)| {
                let total = (i + 1) * (n - i);
                let odd = (total + 1) / 2;
                num * odd as i32
            })
            .sum()
    }
}
