impl Solution {
    pub fn generate(num_rows: i32) -> Vec<Vec<i32>> {
        let n = num_rows as usize;
        let mut triangle: Vec<Vec<i32>> = Vec::with_capacity(n);
        for i in 0..n {
            let mut row = vec![1; i + 1];
            for j in 1..i {
                let prev = &triangle[i - 1];
                row[j] = prev[j - 1] + prev[j];
            }
            triangle.push(row);
        }
        triangle
    }
}
