class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        maxProfit = 0
        curProfit = 0
        for r in range(len(prices)):
            curProfit = prices[r] - prices[l]
            if curProfit < 0:
                l = r
            maxProfit = max(curProfit, maxProfit)
        return maxProfit
            
