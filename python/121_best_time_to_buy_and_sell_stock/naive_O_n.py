class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        if len(prices) == 0:
            return 0
        low = prices[0]
        
        for n in prices:
            if n < low:
                low = n
                continue
            diff = n - low
            if diff > profit:
                profit = diff
        
        return profit
