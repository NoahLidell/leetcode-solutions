use std::collections::HashMap;
fn is_valid(s: String) -> bool {
    let mut stack: Vec<char> = vec![];
	let parens: HashMap<char, char> = "([{".chars().zip(")]}".chars()).collect();
    for c in s.chars() {
        if parens.contains_key(&c) {
            stack.push(c);
        } else {
            if let Some(top) = stack.pop() {
                // if c != *parens.get(&top).unwrap() { // <- this also compiles
                if &c != parens.get(&top).unwrap() {
                    return false
                }
            } else {
                return false
            }
        }
    }
    stack.is_empty()
}
