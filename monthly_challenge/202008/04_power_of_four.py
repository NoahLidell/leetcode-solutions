class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        fours = [4**i for i in range(16)]
        if num in fours:
            return True
        else:
            return False
