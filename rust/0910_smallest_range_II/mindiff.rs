/*
910. Smallest Range II
Medium

Given an array A of integers, for each integer A[i] we need to choose either x = -K or x = K, and add x to A[i] (only once).

After this process, we have some array B.

Return the smallest possible difference between the maximum value of B and the minimum value of B.

 

Example 1:

Input: A = [1], K = 0
Output: 0
Explanation: B = [1]

Example 2:

Input: A = [0,10], K = 2
Output: 6
Explanation: B = [2,8]

Example 3:

Input: A = [1,3,6], K = 3
Output: 3
Explanation: B = [4,6,3]

 

Note:

    1 <= A.length <= 10000
    0 <= A[i] <= 10000
    0 <= K <= 10000

*/
use std::cmp::{min, max};

impl Solution {
    pub fn smallest_range_ii(a: Vec<i32>, k: i32) -> i32 {
        let mut a = a;
        a.sort();
        let amax = a[a.len()-1];
        let amin = a[0];
        let mut mindiff = (amax) - (amin);
        for i in 0..a.len()-1 {
            mindiff = min(max(amax-k, a[i]+k)-min(amin+k, a[i+1]-k), mindiff)
        }
        mindiff
    }
}
