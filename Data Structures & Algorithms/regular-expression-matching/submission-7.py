class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        memoC = {}

        def memo(i, j):
            if j >= len(p):
                if i >= len(s):
                    return True
                return False
            if i == len(s):
                if j+1 < len(p) and p[j+1] == "*" and memo(i, j+2):
                    return True
                return False
            
            if (i, j) in memoC:
                return memoC[(i, j)]

            memoC[(i,j)] = False
      
            if j < len(p)-1 and p[j+1] == "*":
                if p[j] != s[i] and p[j] != ".":
                    memoC[(i,j)] = memoC[(i,j)] or memo(i, j+2)
                else:
                    memoC[(i,j)] = memoC[(i,j)] or memo(i+1, j) or memo(i, j+2)
            elif p[j] == "." or p[j] == s[i]:
                memoC[(i,j)] = memoC[(i,j)] or memo(i+1, j+1)    
            return memoC[(i, j)]
        return memo(0,0)
        