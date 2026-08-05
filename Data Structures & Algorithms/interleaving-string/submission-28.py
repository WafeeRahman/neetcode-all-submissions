class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        memoC = {}
        if (len(s1) + len(s2)) != len(s3):
            return False
        def memo(i, j, p):
            if p == len(s3):
                if i == len(s1) and j == len(s2):
                    return True
                return False
            elif (i,j) in memoC:
                return memoC[(i,j)]
            
            memoC[(i,j)] = False    
            if (i < len(s1) and s1[i] == s3[p]):
                memoC[(i,j)] = memoC[(i,j)] or memo(i+1, j, p+1) 
            if (j < len(s2) and s2[j] == s3[p]):
                memoC[(i,j)] = memoC[(i,j)] or memo(i, j+1, p+1)
            return memoC[(i,j)]
        return memo(0,0,0)
                    

        