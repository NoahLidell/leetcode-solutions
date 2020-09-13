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


class DisjointSet:
    def __init__(self, parts, new_part):
        range_marks = [bound for part_range in parts for bound in part_range]
        range_marks.extend(new_part)
        self.parent = [-1 for i in range(max(range_marks) + 1)]
        self.interval = {}
        for part in parts:
            begin = min(part)
            end = max(part)
            self.parent[begin] = begin
            self.interval[begin] = part
            for n in range(begin + 1, end + 1):
                self.parent[n] = begin
        n0 = min(new_part)
        n1 = max(new_part)
        if self.parent[n0] == -1:
            self.parent[n0] = n0
            self.interval[n0] = new_part
        else:
            root = self.find(n0)
            self.parent[n0] = root
            introot = self.interval[root]
            start = min(introot[0], new_part[0])
            stop = max(introot[1], new_part[1])
            interval = [start, stop]
            self.interval[root] = interval

        for n in range(n0 + 1, n1 + 1):
            if self.parent[n] == -1:
                self.parent[n] = self.find(n0)
            else:
                self.union(n0, n)

    def __call__(self):
        return sorted(list(self.interval.values()), key=lambda x: x[0])

    def find(self, x):
        if self.parent[x] != x:
            return self.find(self.parent[x])
            # self.parent[x] = self.find(self.parent[x]) would also work, basically caches the root parent on the current node
        return self.parent[x]

    def union(self, x, y):
        rootx = self.find(x)
        rooty = self.find(y)
        if rootx != rooty:
            intx = self.interval[rootx]
            inty = self.interval[rooty]
            start = min(intx[0], inty[0])
            stop = max(intx[1], inty[1])
            interval = [start, stop]
            if rootx <= rooty:
                self.interval.pop(rooty)
                self.interval[rootx] = interval
                self.parent[rooty] = rootx
            else:
                self.interval.pop(rootx)
                self.interval[rooty] = interval
                self.parent[rootx] = rooty


class Solution:
    def insert(
        self, intervals: List[List[int]], newInterval: List[int]
    ) -> List[List[int]]:
        make_solution = DisjointSet(intervals, newInterval)
        return make_solution()
