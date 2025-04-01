impl Solution {
    pub fn final_value_after_operations(operations: Vec<String>) -> i32 {
        operations.iter().fold(0, |acc, op| {
            acc + if op.chars().nth(1).unwrap() == '+' { 1 } else { -1 }
        })
    }
}