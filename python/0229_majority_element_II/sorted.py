"""
229. Majority Element II
Medium

Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.

Note: The algorithm should run in linear time and in O(1) space.

Example 1:

Input: [3,2,3]
Output: [3]

Example 2:

Input: [1,1,1,3,3,2,2,2]
Output: [1,2]

"""
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n3 = float(len(nums))/3.
        switch = None
        c = 0
        soln = []
        for n in sorted(nums):
            if n != switch:
                if float(c) > n3:
                    soln.append(switch)
                switch = n
                c = 0
            c += 1
        else:
            if float(c) > n3:
                soln.append(switch)
        return soln
                
