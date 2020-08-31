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

class Solution:
    def largestComponentSize(self, A: List[int]) -> int:
        def gcd(a,b):
            if a<b:
                a,b = b,a
            r = a % b
            if r == 0:
                return b
            else:
                return gcd(b,r)
        def edge(a,b):
            gcf = gcd(a,b)
            if gcf == 1:
                return False
            else:
                return True
        def in_component(node, comp):
            for n in comp:
                if edge(n, node):
                    return True
            return False
        A = [num for num in A if num != 1]
        components = [[A[0]]]
        for i, n in enumerate(A):
            connects = []
            removed = 0
            if i == 0:
                continue
            for i, c in enumerate(components):
                if in_component(n, c):
                    connects.append(i)
                    c.append(n)
            if connects == []:
                components.append([n])
            if len(connects) > 1:
                for idx in connects[1:]:
                    components[connects[0]].extend(components[idx])
                for idx in connects[1:]:
                    del components[idx-removed]
                    removed += 1
        return max([len(set(c)) for c in components])
        
        
