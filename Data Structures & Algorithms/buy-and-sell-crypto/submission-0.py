class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        L = 0
        maxProfit = 0
        for R in range(1, len(prices)):
            profit = prices[R] - prices[L]
            while profit < 0:
                L +=1 
                profit = prices[R] - prices[L]
            maxProfit = max(maxProfit, profit)
        return maxProfit