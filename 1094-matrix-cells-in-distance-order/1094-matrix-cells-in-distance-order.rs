impl Solution {
    pub fn all_cells_dist_order(rows: i32, cols: i32, r_center: i32, c_center: i32) -> Vec<Vec<i32>> {
        let mut cells = Vec::with_capacity((rows * cols) as usize);
        for r in 0..rows {
            for c in 0..cols {
                cells.push(vec![r, c]);
            }
        }
        cells.sort_unstable_by_key(|v| (v[0] - r_center).abs() + (v[1] - c_center).abs());
        cells
    }
}