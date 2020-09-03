/*
169. Majority Element
Easy

Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.

Example 1:

Input: [3,2,3]
Output: 3

Example 2:

Input: [2,2,1,1,1,2,2]
Output: 2*/
use std::collections::HashMap;
impl Solution {
    pub fn majority_element(nums: Vec<i32>) -> i32 {
        let mut target = nums.len() / 2usize;
        let mut counts = HashMap::new();
        for n in nums {
            let mut count = counts.entry(n).or_insert(0);
            *count += 1;
            if count > &mut target {
                return n;
            }
        }
        0
    }
}
