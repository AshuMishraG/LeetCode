impl Solution {
    pub fn max_profit(prices: Vec<i32>) -> i32 {
        let mut min_price = i32::MAX;
        let mut max_profit = 0;
        for &p in &prices {
            if p < min_price {
                min_price = p;
            } else if p - min_price > max_profit {
                max_profit = p - min_price;
            }
        }
        max_profit
    }
}