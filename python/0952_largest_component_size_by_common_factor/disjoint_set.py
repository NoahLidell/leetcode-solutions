"""
952. Largest Component Size by Common Factor
Hard

Given a non-empty array of unique positive integers A, consider the following graph:

    There are A.length nodes, labelled A[0] to A[A.length - 1];
    There is an edge between A[i] and A[j] if and only if A[i] and A[j] share a common factor greater than 1.

Return the size of the largest connected component in the graph.

 

Example 1:

Input: [4,6,15,35]
Output: 4

Example 2:

Input: [20,50,9,63]
Output: 2

Example 3:

Input: [2,3,6,7,4,12,21,39]
Output: 8

Note:

    1 <= A.length <= 20000
    1 <= A[i] <= 100000
"""
class DisjointSet():
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1]*n
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            size_x = self.size[root_x]
            size_y = self.size[root_y]
            if size_x < size_y:
                self.parent[root_x] = root_y
                self.size[root_y] += size_x
            else:
                self.parent[root_y] = root_x
                self.size[root_x] += size_y
                
class Solution:
    def largestComponentSize(self, A: List[int]) -> int:
        factor_index = {}
        tree = DisjointSet(len(A))
        for idx, num in enumerate(A):
            for factor in range(2, int(num**0.5)+1):
                if num % factor == 0:
                    for fac in (factor, num // factor):
                        if fac in factor_index:
                            tree.union(idx, factor_index[fac])
                        else:
                            factor_index[fac] = idx
            if num not in factor_index:
                factor_index[num] = idx
            else:
                tree.union(idx, factor_index[num])
        return max(tree.size)
        
        
