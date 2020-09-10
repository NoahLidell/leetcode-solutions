"""
290. Word Pattern
Easy

Given a pattern and a string str, find if str follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in str.

Example 1:

Input: pattern = "abba", str = "dog cat cat dog"
Output: true

Example 2:

Input:pattern = "abba", str = "dog cat cat fish"
Output: false

Example 3:

Input: pattern = "aaaa", str = "dog cat cat dog"
Output: false

Example 4:

Input: pattern = "abba", str = "dog dog dog dog"
Output: false

Notes:
You may assume pattern contains only lowercase letters, and str contains lowercase letters that may be separated by a single space.
"""
class Solution:
    def wordPattern(self, pattern: str, string: str) -> bool:
        if pattern == '' and string == '':
            return False
        if len(list(pattern)) != len(string.split(' ')):
            return False
        word2char = { w:c for w, c in zip(string.split(' '), list(pattern))}
        char2word = { c:w for w, c in zip(string.split(' '), list(pattern))}
        return (
            pattern == ''.join([word2char[w] for w in string.split(' ')]) 
            and 
            string == ' '.join([char2word[w] for w in list(pattern)])
        )
