/*
395. Longest Substring with At Least K Repeating Characters
Medium

Given a string s and an integer k, return the length of the longest substring of s such that the frequency of each character in this substring is greater than or equal to k.



Example 1:

Input: s = "aaabb", k = 3
Output: 3
Explanation: The longest substring is "aaa", as 'a' is repeated 3 times.

Example 2:

Input: s = "ababbc", k = 2
Output: 5
Explanation: The longest substring is "ababb", as 'a' is repeated 2 times and 'b' is repeated 3 times.



Constraints:

    1 <= s.length <= 104
    s consists of only lowercase English letters.
    1 <= k <= 105

*/
use std::cmp::max;
use std::collections::HashMap;

impl Solution {
    pub fn longest_substring(s: String, k: i32) -> i32 {
        let s = s.into_bytes();
        fn longestsubs(s: &Vec<u8>, a: usize, b: usize, k: i32) -> i32 {
            if (b as i32) < k {
                return 0;
            }
            let mut counter: HashMap<u8, i32> = HashMap::new();
            for c in a..b {
                let count = counter.entry(s[c]).or_insert(0);
                *count += 1;
            }
            for mid in a..b {
                if counter.get(&s[mid]).unwrap() >= &k {
                    continue;
                }
                let mut midNext = mid + 1;
                while midNext < b && counter.get(&s[midNext]).unwrap() < &k {
                    midNext += 1;
                }
                return max(longestsubs(s, a, mid, k), longestsubs(s, midNext, b, k));
            }
            (b - a) as i32
        }
        longestsubs(&s, 0, s.len(), k)
    }
}
