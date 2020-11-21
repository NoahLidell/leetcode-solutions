/*
81. Search in Rotated Sorted Array II
Medium

Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., [0,0,1,2,2,5,6] might become [2,5,6,0,0,1,2]).

You are given a target value to search. If found in the array return true, otherwise return false.

Example 1:

Input: nums = [2,5,6,0,0,1,2], target = 0
Output: true

Example 2:

Input: nums = [2,5,6,0,0,1,2], target = 3
Output: false

Follow up:

    This is a follow up problem to Search in Rotated Sorted Array, where nums may contain duplicates.
    Would this affect the run-time complexity? How and why?

*/
impl Solution {
    pub fn search(nums: Vec<i32>, target: i32) -> bool {
        let N = nums.len();
        if N == 0 {
            return false
        }
        fn dfs(a: usize, b: usize, t: i32, nums: &Vec<i32>) -> bool {
            if b - a <= 1 {
                return nums[a..=b].contains(&t)
            }
            let mid = (a + b)/2;
            if nums[mid] > nums[b] {
                if ((nums[b] < t) && (t<= nums[mid])) {
                    dfs(a, mid, t, nums)
                } else {
                    dfs(mid + 1, b, t, nums)
                }
            } else if nums[mid] < nums[b] {
                if ((nums[mid] < t) && (t <= nums[b])) {
                    dfs(mid+1, b, t, nums)
                } else {
                    dfs(a, mid, t, nums)
                }
            } else {
                dfs(mid+1, b, t, nums) || dfs(a, mid, t, nums)
            }
            
        }
        dfs(0, N-1, target, &nums)
    }
}
