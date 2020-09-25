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
std::cmp::{Ordering, max, min};
impl Solution {
    fn compare_digits(x: &i32, y: &i32 ) -> Ordering {
        if x == y {
            return Ordering::Equal
        }
        let mut a = x.to_string();
        let mut b = y.to_string();
        let lasta = a.chars().nth(0).unwrap();
        let lastb = b.chars().nth(0).unwrap();
        while a.len() < b.len() {
            a.push(lasta);
        }
        while b.len() < a.len() {
            b.push(lastb);
        }
        if a == b {
            if x%10 < y%10 {
                return Ordering::Less
            } else {
                return Ordering::Greater
            }
        }
        for (ac, bc) in a.chars().zip(b.chars()) {
            let n = ac.to_digit(10).unwrap();
            let m = bc.to_digit(10).unwrap();
            if n > m {
                return Ordering::Greater
            }
            if m > n {
                return Ordering::Less
            }
        }
        if x < y {
            Ordering::Greater
        } else {
            Ordering::Less
        }
    }
    pub fn largest_number(mut nums: Vec<i32>) -> String {
        if nums.iter().fold(0, |acc,x| acc+x) == 0 {
            return String::from("0")
        }
        nums.sort_unstable_by(|a,b| Solution::compare_digits(a,b));
        nums.into_iter().rev().map(|x| x.to_string()).collect::<String>()
    }
}
