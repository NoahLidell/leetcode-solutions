"""
821. Shortest Distance to a Character
Easy

Given a string s and a character c that occurs in s, return an array of integers answer where answer.length == s.length and answer[i] is the shortest distance from s[i] to the character c in s.

 

Example 1:

Input: s = "loveleetcode", c = "e"
Output: [3,2,1,0,1,0,0,1,2,2,1,0]

Example 2:

Input: s = "aaab", c = "b"
Output: [3,2,1,0]

 

Constraints:

    1 <= s.length <= 104
    s[i] and c are lowercase English letters.
    c occurs at least once in s.

"""
class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        idxs = set()
        for i,char in enumerate(s):
            if char == c:
                idxs.add(i)
        dist = []
        for i,char in enumerate(s):
            d = 0
            while True:
                if i+d in idxs or i-d in idxs:
                    dist.append(d)
                    break
                else:
                    d += 1
        return dist
