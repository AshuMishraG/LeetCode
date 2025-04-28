// Definition for singly-linked list.
// #[derive(PartialEq, Eq)]
// pub struct ListNode {
//     pub val: i32,
//     pub next: Option<Box<ListNode>>,
// }
// impl ListNode {
//     #[inline]
//     pub fn new(val: i32) -> Self {
//         ListNode { next: None, val }
//     }
// }

impl Solution {
    pub fn get_decimal_value(head: Option<Box<ListNode>>) -> i32 {
        let mut ans = 0;
        let mut node = head.as_ref();
        while let Some(n) = node {
            ans = (ans << 1) | n.val;
            node = n.next.as_ref();
        }
        ans
    }
}