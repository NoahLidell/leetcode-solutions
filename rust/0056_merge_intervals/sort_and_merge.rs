/*
56. Merge Intervals
Medium

Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.



Example 1:

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].

Example 2:

Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.



Constraints:

    1 <= intervals.length <= 104
    intervals[i].length == 2
    0 <= starti <= endi <= 104

*/
use std::cmp;
impl Solution {
    pub fn merge(mut intervals: Vec<Vec<i32>>) -> Vec<Vec<i32>> {
        intervals.sort_by(|a, b| a[0].cmp(&b[0]));
        for idx in 0..intervals.len() - 1 {
            if intervals[idx][1] >= intervals[idx + 1][0] {
                intervals[idx + 1][0] = cmp::min(intervals[idx][0], intervals[idx + 1][0]);
                intervals[idx + 1][1] = cmp::max(intervals[idx][1], intervals[idx + 1][1]);
                intervals[idx] = vec![-1, -1];
            }
        }
        intervals
            .into_iter()
            .filter(|x| x[0] != -1)
            .collect::<Vec<Vec<i32>>>()
    }
}
