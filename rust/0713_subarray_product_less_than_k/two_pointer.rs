/*
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
*/
mpl Solution {
    pub fn num_subarray_product_less_than_k(nums: Vec<i32>, k: i32) -> i32 {
        let mut prod = 1;
        let mut subs = 0;
        let mut l = 0;
        let mut r = 0;
        let range = nums.len();
        while l < range {
            prod *= nums[l];
            while prod >= k && r <= l {
                prod /= nums[r];
                r += 1;
            }
            if prod < k {
                subs += l-r+1;
            }
            l += 1;
        }
        subs as i32
    }
} 
