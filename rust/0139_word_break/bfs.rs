/*
139. Word Break
Medium

Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, determine if s can be segmented into a space-separated sequence of one or more dictionary words.

Note:

    The same word in the dictionary may be reused multiple times in the segmentation.
    You may assume the dictionary does not contain duplicate words.

Example 1:

Input: s = "leetcode", wordDict = ["leet", "code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".

Example 2:

Input: s = "applepenapple", wordDict = ["apple", "pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
             Note that you are allowed to reuse a dictionary word.

Example 3:

Input: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
Output: false


https://leetcode.com/problems/word-break/submissions/
*/
use std::collections::{HashSet, VecDeque};
impl Solution {
    pub fn word_break(s: String, word_dict: Vec<String>) -> bool {
        let mut queue: VecDeque<usize> = VecDeque::new();
        let mut visited: HashSet<usize> = HashSet::new();
        let words = word_dict.into_iter().collect::<HashSet<String>>();
        queue.push_back(0);
        visited.insert(0);
        while queue.len() > 0 {
            let a = queue.pop_front().unwrap();

            for b in a + 1..s.len() + 1 {
                if visited.contains(&b) {
                    continue;
                }
                let maybe = String::from(&s[a..b]);
                if words.contains(&maybe) {
                    if b == s.len() {
                        return true;
                    }
                    queue.push_back(b);
                    visited.insert(b);
                }
            }
        }
        false
    }
}
