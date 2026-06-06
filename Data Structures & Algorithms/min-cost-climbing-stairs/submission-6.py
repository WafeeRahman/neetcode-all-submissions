class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = {}
        n = len(cost)
        def dfs(i):
            if i in memo:
                return memo[i]
    
            if i >= n:
                return 0
            
            memo[i] = cost[i] + dfs(i+1)
            memo[i] = min(memo[i], (cost[i] + dfs(i+2)))

            return memo[i]
             
        dfs(0)
        dfs(1)

        return min(memo[1], memo[0])
            

                