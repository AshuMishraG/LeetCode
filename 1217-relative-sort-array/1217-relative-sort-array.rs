impl Solution {
    pub fn relative_sort_array(arr1: Vec<i32>, arr2: Vec<i32>) -> Vec<i32> {
        let mut count = vec![0; 1001];
        for &x in &arr1 {
            count[x as usize] += 1;
        }
        let mut ans = Vec::with_capacity(arr1.len());
        for &x in &arr2 {
            while count[x as usize] > 0 {
                ans.push(x);
                count[x as usize] -= 1;
            }
        }
        for num in 0..=1000 {
            while count[num] > 0 {
                ans.push(num as i32);
                count[num] -= 1;
            }
        }
        ans
    }
}