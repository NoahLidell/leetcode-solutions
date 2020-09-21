"""
1291. Sequential Digits
Medium

An integer has sequential digits if and only if each digit in the number is one more than the previous digit.

Return a sorted list of all the integers in the range [low, high] inclusive that have sequential digits.

 

Example 1:

Input: low = 100, high = 300
Output: [123,234]

Example 2:

Input: low = 1000, high = 13000
Output: [1234,2345,3456,4567,5678,6789,12345]

 

Constraints:

    10 <= low <= high <= 10^9
"""
class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        def genmag(o):
            oo = o * 10
            seq = []
            for d in range(1,10):
                s = str(d)
                while int(s) * 10 < oo:
                    d += 1
                    if d > 9:
                        break
                    s += str(d)
                seq.append(int(s))
            return seq
        soln = []
        o = 10
        while o <= high:
            soln.extend(genmag(o))
            o *= 10
        return sorted(set([seq for seq in soln if low <= seq <= high]))
