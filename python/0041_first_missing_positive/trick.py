"""
41. First Missing Positive
Hard

Given an unsorted integer array, find the smallest missing positive integer.

Example 1:

Input: [1,2,0]
Output: 3

Example 2:

Input: [3,4,-1,1]
Output: 2

Example 3:

Input: [7,8,9,11,12]
Output: 1

Follow up:

Your algorithm should run in O(n) time and uses constant extra space.

http://leetcode.com/problems/first-missing-positive/
"""
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums = list(set(nums)) + [0]
        N = len(nums)
        for i in range(N):
            if nums[i] >= N or nums[i] < 0:
                nums[i] = 0
        for i in range(N):
            nums[nums[i]%N] += N
        for i in range(1,N):
            if nums[i]//N == 0:
                return i
        return N
