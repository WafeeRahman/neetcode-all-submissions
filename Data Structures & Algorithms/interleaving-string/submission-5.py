class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        
        def dfs(i,j,k):
            if len(s1) + len(s2) != len(s3):
                return False
            if k == len(s3):
                return True
 
            if i < len(s1) and s1[i] == s3[k]:
                if dfs(i+1, j, k+1):
                    return True
            if j < len(s2) and s2[j] == s3[k]:
                if dfs(i,j+1,k+1):
                    return True
            return False


        cache = {}
        def memo(i,j,k):
            if len(s1) + len(s2) != len(s3):
                return False
                
            if k == len(s3):
                return True
            
            if (i,j) in cache:
                return cache[(i,j)]
            
            cache[(i,j)] = False
            if i < len(s1) and s1[i] == s3[k]:
                if memo(i+1, j, k+1):
                    cache[(i,j)] = True
            if j < len(s2) and s2[j] == s3[k]:
                if memo(i,j+1,k+1):
                    cache[(i,j)] = True
            return cache[(i,j)]
        return memo(0,0,0)