/*
394. Decode String
Medium

Given an encoded string, return its decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; No extra white spaces, square brackets are well-formed, etc.

Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there won't be input like 3a or 2[4].

 

Example 1:

Input: s = "3[a]2[bc]"
Output: "aaabcbc"

Example 2:

Input: s = "3[a2[c]]"
Output: "accaccacc"

Example 3:

Input: s = "2[abc]3[cd]ef"
Output: "abcabccdcdcdef"

Example 4:

Input: s = "abc3[cd]xyz"
Output: "abccdcdcdxyz"

 

Constraints:

    1 <= s.length <= 30
    s consists of lowercase English letters, digits, and square brackets '[]'.
    s is guaranteed to be a valid input.
    All the integers in s are in the range [1, 300].

*/

use std::collections::HashSet;
impl Solution {
    pub fn decode_string(s: String) -> String {
        let mut string: Vec<char> = vec![
            "1".chars().next().unwrap(), 
            "[".chars().next().unwrap()
        ];
        string.extend(s.chars().collect::<Vec<char>>());
        string.push("]".chars().next().unwrap());
        let nums = String::from("1234567890").chars().collect::<HashSet<char>>();
        fn decode(string: &Vec<char>, digits: &HashSet<char>, idx: usize) -> (Vec<char>, usize) {
            let close = "]".chars().next().unwrap();
            let mut output = vec![];
            let mut buffer = vec![];
            let mut i = idx;
            let mut n = String::new();
            while digits.contains(&string[i]) {
                n.push(string[i]);
                i += 1
            }
            let k = n.parse::<i32>().unwrap();
            i += 1; // skip "["
            loop {
                if digits.contains(&string[i]) {
                    let (parsed, new_i) = decode(string, digits, i);
                    buffer.extend(parsed);
                    i = new_i+1;
                } else if string[i] == close {
                    break
                } else {
                    buffer.push(string[i]);
                    i += 1;
                }
            }
            for _ in 0..k {
                output.extend(buffer.clone());
            }
            (output, i)
        }
        let (out, _) = decode(&string, &nums, 0);
        out.into_iter().collect()
    }
}
