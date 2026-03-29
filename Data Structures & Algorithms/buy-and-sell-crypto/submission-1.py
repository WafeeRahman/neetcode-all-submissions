class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        L = 0
        maxProfit = 0
        #Buy Low, Sell High
        #Start R in the index next to the initial L index
        for R in range(1, len(prices)):
            #Take the profit
            profit = prices[R] - prices[L]
            #The profit being negative implies that r < l, so increment l 
            
            while profit < 0:
                L +=1 #Continously increment the profit until it is positive
                profit = prices[R] - prices[L]
            
            #Calculate maxprofit
            maxProfit = max(maxProfit, profit)
        return maxProfit