/*
763. Partition Labels
Medium

A string S of lowercase English letters is given. We want to partition this string into as many parts as possible so that each letter appears in at most one part, and return a list of integers representing the size of these parts.

 

Example 1:

Input: S = "ababcbacadefegdehijhklij"
Output: [9,7,8]
Explanation:
The partition is "ababcbaca", "defegde", "hijhklij".
This is a partition so that each letter appears in at most one part.
A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits S into less parts.

 

Note:

    S will have length in range [1, 500].
    S will consist of lowercase English letters ('a' to 'z') only.
*/
use std::collections::HashMap;
use std::cmp;
impl Solution {
    pub fn partition_labels(s: String) -> Vec<i32> {
        let mut last = HashMap::new();
        for i in 0..s.len() {
            last.insert(&s[i..i+1], i);
        }
        let mut partitions = vec![];
        let mut j = 0;
        let mut anchor = 0;
        for i in 0..s.len() {
            let c = &s[i..i+1];
            j = cmp::max(j, *last.get(c).unwrap());
            if i == j {
                let p = (j-anchor+1) as i32;
                partitions.push(p);
                anchor = j+1;
            }
            
        }
        partitions
    }
}
