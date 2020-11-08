"""
1556. Thousand Separator
Easy

Given an integer n, add a dot (".") as the thousands separator and return it in string format.

 

Example 1:

Input: n = 987
Output: "987"

Example 2:

Input: n = 1234
Output: "1.234"

Example 3:

Input: n = 123456789
Output: "123.456.789"

Example 4:

Input: n = 0
Output: "0"

 

Constraints:

    0 <= n < 2^31

"""
class Solution:
    def thousandSeparator(self, n: int) -> str:
        if not n:
            return "0"
        s = ""
        c = 0
        while n:
            if not c % 3 and c != 0:
                s += "."
            s += str(n % 10)
            n //= 10
            c += 1
        return s[::-1]

