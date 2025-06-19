impl Solution {
    pub fn partition_array(nums: Vec<i32>, k: i32) -> i32 {
        let mut a = nums;
        a.sort_unstable();
        let mut count = 1;
        let mut start = a[0];
        for &x in &a[1..] {
            if x - start > k {
                count += 1;
                start = x;
            }
        }
        count
    }
}