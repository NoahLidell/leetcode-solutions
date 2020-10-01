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
        nums += [0]
        for i in range(len(nums)):
            n = nums[i]
            if isinstance(n, complex):
                n = int(n.real)
            if n > 0 and n < len(nums):
                nums[n] += 1j
        res =  [i for i,n in enumerate(nums) if i>0 and not isinstance(n, complex)]
        if res == []:
            return len(nums)
        else:
            return res[0]
