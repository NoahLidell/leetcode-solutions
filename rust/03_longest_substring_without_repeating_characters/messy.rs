use std::collections::HashMap;

impl Solution {
    pub fn length_of_longest_substring(s: String) -> i32 {
        let mut track: HashMap<char, i32> = HashMap::new();
        let mut i = -1i32;
        let mut result = 0i32;
        
        if s.len() == 0 {
            return result
        }
        
        for (idx, c) in s.chars().enumerate() {
            let j: i32 = idx as i32;
            if let Some(seen) = track.get(&c) {
                if seen > &i {
                    i = *seen; 
                }
            }
            track.insert(c, j);
            let chk = j - i;
            if chk > result {
                result = chk;
            }
        }
        result
    }
}
