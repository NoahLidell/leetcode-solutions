/*
216. Combination Sum III
Medium

Find all possible combinations of k numbers that add up to a number n, given that only numbers from 1 to 9 can be used and each combination should be a unique set of numbers.

Note:

    All numbers will be positive integers.
    The solution set must not contain duplicate combinations.

Example 1:

Input: k = 3, n = 7
Output: [[1,2,4]]

Example 2:

Input: k = 3, n = 9
Output: [[1,2,6], [1,3,5], [2,3,4]]
*/
impl Solution {
    pub fn combination_sum3(k: i32, n: i32) -> Vec<Vec<i32>> {
        let mut combs = vec![];
        let digits: Vec<i32> = (1..=9).collect();
        for i in 0i32..2i32.pow(9) {
            let mut sum = 0i32;
            let mut combination = vec![];
            for j in 0..9 {
                if (i & (1 << j)) != 0 {
                    let digit = digits[j as usize];
                    combination.push(digit);
                    sum += (digit);
                }
            }

            if k as usize == combination.len() && sum == n {
                combs.push(combination.clone());
            }
        }
        combs
    }
}
