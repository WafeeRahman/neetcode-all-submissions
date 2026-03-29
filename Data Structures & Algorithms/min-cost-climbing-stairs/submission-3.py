class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cache = {} #Memoization - cache previous calls to save on repeated work
            
        #def dfs(i):
        #    if i >= len(cost):
        #        return 0
        #    return cost[i] + min(dfs(i + 1), dfs(i + 2))
        
        #return min(dfs(0), dfs(1))
       
       
        def memoization(i):
            nonlocal cache
            #Same Base Case, but store solutions in cache
            if i >= len(cost):
                return 0
            #Use O(1) lookup to find cache
            if i in cache:
                return cache[i]
            #Set cache values
            cache[i] = cost[i] + min(memoization(i+1), memoization(i+2))
            return cache[i]
        
        #The cost of getting past the nth value is zero
        cost.append(0)
        def dp(n):
            if n <= 1:
                return cost[n]  
            #Bottom up DP, start at n
            for i in range(n-3, -1, -1):
                #At each step, calculate the cost to reach the ith value
                cost[i] = cost[i] + min(cost[i+1], cost[i+2]) 

            return min(cost[0], cost[1])      
        return dp(len(cost))        


        