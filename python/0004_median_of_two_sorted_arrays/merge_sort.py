"""
4. Median of Two Sorted Arrays
Hard

Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

Follow up: The overall run time complexity should be O(log (m+n)).

 

Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.

Example 2:

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.

Example 3:

Input: nums1 = [0,0], nums2 = [0,0]
Output: 0.00000

Example 4:

Input: nums1 = [], nums2 = [1]
Output: 1.00000

Example 5:

Input: nums1 = [2], nums2 = []
Output: 2.00000

 

Constraints:

    nums1.length == m
    nums2.length == n
    0 <= m <= 1000
    0 <= n <= 1000
    1 <= m + n <= 2000

"""
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        last = None
        mid = (len(nums1) + len(nums2))/2.0
        n1 = 0
        n2 = 0
        c = 0
        while n1 < len(nums1) or n2 < len(nums2):
            if n1 < len(nums1):
                one = nums1[n1]
            else:
                one = None
            if n2 < len(nums2):
                two = nums2[n2]
            else:
                two = None
            if one != None and two != None:
                if one < two:
                    n1 += 1
                    curr = one
                    c += 1
                else:
                    n2 += 1
                    curr = two
                    c += 1
            elif one != None:
                n1 += 1
                curr = one
                c += 1
            else:
                n2 += 1
                curr = two
                c += 1
            if c == mid+1:
                return (curr + last)/2.0
            if c > mid:
                return float(curr)
            last = curr

