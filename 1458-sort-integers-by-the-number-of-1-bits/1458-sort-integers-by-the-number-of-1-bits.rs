impl Solution {
    pub fn sort_by_bits(arr: Vec<i32>) -> Vec<i32> {
        let mut arr = arr;
        arr.sort_unstable_by_key(|&x| (x.count_ones(), x));
        arr
    }
}