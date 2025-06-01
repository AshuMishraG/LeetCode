impl Solution {
    pub fn find_the_distance_value(arr1: Vec<i32>, mut arr2: Vec<i32>, d: i32) -> i32 {
        arr2.sort_unstable();
        arr1.into_iter().filter(|&x| {
            arr2.binary_search_by(|&y| {
                if (y - x).abs() <= d {
                    std::cmp::Ordering::Equal
                } else if y < x {
                    std::cmp::Ordering::Less
                } else {
                    std::cmp::Ordering::Greater
                }
            }).is_err()
        }).count() as i32
    }
}