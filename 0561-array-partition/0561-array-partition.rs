impl Solution {
    pub fn array_pair_sum(nums: Vec<i32>) -> i32 {
        const OFFSET: usize = 10000;
        const SIZE: usize = 20001;
        
        let mut count = vec![0; SIZE];
        
        for num in nums {
            count[(num + OFFSET as i32) as usize] += 1;
        }
        
        let mut result = 0;
        let mut take = true;
        
        for i in 0..SIZE {
            while count[i] > 0 {
                if take {
                    result += i as i32 - OFFSET as i32;
                }
                take = !take;
                count[i] -= 1;
            }
        }
        
        result
    }
}
