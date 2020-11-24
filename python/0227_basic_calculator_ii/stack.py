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
        stack = []
        x = 0
        op = "+"
        s += "+"
        for t in s:
            if t == " ":
                continue
            if t.isdigit():
                x = x*10+int(t)
            else:
                if op == "+":
                    stack.append(x)
                elif op == "-":
                    x *= -1
                    stack.append(x)
                elif op == "*":
                    term = stack.pop()
                    stack.append(term*x)
                elif op == "/":
                    term = stack.pop()
                    stack.append(math.trunc(term/x))
                x = 0
                op = t
        return sum(stack)
