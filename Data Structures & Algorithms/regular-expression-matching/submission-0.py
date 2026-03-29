class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        

        memoC = {}

        def memo(i,j):
            if i >= len(s) and j >= len(p):
                return True
            if j >= len(p):
                return False
            
            match = i < len(s) and (s[i] == p[j] or p[j] == ".")

            #If there is a glob pattern, we need to make decisions of repeated curchar vs not
            if (j+1) < len(p) and p[j+1] == "*":
                return memo(i, j+2) or (match and memo(i+1, j))
            
            if match:
                return memo(i+1,j+1)
            
            else:
                return False
        
        return memo(0,0)
