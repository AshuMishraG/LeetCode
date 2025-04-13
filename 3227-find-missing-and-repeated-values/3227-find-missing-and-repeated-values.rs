impl Solution {
    pub fn find_missing_and_repeated_values(grid: Vec<Vec<i32>>) -> Vec<i32> {
        let n = grid.len() as i64;
        let total = n * n;
        let expected_sum = total * (total + 1) / 2;
        let expected_sum_sq = total * (total + 1) * (2 * total + 1) / 6;
        
        let mut actual_sum: i64 = 0;
        let mut actual_sum_sq: i64 = 0;
        for row in grid.iter() {
            for &num in row.iter() {
                let x = num as i64;
                actual_sum += x;
                actual_sum_sq += x * x;
            }
        }
        
        let diff = actual_sum - expected_sum;        
        let sum_ab = (actual_sum_sq - expected_sum_sq) / diff; 
        
        let a = (diff + sum_ab) / 2; 
        let b = (sum_ab - diff) / 2;
        
        vec![a as i32, b as i32]
    }
}
