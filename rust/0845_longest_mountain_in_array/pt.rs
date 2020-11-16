/*
845. Longest Mountain in Array
Medium

Let's call any (contiguous) subarray B (of A) a mountain if the following properties hold:

    B.length >= 3
    There exists some 0 < i < B.length - 1 such that B[0] < B[1] < ... B[i-1] < B[i] > B[i+1] > ... > B[B.length - 1]

(Note that B could be any subarray of A, including the entire array A.)

Given an array A of integers, return the length of the longest mountain. 

Return 0 if there is no mountain.

Example 1:

Input: [2,1,4,7,3,2,5]
Output: 5
Explanation: The largest mountain is [1,4,7,3,2] which has length 5.

Example 2:

Input: [2,2,2]
Output: 0
Explanation: There is no mountain.

Note:

    0 <= A.length <= 10000
    0 <= A[i] <= 10000

Follow up:

    Can you solve it using only one pass?
    Can you solve it in O(1) space?

*/

use std::cmp;
impl Solution {
    pub fn longest_mountain(a: Vec<i32>) -> i32 {
        let N = a.len();
        if N < 3 {
            return 0
        }
        let mut mtn = 0;
        for i in 1..N-1 {
            if a[i-1] < a[i] && a[i] > a[i+1] {
                let mut size = 3;
                let mut j_l = i - 2;
                let mut j_r = i + 2;
                while j_l != std::usize::MAX && j_l >= 0 && a[j_l] < a[j_l + 1] {
                    size += 1;
                    j_l -= 1;
                }
                while j_r < N && a[j_r - 1] > a[j_r] {
                    size += 1;
                    j_r += 1;
                }
                mtn = cmp::max(size, mtn);
            }
        }
        mtn
    }
}
