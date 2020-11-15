"""
1653. Minimum Deletions to Make String Balanced
Medium

You are given a string s consisting only of characters 'a' and 'b'​​​​.

You can delete any number of characters in s to make s balanced. s is balanced if there is no pair of indices (i,j) such that i < j and s[i] = 'b' and s[j]= 'a'.

Return the minimum number of deletions needed to make s balanced.

 

Example 1:

Input: s = "aababbab"
Output: 2
Explanation: You can either:
Delete the characters at 0-indexed positions 2 and 6 ("aababbab" -> "aaabbb"), or
Delete the characters at 0-indexed positions 3 and 6 ("aababbab" -> "aabbbb").

Example 2:

Input: s = "bbaaaaabb"
Output: 2
Explanation: The only solution is to delete the first two characters.

 

Constraints:

    1 <= s.length <= 105
    s[i] is 'a' or 'b'​​.

"""


class Solution:
    def minimumDeletions(self, s: str) -> int:
        a_right = s.count("a")
        b_right = s.count("b")
        a_left, b_left = 0, 0
        best = a_right
        for c in s:
            best = min(best, a_right + b_left)
            if c == "a":
                a_left += 1
                a_right -= 1
            else:
                b_left += 1
                b_right -= 1

        best = min(best, b_left + a_right)

        return best
