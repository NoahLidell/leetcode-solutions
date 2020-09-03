/* Repeated Substring Pattern
 * Easy
 *
 * Given a non-empty string check if it can be constructed by taking a substring of it and appending multiple copies of the substring together. You may assume the given string consists of lowercase English letters only and its length will not exceed 10000.
 *
 *
 *
 * Example 1:
 *
 * Input: "abab"
 * Output: True
 * Explanation: It's the substring "ab" twice.
 *
 * Example 2:
 *
 * Input: "aba"
 * Output: False
 *
 * Example 3:
 *
 * Input: "abcabcabcabc"
 * Output: True
 * Explanation: It's the substring "abc" four times. (And the substring "abcabc" twice.)
 */
impl Solution {
    pub fn repeated_substring_pattern(s: String) -> bool {
        if s.len() == 1 {
            return false;
        }
        for d in 2..=s.len() {
            if s.len() % d == 0 {
                let size = s.len() / d;
                let mut chk = true;
                for w in 1..d {
                    let prev = (w - 1) * size;
                    let start = w * size;
                    let end = (w + 1) * size;
                    if &s[prev..start] != &s[start..end] {
                        chk = false;
                        break;
                    }
                }
                if chk == true {
                    return true;
                }
            }
        }
        false
    }
}
