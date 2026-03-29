class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        dpCache = {}

        def rec(holding, i):
            nonlocal dpCache
            
            if i >= len(prices):
                return 0
            
            elif (holding, i) in dpCache:
                return dpCache[(holding, i)]
        
            if holding:
                dpCache[(holding, i)] = max((prices[i] + rec(False, i+1)), rec(True, i+1))
            else:
                dpCache[(holding, i)] =  max((-prices[i] + rec(True, i+1)), rec(False, i+1))
            
            return dpCache[(holding, i)] 
            
        rec(False, 0)

        return dpCache[False, 0]
            
            

            
            


       
            
            

            