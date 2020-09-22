/*
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
*/
impl Solution {
    pub fn majority_element(nums: Vec<i32>) -> Vec<i32> {
        if nums.len() == 0 {
            return vec![];
        }
        let (mut c1, mut c2, mut can1, mut can2) = (0i32, 0i32, 0i32, 0i32);
        for n in &nums {
            if n == &can1 {
                c1 += 1;
            } else if n == &can2 {
                c2 += 1;
            } else if c1 == 0 {
                can1 = *n;
                c1 += 1;
            } else if c2 == 0 {
                can2 = *n;
                c2 += 1;
            } else {
                c1 -= 1;
                c2 -= 1;
            }
        }
        let mut soln = vec![];
        c1 = 0;
        c2 = 0;
        for n in &nums {
            if n == &can1 {
                c1 += 1;
            }
            if n == &can2 {
                c2 += 1
            }
        }
        if c1 > (nums.len() / 3) as i32 {
            soln.push(can1);
        }
        if can1 != can2 && c2 > (nums.len() / 3) as i32 {
            soln.push(can2);
        }
        soln
    }
}
