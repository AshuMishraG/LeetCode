impl Solution {
    pub fn subtract_product_and_sum(n: i32) -> i32 {
        let (mut prod, mut sum, mut x) = (1, 0, n);
        while x > 0 {
            let d = x % 10;
            prod *= d;
            sum += d;
            x /= 10;
        }
        prod - sum
    }
}