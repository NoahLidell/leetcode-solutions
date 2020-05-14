class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        current = ""

        for c in s:
            if len(current) == 0:
                current = c
            elif c in current:
                current = current[current.index(c) + 1 :] + c
            else:
                current += c
            if len(current) > longest:
                longest = len(current)
        return longest
