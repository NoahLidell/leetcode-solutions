"""
704. Binary Search
Easy

Given a sorted (in ascending order) integer array nums of n elements and a target value, write a function to search target in nums. If target exists, then return its index, otherwise return -1.


Example 1:

Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4

Example 2:

Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1
Explanation: 2 does not exist in nums so return -1

 

Note:

    You may assume that all elements in nums are unique.
    n will be in the range [1, 10000].
    The value of each element in nums will be in the range [-9999, 9999].

https://leetcode.com/problems/binary-search/
"""


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums)
        if r == 0:
            return -1
        m = ((r - l) // 2) + l
        mn = nums[m]
        while l < r:
            if mn == target:
                return m
            elif target < mn:
                r = m
            else:
                l = m
            m = ((r - l) // 2) + l
            mn = nums[m]
            if r - l == 1:
                if nums[l] == target:
                    return l
                else:
                    return -1
        return -1
