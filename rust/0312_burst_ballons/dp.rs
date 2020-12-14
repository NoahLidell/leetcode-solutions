/*
312. Burst Balloons
Hard

Given n balloons, indexed from 0 to n-1. Each balloon is painted with a number on it represented by array nums. You are asked to burst all the balloons. If the you burst balloon i you will get nums[left] * nums[i] * nums[right] coins. Here left and right are adjacent indices of i. After the burst, the left and right then becomes adjacent.

Find the maximum coins you can collect by bursting the balloons wisely.

Note:

    You may imagine nums[-1] = nums[n] = 1. They are not real therefore you can not burst them.
    0 ≤ n ≤ 500, 0 ≤ nums[i] ≤ 100

Example:

Input: [3,1,5,8]
Output: 167 
Explanation: nums = [3,1,5,8] --> [3,5,8] -->   [3,8]   -->  [8]  --> []
             coins =  3*1*5      +  3*5*8    +  1*3*8      + 1*8*1   = 167
*/
impl Solution {
    pub fn max_coins(nums: Vec<i32>) -> i32 {
        let numstmp = nums;
        let mut nums = vec![1];
        nums.extend(numstmp);
        nums.push(1);
        let n = nums.len();
        
        let mut dp = vec![vec![0;n];n];
        for gap in 2..n {
            for left in 0..(n-gap) {
                let right = left + gap;
                for i in left+1..right {
                    dp[left][right] = std::cmp::max(dp[left][right],
                    dp[left][i] + dp[i][right] + nums[left]*nums[i]*nums[right])
                }
            }
        }
        dp[0][n-1]
    }
}
