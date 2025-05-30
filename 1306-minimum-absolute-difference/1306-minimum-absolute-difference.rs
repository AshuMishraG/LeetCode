impl Solution {
    pub fn minimum_abs_difference(arr: Vec<i32>) -> Vec<Vec<i32>> {
        let (mut mn, mut mx) = (i32::MAX, i32::MIN);
        for &v in &arr {
            if v < mn { mn = v; }
            if v > mx { mx = v; }
        }
        let offset = mn;
        let size = (mx - mn + 1) as usize;
        let mut count = vec![0u32; size];
        for &v in &arr {
            count[(v - offset) as usize] += 1;
        }
        let mut prev: Option<i32> = None;
        let mut min_diff = i32::MAX;
        let mut result = Vec::new();
        for i in 0..size {
            if count[i] > 0 {
                let val = i as i32 + offset;
                if let Some(p) = prev {
                    let diff = val - p;
                    if diff < min_diff {
                        min_diff = diff;
                        result.clear();
                        result.push(vec![p, val]);
                    } else if diff == min_diff {
                        result.push(vec![p, val]);
                    }
                }
                prev = Some(val);
            }
        }
        result
    }
}