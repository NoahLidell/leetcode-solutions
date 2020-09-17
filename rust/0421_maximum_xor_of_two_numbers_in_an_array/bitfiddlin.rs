/*421. Maximum XOR of Two Numbers in an Array
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

*/
use std::collections::HashSet;
impl Solution {
    pub fn find_maximum_xor(nums: Vec<i32>) -> i32 {
        let nums = nums.into_iter().map(|x| x as u32).collect::<Vec<u32>>();
        let mut mask = 0u32;
        let mut max = 0u32;
        for i in (0..=31).rev() {
            let potential_bit = max | (1 << i);
            mask |= 1 << i;
            let mut bits: HashSet<u32> = HashSet::new();
            for n in nums.iter() {
                bits.insert((*n as u32) & mask);
            }
            for b in bits.iter() {
                if bits.contains(&(b ^ potential_bit)) {
                    max = potential_bit;
                    break;
                }
            }
        }
        max as i32
    }
}
