"""
187. Repeated DNA Sequences
Medium

All DNA is composed of a series of nucleotides abbreviated as 'A', 'C', 'G', and 'T', for example: "ACGAATTCCG". When studying DNA, it is sometimes useful to identify repeated sequences within the DNA.

Write a function to find all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule.

 

Example 1:

Input: s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
Output: ["AAAAACCCCC","CCCCCAAAAA"]

Example 2:

Input: s = "AAAAAAAAAAAAA"
Output: ["AAAAAAAAAA"]

 

Constraints:

    0 <= s.length <= 105
    s[i] is 'A', 'C', 'G', or 'T'.


"""
from collections import defaultdict
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        res = []
        chk = defaultdict(lambda:0)
        if len(s) < 10:
            return res
        for i in range(0, len(s)):
            ss = s[i:i+10]
            if len(ss) > 10:
                break
            chk[ss] += 1
        return [k for k,v in chk.items() if v > 1]
