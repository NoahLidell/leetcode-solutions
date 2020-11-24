"""
227. Basic Calculator II
Medium

Implement a basic calculator to evaluate a simple expression string.

The expression string contains only non-negative integers, +, -, *, / operators and empty spaces . The integer division should truncate toward zero.

Example 1:

Input: "3+2*2"
Output: 7

Example 2:

Input: " 3/2 "
Output: 1

Example 3:

Input: " 3+5 / 2 "
Output: 5

Note:

    You may assume that the given expression is always valid.
    Do not use the eval built-in library function.
"""
class Solution:
    def calculate(self, s: str) -> int:
        tkns = list(s)
        tkns = [tkn for tkn in tkns if tkn != " "]
        ops = set(["*", "/", "-", "+"])
        ntkns = []
        x = ""
        for t in tkns:
            if t not in ops:
                x += t
            if t in ops:
                ntkns.append(x)
                x = ""
                ntkns.append(t)
        if x: ntkns.append(x) 
        tkns = ntkns
        N = len(tkns)
        i = 0
        while i < N:
            if tkns[i] in ["*","/"]:
                a = int(tkns[i-1])
                b = int(tkns[i+1])
                if tkns[i] == "*":
                    c = a * b
                else:
                    c = a//b
                t0 = tkns[:i-1]
                t1 = tkns[i+2:]
                tkns = t0 + [str(c)] + t1
                N = len(tkns)
                i -= 1
            else:
                i += 1
        out = 0
        op = "+"
        for x in tkns:
            if x in ["+","-"]:
                op = x
            else:
                if op == "+":
                    out += int(x)
                else:
                    out -= int(x)
        return out
