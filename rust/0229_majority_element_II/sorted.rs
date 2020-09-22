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
    pub fn majority_element(mut nums: Vec<i32>) -> Vec<i32> {
        let mut soln = vec![];
        let n3 = (nums.len() as f32) / 3f32;
        let mut c = 0;
        let mut can = 0;
        nums.sort_unstable();
        for n in nums {
            if n as i32 != can {
                if c as f32 > n3 {
                    soln.push(can);
                }
                can = n;
                c = 0;
            }
            c += 1;
        }
        if c as f32 > n3 {
            soln.push(can);
        }
        soln
    }
}
