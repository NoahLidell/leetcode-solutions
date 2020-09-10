/*
448. Find All Numbers Disappeared in an Array
Easy

Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

Find all the elements of [1, n] inclusive that do not appear in this array.

Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.

Example:

Input:
[4,3,2,7,8,2,3,1]

Output:
[5,6]
*/
use std::collections::HashSet;

impl Solution {
    pub fn find_disappeared_numbers(nums: Vec<i32>) -> Vec<i32> {
        let a: HashSet<i32> = nums.iter().cloned().collect();
        let range: HashSet<i32> = (1..=nums.len()).into_iter().map(|x| x as i32).collect();
        range.difference(&a).into_iter().map(|x| *x).collect::<Vec<i32>>()
    }
}
