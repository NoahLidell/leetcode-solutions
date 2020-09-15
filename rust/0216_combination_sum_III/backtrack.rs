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
        fn backtrack(
            target: i32,
            mut combs: &mut Vec<Vec<i32>>,
            mut comb: &mut Vec<i32>,
            limit: usize,
            start: i32,
        ) {
            if target == 0 && comb.len() == limit {
                combs.push(comb.to_vec());
            } else if target > 0 && comb.len() < limit {
                for i in start..=9 {
                    comb.push(i);
                    backtrack(target - i, &mut combs, &mut comb, limit, i + 1);
                    comb.pop();
                }
            }
        }
        let mut comb = vec![];
        backtrack(n, &mut combs, &mut comb, k as usize, 1);
        combs
    }
}
