
class Solution:
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        nums = [(n,idx) for idx,n in enumerate(nums)]
        nums = sorted(nums, key=lambda x: x[0])
        for a in range(len(nums)):
            for b in range(a+1, len(nums)):
                x = nums[a][0]
                y = nums[b][0]
                i = nums[a][1]
                j = nums[b][1]
                diff = abs(x-y)
                didx = abs(i-j)
                if diff > t:
                    break
                if diff <= t and didx<= k:
                    return True
        return False


