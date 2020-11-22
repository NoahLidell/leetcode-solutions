/*
283. Move Zeroes
Easy

Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Example:

Input: [0,1,0,3,12]
Output: [1,3,12,0,0]

Note:

    You must do this in-place without making a copy of the array.
    Minimize the total number of operations.
*/
impl Solution {
    pub fn move_zeroes(nums: &mut Vec<i32>) {
        if nums.len() == 0 {
            return;
        }
        for i in 0..(nums.len() - 1) {
            if nums[i] == 0 {
                let mut j = i + 1;
                while nums[j] == 0 && j < nums.len() - 1 {
                    j += 1;
                }
                nums[i] ^= nums[j];
                nums[j] ^= nums[i];
                nums[i] ^= nums[j];
            }
        }
    }
}
