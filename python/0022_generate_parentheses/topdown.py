"""
22. Generate Parentheses
Medium

Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

 

Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]

Example 2:

Input: n = 1
Output: ["()"]

 

Constraints:

    1 <= n <= 8

https://leetcode.com/submissions/detail/406795598/
"""
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def btrack(s, l, r):
            if l == 0 and l == r:
                valid.append(s)
                return
            if l == 0:
                btrack(s+")", l, r-1)
            elif l == r:
                btrack(s+"(", l-1, r)
            else:
                btrack(s+")", l, r-1)
                btrack(s+"(", l-1, r)
        valid = []
        btrack("", n, n)
        return valid
