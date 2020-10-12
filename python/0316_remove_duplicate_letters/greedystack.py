"""
316. Remove Duplicate Letters
Medium

Given a string s, remove duplicate letters so that every letter appears once and only once. You must make sure your result is the smallest in lexicographical order among all possible results.

Note: This question is the same as 1081: https://leetcode.com/problems/smallest-subsequence-of-distinct-characters/

 

Example 1:

Input: s = "bcabc"
Output: "abc"

Example 2:

Input: s = "cbacdcbc"
Output: "acdb"

 

Constraints:

    1 <= s.length <= 104
    s consists of lowercase English letters.

https://leetcode.com/problems/remove-duplicate-letters/
"""
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        stack = []
        in_play = set()
        last_occurence = {}
        
        for i in range(len(s)):
            letter = s[i]
            last_occurence[letter] = i
        
        for i in range(len(s)):
            letter = s[i]
            if letter in in_play:
                continue
            if not stack:
                stack.append(letter)
                in_play.add(letter)
                continue
            while stack and letter < stack[-1] and i < last_occurence[stack[-1]]:
                in_play.remove(stack.pop())
            in_play.add(letter)    
            stack.append(letter)
        
        return ''.join(stack)
