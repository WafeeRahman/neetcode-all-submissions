class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0 
        count = {}
        res = 0
        for r in range(len(s)):
            count[s[r]] = count.get(s[r], 0) + 1
            windowLen = (r-l)+1
            maxCharCount = max(count.values())


            if (windowLen - maxCharCount) <= k:
                res = max(res, windowLen)
            
            #Sliding Condition, while we dont have a valid window, shrink it
            while l <= r and (windowLen - maxCharCount) > k:
                count[s[l]] -= 1
                l+=1
                windowLen = (r-l)+1
                maxCharCount = max(count.values())
        
        return res
            
