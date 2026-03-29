class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        count = {}
        maxChar=""
        maxCount=0
        res = 0
        l=0
        for r in range(len(s)):
            count[s[r]] = count.get(s[r],0 )+  1
            if count[s[r]] > maxCount:
                maxCount = count[s[r]]
                maxChar = s[r]
            
            windowLen = r-l+1
            if r-l+1 - maxCount <= k:
                res = max(res, windowLen)
            
            while r-l+1 - maxCount > k:
                count[s[l]] -= 1
                l+=1  
            windowLen = r-l+1
            res = max(res, windowLen)
        return res
            



        