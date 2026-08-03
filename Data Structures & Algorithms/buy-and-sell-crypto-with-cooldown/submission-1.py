class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        memo = {}
        nums = prices
        def dp(i, prev):
            if i >= len(prices):
                return 0
            if (i, prev) in memo:
                return memo[(i, prev)]
            
            #Can Buy
            if prev == None:
                #Don't Buy
                dontBuy = dp(i+1, None)
                
                #Buy
                buy = dp(i+1, i)

                memo[(i,prev)] = max(buy, dontBuy) 
               
            else:
                if i-prev >= 1:
                    #Sell
                    sell = (nums[i] - nums[prev]) + dp(i+2, None)
             

                    #Hold
                    hold = dp(i+1, prev)
                    memo[(i, prev)] = max(hold, sell)
                else:
                    hold = dp(i+1, prev)
                    memo[(i, prev)] = hold   
        
            return memo[(i,prev)]


        return dp(0, None)