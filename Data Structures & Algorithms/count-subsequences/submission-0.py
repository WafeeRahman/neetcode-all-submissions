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
        return dfs(0,0,s,t)


        

