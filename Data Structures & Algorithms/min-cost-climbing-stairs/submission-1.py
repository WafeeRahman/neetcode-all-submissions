class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cache = {}
       
        def memoization(i):
            nonlocal cache
            if i >= len(cost):
                return 0
            if i in cache:
                return cache[i]
            cache[i] = cost[i] + min(memoization(i+1), memoization(i+2))
            return cache[i]
        
        return min(memoization(0), memoization(1))


        