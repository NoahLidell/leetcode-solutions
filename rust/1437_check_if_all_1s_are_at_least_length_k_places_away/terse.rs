/*
1437. Check If All 1's Are at Least Length K Places Away
Easy

Given an array nums of 0s and 1s and an integer k, return True if all 1's are at least k places away from each other, otherwise return False.

 

Example 1:

Input: nums = [1,0,0,0,1,0,0,1], k = 2
Output: true
Explanation: Each of the 1s are at least 2 places away from each other.

Example 2:

Input: nums = [1,0,0,1,0,1], k = 2
Output: false
Explanation: The second 1 and third 1 are only one apart from each other.

Example 3:

Input: nums = [1,1,1,1,1], k = 0
Output: true

Example 4:

Input: nums = [0,1,0,1], k = 1
Output: true

 

Constraints:

    1 <= nums.length <= 105
    0 <= k <= nums.length
    nums[i] is 0 or 1

*/
use std::i32::MAX;
use std::cmp::min;

impl Solution {
    pub fn k_length_apart(nums: Vec<i32>, k: i32) -> bool {
        nums.iter().fold((MAX, MAX), |acc, x| {
            let (gap, run) = acc;
            match x {
                &0 if run == MAX => acc,
                &0 => (gap, run + 1),
                _ => (min(gap, run), 0)
            }
        }).0 >= k
    }
}
