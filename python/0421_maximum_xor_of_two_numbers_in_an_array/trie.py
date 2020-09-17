"""
421. Maximum XOR of Two Numbers in an Array
Medium

Given an integer array nums, return the maximum result of nums[i] XOR nums[j], where 0 ≤ i ≤ j < n.

Follow up: Could you do this in O(n) runtime?

 

Example 1:

Input: nums = [3,10,5,25,2,8]
Output: 28
Explanation: The maximum result is 5 XOR 25 = 28.

Example 2:

Input: nums = [0]
Output: 0

Example 3:

Input: nums = [2,4]
Output: 6

Example 4:

Input: nums = [8,10,2]
Output: 10

Example 5:

Input: nums = [14,70,53,83,49,91,36,80,92,51,66,70]
Output: 127

 

Constraints:

    1 <= nums.length <= 2 * 104
    0 <= nums[i] <= 231 - 1
"""
from math import log
class Trie():
    def __init__(self):
        self.one = None
        self.zero = None
        self.end = None
        
    def __repr__(self):
        return f"(1:{self.one}|0:{self.zero}[{self.end}])"
    
    def frame(self, n):
        self.pow2 = int(log(n, 2))
        
    def insert(self, n):
        pow2 = self.pow2
        head = self
        while pow2 >= 0:
            if n >> pow2 & 1:
                if head.one == None:
                    head.one = Trie()
                head = head.one
            else:
                if head.zero == None:
                    head.zero = Trie()
                head = head.zero
            pow2 -= 1
        head.end = n
        
    def maxXOR(self, n):
        pow2 = self.pow2
        head = self
        while pow2 >= 0:
            if head.zero and (n >> pow2 & 1):
                head = head.zero
            elif head.one and ((n >> pow2 & 1) == 0):
                head = head.one
            elif head.one:
                head = head.one
            else:
                head = head.zero
            pow2 -= 1
        return head.end ^ n
                    
class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        trie = Trie()
        trie.frame(max(max(nums),1))
        maxXOR = 0
        for n in nums:
            trie.insert(n)
        for n in nums:
            xor = trie.maxXOR(n)
            if xor > maxXOR:
                maxXOR = xor       
        return maxXOR
        
