impl Solution {
    pub fn final_prices(mut prices: Vec<i32>) -> Vec<i32> {
        let mut stack: Vec<usize> = Vec::new();
        for i in 0..prices.len() {
            while let Some(&j) = stack.last() {
                if prices[j] >= prices[i] {
                    prices[j] -= prices[i];
                    stack.pop();
                } else {
                    break;
                }
            }
            stack.push(i);
        }
        prices
    }
}