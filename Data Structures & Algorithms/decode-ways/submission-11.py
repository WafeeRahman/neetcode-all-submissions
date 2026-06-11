class Solution:
    def numDecodings(self, s: str) -> int:
        memo = {}
        def dfs(i):
            if i in memo:
                return memo[i]
            if i == len(s):
                return 1 
     
            
            memo[i] = 0

            if s[i] != "0":
                memo[i] += dfs(i+1)

            if i+1 < len(s) and (s[i] == "1" or s[i] == "2"):
                if s[i] == "1":
                    memo[i] += dfs(i+2)
                elif s[i] == "2":
                    if s[i+1] in "0123456":
                        memo[i] += dfs(i+2)
            return memo[i] 
        
        dfs(0)
        return memo[0]