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
        def isValid(s):
            chk = 0
            for c in s:
                if c == ")":
                    chk -= 1
                else:
                    chk += 1
                if chk < 0: 
                    return False
            if chk == 0:
                return True
            else:
                return False
        valid = []
        def btrack(s):
            if len(s) == 2*n:
                if isValid(s):
                    valid.append(s)
                return
            btrack(s+"(")
            btrack(s+")")
        btrack("(")
        return valid
