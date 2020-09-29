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
impl Solution {
    pub fn word_break(s: String, word_dict: Vec<String>) -> bool {
        let mut track = vec![0; s.len()];
        for i in 0i32..=(s.len() as i32) {
            for w in &word_dict {
                if (i - (w.len() as i32) >= 0
                    && &s[((i - w.len() as i32) as usize)..(i as usize)] == &w[0..w.len()]
                    && (i - (w.len() as i32) <= 0
                        || track[(i - (w.len() as i32) - 1) as usize] == 1))
                {
                    track[(i - 1) as usize] = 1
                }
            }
        }
        track.pop().unwrap() != 0
    }
}
