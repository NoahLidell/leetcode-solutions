/*
179. Largest Number
Medium

Given a list of non negative integers, arrange them such that they form the largest number.

Example 1:

Input: [10,2]
Output: "210"

Example 2:

Input: [3,30,34,5,9]
Output: "9534330"

Note: The result may be very large, so you need to return a string instead of an integer.
*/
use std::cmp::{max, min, Ordering};
impl Solution {
    fn compare_digits(x: &i32, y: &i32) -> Ordering {
        let ab = format!("{}{}", x, y);
        let ba = format!("{}{}", y, x);
        if ab > ba {
            Ordering::Greater
        } else if ba > ab {
            Ordering::Less
        } else {
            Ordering::Equal
        }
    }
    pub fn largest_number(mut nums: Vec<i32>) -> String {
        if nums.iter().fold(0, |acc, x| acc + x) == 0 {
            return String::from("0");
        }
        nums.sort_unstable_by(|a, b| Solution::compare_digits(a, b));
        nums.into_iter()
            .rev()
            .map(|x| x.to_string())
            .collect::<String>()
    }
}
