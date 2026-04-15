class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def isPal(l, r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l+=1
                r-=1
            return True
        res = []
        splits = []
        def backtrack(startIndex):
            if startIndex >= len(s):
                res.append(splits[:])
                return
            
            for j in range(startIndex, len(s)):
                if isPal(startIndex, j):
                    splits.append(s[startIndex:j+1])
                    backtrack(j+1)
                    splits.pop()
                
            return
        backtrack(0)
        return res



