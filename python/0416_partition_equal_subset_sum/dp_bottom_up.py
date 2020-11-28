"""
416. Partition Equal Subset Sum
Medium

Given a non-empty array nums containing only positive integers, find if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal.

 

Example 1:

Input: nums = [1,5,11,5]
Output: true
Explanation: The array can be partitioned as [1, 5, 5] and [11].

Example 2:

Input: nums = [1,2,3,5]
Output: false
Explanation: The array cannot be partitioned into equal sum subsets.

 

Constraints:

    1 <= nums.length <= 200
    1 <= nums[i] <= 100
"""


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        N = len(nums)
        total = sum(nums)
        if total % 2 == 1:
            return False

        half = total // 2
        dp = [[False] * (half + 1) for _ in range(N + 1)]

        dp[0][0] = True

        for idx in range(1, N + 1):
            for k in range(nums[idx - 1], half + 1):
                dp[idx][k] |= dp[idx - 1][k - nums[idx - 1]]
            for k in range(half + 1):
                dp[idx][k] |= dp[idx - 1][k]
        return dp[N][half]
