impl Solution {
    pub fn k_weakest_rows(mat: Vec<Vec<i32>>, k: i32) -> Vec<i32> {
        let mut strength: Vec<(usize, i32)> = mat.iter()
            .enumerate()
            .map(|(i, row)| (i, row.iter().take_while(|&&x| x == 1).count() as i32))
            .collect();
        strength.sort_unstable_by_key(|&(i, s)| (s, i));
        strength.iter().take(k as usize).map(|&(i, _)| i as i32).collect()
    }
}