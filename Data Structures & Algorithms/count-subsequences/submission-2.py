class Solution:
    def numDistinct(self, s: str, t: str) -> int:


        memoC = {}
        def memo(i, j):
            if j == len(t):
                return 1
            elif i >= len(s):
                if j == len(t):
                    return 1
                return 0
            elif (i, j) in memoC:
                return memoC[(i,j)]
            
            #skip
            memoC[(i, j)] = memo(i+1, j)
            if s[i] == t[j]:
                #include
                memoC[(i,j)] += memo(i+1, j+1)
 
            
            return memoC[(i,j)]

        return memo(0,0)

        