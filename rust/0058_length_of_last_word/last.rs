/*
58. Length of Last Word
Easy

Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word (last word means the last appearing word if we loop from left to right) in the string.

If the last word does not exist, return 0.

Note: A word is defined as a maximal substring consisting of non-space characters only.

Example:

Input: "Hello World"
Output: 5
*/
impl Solution {
    pub fn length_of_last_word(s: String) -> i32 {
        let mut len_word = 0;
        let mut reset = false;
        for c in s.chars() {
            match c {
                ' ' => {
                    reset = true;
                }
                _ => {
                    if reset == true {
                        len_word = 0;
                        reset = false;
                    }
                    len_word += 1;
                }
            }
        }
        len_word
    }
}
