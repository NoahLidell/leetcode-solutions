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
impl Solution {
    pub fn find_disappeared_numbers(orig: Vec<i32>) -> Vec<i32> {
        let mut nums = orig.clone();
        for n in orig.iter() {
            nums[{*n as usize} -1] = -1;
        }
        nums.into_iter().enumerate().map(|x| {
            let (idx, n) = x;
            if n == -1 {
                return n
            } else {
                return (idx as i32)+1 
            }
        }).filter(|x| x > &0).collect()
    }
}
