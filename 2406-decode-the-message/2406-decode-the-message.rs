impl Solution {
    pub fn decode_message(key: String, message: String) -> String {
        let mut mapping = [0u8; 26];
        let mut next = b'a';
        for b in key.bytes() {
            if b >= b'a' && b <= b'z' {
                let idx = (b - b'a') as usize;
                if mapping[idx] == 0 {
                    mapping[idx] = next;
                    next = next.saturating_add(1);
                    if next > b'z' {
                        break;
                    }
                }
            }
        }
        
        let mut res = Vec::with_capacity(message.len());
        for b in message.bytes() {
            if b == b' ' {
                res.push(b' ');
            } else {
                let idx = (b - b'a') as usize;
                res.push(mapping[idx]);
            }
        }
        
        String::from_utf8(res).unwrap()
    }
}
