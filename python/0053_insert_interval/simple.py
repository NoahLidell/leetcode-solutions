"""
57. Insert Interval
Hard

Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).

You may assume that the intervals were initially sorted according to their start times.

Example 1:

Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]

Example 2:

Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].

NOTE: input types have been changed on April 15, 2019. Please reset to default code definition to get new method signature.

"""


class Solution:
    def insert(
        self, intervals: List[List[int]], newInterval: List[int]
    ) -> List[List[int]]:
        out = []
        new = newInterval

        def merge(a, b):
            start = min(a[0], b[0])
            stop = max(a[1], b[1])
            return [start, stop]

        for interval in intervals:
            if (
                new[0] <= interval[0] <= new[1]
                or new[0] <= interval[1] <= new[1]
                or interval[0] <= new[0] <= interval[1]
                or interval[0] <= new[1] <= interval[1]
            ):
                new = merge(new, interval)
            else:
                out.append(interval)
        out.append(new)
        return sorted(out, key=lambda x: x[0])
