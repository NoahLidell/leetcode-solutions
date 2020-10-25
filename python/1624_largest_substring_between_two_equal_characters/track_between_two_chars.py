"""
1624. Largest Substring Between Two Equal Characters
Easy

Given a string s, return the length of the longest substring between two equal characters, excluding the two characters. If there is no such substring return -1.

A substring is a contiguous sequence of characters within a string.

 

Example 1:

Input: s = "aa"
Output: 0
Explanation: The optimal substring here is an empty substring between the two 'a's.

Example 2:

Input: s = "abca"
Output: 2
Explanation: The optimal substring here is "bc".

Example 3:

Input: s = "cbzxy"
Output: -1
Explanation: There are no characters that appear twice in s.

Example 4:

Input: s = "cabbac"
Output: 4
Explanation: The optimal substring here is "abba". Other non-optimal substrings include "bb" and "".

 

Constraints:

    1 <= s.length <= 300
    s contains only lowercase English letters.


"""
class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        from collections import defaultdict
        subs = defaultdict(list)
        for i,c in enumerate(list(s)):
            if len(subs[c]) == 2:
                subs[c].pop()
                subs[c].append(i)
            else:
                subs[c].append(i)
        
        subs = [v for v in subs.values() if len(v) == 2]
        m = 0
        pair = None
        for v in subs:
            if v[1] - v[0] > m:
                m = v[1] - v[0]
                pair = v
        if not subs:
            return -1
        if m == 0 or m == 1:
            return len("")
        else:
            return len(s[pair[0]+1:pair[1]])
