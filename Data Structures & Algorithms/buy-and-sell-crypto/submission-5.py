class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = float('-inf')
        l = 0
        for r in range(len(prices)):

            curProfit = prices[r] - prices[l]
            maxProfit = max(maxProfit, curProfit)
            if curProfit < 0:
                l = r
        return maxProfit
            

            


        