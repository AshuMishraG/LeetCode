impl Solution {
    pub fn odd_cells(m: i32, n: i32, indices: Vec<Vec<i32>>) -> i32 {
        let mut row = vec![0; m as usize];
        let mut col = vec![0; n as usize];
        
        for pair in indices {
            row[pair[0] as usize] += 1;
            col[pair[1] as usize] += 1;
        }
        
        let mut count = 0;
        for &r in &row {
            for &c in &col {
                if (r + c) % 2 != 0 {
                    count += 1;
                }
            }
        }
        count
    }
}