use std::collections::*;

impl Solution {
    pub fn find_difference(nums1: Vec<i32>, nums2: Vec<i32>) -> Vec<Vec<i32>> {
        let unique_nums1: HashSet<i32> = nums1.into_iter().collect();
        let unique_nums2: HashSet<i32> = nums2.into_iter().collect();
        Vec::from([
            unique_nums1.difference(&unique_nums2).copied().collect::<Vec<i32>>(),
            unique_nums2.difference(&unique_nums1).copied().collect::<Vec<i32>>(),
        ])
    }
}