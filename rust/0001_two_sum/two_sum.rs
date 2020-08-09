use std::collections::HashMap;

impl Solution {
    pub fn two_sum(nums: Vec<i32>, target: i32) -> Vec<i32> {
        let mut numset : HashMap<i32, i32> = HashMap::new();
        let mut soln: Vec<i32> = vec!();
        for (i, n) in nums.iter().enumerate() {
            let m = target - n;
            let idx = i as i32;
            if numset.contains_key(&m) {
                soln.extend(vec!(idx, *numset.get(&m).unwrap()));
            } else {
                numset.insert(*n, idx);
            }
        }
        soln
    }
}
