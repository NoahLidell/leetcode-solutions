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
            return 0;
        }
        let mut prev = a[0];
        let mut m = 0;
        let mut mx = 0;
        let mut up = false;
        let mut mtn = false;
        for i in 1..N {
            let x = a[i];
            if x > prev && up == false {
                up = true;
                mtn = false;
                mx = 2;
                prev = x;
            } else if x > prev && up == true {
                mx += 1;
                prev = x;
            } else if x < prev && up == true {
                mtn = true;
                mx += 1;
                prev = x;
                up = false
            } else if x == prev {
                mx = 0;
                mtn = false;
            } else if x < prev && up == false && mtn == true {
                mx += 1;
                prev = x;
            } else if x < prev && up == false && mtn == false {
                mx = 0;
                prev = x;
            }
            if mx >= 3 && mtn == true {
                m = cmp::max(m, mx);
            }
        }
        m
    }
}
