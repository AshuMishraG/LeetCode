impl Solution {
    pub fn minimize_max(nums: Vec<i32>, p: i32) -> i32 {
        let mut a = nums;
        a.sort_unstable();
        let n = a.len();
        let mut left = 0;
        let mut right = a[n - 1] - a[0];
        let p = p as usize;

        while left < right {
            let mid = left + (right - left) / 2;
            let mut cnt = 0;
            let mut i = 1;
            while i < n {
                if a[i] - a[i - 1] <= mid {
                    cnt += 1;
                    i += 2;
                } else {
                    i += 1;
                }
            }
            if cnt >= p {
                right = mid;
            } else {
                left = mid + 1;
            }
        }
        left
    }
}