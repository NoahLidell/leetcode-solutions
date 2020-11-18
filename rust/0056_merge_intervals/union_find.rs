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
use std::collections::HashSet;

impl Solution {
    pub fn merge(mut intervals: Vec<Vec<i32>>) -> Vec<Vec<i32>> {
        let mut lookup: [usize; 10_000] = [100_000; 10_000];
        let mut parents = (0..intervals.len()).collect::<Vec<usize>>();
        fn find(p: usize, parents: &mut Vec<usize>) -> usize {
            let parent = parents[p];
            if p == parent {
                parent
            } else {
                parents[p] = find(parent, parents);
                parents[p]
            }
        }
        fn union(a: usize, b: usize, parents: &mut Vec<usize>, intervals: &mut Vec<Vec<i32>>) {
            let pa = find(a, parents);
            let pb = find(b, parents);
            let range = vec![
                cmp::min(intervals[pa][0], intervals[pb][0]),
                cmp::max(intervals[pa][1], intervals[pb][1])
            ];
            let null = vec![-1,-1];
            
            if pa == pb {
                return
            } else if pa < pb {
                parents[pb] = pa;
                intervals[pa] = range;
                intervals[pb] = null;
            } else {
                parents[pa] = pb;
                intervals[pa] = null;
                intervals[pb] = range;
            }
        }
        
        for idx in 0..intervals.len() {
            let ptr = idx;
            let mut seen = HashSet::new();
            let i = intervals[idx][0] as usize;
            let j = intervals[idx][1] as usize;
            for x in i..j+1 {
                if lookup[x] == 100_000 {
                    lookup[x] = ptr;
                } else if seen.contains(&lookup[x]) == false {
                    union(ptr, lookup[x], &mut parents, &mut intervals);
                    seen.insert(lookup[x]);
                } else {
                    lookup[x] = ptr
                }
            }
            
        }
        intervals.into_iter().filter(|x| x[0] != -1).collect::<Vec<Vec<i32>>>()
    }
}
