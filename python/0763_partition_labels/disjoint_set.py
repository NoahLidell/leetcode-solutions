"""
763. Partition Labels
Medium

A string S of lowercase English letters is given. We want to partition this string into as many parts as possible so that each letter appears in at most one part, and return a list of integers representing the size of these parts.

 

Example 1:

Input: S = "ababcbacadefegdehijhklij"
Output: [9,7,8]
Explanation:
The partition is "ababcbaca", "defegde", "hijhklij".
This is a partition so that each letter appears in at most one part.
A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits S into less parts.

 

Note:

    S will have length in range [1, 500].
    S will consist of lowercase English letters ('a' to 'z') only.
"""

class DisjointSet():
    def __init__(self):
        self.parent = [n for n in range(26)]
        self.size = [set() for n in range(26)]
    def find(self, x):
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    def union(self, x, y):
        p_x = self.find(x)
        p_y = self.find(y)
        if p_x != p_y:
            if len(self.size[p_x]) > len(self.size[p_y]):
                self.parent[p_y] = p_x
                self.size[p_x].update(self.size[p_y])
            else:
                self.parent[p_x] = p_y
                self.size[p_y].update(self.size[p_x])

class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        
        abc = "abcdefghijklmnopqrstuvwxyz"
        tree = DisjointSet()
        idx_letter_map = {}
        for i, c in enumerate(abc):
            try:
                scope = set(range(S.index(c), S.rindex(c)+1))
                tree.size[i].update(scope)
                for idx in scope:
                    if idx in idx_letter_map:
                        tree.union(i, idx_letter_map[idx])
                    else:
                        idx_letter_map[idx] = i
            except ValueError:
                pass
        partitions = [abc.index(c) for i,c in enumerate(S) 
                      if tree.find(abc.index(c)) == abc.index(c)
                      and i == S.index(c)
                     ]
        partitions = [len(tree.size[root]) for root in list(partitions) if len(tree.size[root])]
        return partitions
        
