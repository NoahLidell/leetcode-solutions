"""
673. Number of Longest Increasing Subsequence
Medium

Given an integer array nums, return the number of longest increasing subsequences.

 

Example 1:

Input: nums = [1,3,5,4,7]
Output: 2
Explanation: The two longest increasing subsequences are [1, 3, 4, 7] and [1, 3, 5, 7].

Example 2:

Input: nums = [2,2,2,2,2]
Output: 5
Explanation: The length of longest continuous increasing subsequence is 1, and there are 5 subsequences' length is 1, so output 5.

 

Constraints:

    1 <= nums.length <= 2000
    -106 <= nums[i] <= 106

"""
class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        N = len(nums)
        if N <= 1:
            return N
        lengths = [0]*N
        counts = [1]*N
        
        for j, num in enumerate(nums):
            for i in range(j):
                if nums[i] < nums[j]:
                    if lengths[i] >= lengths[j]:
                        lengths[j] = 1 + lengths[i]
                        counts[j] = counts[i]
                    elif lengths[i] + 1 == lengths[j]:
                        counts[j] += counts[i]
        longest = max(lengths)
        return sum(c for i, c in enumerate(counts) if lengths[i] == longest)
        
