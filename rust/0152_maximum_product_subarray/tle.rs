/*
152. Maximum Product Subarray
Medium

Given an integer array nums, find the contiguous subarray within an array (containing at least one number) which has the largest product.

Example 1:

Input: [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.

Example 2:

Input: [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.

*/
use std::cmp::max;

impl Solution {
    pub fn max_product(nums: Vec<i32>) -> i32 {
        let mut maxp = std::i32::MIN;
        for i in 0..nums.len() {
            for j in i + 1..=nums.len() {
                maxp = max(nums[i..j].iter().fold(1, |acc, x| acc * x), maxp);
            }
        }
        maxp
    }
}
