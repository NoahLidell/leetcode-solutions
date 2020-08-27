/*
Find Right Interval

Given a set of intervals, for each of the interval i, check if there exists an interval j whose start point is bigger than or equal to the end point of the interval i, which can be called that j is on the "right" of i.

For any interval i, you need to store the minimum interval j's index, which means that the interval j has the minimum start point to build the "right" relationship for interval i. If the interval j doesn't exist, store -1 for the interval i. Finally, you need output the stored value of each interval as an array.

Note:

    You may assume the interval's end point is always bigger than its start point.
    You may assume none of these intervals have the same start point.



Example 1:

Input: [ [1,2] ]

Output: [-1]

Explanation: There is only one interval in the collection, so it outputs -1.



Example 2:

Input: [ [3,4], [2,3], [1,2] ]

Output: [-1, 0, 1]

Explanation: There is no satisfied "right" interval for [3,4].
For [2,3], the interval [3,4] has minimum-"right" start point;
For [1,2], the interval [2,3] has minimum-"right" start point.



Example 3:

Input: [ [1,4], [2,3], [3,4] ]

Output: [-1, 2, -1]

Explanation: There is no satisfied "right" interval for [1,4] and [3,4].
For [2,3], the interval [3,4] has minimum-"right" start point.
*/
use std::cmp::max;
use std::collections::HashMap;
impl Solution {
    pub fn find_right_interval(intervals: Vec<Vec<i32>>) -> Vec<i32> {
        fn bisect_left(arr: &Vec<i32>, x: i32) -> usize {
            let mut lo: usize = 0;
            let mut hi = arr.len();
            while lo < hi {
                let mid = (hi + lo) / 2;
                if arr[mid] < x {
                    lo = mid + 1;
                } else {
                    hi = mid;
                }
            }
            return lo;
        }
        let mut track: HashMap<i32, i32> = HashMap::new();
        let mut upper = std::i32::MIN;
        let mut output = vec![];

        for (idx, i) in intervals.iter().enumerate() {
            upper = max(i[0], upper);
            track.insert(i[0], idx as i32);
        }
        let mut starts = track.keys().cloned().collect::<Vec<i32>>();
        starts.sort();
        for i in intervals.iter() {
            let idx = bisect_left(&starts, i[1]);
            if idx >= starts.len() {
                output.push(-1);
            } else {
                output.push(*track.get(&starts[idx]).unwrap());
            }
        }
        output
    }
}
