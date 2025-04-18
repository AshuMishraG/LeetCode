impl Solution {
    pub fn get_row(row_index: i32) -> Vec<i32> {
        let k = row_index as usize;
        let mut row = vec![1; k + 1];             
        for i in 2..=k {                          
            for j in (1..i).rev() {            
                row[j] = row[j - 1] + row[j];     
            }
        }
        row
    }
}
