impl Solution {
    pub fn max_product_difference(nums: Vec<i32>) -> i32 {
        let (mut max1, mut max2) = (i32::MIN, i32::MIN);
        let (mut min1, mut min2) = (i32::MAX, i32::MAX);
        for &x in &nums {
            if x > max1 {
                max2 = max1;
                max1 = x;
            } else if x > max2 {
                max2 = x;
            }
            if x < min1 {
                min2 = min1;
                min1 = x;
            } else if x < min2 {
                min2 = x;
            }
        }
        max1 * max2 - min1 * min2
    }
}