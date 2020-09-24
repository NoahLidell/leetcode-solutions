/*
389. Find the Difference
Easy

Given two strings s and t which consist of only lowercase letters.

String t is generated by random shuffling string s and then add one more letter at a random position.

Find the letter that was added in t.

Example:

Input:
s = "abcd"
t = "abcde"

Output:
e

Explanation:
'e' is the letter that was added.
*/
use std::char::from_u32;
impl Solution {
    pub fn find_the_difference(s: String, t: String) -> char {
        from_u32(s.chars().chain(t.chars()).fold(0u32, |c, x| c ^ x as u32)).unwrap()
    }
}
