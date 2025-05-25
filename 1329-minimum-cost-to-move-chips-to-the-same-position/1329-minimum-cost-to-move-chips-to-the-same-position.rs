impl Solution {
    pub fn min_cost_to_move_chips(position: Vec<i32>) -> i32 {
        let odd_count = position.iter().filter(|&&p| p % 2 != 0).count() as i32;
        let even_count = position.len() as i32 - odd_count;
        odd_count.min(even_count)
    }
}