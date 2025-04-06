impl Solution {
    pub fn find_difference(nums1: Vec<i32>, nums2: Vec<i32>) -> Vec<Vec<i32>> {
        const OFFSET: i32 = 1000;
        const SIZE: usize = 2001;

        let mut present1 = [false; SIZE];
        let mut present2 = [false; SIZE];
        
        for num in nums1 {
            present1[(num + OFFSET) as usize] = true;
        }
        for num in nums2 {
            present2[(num + OFFSET) as usize] = true;
        }
        
        let mut diff1 = Vec::new();
        let mut diff2 = Vec::new();
        for i in 0..SIZE {
            if present1[i] && !present2[i] {
                diff1.push(i as i32 - OFFSET);
            }
            if present2[i] && !present1[i] {
                diff2.push(i as i32 - OFFSET);
            }
        }
        
        vec![diff1, diff2]
    }
}