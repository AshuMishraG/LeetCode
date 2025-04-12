impl Solution {
    pub fn find_intersection_values(nums1: Vec<i32>, nums2: Vec<i32>) -> Vec<i32> {
        let mut present1 = [false; 101];
        let mut present2 = [false; 101];
        
        for &num in &nums1 {
            present1[num as usize] = true;
        }
        for &num in &nums2 {
            present2[num as usize] = true;
        }
        
        let answer1 = nums1.iter().filter(|&&num| present2[num as usize]).count() as i32;
        let answer2 = nums2.iter().filter(|&&num| present1[num as usize]).count() as i32;
        
        vec![answer1, answer2]
    }
}
