"""
1745. Palindrome Partitioning IV
Hard

Given a string s, return true if it is possible to split the string s into three non-empty palindromic substrings. Otherwise, return false.​​​​​

A string is said to be palindrome if it the same string when reversed.

 

Example 1:

Input: s = "abcbdd"
Output: true
Explanation: "abcbdd" = "a" + "bcb" + "dd", and all three substrings are palindromes.

Example 2:

Input: s = "bcbddxy"
Output: false
Explanation: s cannot be split into 3 palindromes.

 

Constraints:

    3 <= s.length <= 2000
    s​​​​​​ consists only of lowercase English letters.

"""
class Solution:
    def checkPartitioning(self, s: str) -> bool:
        for i in range(1, len(s)):
            ss1 = s[0:i]
            if ss1 == ss1[::-1]:
                ss2 = s[i:]
                for j in range(1,len(ss2)):
                    a = ss2[:j]
                    b = ss2[j:]
                    if a and b and a == a[::-1] and b == b[::-1]:
                        return True
        return False
