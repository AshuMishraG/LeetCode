impl Solution {
    pub fn find_kth_number(n: i32, k: i32) -> i32 {
        let mut k = k as i64 - 1;
        let mut curr = 1i64;
        let n = n as i64;
        
        while k > 0 {
            let mut steps = 0i64;
            let mut first = curr;
            let mut last = curr + 1;
            
            while first <= n {
                steps += (n.min(last - 1) - first + 1).max(0);
                first *= 10;
                last *= 10;
            }
            
            if steps <= k {
                curr += 1;
                k -= steps;
            } else {
                curr *= 10;
                k -= 1;
            }
        }
        
        curr as i32
    }
}