/*
91. Decode Ways
Medium

A message containing letters from A-Z is being encoded to numbers using the following mapping:

'A' -> 1
'B' -> 2
...
'Z' -> 26

Given a non-empty string containing only digits, determine the total number of ways to decode it.

The answer is guaranteed to fit in a 32-bit integer.

 

Example 1:

Input: s = "12"
Output: 2
Explanation: It could be decoded as "AB" (1 2) or "L" (12).

Example 2:

Input: s = "226"
Output: 3
Explanation: It could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).

Example 3:

Input: s = "0"
Output: 0
Explanation: There is no character that is mapped to a number starting with '0'. We cannot ignore a zero when we face it while decoding. So, each '0' should be part of "10" --> 'J' or "20" --> 'T'.

Example 4:

Input: s = "1"
Output: 1
*/
impl Solution {
    pub fn num_decodings(s: String) -> i32 {
        let mut dp = vec![0; s.len() + 1];
        dp[0] = 1;
        if s.chars().nth(0).unwrap() != '0' {
            dp[1] = 1;
        }
        for i in 2..=s.len() {
            let d1 = s[i-1..i].parse::<i32>().unwrap();
            if d1 > 0 && d1 < 10 {
                dp[i] += dp[i-1];
            }
            let d2 = s[i-2..i].parse::<i32>().unwrap();
            if d2 >= 10 && d2 <= 26 {
                dp[i] += dp[i-2];
            }
        }
        dp[s.len()]
    }
}
