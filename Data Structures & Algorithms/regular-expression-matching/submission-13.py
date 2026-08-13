class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        memoC = {}

        def memo(i, j):
            if j >= len(p):
                if i >= len(s):
                    return True
                return False
            if i >= len(s):
                #If we're done the string and can omit the current char* pattern
                if j+1 < len(p) and p[j+1] == "*" and memo(i, j+2):
                    return True
                return False
            
            if (i, j) in memoC:
                return memoC[(i, j)]

            memoC[(i,j)] = False
      
            if j < len(p)-1 and p[j+1] == "*":
                if p[j] != s[i] and p[j] != ".":
                    #If we have a character mismatch, try taking 0 for the current character and move onto next
                    memoC[(i,j)] = memoC[(i,j)] or memo(i, j+2)
                else:
                    #OTWS we can try using the same character 1 or more times (i+1, j) or skipping it entirely
                    memoC[(i,j)] = memoC[(i,j)] or memo(i+1, j) or memo(i, j+2)
            elif p[j] == "." or p[j] == s[i]:
                memoC[(i,j)] = memoC[(i,j)] or memo(i+1, j+1)    
            return memoC[(i, j)]
        return memo(0,0)
        