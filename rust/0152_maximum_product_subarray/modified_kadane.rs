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
use std::cmp::{max, min};

impl Solution {
    pub fn max_product(nums: Vec<i32>) -> i32 {
        let mut maxp = nums[0];
        let mut products = vec![(nums[0], 1i32)];
        for i in 1..nums.len() {
            let (pos, neg) = products[i - 1];
            let b = min(min(neg * nums[i], pos * nums[i]), 1 * nums[i]);
            let a = max(max(neg * nums[i], pos * nums[i]), 1 * nums[i]);
            products.push((a, b));
            maxp = max(maxp, products[i].0);
        }
        maxp
    }
}
