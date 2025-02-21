impl Solution {
    pub fn height_checker(heights: Vec<i32>) -> i32 {
        let mut count = [0; 101];
        for &height in &heights {
            count[height as usize] += 1;
        }
        
        let mut result = 0;
        let mut index = 0;
        
        for height in 1..=100 {
            while count[height] > 0 {
                if heights[index] != height as i32 {
                    result += 1;
                }
                index += 1;
                count[height] -= 1;
            }
        }
        result
    }
}
