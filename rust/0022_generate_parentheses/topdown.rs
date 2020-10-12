/*
22. Generate Parentheses
Medium

Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.



Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]

Example 2:

Input: n = 1
Output: ["()"]



Constraints:

    1 <= n <= 8

https://leetcode.com/submissions/detail/406795598/
*/
impl Solution {
    pub fn generate_parenthesis(n: i32) -> Vec<String> {
        fn btrack(s: String, l: i32, r: i32, valid: &mut Vec<String>) {
            if l == 0 && r == 0 {
                valid.push(s);
                return;
            }
            if l == 0 {
                btrack(format!("{})", s), l, r - 1, valid);
            } else if l == r {
                btrack(format!("{}(", s), l - 1, r, valid);
            } else {
                btrack(format!("{}(", s), l - 1, r, valid);
                btrack(format!("{})", s), l, r - 1, valid);
            }
        }
        let mut valid: Vec<String> = vec![];
        btrack(String::from(""), n, n, &mut valid);
        valid
    }
}
