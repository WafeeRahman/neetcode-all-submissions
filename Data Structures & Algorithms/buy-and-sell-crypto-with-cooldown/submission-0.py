#Given an integer array of prices where prices[i] is the price of neetcoin on the ith day
#We can buy and sell one neetcoin multiple times, but with respect to the fact that if you sell a neetcoin
#You cannot buy another one on the next day, and you can oonly own one neetcoin at one time
#Return the max profit we can make
class Solution:
    def maxProfit(self, prices: List[int]) -> int:


        def dfs(i, buying):
            if i >= len(prices):
                return 0
            #If we can buy (we dont own neetcoin), then at each step we have two decisions, whether to buy, or not buy
            if buying:
                return max((dfs(i+1, False) - prices[i]), dfs(i+1, True))

            #If we can't buy (we own a neetcoin), we can choose to sell or not to sell
            if not buying:
                return max((dfs(i+2, True) + prices[i]), dfs(i+1, False))


        memo = {}

        def memoize(i, buying):
            if i >= len(prices):
                return 0
            if (i, buying) in memo:
                return memo[(i, buying)]
            
            if buying:
                memo[(i, buying)] =  max((memoize(i+1, False) - prices[i]), memoize(i+1, True))
            if not buying:
                memo[(i, buying)] =  max((memoize(i+2, True) + prices[i]), memoize(i+1, False))
            return memo[(i, buying)]
        return memoize(0, True)