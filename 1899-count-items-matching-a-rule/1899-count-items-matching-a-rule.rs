impl Solution {
    pub fn count_matches(items: Vec<Vec<String>>, rule_key: String, rule_value: String) -> i32 {
        let index = match rule_key.as_str() {
            "type" => 0,
            "color" => 1,
            "name" => 2,
            _ => unreachable!(),
        };
        let rule_value = rule_value.as_str();
        let mut count = 0;
        for item in items.iter() {
            if item[index].as_str() == rule_value {
                count += 1;
            }
        }
        count
    }
}