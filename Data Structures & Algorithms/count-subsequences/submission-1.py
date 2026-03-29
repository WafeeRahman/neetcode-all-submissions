class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        def dfs(i,j, s, t): 
            if j == len(t):
                return 1
            if i >= len(s):
                return 0
            
            res = 0
            if s[i] == t[j]:
                res += dfs(i+1, j+1, s, t)
            
            res += dfs(i+1, j, s, t)
            return res
     
        
        cache = {}
        def memo(i,j,s,t):
            if j == len(t):
                return 1
            if i >= len(s):
                return 0
            
            if (i,j) in cache:
                return cache[(i,j)]
            res = 0 
            if s[i] == t[j]:
                res += memo(i+1, j+1, s, t)
            res += dfs(i+1, j, s, t)
            cache[i,j] = res
            return res
        return memo(0,0,s,t)
            


        

