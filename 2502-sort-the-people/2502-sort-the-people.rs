impl Solution {
    pub fn sort_people(names: Vec<String>, heights: Vec<i32>) -> Vec<String> {
        let mut people: Vec<(i32, String)> = heights.into_iter().zip(names).collect();
        people.sort_by(|a, b| b.0.cmp(&a.0));
        people.into_iter().map(|(h, name)| name).collect()
    }
}
