class Solution:
    def canJump(self, nums: List[int]) -> bool:
        possible = 1
        final_idx = len(nums) - 1
        for i, n in enumerate(nums):
            possible -= 1 # burn a step
            possible = max(possible, n)
            if possible == 0 and i != final_idx:
                return False
        return True

