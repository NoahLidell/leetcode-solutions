"""
131. Palindrome Partitioning
Medium

Given a string s, partition s such that every substring of the partition is a palindrome. Return all possible palindrome partitioning of s.

A palindrome string is a string that reads the same backward as forward.

 

Example 1:

Input: s = "aab"
Output: [["a","a","b"],["aa","b"]]

Example 2:

Input: s = "a"
Output: [["a"]]

 

Constraints:

    1 <= s.length <= 16
    s contains only lowercase English letters.


"""

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        N = len(s)
        dp = [[False]*N]*N
        res = []
        def dfs(idx, lis):
            nonlocal dp, s, res, N
            if idx >= len(s) and all([w == w[::-1] for w in lis]):
                res.append(lis)
            for j in range(idx, N):
                if s[idx] == s[j] and (j - idx <= 2 or dp[idx+1][j-1]):
                    dp[idx][j] = True
                    dfs(j+1, lis+[s[idx:j+1]])
        
        dfs(0, [])
        return res
        
