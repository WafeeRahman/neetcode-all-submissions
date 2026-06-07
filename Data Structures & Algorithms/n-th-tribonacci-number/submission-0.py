class Solution:
    def tribonacci(self, n: int) -> int:
        memo = {0: 0, 1: 1, 2:1}


        def dfs(i):
            if i > n:
                return
            if i >= 3:
                memo[i] = memo[i-1] + memo[i-2] + memo[i-3]
            
            dfs(i+1)
            
        dfs(0)
        return memo[n]
        