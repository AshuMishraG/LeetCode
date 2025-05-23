impl Solution {
    pub fn projection_area(grid: Vec<Vec<i32>>) -> i32 {
        let n = grid.len();
        let mut top = 0;
        let mut front = 0;
        let mut side = 0;
        
        for i in 0..n {
            for j in 0..n {
                if grid[i][j] > 0 {
                    top += 1;
                }
            }
        }
        
        for j in 0..n {
            let mut col_max = 0;
            for i in 0..n {
                col_max = col_max.max(grid[i][j]);
            }
            front += col_max;
        }
        
        for i in 0..n {
            let mut row_max = 0;
            for &v in &grid[i] {
                row_max = row_max.max(v);
            }
            side += row_max;
        }
        
        top + front + side
    }
}