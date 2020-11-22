"""
1663. Smallest String With A Given Numeric Value
Medium

The numeric value of a lowercase character is defined as its position (1-indexed) in the alphabet, so the numeric value of a is 1, the numeric value of b is 2, the numeric value of c is 3, and so on.

The numeric value of a string consisting of lowercase characters is defined as the sum of its characters' numeric values. For example, the numeric value of the string "abe" is equal to 1 + 2 + 5 = 8.

You are given two integers n and k. Return the lexicographically smallest string with length equal to n and numeric value equal to k.

Note that a string x is lexicographically smaller than string y if x comes before y in dictionary order, that is, either x is a prefix of y, or if i is the first position such that x[i] != y[i], then x[i] comes before y[i] in alphabetic order.

 

Example 1:

Input: n = 3, k = 27
Output: "aay"
Explanation: The numeric value of the string is 1 + 1 + 25 = 27, and it is the smallest string with such a value and length equal to 3.

Example 2:

Input: n = 5, k = 73
Output: "aaszz"
"""


class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        from string import ascii_lowercase as alpha

        alpha = "!" + alpha  # make alphabet lookup "1-indexed"
        letters = []

        # keep selecting Z until you get close to running out of space
        # (number of letters left begins to approach amount of `k` remaining)
        while k > 26 + n:
            letters.append(26)
            n -= 1
            k -= 26

        while True:
            if n > 1:  # keep adding A until we have one letter left
                letters.append(1)
                k -= 1
                n -= 1
            if n == 1:
                if (
                    k == 27
                ):  # special case if we have k=27 at this point we need a Z and to change are current lowest letter to the next one to the right
                    letters.append(26)
                    letters.sort()
                    letters[0] += 1
                    n -= 1
                else:  # non special case, remaining K is the last letter to add (will be 26 or lower)
                    letters.append(k)
                    n -= 1
                break

        letters.sort()
        return "".join([alpha[x] for x in letters])
