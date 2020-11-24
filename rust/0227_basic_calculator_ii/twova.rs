/* 
227. Basic Calculator II
Medium

Implement a basic calculator to evaluate a simple expression string.

The expression string contains only non-negative integers, +, -, *, / operators and empty spaces . The integer division should truncate toward zero.

Example 1:

Input: "3+2*2"
Output: 7

Example 2:

Input: " 3/2 "
Output: 1

Example 3:

Input: " 3+5 / 2 "
Output: 5

Note:

    You may assume that the given expression is always valid.
    Do not use the eval built-in library function.
*/
impl Solution {
    pub fn calculate(s: String) -> i32 {
        let mut prev = 0;
        let plus = String::from("+").chars().next().unwrap();
        let minus = String::from("-").chars().next().unwrap();
        let mult = String::from("*").chars().next().unwrap();
        let div = String::from("/").chars().next().unwrap();
        let space = String::from(" ").chars().next().unwrap();
        let mut op: char = plus;
        let mut curr = 0i32;
        let mut prev = 0i32;
        let mut result = 0i32;
        
        for c in s.chars().chain(String::from("+").chars()) {
            if c.is_digit(10) {
                curr = curr*10+(c.to_digit(10).unwrap() as i32);
                
            } else if c == space {
                continue
            } else {
                if op == plus {
                    result += prev;
                    prev = curr;
                } else if op == minus {
                    result += prev;
                    prev = -1*curr;
                } else if op == mult {
                    prev *= curr;
                } else if op == div {
                    prev /= curr
                }
                curr = 0;
                op = c;
            }
        }
        result + prev
    }
}
