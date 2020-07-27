class Solution:
    def countOdds(self, low: int, high: int) -> int:
        below_low = low//2
        below_high = high//2
        if high % 2 == 1:
            below_high += 1
        return below_high - below_low
