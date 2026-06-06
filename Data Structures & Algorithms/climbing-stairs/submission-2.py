class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}

        def dfs(i):
            if i >= n:
                if i == n:
                    return 1
                return 0
            if i in memo:
                return memo[i]
            
            memo[i] = dfs(i+1)
            memo[i] += dfs(i+2)
            
            return memo[i]
        
        dfs(0)
        return memo[0]