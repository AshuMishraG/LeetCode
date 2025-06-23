impl Solution {
    fn to_base_k(mut x: i64, k: i32) -> Vec<u8> {
        let mut d = Vec::new();
        while x > 0 {
            d.push((x % k as i64) as u8);
            x /= k as i64;
        }
        d
    }
    
    fn is_pal(d: &[u8]) -> bool {
        let n = d.len();
        for i in 0..n/2 {
            if d[i] != d[n-1-i] { return false; }
        }
        true
    }
    
    fn make_pal(mut half: i64, odd: bool) -> i64 {
        let mut x = half;
        if odd { half /= 10; }
        while half > 0 {
            x = x * 10 + (half % 10);
            half /= 10;
        }
        x
    }

    pub fn k_mirror(k: i32, n: i32) -> i64 {
        let mut found = 0;
        let mut sum = 0;
        for len in 1.. {
            let half_len = (len + 1) / 2;
            let start = 10_i64.pow(half_len as u32 - 1);
            let end = 10_i64.pow(half_len as u32);
            for half in start..end {
                for &odd in &[false, true] {
                    if odd && len % 2 == 0 { continue; }
                    if !odd && len % 2 == 1 { continue; }
                    let p = Self::make_pal(half, odd);
                    let bd = Self::to_base_k(p, k);
                    if Self::is_pal(&bd) {
                        sum += p;
                        found += 1;
                        if found == n {
                            return sum;
                        }
                    }
                }
            }
        }
        sum
    }
}