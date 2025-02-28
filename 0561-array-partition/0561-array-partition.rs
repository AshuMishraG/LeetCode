impl Solution {
    pub fn array_pair_sum(mut nums: Vec<i32>) -> i32 {
        let offset = 10000;
        let range = 20001;  
        let mut count = vec![0; range];

        for num in nums.iter() {
            count[(num + offset) as usize] += 1;
        }

        let mut sum = 0;
        let mut add = true; 
        
        for (i, &freq) in count.iter().enumerate() {
            let value = i as i32 - offset; 
            for _ in 0..freq {
                if add {
                    sum += value;
                }
                add = !add;
            }
        }
        sum
    }
}