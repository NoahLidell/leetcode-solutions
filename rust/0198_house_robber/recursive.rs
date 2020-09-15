/*
198. House Robber
Easy

You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.



Example 1:

Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
             Total amount you can rob = 1 + 3 = 4.

Example 2:

Input: nums = [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
             Total amount you can rob = 2 + 9 + 1 = 12.



Constraints:

    0 <= nums.length <= 100
    0 <= nums[i] <= 400

*/

use std::cmp;

impl Solution {
    pub fn rob(nums: Vec<i32>) -> i32 {
        fn recurse(houses: &Vec<i32>, mut memo: &mut Vec<i32>, idx: usize) -> i32 {
            if idx == std::usize::MAX || idx == std::usize::MAX - 1 {
                return 0;
            }
            if memo[idx] >= 0 {
                return memo[idx];
            }
            let a = recurse(&houses, &mut memo, idx - 1);
            let b = recurse(&houses, &mut memo, idx - 2) + houses[idx];
            let result = cmp::max(a, b);
            memo[idx] = result;
            result
        }
        let mut memo = vec![-1; nums.len()];
        recurse(&nums, &mut memo, nums.len() - 1)
    }
}
