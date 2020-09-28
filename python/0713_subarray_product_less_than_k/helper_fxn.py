"""
713. Subarray Product Less Than K
Medium

Your are given an array of positive integers nums.

Count and print the number of (contiguous) subarrays where the product of all the elements in the subarray is less than k.

Example 1:

Input: nums = [10, 5, 2, 6], k = 100
Output: 8
Explanation: The 8 subarrays that have product less than 100 are: [10], [5], [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6].
Note that [10, 5, 2] is not included as the product of 100 is not strictly less than k.

Note:
0 < nums.length <= 50000.
0 < nums[i] < 1000.
0 <= k < 10^6.
https://leetcode.com/problems/subarray-product-less-than-k/
"""
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        def opt(j, curr, i):
            prod = curr * nums[j]
            while prod >= k and i < j:
                prod /= nums[i]
                i += 1
            return prod, i
        if len(nums) == 1:
            return 1 if nums[0] < k else 0
        subs = 1 if nums[0] < k else 0
        curr = nums[0]
        i = 0
        for j in range(1, len(nums)):
            curr, i = opt(j, curr, i)
            if curr < k:
                subs += j-i+1
        return subs
