class Solution:
    def numSplits(self, s: str) -> int:
        output = 0
        if len(s) in [0, 1]:
            return 0
        from collections import Counter
        counts = Counter(s)
        a = set()
        b = set([c for c in s])
        for c in s:
            a.add(c)
            count = counts.get(c)
            count -= 1
            if count == 0:
                b.remove(c)
            counts[c] = count
            if len(a) == len(b):
                output += 1
            if len(a) > len(b):
                break
        return output
